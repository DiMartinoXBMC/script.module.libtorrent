import sys
import os
import xbmc, xbmcgui, xbmcvfs
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
            log("try to fetch %s" % libname)
            url = "%s/%s/%s.zip" % (__libbaseurl__, self.platform['system'], libname)
            dest = os.path.join(self.dest_path, libname)
            try:
                self.http = HTTP()
                self.http.fetch(url, download=dest + ".zip", progress=True)
                log("%s -> %s" % (url, dest))
                xbmc.executebuiltin('XBMC.Extract("%s.zip","%s")' % (dest, self.dest_path), True)
                xbmcvfs.delete(dest + ".zip")
            except:
                text = 'Failed!'
                xbmc.executebuiltin("XBMC.Notification(%s,%s,%s,%s)" % (__scriptname__,text,750,__icon__))

def log(msg):
    xbmc.log("### [%s]: %s" % (__scriptname__,msg,), level=xbmc.LOGINFO )
    #print "### [%s]: %s" % (__scriptname__,msg,)

def get_libname(platform):
    libname=[]
    if platform['system'] == 'darwin':
        libname=['libtorrent.so']
    elif platform['system'] == 'linux_x86':
        libname=['libtorrent.so']
    elif platform['system'] == 'linux_x86_64':
        libname=['libtorrent.so']
    elif platform['system'] == 'windows':
        libname=['libtorrent.pyd']
    elif platform['system'] == 'android' and platform['arch'] == 'arm':
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
        ret["system"] = 'android'
        ret["message"] = ['Please use install Ace Stream APK and choose it in Settings.',
                          'It is possible to compile python-libtorrent for Android, but I don\'t know how.']
    elif ret["os"] == "darwin":
        ret["system"] = 'darwin'
        ret["message"] = ['It is possible to compile python-libtorrent for OS X.',
                          'But you would have to do it by yourself, there is some info on github.com.']
    elif ret["os"] == "ios":
        ret["system"] = 'ios'
        ret["message"] = ['It is NOT possible to compile python-libtorrent for iOS.',
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

    def check_exist(self):
        for libname in get_libname(self.platform):
            if not xbmcvfs.exists(os.path.join(self.dest_path,libname)):
                return False
        return True

    def check_update(self):
        return False

    def update(self):
        if self.check_update():
            #DO UPDATE
            pass