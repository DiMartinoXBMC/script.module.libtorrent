python-libtorrent for Kodi
==================
script.module.libtorrent is a Kodi module that makes easy import of python-libtorrent for you.

**Support**
- English forum: https://forums.tvaddons.ag/addon-releases/29224-torrenter-v2.html
- Russian forum: http://xbmc.ru/forum/showthread.php?t=4728

**Used in projects**
- [Torrenter v2](https://github.com/DiMartinoXBMC/plugin.video.torrenter)
- [YATP](https://github.com/romanvm/kodi.yatp)

**Usage**

Add module in requires of your addon.xml:
```python
<import addon="script.module.libtorrent"/>
```

Use it in any python file:
```python
from python_libtorrent import get_libtorrent
libtorrent=get_libtorrent()
```

**License**

MIT License