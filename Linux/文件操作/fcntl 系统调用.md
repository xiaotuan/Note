`fcntl` 系统调用对底层文件描述符提供了更多的操纵方法。该函数原型如下所示：

```c
#include <fcntl.h>

int fcntl(int fildes, int cmd);
int fcntl(int fildes, int cmd, long arg);
```

利用 `fcntl` 系统调用，你可以对打开的文件描述符执行各种操纵，包括对它们进行复制、获取和设置文件描述符标志、获取和设置文件状态标志，以及管理建议性文件锁等。

对不同操纵的选择是通过选取命令参数 `cmd` 不同的值来实现的，其取值定义在头文件 `fcntl.h` 中。根据所选择命令的不同，系统调用可能还需要第三个参数 `arg`。

+ `fcntl(fildes, F_DUPFD, newfd)`：这个调用返回一个新的文件描述符，其数值等于或大于整数 newfd。新文件描述符是描述符 fildes 的一个副本。根据已打开文件数目和 newfd 值的情况，它的效果可能和系统调用 `dup(fildes)` 完全一样。
+ `fcntl(fildes, F_GETFD)` ：这个调用返回在 `fcntl.h` 头文件里定义的文件描述符标志，其中包括 `FD_CLOEXEC`，它的作用是决定是否在成功调用了某个 `exec` 系列的系统调用之后关闭该文件描述符。
+ `fcntl(fildes, F_SETFD, flags)`：这个调用用于设置文件描述符标志，通常仅用来设置 `FD_CLOEXEC`。
+ `fcntl(fildes, F_GETFL)` 和 `fcntl(fildes, F_SETFL, flags)`：这两个调用分别用来获取和设置文件状态标志和访问模式。你可以利用在 `fcntl.h` 头文件中定义的掩码 `O_ACCMODE` 来提取出文件的访问模式。其他标志包括那些当 `open` 调用使用 `O_CREAT` 打开文件时作为第三参数出现的标志。注意，你不能设置所有的标志，特别是不能通过 `fcntl` 设置文件的权限。