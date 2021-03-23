#### 7.6.1　 `continue` 语句

3种循环都可以使用 `continue` 语句。执行到该语句时，会跳过本次迭代的剩余部分，并开始下一轮迭代。如果 `continue` 语句在嵌套循环内，则只会影响包含该语句的内层循环。程序清单7.9中的简短程序演示了如何使用 `continue` 。

程序清单7.9　 `skippart.c` 程序

```c
/* skippart.c  -- 使用continue跳过部分循环 */
#include <stdio.h>
int main(void)
{
     const float MIN = 0.0f;
     const float MAX = 100.0f;
     float score;
     float total = 0.0f;
     int n = 0;
     float min = MAX;
     float max = MIN;
     printf("Enter the first score (q to quit): ");
     while (scanf("%f", &score) == 1)
     {
          if (score < MIN || score > MAX)
          {
               printf("%0.1f is an invalid value. Try again: ",score);
               continue;   // 跳转至while循环的测试条件
          }
          printf("Accepting %0.1f:\n", score);
          min = (score < min) ? score : min;
          max = (score > max) ? score : max;
          total += score;
          n++;
          printf("Enter next score (q to quit): ");
     }
     if (n > 0)
     {
          printf("Average of %d scores is %0.1f.\n", n, total / n);
          printf("Low = %0.1f, high = %0.1f\n", min, max);
     }
     else
          printf("No valid scores were entered.\n");
     return 0;
}
```

在程序清单7.9中， `while` 循环读取输入，直至用户输入非数值数据。循环中的 `if` 语句筛选出无效的分数。假设输入 `188` ，程序会报告： `188 is an invalid value` 。在本例中， `continue` 语句让程序跳过处理有效输入部分的代码。程序开始下一轮循环，准备读取下一个输入值。

注意，有两种方法可以避免使用 `continue` ，一是省略 `continue` ，把剩余部分放在一个 `else` 块中：

```c
if (score < 0 || score > 100)
     /* printf()语句 */
else
{
     /* 语句*/
}
```

另一种方法是，用以下格式来代替：

```c
if (score >= 0 && score <= 100)
{
     /* 语句 */
}
```

这种情况下，使用 `continue` 的好处是减少主语句组中的一级缩进。当语句很长或嵌套较多时，紧凑简洁的格式提高了代码的可读性。

`continue` 还可用作占位符。例如，下面的循环读取并丢弃输入的数据，直至读到行末尾：

```c
while (getchar() != '\n')
     ;
```

当程序已经读取一行中的某些内容，要跳至下一行开始处时，这种用法很方便。问题是，一般很难注意到一个单独的分号。如果使用 `continue` ，可读性会更高：

```c
while (getchar() != '\n')
     continue;
```

如果用了 `continue` 没有简化代码反而让代码更复杂，就不要使用 `continue` 。例如，考虑下面的程序段：

```c
while ((ch = getchar() ) != '\n')
{
     if (ch == '\t')
          continue;
     putchar(ch);
}
```

该循环跳过制表符，并在读到换行符时退出循环。以上代码这样表示更简洁：

```c
while ((ch = getchar()) != '\n')
     if (ch != '\t')
          putchar(ch);
```

通常，在这种情况下，把 `if` 的测试条件的关系反过来便可避免使用 `continue` 。

以上介绍了 `continue` 语句让程序跳过循环体的余下部分。那么，从何处开始继续循环？对于 `while` 和 `do` 　 `while` 循环，执行 `continue` 语句后的下一个行为是对循环的测试表达式求值。考虑下面的循环：

```c
count = 0;
while (count < 10)
{
     ch = getchar();
     if (ch == '\n')
          continue;
     putchar(ch);
     count++;
}
```

该循环读取10个字符（除换行符外，因为当 `ch` 是换行符时，程序会跳过 `count++;` 语句）并重新显示它们，其中不包括换行符。执行 `continue` 后，下一个被求值的表达式是循环测试条件。

对于 `for` 循环，执行 `continue` 后的下一个行为是对更新表达式求值，然后是对循环测试表达式求值。例如，考虑下面的循环：

```c
for (count = 0; count < 10; count++)
{
     ch = getchar();
     if (ch == '\n')
          continue;
     putchar(ch);
}
```

该例中，执行完 `continue` 后，首先递增 `count` ，然后将递增后的值和 `10` 作比较。因此，该循环与上面 `while` 循环的例子稍有不同。 `while` 循环的例子中，除了换行符，其余字符都显示；而本例中，换行符也计算在内，所以读取的10个字符中包含换行符。

