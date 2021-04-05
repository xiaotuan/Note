### B.4　在Ubuntu Linux操作系统上运行 Python 程序

在Ubuntu Linux操作系统中，从Dash菜单中运行你的Python脚本需要大量的设置。假设我们有一个/home/al/example.py脚本（你的Python脚本可能在不同的文件夹里有不同的文件名），我们要在Dash中运行。首先，使用 gedit 等文本编辑器创建一个新文件，内容如下：

```javascript
[Desktop Entry]
Name=example.py
Exec=gnome-terminal -- /home/al/example.sh
Type=Application
Categories=GTK;GNOME;Utility;
```

将此文件保存到/home/<al>/.local/share/applications文件夹（用你自己的用户名替换al），名为example.desktop。如果你的文本编辑器没有显示.local文件夹（因为以句点开头的文件夹被隐藏了），那么可能必须将它先保存到主文件夹（例如/home/al），再打开一个命令行窗口，用 ` `mv/home/al/example.desktop/home/al/.local/share/applications` ` 命令移动该文件。

如果example.desktop文件位于/home/al/.local/share/applications文件夹中，你就可以按键盘上的win键以显示Dash，并输入example.py（或你在 ` `Name` ` 字段中输入的任何内容）。这将打开一个新的命令行窗口（具体来说，是 ` `gnome-terminal` ` 程序），该窗口运行shell脚本/home/al/example.sh，我们接下来就创建它。

在文本编辑器中，创建一个包含以下内容的新文件：

```javascript
#!/usr/bin/env bash
python3 /home/al/example.py
bash
```

将此文件保存为/home/al/example.sh。这是一个shell脚本：运行一系列命令行命令的脚本。这个shell脚本将运行我们的Python脚本/home/al/ example.py，然后运行bash shell程序。 如果没有最后一行的 ` `bash` ` 命令，Python脚本完成后，命令行窗口将关闭，你会错过调用 ` `print()` ` 函数在屏幕上显示的所有文本。

需要为这个shell脚本添加执行权限，因此请在命令行窗口中运行以下命令：

```javascript
al@ubuntu:~$ chmod u+x /home/al/example.sh
```

设置好example.desktop和example.sh文件后，现在可以通过按win键并输入example来运行example.py脚本了。（或你在example.desktop文件的 ` `Name` ` 字段中输入的任何名称。）

