[toc]

### 1. 声明 int 变量

先写上 int，然后写变量名，最后加上一个分号。要声明多个变量，可以单独声明每个变量，也可在 int 后面列出多个变量名，变量名之间用逗号分隔。例如：

```c
int erns;
int hogs, cows, goats;
```

为变量提供值的方式有两种：

+ 赋值：`cows=112;`
+ 通过 `scanf()` 获取值。

### 2. 初始化变量

只需在变量名后面加上赋值运算符（`=`）和待赋给变量的值即可。例如：

```c
int hogs = 21;
int cows = 32, goats = 14;
int dogs, cats = 94;	/* 有效，但是这种格式很槽糕 */
```

### 3. 打印 int 值

可以使用 `printf()` 函数打印 `int` 类型的值。`%d` 称为转换说明，它指定了 `printf()` 应使用声明格式来显示一个值，同时指明了在一行中打印整数的位置。例如：

```c
/* print1.c - 演示 printf() 的一些特性 */
#include <stdio.h>
int main(void)
{
	int ten = 10;
	int two = 2;
	printf("Doing it right: ");
	printf("%d minus %d is %d\n", ten, 2, ten - two);
	printf("Doing it wrong: ");
	printf("%d minus %dis %d\n", ten);	// 遗漏 2 个参数
	return 0;
}
```

### 4. 八进制和十六进制

`0x` 或 `0X` 前缀表示十六进制值，所以十进制数 16 表示成十六进制是 `0x10` 或 `0X10`。`0` 前缀表示八进制。

### 5. 显示八进制和十六进制

不同的进制要使用不同的转换说明。以十进制显示数字，使用 `%d`；以八进制显示数字，使用 `%o`；以十六进制显示数字，使用 `%x`。另外，要显示各进制数的前缀 `0`、`0x` 和 `0X`，必须分别使用 `%#o`、`%#x`、`%#X`。例如：

```c
/* bases.c -- 以十进制、八进制、十六进制打印十进制数 100 */
#include <stdio.h>
int main(void)
{
	int x = 100;
	printf("dec = %d; octal = %o; hex = %x\n", x, x, x);
	printf("dec = %d; octal = %#o; hex = %#x\n", x, x, x);
	return 0;
}
```

### 6. 其他整数类型

#### 6.1 声明其他整数类型

```c
long int estine;
long johns;
short int erns;
short ribs;
unsigned int s_count;
unsigned players;
unsigned long headcount;
unsigned short yesvotes;
long long ago;
```

#### 6.2 long 常量和 long long 常量

要把一个较小的常量作为 `long` 类型对待，可以在值的末尾加上 `l`（小写的 `L`）或 `L` 后缀。类似地，在支持 `long long` 类型的系统中，也可以使用 `ll` 或 `LL` 后缀来表示 `long long` 类型的值，如 3LL。另外，`u` 或 `U` 后缀表示 `unsigneed long long`，如 `5ull`、`10LLU` 或 `9Ull`。

#### 6.3 打印 short、long、long long 和 unsigned 类型

C 语言有多种 `printf()` 格式。对于 `short` 类型，可以使用 `h` 前缀。`%hd` 表示以十进制显示 `short` 类型的整数，`%ho` 表示以八进制显示 `short` 类型的整数。`h` 和 `l` 前缀都可以和 `u` 一起使用，用于表示无符号类型。例如，`%lu` 表示打印 `unsigned long` 类型的值。例如：

```c
/* print2.c -- 更多 printf() 的特性 */
#include <stdio.h>
int main(void)
{
	unsigned int un = 3000000000;	/* int 为 32 位和 short 为 16 位的系统 */
	short end = 200;
	long big = 65537;
	long long verybig = 12345678908642;
	printf("un = %u and not %d\n", un, un);
	printf("end= %hd an %d\n", end, end);
	printf("big = %ld and not %hd\n", big, big);
	printf("verybig = %lld and not %ld\n", verybig, verybig);
	return 0;
}
```

### 7. 整型常量

<center><b>整型常量的例子</b></center>

| 类型               | 十六进制 | 八进制  | 十进制 |
| ------------------ | -------- | ------- | ------ |
| char               | \0x41    | \0101   | N.A.   |
| int                | 0x41     | 0101    | 65     |
| unsigned int       | 0x41u    | 0101u   | 65u    |
| long               | 0x41L    | 0101L   | 65L    |
| unsigned long      | 0x41UL   | 0101UL  | 65UL   |
| long long          | 0x41LL   | 0101LL  | 65LL   |
| unsigned long long | 0x41ULL  | 0101ULL | 65ULL  |

