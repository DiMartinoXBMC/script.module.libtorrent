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

libtorrent=None
platform = get_platform()
dirname = os.path.join(xbmc.translatePath('special://temp'), 'xbmcup', 'script.module.libtorrent',
                       'python_libtorrent')
dest_path = os.path.join(dirname, platform['system'])
sys.path.insert(0, dest_path)

lm=LibraryManager(dest_path)
if not lm.check_exist():
    ok=lm.download()
    xbmc.sleep(2000)


if __settings__.getSetting('plugin_name')!=__plugin__:
    __settings__.setSetting('plugin_name', __plugin__)
    lm.update()

log('platform ' + str(platform))
try:
    if platform['system'] in ['darwin', 'linux_x86', 'linux_x86_64', 'windows']:
        import libtorrent
    elif platform['system'] in ['android_armv7', 'android_x86']:
        import imp
        from ctypes import *

        dll_path=os.path.join(dest_path, 'liblibtorrent.so')
        print "CDLL path = " + dll_path
        liblibtorrent=CDLL(dll_path)
        log('CDLL = ' + str(liblibtorrent))

        path_list = [dest_path]
        log('path_list = ' + str(path_list))
        fp, pathname, description = imp.find_module('libtorrent', path_list)
        log('fp = ' + str(fp))
        log('pathname = ' + str(pathname))
        try:
            libtorrent = imp.load_module('libtorrent', fp, pathname, description)
        finally:
            if fp: fp.close()

    log('Imported libtorrent v' + libtorrent.version + ' from ' + dest_path)

except Exception, e:
    log('Error importing libtorrent from' + dest_path + '. Exception: ' + str(e))
    pass

def get_libtorrent():
    return libtorrent
