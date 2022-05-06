`fwrite` 库函数与 `fread` 有相似的接口。它从指定的数据缓冲区里取出数据记录，并把它们写到输入流中。它的返回值是成功写入的记录个数。

该函数原型如下所示：

```c
#include <stdio.h>

size_t fwrite(const void *ptr, size_t size, size_t nitems, FILE *stream);
```

> 注意：不推荐把 `fread` 和 `fwrite` 用于结构化数据。部分原因在于用 `fwrite` 写的文件在不同的计算机体系结构之间可能不具备可移植性。

例如：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(void)
{
	const int buffer_size = 1024;
	char buffer[buffer_size];
	char *write_content = "这是通过 fwrite 写入的数据。\n";
	FILE *fd;
	int count;
	int start;
	int seek_result;
	
	fd = fopen("/home/xiaotuan/test.py", "a+");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}
	
	count = fwrite(write_content, sizeof(char), strlen(write_content), fd);
	if (count == strlen(write_content))
	{
		printf("写入数据成功！\n");
	} else {
		printf("写入数据失败！\n");
		exit(-2);
	}
	
	printf("下面是修改后的内容：\n");
	seek_result = fseek(fd, 0, SEEK_SET);
	if (seek_result) {
		printf("移动读取位置失败。错误代码: %d", errno);
		exit(-3);
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

