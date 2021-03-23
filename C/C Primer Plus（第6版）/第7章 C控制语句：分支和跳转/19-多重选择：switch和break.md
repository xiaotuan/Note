### 7.7　多重选择： `switch` 和 `break` 

使用条件运算符和 `if` 　 `else` 语句很容易编写二选一的程序。然而，有时程序需要在多个选项中进行选择。可以用 `if` 　 `else` 　 `if...else` 来完成。但是，大多数情况下使用 `switch` 语句更方便。程序清单7.11演示了如何使用 `switch` 语句。该程序读入一个字母，然后打印出以该字母开头的动物名。

程序清单7.11　 `animals.c` 程序

```c
/* animals.c -- 使用switch语句 */
#include <stdio.h>
#include <ctype.h>
int main(void)
{
     char ch;
     printf("Give me a letter of the alphabet, and I will give ");
     printf("an animal name\nbeginning with that letter.\n");
     printf("Please type in a letter; type # to end my act.\n");
     while ((ch = getchar()) != '#')
     {
          if ('\n' == ch)
               continue;
          if (islower(ch))     /* 只接受小写字母*/
               switch (ch)
          {
               case 'a':
                      printf("argali, a wild sheep of Asia\n");
                      break;
               case 'b':
                      printf("babirusa, a wild pig of Malay\n");
                      break;
               case 'c':
                      printf("coati, racoonlike mammal\n");
                      break;
               case 'd':
                      printf("desman, aquatic, molelike critter\n");
                      break;
               case 'e':
                      printf("echidna, the spiny anteater\n");
                      break;
               case 'f':
                      printf("fisher, brownish marten\n");
                      break;
               default:
                      printf("That's a stumper!\n");
          }                    /* switch结束            */
          else
               printf("I recognize only lowercase letters.\n");
          while (getchar() != '\n')
               continue;        /* 跳过输入行的剩余部分    */
          printf("Please type another letter or a #.\n");
     }                    /* while循环结束        */
     printf("Bye!\n");
     return 0;
}
```

篇幅有限，我们只编到 `f` ，后面的字母以此类推。在进一步解释该程序之前，先看看输出示例：

```c
Give me a letter of the alphabet, and I will give an animal name
beginning with that letter.
Please type in a letter; type # to end my act.
a [enter]
argali, a wild sheep of Asia
Please type another letter or a #.
dab [enter]
desman, aquatic, molelike critter
Please type another letter or a #.
r [enter]
That's a stumper!
Please type another letter or a #.
Q [enter]
I recognize only lowercase letters.
Please type another letter or a #.
# [enter]
Bye!

```

该程序的两个主要特点是：使用了 `switch` 语句和它对输出的处理。我们先分析 `switch` 的工作原理。

