[toc]

dup 系统调用提供了一种复制文件描述符的方法，使我们能够通过两个或更多个不同的描述符来访问同一个文件。这可以用于在不同位置对数据进行读写。dup 系统调用则是通过明确指定目标描述符来把一个文件描述符复制为另外一个。

### 1. dup 和 dup2 系统调用原型

下面是 dup 和 dup2 系统调用的原型：

```c
#include <unistd.h>

int dup(int fildes);
int dup2(int fildes, int fildes2);
```

### 2. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdio.h>

int main() 
{
	int in;
	int other;
	struct stat info;
	
	in = open("file.in", O_WRONLY | O_APPEND);
	if (in == -1) {
		write(2, "Unable open file.\n", 18);
		exit(1);
	}
	other = dup(in);
	write(other, "This is write by other fildes.\n", 31);
	close(in);
	exit(0);
}
```

