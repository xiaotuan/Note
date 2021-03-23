#### 11.5.3　strncat()函数

`strcat()` 函数无法检查第1个数组是否能容纳第2个字符串。如果分配给第1个数组的空间不够大，多出来的字符溢出到相邻存储单元时就会出问题。当然，可以像程序清单11.15那样，用 `strlen()` 查看第1个数组的长度。注意，要给拼接后的字符串长度加1才够空间存放末尾的空字符。或者，用 `strncat()` ，该函数的第3个参数指定了最大添加字符数。例如， `strncat(bugs, addon, 13)` 将把 `addon` 字符串的内容附加给 `bugs` ，在加到第13个字符或遇到空字符时停止。因此，算上空字符（无论哪种情况都要添加空字符）， `bugs` 数组应该足够大，以容纳原始字符串（不包含空字符）、添加原始字符串在后面的13个字符和末尾的空字符。程序清单11.19使用这种方法，计算 `avaiable` 变量的值，用于表示允许添加的最大字符数。

程序清单11.19　 `join_chk.c` 程序

```c
/* join_chk.c -- 拼接两个字符串，检查第1个数组的大小 */
#include <stdio.h>
#include <string.h>
#define SIZE 30
#define BUGSIZE 13
char * s_gets(char * st, int n);
int main(void)
{
     char flower[SIZE];
     char addon [] = "s smell like old shoes.";
     char bug[BUGSIZE];
     int available;
     puts("What is your favorite flower?");
     s_gets(flower, SIZE);
     if ((strlen(addon) + strlen(flower) + 1) <= SIZE)
          strcat(flower, addon);
     puts(flower);
     puts("What is your favorite bug?");
     s_gets(bug, BUGSIZE);
     available = BUGSIZE - strlen(bug) - 1;
     strncat(bug, addon, available);
     puts(bug);
     return 0;
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     int i = 0;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          while (st[i] != '\n' && st[i] != '\0')
               i++;
          if (st[i] == '\n')
               st[i] = '\0';
          else 
               while (getchar() != '\n')
                    continue;
     }
     return ret_val;
}
```

下面是该程序的运行示例：

```c
What is your favorite flower?
Rose
Roses smell like old shoes.
What is your favorite bug?
Aphid
Aphids smell

```

读者可能已经注意到， `strcat()` 和 `gets()` 类似，也会导致缓冲区溢出。为什么C11标准不废弃 `strcat()` ，只留下 `strncat()` ？为何对 `gets()` 那么残忍？这也许是因为 `gets()` 造成的安全隐患来自于使用该程序的人，而 `strcat()` 暴露的问题是那些粗心的程序员造成的。无法控制用户会进行什么操作，但是，可以控制你的程序做什么。C语言相信程序员，因此程序员有责任确保 `strcat()` 的使用安全。

