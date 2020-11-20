[toc]

### 1. printf() 函数

请求 printf() 函数打印数据的指令要与待打印数据的类型相匹配。

<center>4.3 转换说明及其打印的输出结果</center>

| 转换说明 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| %a       | 浮点数、十六进制数和 p 记数法（C99/C11）                     |
| %A       | 浮点数、十六进制数和 p 记数法（C99/C11）                     |
| %c       | 单个字符                                                     |
| %d       | 有符号十进制整数                                             |
| %e       | 浮点数，e 记数法                                             |
| %E       | 浮点数，e 记数法                                             |
| %f       | 浮点数，十进制记数法                                         |
| %g       | 根据值的不同，自动选择 %f 或 %e。%e 格式用于指数小于 -4 或者大于或等于精度时 |
| %G       | 根据值的不同，自动选择 %f 或 %E。%E 格式用于指数小于 -4 或者大于或等于精度时 |
| %i       | 有符号十进制整数（与 %d 相同）                               |
| %o       | 无符号八进制整数                                             |
| %p       | 指针                                                         |
| %s       | 字符串                                                       |
| %u       | 无符号十进制整数                                             |
| %x       | 无符号十六进制整数，使用十六进制数 0f                        |
| %X       | 无符号十六进制整数，使用十六进制数 0F                        |
| %%       | 打印一个百分号                                               |

### 2. 使用 printf()

程序清单**4.6 printout.c**程序

```c
/* printout.c -- 使用转换说明 */
#include <stdio.h>

#define PI 3.141593

int main(void)
{
	int number = 7;
	float pies = 12.75;
	int cost = 7800;
	printf("The %d contestants ate %f berry pies.\n", number, pies);
	printf("The value of pi is %f.\n", PI);
	printf("Farewell! thou art too dear for my possessing,\n");
	printf("%c%d\n", '$', 2 * cost);
	return 0;
}
```

运行后输出如下：

```console
The 7 contestants ate 12.750000 berry pies.
The value of pi is 3.141593.
Farewell! thou art too dear for my possessing,
$15600
```

这是 printf() 函数的格式：

printf(格式字符串, 待打印项1, 待打印项2, ...);

> 警告：格式字符串中的转换说明一定要与后面的每个项相匹配。

### 3. printf() 的转换说明修饰符

在 % 和转换字符之间插入修饰符可修饰基本的转换说明。

<center>表4.4 printf() 的修饰符</center>

| 修饰符 | 含义                                                         |
| ------ | ------------------------------------------------------------ |
| 标记   | 表 4.5 描述了 5 种标记（-、+、空格、# 和 0），可以不使用标记或使用多个标记<br />示例："%-10d" |
| 数字   | 最小字段宽度<br />如果该字段不能容纳待打印的数字或字符串，系统会使用更宽的字段<br />示例："%4d" |
| .数字  | 精度<br />对于 %e、%E 和 %f 转换，表示小数点右边数字的位数<br />对于 %g 和 %G 转换，表示有效数字最大位数<br />对于 %s 转换，表示待打印字符的最大数量<br />对于整型转换，表示待打印数字的最小位数<br />如有必要，使用前导 0 来达到这个位数<br />只使用.表示气候跟随一个 0，所以 %.f 和 %.0f 相同<br />示例："%5.2f" 打印一个浮点数，字段宽度为 5 字符，其中小数点后有两位数字 |
| h      | 和整型转换说明一起使用，表示 short int 或 unsigned short int 类型的值<br />示例："%hu"、"%hx"、"%6.4hd" |
| hh     | 和整型转换说明一起使用，表示 signed char 或 unsigned char 类型的值<br />示例："%hhu"、"%hhx"、"%6.4hhd" |
| j      | 和整型转换说明一起使用，表示 intmax_t 或 uintmax_t 类型的值。这些类型定义在<br />stdint.h 中。示例："%jd"、"%8jx" |
| l      | 和整型转换说明一起使用，表示 long int 或 unsigned long int 类型的值<br />示例："%ld"、"%8lu" |
| ll     | 和整型转换说明一起使用，表示 long long int 或 unsigned long long int 类型的值（C99）<br />示例："%lld"、"%8llu" |
| L      | 和浮点转换说明一起使用，表示 long double 类型的值<br />示例："%Lf"、"%10.4Le" |
| t      | 和整型转换说明一起使用，表示  ptrdiff_t 类型的值。ptrdiff_t 是两个指针差值的类型（C99)<br />示例："%td"、"%12td" |
| z      | 和整型转换说明一起使用，表示 size_t 类型的值。size_t 是 sizeof 返回的类型（C99）<br />示例："%zd"、"%12zd" |

