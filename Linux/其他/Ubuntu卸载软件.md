1. 打开终端，输入 `dpkg --list` 命令，查看要卸载的应用的包名。

   ```console
   $ dpkg --list
   ......
   ii  pyotherside    1.4.0-2      all          transitional dummy package
   ii  python-apt-com 1.1.0~beta1u all          Python interface to libapt-pkg (l
   ii  python-pip-whl 8.1.1-2ubunt all          alternative Python package instal
   ii  python3        3.5.1-3      amd64        interactive high-level object-ori
   ii  python3-apport 2.20.1-0ubun all          Python 3 library for Apport crash
   ii  python3-apt    1.1.0~beta1u amd64        Python 3 interface to libapt-pkg
   ii  python3-aptdae 1.1.1+bzr982 all          Python 3 module for the server an
   ii  python3-aptdae 1.1.1+bzr982 all          Python 3 GTK+ 3 widgets to run an
   ii  python3-aptdae 1.1.1+bzr982 all          PackageKit compatibilty for AptDa
   ii  python3-blinke 1.3.dfsg2-1b all          fast, simple object-to-object and
   ii  python3-brlapi 5.3.1-2ubunt amd64        Braille display access via BRLTTY
   ii  python3-bs4    4.4.1-1      all          error-tolerant HTML parser for Py
   ii  python3-cairo  1.10.0+dfsg- amd64        Python 3 bindings for the Cairo v
   ii  python3-cffi-b 1.5.2-1ubunt amd64        Foreign Function Interface for Py
   ii  python3-charde 2.3.0-2      all          universal character encoding dete
   ii  python3-checkb 0.22-1       all          collection of Python modules used
   ii  python3-comman 0.3ubuntu16. all          Python 3 bindings for command-not
   ii  python3-crypto 1.2.3-1ubunt amd64        Python library exposing cryptogra
   ii  python3-cups   1.9.73-0ubun amd64        Python3 bindings for CUPS
   ii  python3-cupshe 1.5.7+201602 all          Python modules for printer config
   ii  python3-dbus   1.2.0-3      amd64        simple interprocess messaging sys
   ii  python3-debian 0.1.27ubuntu all          Python 3 modules to work with Deb
   ii  python3-defer  1.0.6-2build all          Small framework for asynchronous 
   ii  python3-distup 1:16.04.30   all          manage release upgrades
   ii  python3-feedpa 5.1.3-3build all          Universal Feed Parser for Python 
   ii  python3-gdbm:a 3.5.1-1      amd64        GNU dbm database support for Pyth
   ii  python3-gi     3.20.0-0ubun amd64        Python 3 bindings for gobject-int
   ii  python3-gi-cai 3.20.0-0ubun amd64        Python 3 Cairo bindings for the G
   ii  python3-guacam 0.9.2-1      all          framework for creating command li
   ii  python3-html5l 0.999-4      all          HTML parser/tokenizer based on th
   ii  python3-httpli 0.9.1+dfsg-1 all          comprehensive HTTP client library
   ii  python3-idna   2.0-3        all          Python IDNA2008 (RFC 5891) handli
   ii  python3-jinja2 2.8-1ubuntu0 all          small but fast and easy to use st
   ii  python3-jwt    1.3.0-1ubunt all          Python 3 implementation of JSON W
   ii  python3-louis  2.6.4-2ubunt all          Python bindings for liblouis
   ii  python3-lxml   3.5.0-1ubunt amd64        pythonic binding for the libxml2 
   ii  python3-mako   1.0.3+ds1-1u all          fast and lightweight templating f
   ii  python3-markup 0.23-2build2 amd64        HTML/XHTML/XML string library for
   ii  python3-minima 3.5.1-3      amd64        minimal subset of the Python lang
   ii  python3-oauthl 1.0.3-1      all          generic, spec-compliant implement
   ii  python3-padme  1.1.1-2      all          mostly transparent proxy class fo
   ii  python3-pexpec 4.0.1-1      all          Python 3 module for automating in
   ii  python3-pil:am 3.1.2-0ubunt amd64        Python Imaging Library (Python3)
   ii  python3-pkg-re 20.7.0-1     all          Package Discovery and Resource Ac
   ii  python3-plainb 0.25-1       all          toolkit for software and hardware
   ii  python3-proble 2.20.1-0ubun all          Python 3 library to handle proble
   ii  python3-ptypro 0.5-1        all          Run a subprocess in a pseudo term
   ii  python3-pyasn1 0.1.9-1      all          ASN.1 library for Python (Python 
   ii  python3-pyatsp 2.18.0+dfsg- all          Assistive Technology Service Prov
   ii  python3-pycurl 7.43.0-1ubun amd64        Python bindings to libcurl (Pytho
   ii  python3-pypars 2.0.3+dfsg1- all          Python parsing module, Python3 pa
   ii  python3-render 3.3.0-1ubunt amd64        python low level render interface
   ii  python3-report 3.3.0-1ubunt all          ReportLab library to create PDF d
   ii  python3-report 3.3.0-1ubunt amd64        C coded extension accelerator for
   ii  python3-reques 2.9.1-3ubunt all          elegant and simple HTTP library f
   ii  python3-six    1.10.0-3     all          Python 2 and 3 compatibility libr
   ii  python3-softwa 0.96.20.10   all          manage the repositories that you 
   ii  python3-speech 0.8.3-1ubunt all          Python interface to Speech Dispat
   ii  python3-system 231-2build1  amd64        Python 3 bindings for systemd
   ii  python3-uno    1:5.1.6~rc2- amd64        Python-UNO bridge
   ii  python3-update 1:16.04.17   all          python 3.x module for update-mana
   ii  python3-urllib 1.13.1-2ubun all          HTTP library with thread-safe con
   ii  python3-xdg    0.25-4       all          Python 3 library to access freede
   ii  python3-xkit   0.5.0ubuntu2 all          library for the manipulation of x
   ii  python3-xlsxwr 0.7.3-1      all          Python 3 module for creating Exce
   ii  python3.5      3.5.2-2ubunt amd64        Interactive high-level object-ori
   ii  python3.5-mini 3.5.2-2ubunt amd64        Minimal subset of the Python lang
   ii  qdbus          4:4.8.7+dfsg amd64        Qt 4 D-Bus tool
   ......
   ```

   2. 比如我们要卸载 python ，从上面的打印信息可以看出它的包名是 python3.5。
   3. 在终端上输入 `sudo apt-get --purge remove 包名`（`--purge` 是可选项，写上这个属性是将软件及其配置文件一并删除，如不需要删除配置文件，可执行 `sudo apt-get --purge remove 包名` ），此处，我们要删除 python，那么在终端上输入 `sudo apt-get --purge remove python3.5`，按下回车键，输入密码，再次按回车键即可卸载 python。

