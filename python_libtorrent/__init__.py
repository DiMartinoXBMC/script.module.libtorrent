#-*- coding: utf-8 -*-
'''
    Torrenter v2 plugin for XBMC/Kodi
    Copyright (C) 2012-2015 Vadim Skorba - DiMartino
'''

from platform_pulsar import get_platform

platform = get_platform()

print '[script.module.libtorrent]: platform ' + str(platform)

try:
    import libtorrent

    print '[script.module.libtorrent]: Imported libtorrent v' + libtorrent.version + ' from system'
except Exception, e:
    print '[script.module.libtorrent]: Error importing from system. Exception: ' + str(e)

    try:
        #dirname = os.path.join(xbmc.translatePath('special://home'), 'addons', 'script.module.libtorrent',
        #                       'python_libtorrent', platform['system'])
        #sys.path.insert(0, dirname)
        if platform['system'] == 'darwin':
            from darwin.libtorrent import *
        elif platform['system'] == 'linux_x86':
            from linux_x86.libtorrent import *
        elif platform['system'] == 'linux_x86_64':
            from linux_x86_64.libtorrent import *
        elif platform['system'] == 'windows':
            from windows.libtorrent import *

        #print '[script.module.libtorrent]: Imported libtorrent v' + libtorrent.version + ' from python_libtorrent.' + platform[
        #    'system']
    except Exception, e:
        print '[script.module.libtorrent]: Error importing python_libtorrent.' + platform['system'] + '. Exception: ' + str(e)
        pass