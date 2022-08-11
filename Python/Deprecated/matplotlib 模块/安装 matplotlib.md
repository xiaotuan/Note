[toc]

### 1. 在 Linux 系统中安装 matplotlib

如果你使用的是系统自带的 Python 版本，可使用系统的包管理器来安装 `matplotlib`，为此只需只需一行命令：

```shell
$ sudo apt-get install python3-matplotlib
```

如果你使用的是 Python 2.7，请执行如下命令：

```shell
$ sudo apt-get install python-matplotlib
```

如果你安装了较新的 Python  版本，就必须安装 `matplotlib` 依赖的一些库：

```shell
$ sudo apt-get install python3.5-dev python3.5-tk tk-dev
$ sudo apt-get install libfreetype6-dev g++
```

再使用 `pip` 来安装 `matplotlib` ：

```shell
$ pip install --user matplotlib
```

### 2. 在 OS X 系统中安装 matplotlib

Apple 的标准 Python 安装自带了 `matplotlib`。要检查系统是否安装了 `matplotlib`，可打开一个终端会话并尝试导入 `matplotlib`。如果系统没有自带 `matplotlib`，且你的 Python 是使用 Homebrew 安装的，则可以像下面这样安装 `matplotlib`：

```shell
$ pip install --user matplotlib
```

> 注意：安装包时可能需要使用 `pip3`，而不是 `pip`。另外，如果这个命令不管用，你可能需要删除标志 `--user`。

### 3. 在 Windows 系统中安装 matplotlib

请访问 <https://pypi.python.org/pypi/matplotlib/>，并查找与你使用的 Python 版本匹配的 wheel 文件（扩展名为 `.whl` 的文件）。

> 注意：如果找不到与你安装的 Python 版本匹配的文件，请去 <http://www.lfd.uci.edu/-gohlke/pythonlibs/#matplotlib> 看看，这个网站发布安装程序的实际通常比 `matplotlib` 官网早些。

将这个 `.whl` 文件复制到你的项目文件夹，打开一个命令窗口，并切换到该项目文件夹，再使用 `pip` 来安装 `matplotlib`：

```shell
> cd python_work
python_work> python -m pip install --user matplotlib-1.4.3-cp35-none-win32.whl
```

