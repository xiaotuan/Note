`fgetc` 函数从文件流里取出下一个字节并把它作为一个字符返回。当它到达文件尾货出现错误时，它返回 EOF。你必须通过 `ferror` 或 `feof` 来区分这两种情况。

这些函数的原型如下所示：

```c
#include <stdio.h>

int fgetc(FILE *stream);
int getc(FILE *stream);
int getchar();
```

`getc` 函数的作用和 `fgetc` 一样，但它有可能被实现为一个宏，如果是这样，stream 参数就可能被计算不止一次，所以它不能有副作用（例如，它不能影响变量）。此外，你也不能保证能够使用 `getc` 的地址作为一个函数指针。

`getchar` 函数的作用相当于 `getc(stdin)`，它从标准输入里读取下一个字符。

例如：

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(void)
{
	FILE *fd;
	int ch;
	
	fd = fopen("/home/xiaotuan/test.py", "r");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}

	ch = fgetc(fd);
	while (ch != EOF)
	{
		putc(ch, stdout);
		ch = getc(fd);
	}
	
	if (ferror(fd))
	{
		printf("读取文件失败！\n");
	}
	
	if (feof(fd))
	{
		printf("已读取完文件！请输入 q 结束程序：");
		ch = getchar();
		getchar();
		while (ch != 'q')
		{
			printf("输入错误。请重新输入：");
			ch = getchar();
			getchar();
		}
	}
	
	fclose(fd);
	return 0;
}
```

