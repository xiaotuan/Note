#### 14.11.4　 `enum` 的用法

枚举类型的目的是为了提高程序的可读性和可维护性。如果要处理颜色，使用 `red` 和 `blue` 比使用 `0` 和 `1` 更直观。注意，枚举类型只能在内部使用。如果要输入 `color` 中 `orange` 的值，只能输入 `1` ，而不是单词 `orange` 。或者，让程序先读入字符串 `"orange"` ，再将其转换为 `orange` 代表的值。

因为枚举类型是整数类型，所以可以在表达式中以使用整数变量的方式使用 `enum` 变量。它们用在 `case` 语句中很方便。

程序清单14.15演示了一个使用 `enum` 的小程序。该程序示例使用默认值的方案，把 `red` 的值设置为 `0` ，使之成为指向字符串 `"red"` 的指针的索引。

程序清单14.15　 `enum.c` 程序

```c
/* enum.c -- 使用枚举类型的值 */
#include <stdio.h>
#include <string.h>     // 提供 strcmp()、strchr()函数的原型
#include <stdbool.h>    // C99 特性
char * s_gets(char * st, int n);
enum spectrum { red, orange, yellow, green, blue, violet };
const char * colors [] = { "red", "orange", "yellow",
"green", "blue", "violet" };
#define LEN 30
int main(void)
{
     char choice[LEN];
     enum spectrum color;
     bool color_is_found = false;
     puts("Enter a color (empty line to quit):");
     while (s_gets(choice, LEN) != NULL && choice[0] != '\0')
     {
          for (color = red; color <= violet; color++)
          {
               if (strcmp(choice, colors[color]) == 0)
               {
                    color_is_found = true;
                    break;
               }
          }
          if (color_is_found)
               switch (color)
          {
               case red: puts("Roses are red.");
                    break;
               case orange: puts("Poppies are orange.");
                    break;
               case yellow: puts("Sunflowers are yellow.");
                    break;
               case green: puts("Grass is green.");
                    break;
               case blue: puts("Bluebells are blue.");
                    break;
               case violet: puts("Violets are violet.");
                    break;
          }
          else
               printf("I don't know about the color %s.\n", choice);
          color_is_found = false;
          puts("Next color, please (empty line to quit):");
     }
     puts("Goodbye!");
     return 0;
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     char * find;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          find = strchr(st, '\n');    // 查找换行符
          if (find)                   // 如果地址不是 NULL，
               *find = '\0';          // 在此处放置一个空字符
          else
               while (getchar() != '\n')
                    continue;         // 清理输入行
     }
     return ret_val;
}
```

当输入的字符串与 `color` 数组的成员指向的字符串相匹配时， `for` 循环结束。如果循环找到匹配的颜色，程序就用枚举变量的值与作为 `case` 标签的枚举常量匹配。下面是该程序的一个运行示例：

```c
Enter a color (empty line to quit):
blue
Bluebells are blue.
Next color, please (empty line to quit):
orange
Poppies are orange.
Next color, please (empty line to quit):
purple
I don't know about the color purple.
Next color, please (empty line to quit):
Goodbye!

```

