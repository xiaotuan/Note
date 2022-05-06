`fputc` 函数把一个字符写到一个输出文件流中。它返回写入的值，如果失败，则返回 EOF。

这些函数的原型如下所示：

```c
#include <stdio.h>

int fputc(int c, FILE *stream);
int putc(int c, FILE *stream);
int putchar(int c);
```

类似于 `fgetc` 和 `getc` 之间的关系，`putc` 函数的作用也相当于 `fputc`，但它可能被实现为一个宏。

`putchar` 函数相当于 `putc(c, stdout)`，它把单个字符写到标准输出。注意，`putchar` 和 `getchar()` 都是把字符当作 int 类型而不是 char 类型来使用的。这就允许文件尾（EOF）标识取值 -1，这是一个超出字符数字编码范围的值。

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
	char *write_content = "这是通过 fputc 和 putc 写入的数据。\n";
	char *tip = "写入数据成功！";
	FILE *fd;
	int write_result;
	int count;
	int seek_result;
	
	fd = fopen("/home/xiaotuan/test.py", "a+");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}
	
	for (int i = 0; i < strlen(write_content); i++)
	{
		if (i % 2 == 0)
		{
			write_result = fputc(write_content[i], fd);
		} else {
			write_result = putc(write_content[i], fd);
		}
		if (write_result == EOF)
		{
			printf("写入文件失败！\n");
			fclose(fd);
			exit(-2);
		}
	}
	
	for (int i = 0; i < strlen(tip); i++)
	{
		putchar(tip[i]);
	}
	putchar('\n');
	
	printf("下面是修改后的内容：\n");
	seek_result = fseek(fd, 0, SEEK_SET);
	if (seek_result) {
		printf("移动读取位置失败。错误代码: %d", errno);
		fclose(fd);
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

