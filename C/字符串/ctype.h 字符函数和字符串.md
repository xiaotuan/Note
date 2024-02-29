`ctype.h` 头文件包含了与字符相关的函数，虽然这些函数不能处理整个字符串，但是可以处理字符串中的字符。

**程序清单 mod_str.c**

```c
/* mod_str.c -- 修改字符串 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define LIMIT 81

void ToUpper(char*);
int PunctCount(const char*);

int main(void)
{
	char line[LIMIT];
	char* find;
	puts("Please enter a line:");
	fgets(line, LIMIT, stdin);
	find = strchr(line, '\n');	// 查找换行符
	if (find)	// 如果地址不是 NULL,
		*find = '\0';	// 用空字符替换
	ToUpper(line);
	puts(line);
	printf("That line has %d punctuation characters.\n", PunctCount(line));
	return 0;
}

void ToUpper(char* str)
{
	while (*str)
	{
		*str = toupper(*str);
		str++;
	}
}

int PunctCount(const char* str)
{
	int ct = 0;
	while (*str)
	{
		if (ispunct(*str))
			ct++;
		str++;
	}
	return ct;
}
```

运行结果如下：

```shell
$ gcc mod_str.c 
$ ./a.out 
Please enter a line:
Me? You talkin' to me? Get outta here!
ME? YOU TALKIN' TO ME? GET OUTTA HERE!
That line has 4 punctuation characters.
```

