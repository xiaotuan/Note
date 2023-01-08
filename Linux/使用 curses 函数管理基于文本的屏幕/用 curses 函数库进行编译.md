> 提示：如果系统没有安装 curses，可以使用下面命令进行安装：
>
> ```shell
> $ sudo apt install libncurses5-dev
> ```

`Linux` 使用的 `curses` 版本是 `ncurses`（又称为 `new curses`），它是在 `Linux` 系统上开发的、针对系统 V 版本 4.0 上 `curses` 函数库的免费仿真软件。如果使用的 UNIX 系统自带的 `curses` 函数库不支持某些功能，你可以尝试获取一份 `ncurses` 函数库来替换它。`Linux` 用户通常都会发现系统已预装好了 `ncurses` 函数库，或至少安装好了运行基于 `curses` 函数库的程序锁需的组件。如果 `ncurses` 的开发函数库并没有在发行版中预装（系统中没有头文件 `curses.h` 或用于链接的 `curses` 库文件），它们通常会以一个标准软件包的形式存在于大多数主要的 Linux 发行版中，例如，它可能被命名为 `libncurses5-dev`。

> 提示：`X/Open` 规范定义了两个级别的 `curses` 函数库：基本 `curses` 函数库和扩展 `curses` 函数库。扩展 `curses` 函数库包含一组混杂的附加函数，比如处理多列字符和控制颜色的函数。

当对使用 `curses` 函数库的程序进行编译时，你必须在程序中包含头文件 `curses.h`，并在编译命令行中用 `-lcurses` 选项来链接 `curses` 函数库。在许多 `Linux` 系统中，你可以直接使用 `curses`，但你会发现实际使用的是更好的、更新的 `ncurses` 实现版本。

你可以检查自己的 `curses` 的配置情况，命令：

```shell
ls -l /usr/include/*curses.h
```

用来查看 `curses` 头文件，命令：

```shell
ls -l /usr/lib/lib*curses*
```

用来检查库文件。如果发现头文件 `curses.h` 和 `ncurses.h` 都只是链接文件，而且系统中存在一个 `ncurses` 库文件，那么你就可以使用如下命令来编译本章中的程序：

```shell
$ gcc program.c -o program -lcurses
```

但如果 `curses` 配置并未自动使用 `ncurses` 函数库，那么你可能不得不再程序中明确包含头文件 `ncurses.h` 而不是 `curses.h` 来强制使用 `ncurses` 函数库，同时需要执行如下的编译命令：

```shell
$ gcc -I/usr/include/ncurses program.c -o program -lncurses
```

其中，`-I` 选项用于指定搜索头文件的目录。