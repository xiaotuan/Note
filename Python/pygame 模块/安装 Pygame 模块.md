[toc]

### 1. 在 Linux 系统中安装 Pygame

如果你使用的是 `Python 2.7`，请使用包管理器来安装 `Pygame`。为此，打开一个终端窗口，并执行下面的命令，这将下载 `Pygame`，并将其安装到你的系统中：

```shell
$ sudo apt-get install python-pygame
```

或者:

```shell
$ sudo pip install pygame
```

如果你使用的是 `Python 3`，就需要执行两个步骤：安装 `Pygame` 依赖库；下载并安装 `Pygame`。

执行下面的命令来安装 `Pygame` 依赖库（如果你开始终端会话时使用的是命令 `Python 3.5`，请将 `python3-dev` 替换为 `python3.5-dev`：

```shell
$ sudo apt-get install python3-dev mercurial
$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
```

如果你要启用 `Pygame` 的一些高级功能，如添加声音的功能，可安装下面这些额外的库：

```shell
$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
$ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
$ sudo apt-get install python-numpy
```

接下来，执行下面的命令来安装 `Pygame`（如有必要，将 `pip` 替换为 `pip3`）：

```shell
$ pip install --user hg+http://bitbucket.org/pygame/pygame
```

### 2. 在 OS X 系统中安装 Pygame

要安装 `Pygame` 依赖的有些包，需要 `Homebrew`。如果你没有安装 `Homebrew`，请参阅。

为安装 `Pygame` 依赖的库，请执行下面的命令：

```shell
$ brew install hg sdl sdl_image sdl_ttf
```

如果你还想启用较高级的功能，如在游戏中包含声音，可安装下面两个额外的库：

```shell
$ brew install sdl_mixer portmidi
```

使用下面的命令来安装 `Pygame`（如果你运行的是 `Python 2.7`，请将 `pip3` 替换为 `pip`）：

```shell
$ pip3 install --user hg+http://bitbucket.org/pygame/pygame
```

或者

```shell
$ sudo pip3 install pygame
```

### 3. 在 Windows 系统中安装 Pygame

要在 `Windows` 系统中安装 `Pygame`，请访问 <https://bitbucket.org/pygame/pygame/downloads/>，查找与你运行的 `Python` 版本匹配的 `Windows` 安装程序。如果在 Bitbucket 上找不到合适的安装程序，请去 <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame> 看看。

下载合适的文件后，如果它是 `.exe` 文件，就运行它。

如果该文件的扩展名为 `.whl`，就将它赋值到你的项目文件夹中。再打开一个命令窗口，切换到该文件所在文件夹，并使用 `pip` 来运行它：

```shell
> python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl
```

或者：

```shell
> pip3 install pygame
```

