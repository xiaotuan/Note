### 11.7　 `ctype.h` 字符函数和字符串

第7章中介绍了 `ctype.h` 系列与字符相关的函数。虽然这些函数不能处理整个字符串，但是可以处理字符串中的字符。例如，程序清单11.30中定义的 `ToUpper()` 函数，利用 `toupper()` 函数处理字符串中的每个字符，把整个字符串转换成大写；定义的 `PunctCount()` 函数，利用 `ispunct()` 统计字符串中的标点符号个数。另外，该程序使用 `strchr()` 处理 `fgets()` 读入字符串的换行符（如果有的话）。

程序清单11.30　 `mod_str.c` 程序

```c
/* mod_str.c -- 修改字符串 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define LIMIT 81
void ToUpper(char *);
int PunctCount(const char *);
int main(void)
{
     char line[LIMIT];
     char * find;
     puts("Please enter a line:");
     fgets(line, LIMIT, stdin);
     find = strchr(line, '\n');    // 查找换行符
     if (find)                // 如果地址不是 NULL，
          *find = '\0';            // 用空字符替换
     ToUpper(line);
     puts(line);
     printf("That line has %d punctuation characters.\n", PunctCount(line));
     return 0;
}
void ToUpper(char * str)
{
     while (*str)
     {
          *str = toupper(*str);
          str++;
     }
}
int PunctCount(const char * str)
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

`while (` * `str)` 循环处理 `str` 指向的字符串中的每个字符，直至遇到空字符。此时* `str` 的值为 `0` （空字符的编码值为 `0` ），即循环条件为假，循环结束。下面是该程序的运行示例：

```c
Please enter a line:
Me? You talkin' to me? Get outta here!
ME? YOU TALKIN' TO ME? GET OUTTA HERE!
That line has 4 punctuation characters.

```

`ToUpper()` 函数利用 `toupper()` 处理字符串中的每个字符（由于C区分大小写，所以这是两个不同的函数名）。根据ANSI C中的定义， `toupper()` 函数只改变小写字符。但是一些很旧的C实现不会自动检查大小写，所以以前的代码通常会这样写：

```c
if (islower(*str)) /* ANSI C之前的做法 -- 在转换大小写之前先检查 */
     *str = toupper(*str);
```

顺带一提， `ctype.h` 中的函数通常作为宏（macro）来实现。这些C预处理器宏的作用很像函数，但是两者有一些重要的区别。我们在第16章再讨论关于宏的内容。

该程序使用 `fgets()` 和 `strchr()` 组合，读取一行输入并把换行符替换成空字符。这种方法与使用 `s_gets()` 的区别是： `s_gets()` 会处理输入行剩余字符（如果有的话），为下一次输入做好准备。而本例只有一条输入语句，就没必要进行多余的步骤。

