`fgets` 函数从输入文件流 stream 里读取一个字符串。

这些函数的原型如下所示：

```c
#include <stdio.h>

char *fgets(char *s, int n, FILE *stream);
char *gets(char *s);
```

`fgets` 把读到的字符写到 s 指向的字符串里，直到出现下面某种情况：遇到换行符，已经传输了 n - 1 个字符，或者达到文件尾。它会把遇到换行符也传递到接收字符串里，再加上一个表示结尾的空字节 `\0`。一次调用最多值能传输 n - 1 个字符，因为它必须把空字节加上以结束字符串。

当成功完成时，`fgets` 返回一个指向字符串 s 的指针。如果文件流已经达到文件尾，`fgets` 会设置这个文件流的 EOF 标识并返回一个空指针。如果出现读错误，`fgets` 返回一个空指针并设置 errno 以指出错误的类型。

`gets` 函数类似于 `fgets`，只不过它从标准输入读取数据并丢弃遇到的换行符。它在接收字符串的尾部加上一个 null 字节。

> 警告：`gets` 对传输字符的个数并没有限制，所以它可能会溢出自己的传输缓冲区。因此，应该避免使用它并使用 `fgets` 来代替。`gets` 在最新编译器中已经无法编译通过。

例如：

**fgets 的使用**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(void)
{
	const int read_size = 1024;
	FILE *fd;
	char str[1024];
	char *read_str;
	int result;
	
	fd = fopen("/home/xiaotuan/test.py", "r");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}

	read_str = fgets(str, read_size, fd);
	printf("%p", read_str);
	while (read_str)
	{
		printf("%s", read_str);
		read_str = fgets(str, read_size, fd);
	}
	
	if (errno)
	{
		printf("读取失败！错误代码：%d\n", errno);
	}
    
    fclose(fd);
    
	return 0;
}
```

