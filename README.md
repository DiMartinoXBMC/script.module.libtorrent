Python-Libtorrent for Kodi
==================
script.module.libtorrent is a Kodi module that makes easy import of python-libtorrent for you. Example of usage is Torrenter v2 at https://github.com/DiMartinoXBMC/plugin.video.torrenter

- Forum: https://forums.tvaddons.ag/addon-releases/29224-torrenter-v2.html

Usage
---------------

Add module in requires of your addon.xml::

    <import addon="script.module.libtorrent"/>

Use it in any python file::

    from python_libtorrent import get_libtorrent
    libtorrent=get_libtorrent()