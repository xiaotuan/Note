### 6.1　再探 `while` 循环

经过上一章的学习，读者已经熟悉了 `while` 循环。这里，我们用一个程序来回顾一下，程序清单6.1根据用户从键盘输入的整数进行求和。程序利用了 `scanf()` 的返回值来结束循环。

程序清单6.1　 `summing.c` 程序

```c
/* summing.c -- 根据用户键入的整数求和 */
#include <stdio.h>
int main(void)
{
     long num;
     long sum = 0L;        /* 把sum初始化为0   */
     int status;
     printf("Please enter an integer to be summed ");
     printf("(q to quit): ");
     status = scanf("%ld", &num);
     while (status == 1)    /* == 的意思是“等于”   */
     {
          sum = sum + num;
          printf("Please enter next integer (q to quit): ");
          status = scanf("%ld", &num);
     }
     printf("Those integers sum to %ld.\n", sum);
     return 0;
}
```

该程序使用 `long` 类型以存储更大的整数。尽管C编译器会把0自动转换为合适的类型，但是为了保持程序的一致性，我们把 `sum` 初始化为 `0L` （ `long` 类型的 `0` ），而不是 `0` （ `int` 类型的 `0` ）。

该程序的运行示例如下：

```c
Please enter an integer to be summed (q to quit): 44
Please enter next integer (q to quit): 33
Please enter next integer (q to quit): 88
Please enter next integer (q to quit): 121
Please enter next integer (q to quit): q
Those integers sum to 286.

```

