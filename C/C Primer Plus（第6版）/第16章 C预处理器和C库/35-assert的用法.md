#### 16.12.1　 `assert` 的用法

程序清单16.18演示了一个使用 `assert` 的小程序。在求平方根之前，该程序断言 `z` 是否大于或等于 `0` 。程序还错误地减去一个值而不是加上一个值，故意让 `z` 得到不合适的值。

程序清单16.18　 `assert.c` 程序

```c
/* assert.c -- 使用 assert() */
#include <stdio.h>
#include <math.h>
#include <assert.h>
int main()
{
　　 double x, y, z;
　　 puts("Enter a pair of numbers (0 0 to quit): ");
　　 while (scanf("%lf%lf", &x, &y) == 2
　　　　　&& (x != 0 || y != 0))
　　 {
　　　　　z = x * x - y * y;　/* 应该用 + */
　　　　　assert(z >= 0);
　　　　　printf("answer is %f\n", sqrt(z));
　　　　　puts("Next pair of numbers: ");
　　 }
　　 puts("Done");
　　 return 0;
}
```

下面是该程序的运行示例：

```c
Enter a pair of numbers (0 0 to quit):
4 3
answer is 2.645751
Next pair of numbers:
5 3
answer is 4.000000
Next pair of numbers:
3 5
Assertion failed: (z >= 0), function main, file /Users/assert.c, line 14.

```

具体的错误提示因编译器而异。让人困惑的是，这条消息可能不是指明 `z >= 0` ，而是指明没有满足 `z >= 0` 的条件。

用 `if` 语句也能完成类似的任务：

```c
if (z < 0)
{
　　 puts("z less than 0");
　　 abort();
}
```

但是，使用 `assert()` 有几个好处：它不仅能自动标识文件和出问题的行号，还有一种无需更改代码就能开启或关闭 `assert()` 的机制。如果认为已经排除了程序的bug，就可以把下面的宏定义写在包含 `assert.h` 的位置前面：

```c
#define NDEBUG
```

并重新编译程序，这样编译器就会禁用文件中的所有 `assert()` 语句。如果程序又出现问题，可以移除这条 `#define` 指令（或者把它注释掉），然后重新编译程序，这样就重新启用了 `assert()` 语句。

