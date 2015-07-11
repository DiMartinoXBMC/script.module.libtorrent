# -*- coding: utf-8 -*-

import xbmcplugin, xbmcgui, os
from python_libtorrent.platform_pulsar import get_platform
from ctypes import *

sucsess=False
dialog = xbmcgui.Dialog()
p=get_platform()
ROOT_PATH=os.path.dirname(__file__)
dirname=os.path.join(ROOT_PATH, 'python_libtorrent', p['system'])
#dirname = os.path.join(xbmc.translatePath('special://home'), 'addons', 'script.module.libtorrent',
#                       'python_libtorrent', platform['system'])
#sys.path.insert(0, dirname)

try:
    import python_libtorrent as libtorrent

    print '[script.module.libtorrent]: Imported libtorrent v' + libtorrent.version + ' from python_libtorrent'
    sucsess=True
except Exception, e:
    print '[script.module.libtorrent]: Error importing from system. Exception: ' + str(e)

try:
    cdll.LoadLibrary(dirname + '/libpython2.6.so')
except Exception, e:
    print '[script.module.libtorrent]: Error importing from '+str(dirname)+'. Exception: ' + str(e)
	
try:
    cdll.LoadLibrary(dirname + '/libpython2.6.so')
    cdll.LoadLibrary(dirname + '/libtorrent.so')

    print '[script.module.libtorrent]: Imported libtorrent v' + libtorrent.version + ' from cdll'
    sucsess=True
except Exception, e:
    print '[script.module.libtorrent]: Error importing from '+str(dirname)+'. Exception: ' + str(e)


line2='WE DID IT! IMPORTED' if sucsess else 'Failed!'
dialog.ok('Libtorrent','OS:'+p['os']+' arch:'+p['arch'], line2)