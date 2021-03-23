#### 6.11.1　在 `for` 循环中使用数组

程序中有许多地方要用到数组，程序清单6.19是一个较为简单的例子。该程序读取10个高尔夫分数，稍后进行处理。使用数组，就不用创建10个不同的变量来存储10个高尔夫分数。而且，还可以用 `for` 循环来读取数据。程序打印总分、平均分、差点（handicap，它是平均分与标准分的差值）。

程序清单6.19　 `scores_in.c` 程序

```c
// scores_in.c -- 使用循环处理数组
#include <stdio.h>
#define SIZE 10
#define PAR 72
int main(void)
{
     int index, score[SIZE];
     int sum = 0;
     float average;
     printf("Enter %d golf scores:\n", SIZE);
     for (index = 0; index < SIZE; index++)
          scanf("%d", &score[index]);        // 读取10个分数
     printf("The scores read in are as follows:\n");
     for (index = 0; index < SIZE; index++)
          printf("%5d", score[index]);    // 验证输入
     printf("\n");
     for (index = 0; index < SIZE; index++)
          sum += score[index];            // 求总分数
     average = (float) sum / SIZE;        // 求平均分
     printf("Sum of scores = %d, average = %.2f\n", sum, average);
     printf("That's a handicap of %.0f.\n", average - PAR);
     return 0;
}
```

先看看程序清单6.19是否能正常工作，接下来再做一些解释。下面是程序的输出：

```c
Enter 10 golf scores:
99 95 109 105 100
96 98 93 99 97 98
The scores read in are as follows:
   99 95 109 105 100 96 98 93 99 97
Sum of scores = 991, average = 99.10
That's a handicap of 27.

```

程序运行没问题，我们来仔细分析一下。首先，注意程序示例虽然输入了11个数字，但是只读入了10个数字，因为循环只读了10个值。由于 `scanf()` 会跳过空白字符，所以可以在一行输入10个数字，也可以每行只输入一个数字，或者像本例这样混合使用空格和换行符隔开每个数字（因为输入是缓冲的，只有当用户键入Enter键后数字才会被发送给程序）。

然后，程序使用数组和循环处理数据，这比使用10个单独的 `scanf()` 语句和10个单独的 `printf()` 语句读取10个分数方便得多。 `for` 循环提供了一个简单直接的方法来使用数组下标。注意， `int` 类型数组元素的用法与 `int` 类型变量的用法类似。要读取 `int` 类型变量 `fue` ，应这样写： `scanf("%d", &fue)` 。程序清单6.19中要读取 `int` 类型的元素 `score[index]` ，所以这样写 `scanf("%d", &score[index]` )。

该程序示例演示了一些较好的编程风格。第一，用 `#define` 指令创建的明示常量（ `SIZE` ）来指定数组的大小。这样就可以在定义数组和设置循环边界时使用该明示常量。如果以后要扩展程序处理20个分数，只需简单地把 `SIZE` 重新定义为20即可，不用逐一修改程序中使用了数组大小的每一处。

第二，下面的代码可以很方便地处理一个大小为 `SIZE` 的数组：

```c
for (index = 0; index < SIZE; index++)
```

设置正确的数组边界很重要。第1个元素的下标是0，因此循环开始时把 `index` 设置为 `0` 。因为从 `0` 开始编号，所以数组中最后一个元素的下标是 `SIZE - 1` 。也就是说，第10个元素是 `score[9]` 。通过测试条件 `index < SIZE` 来控制循环中使用的最后一个 `index` 的值是 `SIZE - 1` 。

第三，程序能重复显示刚读入的数据。这是很好的编程习惯，有助于确保程序处理的数据与期望相符。

最后，注意该程序使用了3个独立的 `for` 循环。这是否必要？是否可以将其合并成一个循环？当然可以，读者可以动手试试，合并后的程序显得更加紧凑。但是，调整时要注意遵循模块化（modularity）的原则。模块化隐含的思想是：应该把程序划分为一些独立的单元，每个单元执行一个任务。这样做提高了程序的可读性。也许更重要的是，模块化使程序的不同部分彼此独立，方便后续更新或修改程序。在掌握如何使用函数后，可以把每个执行任务的单元放进函数中，提高程序的模块化。

