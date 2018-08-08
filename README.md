python-libtorrent for Kodi
==================
script.module.libtorrent is a Kodi module that makes easy import of python-libtorrent

**Support**
- Russian forum: http://xbmc.ru/forum/showthread.php?t=4728

**Used in projects**
- [Torrenter v2](https://github.com/DiMartinoXBMC/plugin.video.torrenter)
- [YATP](https://github.com/romanvm/kodi.yatp)
- [pyrrent2http](https://github.com/inpos/script.module.pyrrent2http)

**Usage**

Add module to your repository and requires in addon.xml:
```python
<import addon="script.module.libtorrent"/>
```

Use it in any python file:
```python
from python_libtorrent import libtorrent
```

**License**

MIT License