<center>表4.5 printf() 中的标记</center>

| 标记 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| -    | 待打印项左对齐，即，从字段的左侧开始打印该项<br />示例："%-20s" |
| +    | 有符号值若为正，则在值前面显示加号；若为负，则在值前面显示减号<br />示例："%+6.2f" |
| 空格 | 有符号值若为正，则在值前面显示前导空格（不显示任何符号）；若为负，则在值前面显示减号<br />+ 标记覆盖一个空格<br />示例："% 6.2f" |
| #    | 把结果转换为另一种形式。如果是 %o 格式，则以 0 开始；如果是 %x 或者 %X 格式，则以 0x 或 0X 开始；对于所有的浮点格式，# 保证了即使后面没有任何数字，也打印一个小数点字符。对于 %g 和 %G 格式， # 防止结果后面的 0 被删除。<br />示例："%#o"、"%#8.0f"、"%+#10.3e" |
| 0    | 对于数值格式，用前导 0 代替空格填充字段宽度。对于整数格式，如果出现 - 标记或指定精度，则忽略该标记。 |

程序清单**4.7 width.c**程序

```c
/* width.c -- 字段宽度 */
#include <stdio.h>

#define PAGES 959

int main(void)
{
	printf("*%d*\n", PAGES);
	printf("*%2d*\n", PAGES);
	printf("*%10d*\n", PAGES);
	printf("*%-10d*\n", PAGES);
	return 0;
}
```

运行程序输出如下：

```console
*959*
*959*
*       959*
*959       *
```

程序清单**4.8 floats.c**程序

```c
// floats.c -- 一些浮点型修饰符的组合
#include <stdio.h>

int main(void)
{
	const double RENT = 3852.99;	// const 变量
	printf("*%f*\n", RENT);
	printf("*%e*\n", RENT);
	printf("*%4.2f*\n", RENT);
	printf("*%3.1f*\n", RENT);
	printf("*%10.3f*\n", RENT);
	printf("*%10.3E*\n", RENT);
	printf("*%+4.2f*\n", RENT);
	printf("*%010.2f*\n", RENT);
	return 0;
}
```

运行输出如下：

```console
*3852.990000*
*3.852990e+03*
*3852.99*
*3853.0*
*  3852.990*
* 3.853E+03*
*+3852.99*
*0003852.99*
```

程序清单**4.9 flags.c**程序

```c
/* flags.c -- 演示一些格式标记 */
#include <stdio.h>

int main(void)
{
	printf("%x %X %#x\n", 31, 31, 31);
	printf("**%d**% d**% d**\n", 42, 42, 42);
	printf("**%5d**%5.3d**%05d**%05.3d**\n", 6, 6, 6, 6);
	return 0;
}
```

运行后输出如下：

```console
1f 1F 0x1f
**42** 42** 42**
**    6**  006**00006**  006**
```

程序清单**4.10 stringf.c**程序

```c
/* stringf.c -- 字符串格式 */
#include <stdio.h>

#define BLURB "Authentic imitation!"

int main(void)
{
	printf("[%2s]\n", BLURB);
	printf("[%24s]\n", BLURB);
	printf("[%24.5s]\n", BLURB);
	printf("[%-24.5s]\n", BLURB);
	return 0;
}
```

运行后输出如下：

```console
[Authentic imitation!]
[    Authentic imitation!]
[                   Authe]
[Authe                   ]
```

### 4. 转换说明的意义

转换说明把以二进制格式存储在计算机中的值转换成一系列字符（字符串）以便显示。转换可能会误导读者以为原始值被转替换成转换后的值。实际上，转换说明是翻译说明。

#### 4.1 转换不匹配

程序请单**4.11 intconv.c** 程序

```c
/* intconv.c -- 一些不匹配的整型转换 */
#include <stdio.h>

#define PAGES 336
#define WORDS 65618

int main(void)
{
	short num = PAGES;
	short mnum = -PAGES;
	printf("num as short and unsigned short: %hd %hu\n", num, num);
	printf("-num as short and unsigned short: %hd %hu\n", mnum, mnum);
	printf("num as int and char: %d %c\n", num, num);
	printf("WORDS as int, short, and char: %d %hd %c\n", WORDS, WORDS, WORDS);
	return 0;
}
```

运行后输出如下：

```console
num as short and unsigned short: 336 336
-num as short and unsigned short: -336 65200
num as int and char: 336 P
WORDS as int, short, and char: 65618 82 R
```

程序清单**4.12 floatcnv.c**程序

