[toc]

lseek 系统调用对文件描述符 fildes 的读写指针进行设置。也就是说，你可以用它来设置文件的下一个读写位置。读写指针既可以被设置为文件中的某个绝对位置，也可以把它设置为相对于当前位置或文件尾的某个相对位置。

### 1. lseek 系统调用原型

下面是 lseek 系统调用的原型：

```c
#include <unistd.h>
#include <sys/types.h>

off_t lseek(int fildes, off_t offset, int whence);
```

### 2. 参数说明

offset 参数用来指定位置，而 whence 参数定义该偏移值的用法。whence 可以去下列值之一：

+ `SEEK_SET`：offset 是一个绝对值。
+ `SEEK_CUR`：offset 是相对于当前位置的一个相对位置。
+ `SEEK_END`：offset 是相对于文件尾的一个相对位置。

lseek 返回从文件头到文件指针被设置处的字节偏移值，失败时返回 -1。参数 offset 的类型 off_t 是一个与具体实现有关的整数类型，它定义在头文件 `sys/types.h` 中。

### 3. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>

int main() 
{
	char buff[50];
	int in;
	int nread;
	int location;
	
	in = open("file.in", O_RDONLY);
	if (in == -1) {
		write(2, "Unable open file.\n", 18);
		exit(1);
	}
	location = lseek(in, 100, SEEK_SET);
	if (location == -1) {
		write(2, "Seek position fail.\n", 20);
		exit(2);
	}
	if ((nread = read(in, buff, sizeof(buff))) > 0) 
	{
		write(1, buff, nread);
	}
	close(in);
	exit(0);
}
```

