#### 11.5.6　 `sprintf()` 函数

`sprintf()` 函数声明在 `stdio.h` 中，而不是在 `string.h` 中。该函数和 `printf()` 类似，但是它是把数据写入字符串，而不是打印在显示器上。因此，该函数可以把多个元素组合成一个字符串。 `sprintf()` 的第1个参数是目标字符串的地址。其余参数和 `printf()` 相同，即格式字符串和待写入项的列表。

程序清单11.28中的程序用 `sprintf()` 把3个项（两个字符串和一个数字）组合成一个字符串。注意， `sprintf()` 的用法和 `printf()` 相同，只不过 `sprintf()` 把组合后的字符串存储在数组 `formal` 中而不是显示在屏幕上。

程序清单11.28　 `format.c` 程序

```c
/* format.c -- 格式化字符串 */
#include <stdio.h>
#define MAX 20
char * s_gets(char * st, int n);
int main(void)
{
     char first[MAX];
     char last[MAX];
     char formal[2 * MAX + 10];
     double prize;
     puts("Enter your first name:");
     s_gets(first, MAX);
     puts("Enter your last name:");
     s_gets(last, MAX);
     puts("Enter your prize money:");
     scanf("%lf", &prize);
     sprintf(formal, "%s, %-19s: $%6.2f\n", last, first, prize);
     puts(formal);
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
Enter your first name:
Annie
Enter your last name:
von Wurstkasse
Enter your prize money:
25000
von Wurstkasse, Annie            : $25000.00

```

`sprintf()` 函数获取输入，并将其格式化为标准形式，然后把格式化后的字符串存储在 `formal` 中。