```c
/* floatcnv.c -- 不匹配的浮点类型转换 */
#include <stdio.h>

int main(void)
{
	float n1 = 3.0;
	double n2 = 3.0;
	long n3 = 200000000;
	long n4 = 1234567890;
	printf("%.1e %.1e %.1e %.1e\n", n1, n2, n3, n4);
	printf("%ld %ld\n", n3, n4);
	printf("%ld %ld %ld %ld\n", n1, n2, n3, n4);
	return 0;
}
```

运行输出如下：

```console
3.0e+00 3.0e+00 3.1e+46 1.8e-304
200000000 1234567890
0 1074266112 0 1074266112
```

#### 4.2 printf() 的返回值

printf() 函数也有一个返回值，它返回打印字符的个数。如果有输出错误，printf() 则返回一个复制（printf() 的旧版本会返回不同的值）。

程序清单**4.13 prntval.c**程序

```c
/* prntval.c -- printf() 的返回值 */
#include <stdio.h>

int main(void)
{
	int bph2o = 212;
	int rv;
	rv = printf("%d F is water's boiling point.\n", bph2o);
	printf("The printf() function printed %d characters.\n", rv);
	return 0;
}
```

运行后输出如下：

```console
212 F is water's boiling point.
The printf() function printed 32 characters.
```

> 注意，printf() 函数返回值计算针对所有字符数，包括空格和不可见的换行符（\n）。

#### 4.3 打印较长的字符串

有时，printf() 语句太长，在屏幕上不方便阅读。如果空白（空格、制表符、换行符）仅用于分隔不同的部分，C 编译器会忽略它们。因此，一条语句可以写成多行，只需在不同部分之间输入空白即可。

程序清单**4.14 longstrg.c**程序

```c
/* longstrg.c -- 打印较长的字符串 */
#include <stdio.h>

int main(void)
{
	printf("Here's one way to print a");
	printf("long string. \n");
	printf("Here's another way to print a \
long string.\n");
	printf("Here's the newest way to print a "
		"long string.\n");	/* ANSI C */
	return 0;
}
```

运行后输出如下：

```console
Here's one way to print along string.
Here's another way to print a long string.
Here's the newest way to print a long string.
```

方法1：使用多个 printf() 语句。

方法2： 用反斜杠（\）和 Enter（或 Return）键组合来断行。这使得光标移至下一行，而且字符串中不会包含换行符。但是，下一行代码必须和程序清单中的代码一样从最左边开始。如果缩进该行，比如缩进 5 个空格，那么这 5 个空格就会成为字符串的一部分。

方法3：ANSI C 引入的字符串连接。在两个用双引号括起来的字符串之间用空白隔开，C 编译器会把多个字符串看作是一个字符串。

### 5. 使用 scanf()

scanf() 和 printf() 类似，也使用格式字符串和参数列表。scanf() 中的格式字符串表明字符输入流的目标数据类型。两个函数主要的区别在参数列表中。printf() 函数使用变量、常量和表达式，而 scanf() 函数使用指向变量的指针。这里，读者不必了解如何使用指针，只需记住以下两条简单的规则：

+ 如果用 scanf() 读取基本变量类型的值，在变量名前加上一个 &;
+ 如果用 scanf() 把字符串读入字符数组中，不要使用 &.

程序清单**4.15 input.c**程序

```c
// input.c -- 何时使用&
#include <stdio.h>

int main(void)
{
	int age;	// 变量
	float assets;	// 变量
	char pet[30];	// 字符数组，用于存储字符串
	printf("Enter your age, assets, and favorite pet.\n");
	scanf("%d %f", &age, &assets);	// 这里要使用 &
	scanf("%s", pet);	// 字符数组不使用 &
	printf("%d $%.2f %s\n", age, assets, pet);
	return 0;
}
```

运行后输出如下：

```console
Enter your age, assets, and favorite pet.
38
92360.88 llama
38 $92360.88 llama
```

scanf() 函数使用空白（换行符、制表符和空格）把输入分成多个字段。在依次把转换说明和字段匹配时跳过空白。注意上面示例的输入项分成了两行。只要在每个输入项之间输入至少一个换行符、空格或制表符即可，可以在一行或多行输入。

<center>表4.6 ANSI C 中 scanf() 的转换说明</center>

| 转换说明       | 含义                                                         |
| -------------- | ------------------------------------------------------------ |
| %c             | 把输入解释成字符                                             |
| %d             | 把输入解释成有符号十进制整数                                 |
| %e、%f、%g、%a | 把输入解释成浮点数（C99 标准新增了 %a）                      |
| %E、%F、%G、%A | 把输入解释成浮点数（C99 标准新增了 %A）                      |
| %i             | 把输入解释成有符号十进制整数                                 |
| %o             | 把输入解释成有符号八进制                                     |
| %p             | 把输入解释成指针（地址）                                     |
| %s             | 把输入解释成字符串。从第 1 个非空白字符开始，到下一个空白字符之前的所有字符都是输入 |
| %u             | 把输入解释成无符号十进制整数                                 |
| %x、%X         | 把输入揭示出有符号十六进制整数                               |

