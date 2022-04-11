[toc]

系统调用 read 的作用是：从与文件描述符 fildes 相关联的文件里读入 nbytes 个字节的数据，并把它们放到数据区 buf 中。它返回实际读入的字节数，这可能会小于请求的字节数。如果 read 调用返回 0，就表示未读入任何数据，已到达了文件尾；如果返回的是 -1，就表示 read 调用出现了错误。

### 1. read 系统调用原型

下面是 read 系统调用的原型：

```c
#include <unistd.h>

size_t read(int fildes, void *buf, size_t nbytes);
```

### 2. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>

int main()
{
    char buffer[128];
    int nread;
    nread = read(0, buffer, 128);
    if (nread == -1)
    {
		write(2, "A read error has occurred\n", 26);
	}
	if ((write(1, buffer, nread)) != nread)
	{
		write(2, "A write error has occurred\n", 27);
	}
	exit(0);
}
```

