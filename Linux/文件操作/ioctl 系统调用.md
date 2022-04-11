[toc]

ioctl 调用有点像是个大杂烩。它提供了一个用于控制设备及其描述符行为和配置底层服务的接口。终端、文件描述符、套接字甚至磁带机都可以有为它们定义的 ioctl。

### 1. ioctl 系统调用原型

下面是 ioctl 系统调用的原型：

```c
#include <unistd.h>

int ioctl(int fildes, int cmd, ...);
```

ioctl 对描述符 fildes 引用的对象执行 cmd 参数中给出的操作。根据特定设备所支持操作的不同，它还可能会有一个可选的第三个参数。

### 2. 示例代码

在 Linux 系统上对 ioctl 的如下调用将打开键盘上的 LED 等：

```c
ioctl(tty_fd, KDSETLED, LED_NUM|LED_CAP|LED_SCR);
```

