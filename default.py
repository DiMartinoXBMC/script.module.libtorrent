# -*- coding: utf-8 -*-

from python_libtorrent import get_libtorrent, get_platform, log
import xbmcgui

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


line2='Python-libtorrent %s IMPORTED successfully' % version if sucsess else 'Failed to import python-libtorrent!'
dialog.ok('Libtorrent','OS:'+p['os']+' arch:'+p['arch'], line2)