python-libtorrent for Kodi
==================
script.module.libtorrent is a Kodi module that makes easy import of python-libtorrent for you.

- Forum: https://forums.tvaddons.ag/addon-releases/29224-torrenter-v2.html

Used in projects
----------------

- [Torrenter v2](https://github.com/DiMartinoXBMC/plugin.video.torrenter)
- [YATP](https://github.com/romanvm/kodi.yatp)

Usage
-----

### Add module in requires of your addon.xml: ###
```python
<import addon="script.module.libtorrent"/>
```

### Use it in any python file: ###
```python
from python_libtorrent import get_libtorrent
libtorrent=get_libtorrent()
```

License
-------
[GPL v.3](http://www.gnu.org/licenses/gpl-3.0.en.html).