# -*- coding: utf-8 -*-

from python_libtorrent import get_libtorrent, get_platform, log
import xbmcgui
import xbmcaddon, xbmc

sucsess=False
version=''
p=get_platform()
dialog = xbmcgui.Dialog()

try:
    libtorrent=get_libtorrent()

    log('Imported libtorrent v' + libtorrent.version + ' from get_libtorrent()')
    version=str(libtorrent.version)
    sucsess=True
except Exception, e:
    log('Error importing from get_libtorrent(). Exception: ' + str(e))


line2='python-libtorrent %s IMPORTED successfully' % version if sucsess else 'Failed to import python-libtorrent!'
dialog.ok('Libtorrent','OS:'+p['os']+' arch:'+p['arch'], line2)

__settings__ = xbmcaddon.Addon(id='script.module.libtorrent')
__language__ = __settings__.getLocalizedString
if __settings__.getSetting('ask_dirname')=='true':
    set_dirname=__settings__.getSetting('dirname')
    __settings__.setSetting('ask_dirname','false')
    keyboard = xbmc.Keyboard(set_dirname, __language__(1002))
    keyboard.doModal()
    path_keyboard = keyboard.getText()
    if path_keyboard and keyboard.isConfirmed():
        __settings__.setSetting('dirname', path_keyboard)