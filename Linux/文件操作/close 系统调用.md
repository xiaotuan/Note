[toc]

可以使用 close 调用终止文件描述符 fildes 与其对应文件的关联。文件描述符被释放并能够重新使用。close 调用成功时返回 0，出错时返回 -1。

### 1. close 系统调用原型

下面是 close 系统调用的原型：

```c
#include <unistd.h>

int close(int fildes);
```

> 注意
>
> 检查 close 调用的返回结果非常重要。有的文件系统，特别是网络文件系统，可能不会在关闭文件之前报告文件写操作中出现的错误，这是因为在写操作时，数据可能未被确认写入。

### 2. 实例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() 
{
    int fd = creat("myfile", S_IRUSR|S_IWUSR|S_IRGRP);
	if (fd == -1)
	{
		write(2, "Unable create myfile file\n", 26);
		exit(1);
	}
	if ((write(fd, "This is new file content.\n", 26)) != 26) {
		write(2, "Write content failed.\n", 22);
	}
    if (close(fd) != 0) {
		write(2, "Close file error.\n", 18);
	}
	exit(0);
}
```

