#-*- coding: utf-8 -*-
'''
    Torrenter v2 plugin for XBMC/Kodi
    Copyright (C) 2015 srg70, RussakHH, DiMartino
'''

from functions import *
import xbmc, xbmcgui, xbmcvfs, xbmcaddon
import sys
import os

__settings__ = xbmcaddon.Addon(id='script.module.libtorrent')
__version__ = __settings__.getAddonInfo('version')
__plugin__ = __settings__.getAddonInfo('name') + " v." + __version__
__root__ = __settings__.getAddonInfo('path')

platform = get_platform()
dirname = os.path.join(xbmc.translatePath('special://temp'), 'xbmcup', 'script.module.libtorrent',
                       'python_libtorrent')
#dirname = os.path.join(xbmc.translatePath('special://home'), 'addons', 'script.module.libtorrent',
#                       'python_libtorrent')
dest_path = os.path.join(dirname, platform['system'])
sys.path.insert(0, dirname)

lm=LibraryManager(dest_path)
if not lm.check_exist():
    DownloaderClass(dest_path).tools_download()


if __settings__.getSetting('plugin_name')!=__plugin__:
    __settings__.setSetting('plugin_name', __plugin__)
    lm.update()

log('platform ' + str(platform))
try:
    if platform['system'] == 'darwin':
        from darwin import libtorrent
    elif platform['system'] == 'linux_x86':
        from linux_x86 import libtorrent
    elif platform['system'] == 'linux_x86_64':
        from linux_x86_64 import libtorrent
    elif platform['system'] == 'windows':
        from windows import libtorrent
    elif platform['system'] == 'android' and platform['arch'] == 'arm':
        import imp
        from ctypes import *

        dll_path=os.path.join(dest_path, 'liblibtorrent.so')
        print "CDLL path = " + dll_path
        liblibtorrent=CDLL(dll_path)
        print 'CDLL = ' + str(liblibtorrent)

        path_list = [dest_path]
        print 'path_list = ' + str(path_list)
        fp, pathname, description = imp.find_module('libtorrent', path_list)
        print 'fp = ' + str(fp)
        print 'pathname = ' + str(pathname)
        libtorrent = imp.load_module('libtorrent', fp, pathname, description)

    print '[script.module.libtorrent]: Imported libtorrent v' + libtorrent.version + ' from python_libtorrent.' + platform[
        'system']

except Exception, e:
    print '[script.module.libtorrent]: Error importing python_libtorrent.' + platform['system'] + '. Exception: ' + str(e)
    pass

def get_libtorrent():
    return libtorrent
