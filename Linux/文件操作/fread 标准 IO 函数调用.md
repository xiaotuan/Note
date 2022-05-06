`fread` 库函数用于从一个文件流里读取数据。数据从文件流 stream 读到由 ptr 执行的数据缓冲区里，`fread` 和 `fwrite` 都是对数据记录进行操作，size 参数指定每个数据记录的长度，计数器 nitems 给出要传输的记录个数。它的返回值是成功读到数据缓冲区里的记录个数（而不是字节数）。当到达文件尾时，它的返回值可能会小于 nitems，甚至可以是零。

该函数原型如下所示：

```c
#include <stdio.h>

size_t fread(void *ptr, size_t size, size_t nitems, FILE *stream);
```

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



