[toc]

### 1. 声明 char 类型变量

```c
char response;
char itable, latan;
```

### 2. 字符常量和初始化

在 C 语言中，用单引号括起来的单个字符被称为字符常量，例如：

```c
char broiled;	/* 声明一个 char 类型的变量 */
broileed = 'T';	/* 为其赋值，正确 */
```

实际上，字符是以数值形式存储的，所以也可以使用数字代码值来赋值：

```c
char grade = 65;	/* 对与 ASCII，这样做没有问题，但这是一种不好的编程风格 */
```

### 3.打印字符

`printf()` 函数用`%c` 指明待打印的字符。如果用 `%d` 转换说明打印 `char` 类型变量的值，打印的是一个整数。例如：

```c
/* charcode.c -- 显示字符的代码编号 */
#include <stdio.h>
int main(void)
{
	char ch;
	printf("Please enter a character.\n");
	scanf("%c", &ch);	/* 用户输入字符 */
	printf("The code for %c is %d.\n", ch, ch);
	return 0;
}
```

### 4. 有符号字符和无符号字符

有些 C 编译器把 `char` 实现为有符号类型，这意味着 `char` 可表示的范围是 -128 ~ 127 。而有些 C 编译器把 `char` 实现为无符号类型，那么 `char` 可表示的范围是 0 ~ 255。

根据 C90 标准，C 语言允许在关键字 `char` 前面使用 `signed` 或 `unsigned`，`signed char` 表示有符号类型，而 `unsigned char` 表示无符号类型。
