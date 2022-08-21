[toc]

### 1. termios 结构

`termios` 是在 POSIX 规范中定义的标准接口，它类似于系统 V 中的 `termio` 接口。通过设置 `termios` 类型的数据结构中的值和使用一小组函数调用，你就可以对终端接口进行控制。`termios` 数据结构和相关函数调用都定义在头文件 `termios.h` 中。

> 注意：如果程序需要调用定义在 `termios.h` 头文件中的函数，它就需要与一个正确的函数库进行链接，这个函数库可能是标准的 C 函数库或者 `curses` 函数库（取决于你的安装情况）。如果需要，在编译本章中的实例程序时，在编译命令的末尾加上 `-lcurses`。在一些老版本的 Linux 系统中，`curses` 库被命名为 `new curses`。在这种情况下，库名和链接参数就需要相应地改为 `ncurses` 和 `-lncurses`。

可以被调整来影响终端的值按照不同的模式被分成如下几组：

+ 输入模式
+ 输出模式
+ 控制模式
+ 本地模式
+ 特殊控制字符

最小的 `termios` 结构的典型定义如下（X/Open 规范允许包含附加字段）：

```c
#include <termios.h>
struct termios {
    tcflag_t c_iflag;
    tcflag_t c_oflag;
    tcflag_t c_cflag;
    tcflag_t c_lflag;
    cc_t c_cc[NCCS];
};
```

### 2. 获取终端的 termios 结构

你可以调用函数 `tcgetattr` 来初始化与一个终端对应的 `termios` 结构，该函数的原型如下：

```c
#include <termios.h>

int tcgetattr(int fd, struct termios *termios_p);
```

### 3. 设置终端的 termios 结构

这个函数调用把当前终端接口变量的值写入 `termios_p` 参数指向的结构。如果这些值其后被修改了，你可通过调用函数 `tcsetattr` 来重新配置终端接口，该函数的原型如下：

```c
#include <termios.h>

int tcsetattr(int fd, int actions, const struct termios *termios_p);
```

参数 `actions` 控制修改方式，共有 3 种修改方式，如下所示：

+ **TCSANOW：**立刻对值进行修改。
+ **TCSADRAIN：**等当前的输出完成后再对值进行修改。
+ **TCSAFLUSH：**等当前的输出完成后再对值进行修改，但丢弃还未从 read 调用返回的当前可用的任何输入。

> 注意：程序有责任将终端设置恢复到程序开始运行之前的状态，这一点是非常重要的。首先保存这些值，然后在程序结束时恢复它们，这永远是程序的职责。

### 4. 输入模式

输入模式控制输入数据（终端驱动程序从串行口或键盘接收到的字符）在被传递给程序之前的处理方式。你通过设置 `termios` 结构中 `c_iflag` 成员的标志对它们进行控制。所有的标志都被定义为宏，并可通过按位或的方式结合起来。这也是所有终端模式都采用的方法。

可用于 `c_iflag` 成员的宏如下所示：

+ **BRKINT：**当在输入行中检测到一个终止状态（连接丢失）时，产生一个中断。
+ **IGNBRK：**忽略输入行中的终止状态。
+ **ICRNL：**将接收到的回车符转换为新行符。
+ **IGNCR：**忽略接收到的回车符。
+ **INLCR：**将接收到的新行符转换为回车符。
+ **IGNPAR：**忽略奇偶校验错误的字符。
+ **INPCK：**对接收到的字符执行奇偶校验。
+ **PARMRK：**对奇偶校验错误做出标记。
+ **ISTRIP：**将所有接收到的字符裁减为 7 比特。
+ **IXOFF：**对输入启用软件流控。
+ **IXON：**对输出启用软件流控。

> 注意：如果 **BRKINT** 和 **IGNBRK** 标志都未被设置，则输入行中的终止状态就背读取为 NULL（0x00）字符。

### 5. 输出模式

输出模式控制输出字符的处理方式，即由程序发送出去的字符在传递到串行口或屏幕之前是如何处理的。你通过设置 `termios` 结构中 `c_oflag` 成员的标志对输出模式进行控制。可用于 `c_oflag` 成员的宏如下所示：

+ **OPOST：**打开输出处理功能。
+ **ONLCR：**将输出中的换行符转换为回车/换行符。
+ **OCRNL：**将输出中的回车符转换为新行符。
+ **ONOCR：**在第 0 列不输出回车符。
+ **ONLRET：**不输出回车符。
+ **OFILL：**发送填充字符以提供延时。
+ **OFDEL：**用 DEL 而不是 NULL 字符作为填充字符。
+ **NLDLY：**新行符延时选择。
+ **CRDLY：**回车符延时选择。
+ **TABDLY：**制表符延时选择。
+ **BSDLY：**退格延时选择。
+ **VTDLY：**垂直制表符延时选择。
+ **FFDLY：**换页符延时选择。

