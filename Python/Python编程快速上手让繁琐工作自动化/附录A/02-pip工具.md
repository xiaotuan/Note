### A.1　pip工具

虽然在Windows操作系统和macOS上pip会随Python3.4自动安装，但在Linux操作系统上，必须单独安装。你可以通过在命令行窗口中运行pip3来查看Linux操作系统上是否已经安装了pip。如果已经安装了，你会看到pip3的位置显示；否则，什么也不会显示。要在Ubuntu Linux或Debian Linux操作系统上安装pip3，就打开一个新的命令行窗口，输入 `sudo apt-get install python3-pip` 。要在Fedora Linux操作系统上安装pip3，就在命令行窗口输入 `sudo yum install python3-pip` 。为了安装这个软件，需要输入计算机的管理员密码。

pip工具在命令行（也叫终端）窗口中运行，而不是在Python的交互式环境中运行。在Windows操作系统上，从开始菜单中运行“命令提示符”程序。在macOS上，从Spotlight中运行Terminal。在Ubuntu Linux操作系统上，从Ubuntu Dash中运行Terminal，或者按Ctrl-Alt-T快捷键。

如果pip的文件夹没有在PATH环境变量中列出，你可能需要在运行pip之前在命令行窗口中用 `cd` 命令更改目录。如果你需要知道你的用户名，那么可以在Windows操作系统上运行 `echo  `echo %USERNAME%` ` ，在macOS和Linux操作系统上运行 `whoami` 。然后运行 `cd <pip's folder>` ，其中 `pip's folder` 在Windows操作系统上是C:\Users\Users<USERNAME>\ AppData\Local\ Programs\Python\Python37\Scripts。在macOS上，它在/Library/ Frameworks/Python. framework/ Versions/3.7/bin/。在Linux操作系统上，它在/home/<USERNAME>/.local/bin/。然后你就可以在正确的文件夹中运行pip工具了。

