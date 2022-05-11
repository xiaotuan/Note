`printf` 系列函数能够对各种不同类型的参数进行格式编排和输出。每个参数在输出流中的表示形式由格式化参数 `format` 控制，它是一个包含需要输出的普通字符和称为转换控制符代码的字符串，转换控制符规定了其余的参数应该以何种方式被输出到何种地方。

它们的原型如下所示：

```c
#include <stdio.h>

int printf(const char *format, ...);
int sprintf(char *s, const char *format, ...);
int fprintf(FILE *stream, const char *format, ...);
```

`printf` 函数把自己的输出送到标准输出。`fprintf` 函数把自己的输出送到一个指定的文件流。`sprintf` 函数把自己的输出和一个结尾空字符写到作为参数传递过来的字符串 s 里。这个字符串必须足够容纳所有的输出函数。例如：

```c
printf("Some numbers: %d, %d, and %d\n", 1, 2, 3);
```

下面是一些常用的转换转换控制符：

+ `%d`，`%i` ：以十进制格式输出一个整数。
+ `%o`，`%x`：以八进制或十六进制格式输出一个整数。
+ `%c` ：输出一个字符。
+ `%s`：输出一个字符串。
+ `%f`：输出一个（单精度）浮点数。
+ `%e`：以科学计数法格式输出一个双精度浮点数。
+ `%g`：以通用格式输出一个双精度浮点数。

> 提示：要想输出 `%` 字符，需要使用 `%%` 。

让传递到 `printf` 函数里的参数数目和类型与 format 字符串里的转换控制符相匹配是非常重要的。整数参数的类型可以用一个可选的长度限定符来指定。它可以是 h，例如 `%hd` 表示这是一个短整数（short int），或者 `l`， 例如 `%ld` 表示这是一个长整数（long int）。例如：

```c
#include <stdio.h>

int main(void)
{
	char initial = 'A';
	char *surname = "Matthew";
	unsigned int age = 16;
	
	printf("Hello Mr %c %s, aged %u\n", initial, surname, age);
	
	return 0;
}
```

你可以利用字段限定符对数据的输出格式做进一步的控制。字段限定符是转换控制符里紧跟在 `%` 字符后面的数字。如下表所示：

| 格式   | 参数        | 输出           |
| ------ | ----------- | -------------- |
| %10s   | "Hello"     | \|     Hello\| |
| %-10s  | "Hello"     | \|Hello     \| |
| %10d   | 1234        | \|      1234\| |
| %-10d  | 1234        | \|1234      \| |
| %010d  | 1234        | \|0000001234\| |
| %10.4f | 12.34       | \|   12.3400\| |
| %*s    | 10, "Hello" | \|     Hello\| |

> 注意：负值的字段宽度表示数据在该字段里以左对齐的格式输出。可变字段宽度用一个星号（*）来表示。在这种情况下，下一个参数用来表示字段宽度。`%` 字符后面以 0 开头表示数据前面要用数字 0 填充。根据 POSIX 规范的要求，`printf` 不对数据字段进行截断，而是扩充数据字段以适应数据的宽度。

`printf` 函数返回一个整数以表明它输出的字符个数。但在 `sprintf` 的返回值里没有算上结尾的那个 `null` 空字符。如果发生错误，这些函数返回一个负值并设置 `errno`。

例如：

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>


int main(void)
{
	const unsigned int STR_LENGTH = 100;
	
	int fd;
	char str[STR_LENGTH];
	FILE *file;

	fd = open("./printf.txt", O_CREAT|O_EXCL|O_APPEND, S_IRUSR|S_IWUSR|S_IRGRP|S_IWGRP);
	
	if (fd == -1)
	{
		write(2, "Unable create file printf.txt", 29);
		return -1;
	}
	
	close(fd);
	
	printf("这是 printf 函数输出的信息！\n");
	
	sprintf(str, "这是通过 sprintf 函数生成的字符串，它的长度为: %u\n", STR_LENGTH);
	printf("%s", str);
	
	file = fopen("./printf.txt", "a+");
	if (!file)
	{
		printf("无法打开文件 printf.txt！\n");
		return -2;
	}
	fprintf(file, "这是通过 sprintf 函数写入的内容，该文件名为：%s\n", "printf.txt");
	return 0;
}
```

