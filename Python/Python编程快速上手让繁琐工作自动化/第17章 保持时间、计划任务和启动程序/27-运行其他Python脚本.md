### 17.8.4　运行其他Python脚本

可以在Python中启动另一个Python脚本，就像任何其他的应用程序一样。只需向 `Popen()` 传入python.exe可执行文件，并将想运行的.py脚本的文件名作为它的参数即可启动脚本。例如，下面代码将运行第1章的hello.py脚本：

```javascript
>>> subprocess.Popen(['C:\\Users\\<YOUR USERNAME>\\AppData\\Local\\Programs\\ Python\\
Python38\\python.exe', 'hello.py'])
<subprocess.Popen object at 0x000000000331CF28>
```

向 `Popen()` 传入一个列表，其中包含Python可执行文件的路径字符串，以及脚本文件名的字符串。如果要启动的脚本需要命令行参数，那就将它们添加到列表中，并放在脚本文件名后面。在Windows操作系统上，Python可执行文件的路径是C:\Users\<YOUR USERNAME>\ AppData\Local\Programs\Python\Python38\python.exe。在macOS上，路径是/Library/Frameworks/ Python. framework/Versions/3.8/bin/python3。在Linux操作系统上，路径是/usr/bin/python3.8。

不同于将Python程序导入为一个模块，如果Python程序启动了另一个Python程序，那么两者将在独立的进程中运行，不能分享彼此的变量。

