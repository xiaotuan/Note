`fseek` 函数是与 `lseek` 系统调用对应的文件流函数。它在文件流里为下一次读写操作指定位置。offset 和 whence 参数的含义与 `lseek` 系统调用完全一样。但 `lseek` 返回的是一个 off_t 数值，而 `fseek` 返回的是一个整数：0 表示成功， -1 表示失败并设置 errno 支持错误。

whence 可以去下列值之一：

+ `SEEK_SET`：offset 是一个绝对值。
+ `SEEK_CUR`：offset 是相对于当前位置的一个相对位置。
+ `SEEK_END`：offset 是相对于文件尾的一个相对位置。

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

