import sys
import os
try:
    import xbmc, xbmcgui, xbmcvfs
except:
    pass
from net import HTTP

__libbaseurl__ = "https://github.com/DiMartinoXBMC/script.module.libtorrent/raw/master/python_libtorrent/"
__scriptname__ = "script.module.libtorrent"
__icon__=os.path.join(xbmc.translatePath('special://home'), 'addons',
                                   'script.module.libtorrent', 'icon.png')

class DownloaderClass():
    def __init__(self, dest_path):
        self.dest_path = dest_path
        self.platform = get_platform()
        tempdir(self.platform)

    def tools_download(self):
        for libname in get_libname(self.platform):
            dest = os.path.join(self.dest_path, libname)
            log("try to fetch %s" % libname)
            url = "%s/%s/%s.zip" % (__libbaseurl__, self.platform['system'], libname)
            if libname!='liblibtorrent.so':
                try:
                    self.http = HTTP()
                    self.http.fetch(url, download=dest + ".zip", progress=True)
                    log("%s -> %s" % (url, dest))
                    xbmc.executebuiltin('XBMC.Extract("%s.zip","%s")' % (dest, self.dest_path), True)
                    xbmcvfs.delete(dest + ".zip")
                except:
                    text = 'Failed download %s!' % libname
                    xbmc.executebuiltin("XBMC.Notification(%s,%s,%s,%s)" % (__scriptname__,text,750,__icon__))
            else:
                x=xbmcvfs.copy(os.path.join(self.dest_path, 'libtorrent.so', dest))
        return True

def log(msg):
    xbmc.log("### [%s]: %s" % (__scriptname__,msg,), level=xbmc.LOGNOTICE )
    #print "### [%s]: %s" % (__scriptname__,msg,)

def get_libname(platform):
    libname=[]
    if platform['system'] in ['darwin', 'linux_x86', 'linux_x86_64']:
        libname=['libtorrent.so']
    elif platform['system'] == 'windows':
        libname=['libtorrent.pyd']
    elif platform['system'] == 'android_armv7':
        libname=['libtorrent.so', 'liblibtorrent.so']
    return libname

def get_platform():
    ret = {
        "arch": sys.maxsize > 2 ** 32 and "x64" or "x86",
    }
    if xbmc.getCondVisibility("system.platform.android"):
        ret["os"] = "android"
        if "arm" in os.uname()[4]:
            ret["arch"] = "arm"
    elif xbmc.getCondVisibility("system.platform.linux"):
        ret["os"] = "linux"
        if "arm" in os.uname()[4]:
            ret["arch"] = "arm"
    elif xbmc.getCondVisibility("system.platform.xbox"):
        system_platform = "xbox"
        ret["arch"] = ""
    elif xbmc.getCondVisibility("system.platform.windows"):
        ret["os"] = "windows"
    elif xbmc.getCondVisibility("system.platform.osx"):
        ret["os"] = "darwin"
    elif xbmc.getCondVisibility("system.platform.ios"):
        ret["os"] = "ios"
        ret["arch"] = "arm"

    ret["system"] = ''
    ret["message"] = ['', '']

    if ret["os"] == 'windows':
        ret["system"] = 'windows'
        ret["message"] = ['Windows has static compiled python-libtorrent included.',
                          'You should install "script.module.libtorrent" from "MyShows.me Kodi Repo"']
    elif ret["os"] == "linux" and ret["arch"] == "x64":
        ret["system"] = 'linux_x86_64'
        ret["message"] = ['Linux x64 has not static compiled python-libtorrent included.',
                          'You should install it by "sudo apt-get install python-libtorrent"']
    elif ret["os"] == "linux" and ret["arch"] == "x86":
        ret["system"] = 'linux_x86'
        ret["message"] = ['Linux has static compiled python-libtorrent included but it didn\'t work.',
                          'You should install it by "sudo apt-get install python-libtorrent"']
    elif ret["os"] == "linux" and ret["arch"] == "arm":
        ret["system"] = 'linux_arm'
        ret["message"] = ['As far as I know you can compile python-libtorrent for ARMv6-7.',
                          'You should search for "OneEvil\'s OpenELEC libtorrent" or use Ace Stream.']
    elif ret["os"] == "android":
        if ret["arch"]=='arm':
            ret["system"] = 'android_armv7'
        else:
            ret["system"] = 'android_x86'
        ret["message"] = ['Please contact DiMartino on kodi.tv forum. We compiled python-libtorrent for Android,',
                          'but we need your help with some tests on diffrient processeors.']
    elif ret["os"] == "darwin":
        ret["system"] = 'darwin'
        ret["message"] = ['It is possible to compile python-libtorrent for OS X.',
                          'But you would have to do it by yourself, there is some info on github.com.']
    elif ret["os"] == "ios":
        ret["system"] = 'ios'
        ret["message"] = ['It is probably NOT possible to compile python-libtorrent for iOS.',
                          'But you can use torrent-client control functions.']

    return ret

def tempdir(platform):
    dirname=xbmc.translatePath('special://temp')
    for subdir in ('xbmcup', 'script.module.libtorrent', 'python_libtorrent', platform['system']):
        dirname = os.path.join(dirname, subdir)
        if not xbmcvfs.exists(dirname):
            xbmcvfs.mkdir(dirname)
    return dirname

class LibraryManager():
    def __init__(self, dest_path):
        self.dest_path = dest_path
        self.platform = get_platform()
        self.root=os.path.dirname(__file__)

    def check_exist(self):
        for libname in get_libname(self.platform):
            if not xbmcvfs.exists(os.path.join(self.dest_path,libname)):
                return False
        return True

    def check_update(self):
        need_update=False
        for libname in get_libname(self.platform):
            if libname!='liblibtorrent.so':
                self.libpath = os.path.join(self.dest_path, libname)
                self.sizepath=os.path.join(self.root, self.platform['system'], libname+'.size.txt')
                size=str(os.path.getsize(self.libpath))
                size_old=open( self.sizepath, "r" ).read()
                if size_old!=size:
                    need_update=True
        return need_update

    def update(self):
        if self.check_update():
            for libname in get_libname(self.platform):
                self.libpath = os.path.join(self.dest_path, libname)
                xbmcvfs.delete(self.libpath)
            self.download()

    def download(self):
        DownloaderClass(self.dest_path).tools_download()