<center>表4.7 scanf() 转换说明中的修饰符</center>

| 转换说明  | 含义                                                         |
| --------- | ------------------------------------------------------------ |
| *         | 抑制赋值（详见后面解释）<br />示例："%*d"                    |
| 数字      | 最大字段宽度。输入达到最大字段宽度处，或第1次遇到空白字符时停止<br />示例："%10s" |
| hh        | 把整数作为 signed char 或 unsigned char 类型读取<br />示例："%hhd"、"%hhu" |
| ll        | 把整数作为 long long 或 unsigned long long 类型读取（C99）<br />示例："%lld"、"%llu" |
| h、l 或 L | "%hd" 和 "%hi" 表明把对应的值存储为 short int 类型<br />"%ho"、"%hx" 和 "%hu" 表明把对应的值储存为 unsigned short int 类型<br />"%ld" 和 "%li" 表明把对应的值储存为 long 类型<br />"%lo"、"%lx" 和 "%lu" 表明把对应的值储存为 unsigned long 类型<br />"%le"、"%lf" 和 "%lg" 表明把对应的值储存为 double 类型<br />在 e、f 和 g 前面使用 L 而不是 l，表明把对应的值储存为 long double 类型。<br />如果没有修饰符，d、i、o 和 x 表明对应的值被储存为 int 类型，f 和 g 表明把对应的值储存为 float 类型 |
| j         | 在整型转换说明后面时，表明使用 intmax_t 或 uintmax_t 类型（C99）<br />示例： "%jd"、"%jo" |
| z         | 在整型转换说明后面时，表明使用 sizeof 的返回类型（C99）      |
| t         | 在整型转换说明后面时，表明使用表示两个指针差值的类型（C99）<br />示例："%td"、"%tx" |

scanf() 函数允许把普通字符放在格式字符串中。除空格字符外的普通字符必须与输入字符串严格匹配。例如，假设在两个转换说明中添加一个逗号：

```c
scanf("%d,%d", &n, &m);
```

scanf() 函数将其解释成：用户将输入一个数字、一个逗号，然后再输入一个数字。

scanf() 函数返回成功读取的项数。如果没有读取任何项，且需要读取一个数字而用户却输入一个非数值字符，scanf() 便返回 0。当 scanf() 检测到 "文件结尾" 时，会返回 EOF（EOF 是 stdio.h 中定义的特殊值，通常用 #define 指令把 EOF 定义为 -1）。

### 6. printf() 和 scanf() 的 * 修饰符

在 printf() 函数中，如果你不想预先指定字段宽度，希望通过程序来指定，那么可以用 * 修饰符代替字段宽度。但还是要用一个参数告诉函数，字段宽度应该是多少。

程序清单**4.16 varwid.c**程序

```c
/* varwid.c -- 使用变宽输出字段 */
#include <stdio.h>

int main(void)
{
	unsigned width, precision;
	int number = 256;
	double weight = 242.5;
	printf("Enter a field width:\n");
	scanf("%d", &width);
	printf("The number is : %*d:\n", width, number);
	printf("Now enter a width and a precision:\n");
	scanf("%d %d", &width, &precision);
	printf("Weight = %*.*f\n", width, precision, weight);
	printf("Done!\n");
	return 0;
}
```

运行后输出如下：

```console
Enter a field width:
6
The number is :    256:
Now enter a width and a precision:
8 3
Weight =  242.500
Done!
```

scanf() 中 * 的用法与此不同。把 * 放在 % 和转换字符之间时，会使得 scanf() 跳过相应的输出项。

程序清单**4.17 skip2.c** 程序

```c
/* skiptwo.c -- 跳过输入中的前两个整数 */
#include <stdio.h>

int main(void)
{
	int n;
	printf("Please enter three integers:\n");
	scanf("%*d %*d %d", &n);
	printf("The last integer was %d\n", n);
	return 0;
}
```

运行后输出如下：

```console
Please enter three integers:
2013 2014 2015
The last integer was 2015
```

### 7. printf() 的用法提示

想把数据打印成列，指定固定字段宽度很有用。因为默认的字段宽度时待打印数字宽度，如果同一列中打印的数字位数不同，那么下面的语句：

```c
printf("%d %d %d\n", val1, val2, val3);
```

打印出来的数字可能参差不齐。使用足够大的固定字段宽度可以让输出整齐美观。

