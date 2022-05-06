`fopen` 库函数类似于底层的 open 系统调用。它主要用于文件和终端的输入输出。如果你需要对设备进行明确的控制，那最后使用底层系统调用，因为这可以避免用库函数带来的一些潜在问题，如输入/输出缓存。

该函数原型如下所示：

```cpp
#include <stdio.h>

FILE *fopen(const char *filename, const char *mode);
```

`fopen` 打开由 `filename` 参数指定的文件，并把它与一个文件流关联起来。`mode` 参数指定文件的打开方式，它取下列字符串中的值：

+ `r` 或 `rb`：以只读方式打开。
+ `w` 或 `wb`：以写方式打开，并把文件长度截短为零。
+ `a` 或 `ab`：以写方式打开，新内容追加在文件尾。
+ `r+` 或 `rb+` 或 `r+b`：以更新方式打开（读和写）。
+ `w+` 或 `wb+` 或 `w+b`：以更新方式打开，并把文件长度截短为零。
+ `a+` 或 `ab+` 或 `a+b`：以更新方式打开，新内容追加在文件尾。

> 提示：字母 b 表示文件是一个二进制文件而不是文本文件。

`fopen` 在成功时返回一个非空的 `FILE *` 指针，失败时返回 NULL 值，NULL 值在头文件 `stdio.h` 里定义。

可用的文件流数量和文件描述符一样，都是有限制的。实际的限制是由头文件 `stdio.h` 中定义的 `FOPEN_MAX` 来定义的，它的值至少为 8，在 Linux 系统中，通常是 16。

例如：

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	const int buffer_size = 1024;
	char buffer[buffer_size];
	FILE *fd;
	int count;
	int start;
	
	fd = fopen("/home/xiaotuan/test.py", "r");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}
	
	count = fread(buffer, sizeof(char), buffer_size, fd);
	while (count > 0)
	{
		for (int i = 0; i < count; i++)
		{
			putc(buffer[i], stdout);
		}
		count = fread(buffer, sizeof(char), buffer_size, fd);
	}
	
    fclose(fd);
    
	return 0;
}
```

