[toc]

系统调用 write 的作用是把缓冲区 buf 的前 nbytes 个字节写入与文件描述符 fildes 关联的文件中。它返回实际写入的字节数。如果文件描述符有误或者底层的设备驱动程序对数据块长度比较敏感，该返回值可能小于 nbytes。如果这个函数返回 0，就表示未写入任何数据；如果它返回的是 -1，就表示在 write 调用中出现了错误，错误代码报错在全局变量 errno 里。

### 1. write 系统调用原型

下面是 write 系统调用的原型：

```c
#include <unistd.h>

size_t write(int fildes, const void *buf, size_t nbytes);
```

### 2. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main()
{
    if ((write(1, "Here is some data\n", 18)) != 18) 
    {
        write(2, "A write error has occurred on file descriptor 1\n", 46);
    }
    char errnoStr[10];
    sprintf(errnoStr, "Errno: %d\n", errno);
    write(1, errnoStr, 10);
    exit(0);
}

```

> 提示
>
> 1. 当程序退出运行时，所有已经打开的文件描述符都会自动关闭，所以你不需要明确地关闭它们。但处理被缓存的输出时，情况就不一样了。
> 2. 