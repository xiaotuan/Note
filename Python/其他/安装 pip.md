[toc]

### 1. 检查 pip 是否安装

#### 1.1 在 Linux 和 OS X 系统中检查是否安装了 pip

打开一个终端窗口，并执行如下命令：

```shell
$ pip --version
pip 22.0.4 from C:\Users\xiaotuan\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```

如果出现了错误信息，请尝试将 `pip` 替换为 `pip3`。

#### 1.2 在 Windows 系统中检查是否安装了 pip

打开一个终端窗口，并执行如下命令：

```shell
> python -m pip --version
pip 22.0.4 from C:\Users\xiaotuan\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```

### 2. 安装 pip

要安装 `pip`，请访问 <https://bootstrap.pypa.io/get-pip.py>。如果出现对话框，请选择保持文件；如果 `get-pip.py` 的代码出现在浏览器中，请将这些代码复制并粘贴到文本编辑器中，再将文件保存为 `get-pip.py`。将 `get-pip.py` 保存到计算机中后，你需要以管理员身份运行它，因为 `pip` 将在你的系统中安装新包。

#### 2.1 在 Linux 和 OS X 系统中安装 pip

使用下面的命令以管理员身份运行 `get-pip.py`：

```shell
$ sudo python get-pip.py
```

> 注意：如果你启动终端会话时使用的是命令 `python3` ，那么在这里应使用命令 `sudo python3 get-pip.py`。

或者使用如下命令：

```shell
$ sudo apt install python3-pip
```

#### 2.2 在 Windows 系统中安装 pip

使用下面的命令运行 `get-pip.py`：

```shell
> python get-pip.py
```

> 提示：Python 的 Windows 安装包内就包含 pip 工具，只需在安装 python 时勾选安装 pip 即可。