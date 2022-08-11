[toc]

> 提示：不同系统安装方法请参阅 <https://tkdocs.com/tutorial/install.html#installwin>。

### 1. Ubuntu 系统

#### 1.1 Python2 安装 tkinter 模块

```shell
$ sudo apt-get install python-tk
```

#### 1.2 Python3 安装 tkinter 模块

```shell
$ sudo apt-get install python3-tk
或
$ sudo apt install python3-tk
```

### 2. Windows 系统

Tkinter（以及，自 Python 3.1 起，ttk，新主题小部件的接口）包含在 Python 标准库中。[我们强烈建议使用来自python.org](https://python.org/)的标准二进制发行版安装 Python 。这些将自动安装 Tcl/Tk，这当然是 Tkinter 需要的。

如果您是从源代码构建 Python，“PCbuild”目录中包含的 Visual Studio 项目可以自动获取和编译您系统上的 Tcl/Tk。

安装或编译 Python 后，对其进行测试以确保 Tkinter 正常工作。在 Python 提示符下，输入以下两个命令：

```python
>>> import tkinter
>>> tkinter._test()
```

这应该会弹出一个小窗口；窗口顶部的第一行应该是“This is Tcl/Tk version 8.6”；确保它不是 8.4 或 8.5！

得到一个错误说`"No module named tkinter"`？您可能正在使用 Python 2。本教程假定使用 Python 3。

您还可以获得正在使用的 Tcl/Tk 的确切版本：

```python
>>> tkinter.Tcl().eval('info patchlevel')
```

它应该返回类似“8.6.9”的内容。

在 Windows 10 版本 1809 上使用来自 python.org（包含 Tcl/Tk 8.6.9）的 Python 3.9.0rc1 二进制安装程序进行了验证。

### 3. MAC 系统

如前所述，在您的系统上安装 Tk 和 Tkinter 的最简单方法是使用 Python 的二进制安装程序，可在[python.org 获得](https://python.org/)。感谢 Python 核心开发人员 Ned Deily 的工作，从 3.7 版开始的二进制安装程序包括 Tcl 和 Tk。

> 请记住，我们在这里使用的是 Python 3.x，而不是 2.x。在撰写本文时，最新的 3.9 安装程序 (3.9.0rc1) 包括 Tk 8.6.8。

但是，如果您自己编译 Python，您将有更多工作要做。继续阅读...