> 注意：如果没有设置 **OPOST**，则所有其他标志都被忽略。

### 6. 控制模式

控制模式控制终端的硬件特性。你通过设置 `termios` 结构中 `c_cflag` 成员的标志对控制模式进行配置。可用于 `c_cflag` 成员的宏如下所示：

+ **CLOCAL：**忽略所有调制解调器的状态行。
+ **CREAD：**启用字符接收器。
+ **CS5：**发送或接收字符时使用 5 比特。
+ **CS6：**发送或接收字符时使用 6 比特。
+ **CS7：**发送或接收字符时使用 7 比特。
+ **CS8：**发送或接收字符时使用 8 比特。
+ **CSTOPB：**每个字符使用两个停止位而不是一个。
+ **HUPCL：**关闭时挂断调制解调器。
+ **PARENB：**启用奇偶校验码的生成和检测功能。
+ **PARODD：**使用奇校验而不是偶校验。

> 注意：如果设置了 HUPCL 标志，当终端驱动程序检测到与终端对应的最后一个文件描述符被关闭时，它将通过设置调制解调器的控制线来挂断电话线路。

### 7. 本地模式

本地模式控制终端的各种特性。你通过设置 `termios` 结构中 `c_lflag` 成员的标志对本地模式进行配置。可用于 `c_lflag` 成员的宏如下所示：

+ **ECHO：**启用输入字符的本地回显功能。
+ **ECHOE：**接收到 ERASE 时执行退格、空格、退格的动作组合。
+ **ECHOK：**接收到 KILL 字符时执行行删除操作。
+ **ECHONL：**回显新行符。
+ **ICANON：**启用标准输入处理（参加下面的说明）。
+ **IEXTEN：**启用基于特定实现的函数。
+ **ISIG：**启用信号。
+ **NOFLSH：**禁止清空队列。
+ **TOSTOP：**在试图进行写操作之前给后台进程发送一个信号。

> 提示：这里最重要的两个标志是 **ECHO** 和 **ICANON**。前者的作用是抑制键入字符的回显，而后者是将终端在两个截然不同的接收字符处理模式间进行切换。如果设置了 **ICANON** 标志，就启用标准输入行处理模式，否则，就启用非标准模式。

### 8 特殊控制字符

特殊控制字符是一些字符组合，如 <kbd>Ctrl</kbd> + <kbd>C</kbd>，当用户键入这样的组合键时，终端会采用一些特殊的处理方式。`termios` 结构中的 `c_cc` 数组成员将各种特殊控制字符映射到对应的支持函数。每个字符的位置（它在数组中的下标）是由一个宏定义的，但并不限制这些字符必须是控制字符。

根据终端是否被设置为标准模式（即 `termios` 结构中 `c_lflag` 成员是否设置了 **ICANON** 标志），`c_cc` 数组有两种差别很大的用法。

要特别注意的一点是，在两种不同的模式下，数组下标值有一部分是重叠的。处于这个原因，你一定要注意不要将两种模式各自的下标值混用。

下面是在标准模式中可以使用的数组下标：

+ **VEOF：**EOF 字符。
+ **VEOL：**EOL 字符。
+ **VERASE：**ERASE 字符。
+ **VINTR：**INTR 字符。
+ **VKILL：**KILL 字符。
+ **VQUIT：**QUIT 字符。
+ **VSUSP：**SUSP 字符。
+ **VSTART：**START 字符。
+ **VSTOP：**STOP 字符。

下面是在非标准模式中可以使用的数组下标：

+ **VINTR：**INTR 字符。
+ **VMIN：**MIN 值。
+ **VQUIT：**QUIT 字符。
+ **VSUSP：**SUSP 字符。
+ **VTIME：**TIME 值。
+ **VSTART：**START 字符。
+ **VSTOP：**STOP 字符。

#### 8.1 字符

| 字符  | 说明                                                         |
| ----- | ------------------------------------------------------------ |
| INTR  | 该字符使终端驱动程序向与终端相连的进程发送 SIGINT 信号。     |
| QUIT  | 该字符使终端驱动程序向与终端相连的进程发送 SIGQUIT 信号。    |
| ERASE | 该字符使终端驱动程序删除输入行中的最后一个字符               |
| KILL  | 该字符使终端驱动程序删除整个输入行                           |
| EOF   | 该字符使终端驱动程序将输入行中的全部字符传递给正在读取输入的应用程序。如果输入行为空，read 调用将返回 0，就好像在文件结尾调用 read 一样 |
| EOL   | 该字符的作用类似行结束符，效果和常用的新行符相同。           |
| SUSP  | 该字符使终端驱动程序向与终端相连的进程发送 SIGSUSP 信号。如果你的 UNIX 系统支持作业控制功能，当前应用程序将被挂起。 |
| STOP  | 该字符的作用是 ”截流“，即阻止向终端的进一步输出。它用于支持 XON/XOFF 流控，通常被设置为 ASCII 的 XOFF 字符，即组合键 <kbd>Ctrl</kbd> + <kbd>S</kbd> |
| START | 该字符重新启动被 STOP 字符暂停的输出，它通常被设置为 ASCII 的 XON 字符 |

