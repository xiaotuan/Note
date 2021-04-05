### B.3　在macOS上运行Python程序

在macOS上，你可以创建一个文本文件，并使用.command扩展名，从而创建一个shell脚本来运行Python脚本。在文本编辑器（如TextEdit）中创建一个新文件，然后添加以下内容：

```javascript
#!/usr/bin/env bash
python3 /path/to/your/pythonScript.py
```

以.command作为扩展名，将这个文件保存在你的主文件夹中（例如，在我的计算机上是/Users/al）。在命令行窗口中，运行 ` `chmod u+x yourScript.command` ` 使这个shell脚本可执行。现在你可以单击Spotlight图标（或按Command-Space快捷键）并输入 ` `yourScript.command` ` 来运行该shell脚本，而该shell脚本又会运行你的Python脚本。

