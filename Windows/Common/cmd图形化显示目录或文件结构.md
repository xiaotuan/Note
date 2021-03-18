可以使用 `tree /a` 显示目录结构，使用 `tree /f` 显示文件结构。

**图形化显示目录结构**

```console
PS C:\Users\Xiaotuan\Desktop> tree /a
文件夹 PATH 列表
卷序列号为 A5EB-573A
C:.
+---test
|   +---chapter01
|   |   \---__pycache__
|   \---chapter02
|       \---__pycache__
\---Web
```

**图形化显示文件结构**

```console
PS C:\Users\Xiaotuan\Desktop> tree /f
文件夹 PATH 列表
卷序列号为 A5EB-573A
C:.
│  Adobe Illustrator 2020.lnk
│  Adobe Photoshop 2020.lnk
│  Adobe XD.lnk
│  Android Studio.lnk
│  Bypass.exe - 快捷方式.lnk
│  Eclipse.lnk
│  Excel.lnk
│  Filezilla.lnk
│  HiTool.exe - 快捷方式.lnk
│  iTunes.lnk
│  JavaWeb视频教程_day9-资料源码.zip
│  JDGUI.lnk
│  Kindle.lnk
│  log.properties
│  Notepad++.lnk
│  Qt Creator 4.7.1 (Enterprise).lnk
│  trojan-qt5 - 快捷方式.lnk
│  Untitled-1.json
│  Visual Studio 2019.lnk
│  Visual Studio Code.lnk
│  vue.html
│  蓝湖 XD.lnk
│
├─test
│  │  main.py
│  │
│  ├─chapter01
│  │  │  throttle.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          throttle.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │
│  └─chapter02
│      │  download.py
│      │  __init__.py
│      │
│      └─__pycache__
│              download.cpython-38.pyc
│              __init__.cpython-38.pyc
│
└─Web
        test.html
        test.js
```