#### 8.2 TIME 和 MIN 值

**TIME** 和 **MIN** 的值只能用于非标准模式，两者结合起来共同控制对输入的读取。此外，两者的结合使用还能控制在一个程序试图读取与一个终端关联的文件描述符时将发生的情况。

两者的结合分为如下 4 种情况：

+ **MIN = 0** 和 **TIME = 0**：在这种情况下，read 调用总是立刻返回。如果有等待处理的字符，它们就会被返回；如果没有字符等待处理，read 调用返回 0，并且不读取任何字符。
+ **MIN = 0** 和 **TIME > 0**：在这种情况下，只要有字符可以处理或者是经过 TIME 个十分之一秒的时间间隔，read 调用就返回。如果因为超时而未读到任何字符，read 返回 0，否则 read 返回读取的字符数目。
+ **MIN > 0** 和 **TIME = 0**：在这种情况下，read 调用将一直等待，直到有 MIN 个字符可以读取时才返回，返回值是读取的字符数量。到达文件尾时返回 0。
+ **MIN > 0** 和 **TIME > 0**：这是最复杂的一种情况。当 read 被调用时，它会等待接收一个字符。在接收到第一个字符及后续的每个字符后，一个字符间隔定时器被启动（如果定时器已在运行，则重启它）。当有 MIN 个字符可读或两个字符之间的时间间隔超过 TIME 个十分之一秒时，read 调用返回。这个功能可用于区分是单独按下了 Escape 键还是按下一个以 Escape 键开始的功能组合键。但要注意的是，网络通信或处理器的高负载将使得类似这样的定时器失去作用。

通过设置非标准模式与使用 MIN 和 TIME 值，程序可以逐个字符地处理输入。

#### 8.3 通过 shell 访问终端模式

如果在使用过 shell 时向查看当前的 termios 设置情况，可以使用下面的命令：

```shell
$ stty -a
speed 38400 baud; rows 32; columns 103; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>;
start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany -imaxbel
iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho
-extproc
```

当在做终端控制的练习时，一不小心就会将终端设置为非标准状态，这将使得终端的使用非常困难。下面几种方法可以帮你摆脱这种困境。

+ 第一中方法的使用如下命令（这要求你的 stty 版本支持这种用法）：

  ```shell
  $ stty sane
  ```

+ 如果回车键和新行符（（用于终止输入行）的映射关系丢失了，你可能就需要输入命令 `stty sane`，然后按下 <kbd>Ctrl</kbd> + <kbd>J</kbd> （它对应新行符），而不是按下回车键 <kbd>Enter</kbd>。

+ 第二种方法是用命令 `stty -g` 将当前的 `stty` 设置保存到某种可以重新读取的形式中。使用的命令如下：

  ```shell
  $ stty -g > save_stty
  ...
  <experiment with settings>
  ...
  $ stty $(cat save_stty)
  ```

+ 注意，对最后一个 stty 命令，你可能还需要使用 <kbd>Ctrl</kbd> + <kbd>J</kbd> 的组合键来代替回车键 <kbd>Enter</kbd>。你也可以在 shell 脚本中使用相同的方法：

  ```shell
  save_stty="$(stty -g)"
  <alter stty settings>
  stty $save_stty
  ```

+ 如果上面两种方法都不能解决问题，还有第三种方法，就是从另一个终端登录，用 ps 命令查找不能使用的那个 shell 的进程号，然后用命令 `kill HUP <进程号>` 强制中止该 shell。因为系统总是在给出登录提示符之前重置 stty 参数，所以你就可以正常地登录系统了。

#### 8.4 在命令提示符下设置终端模式

你还可以在命令提示符下用 stty 命令直接设置终端模式。

比如说，如果想让 shell 脚本可以读取单字符，你就需要关闭终端的标准模式，同时将 MIN 设为 1，TIME 设为 0.使用的命令如下：

```shell
$ stty -icanon min 1 time 0
```

你还可以对密码检查程序加以改进，在程序提示输入密码前将回显功能关闭。使用的命令如下：

```shell
$ stty -echo
```

> 注意：在使用上面命令之后要记住用命令 `stty echo` 将回显功能再次恢复启用。
