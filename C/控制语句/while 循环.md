`while` 循环的通用形式如下：

```c
while (expression) {
    statement
}
```

statement 部分可以是以分号结尾的简单语句，也可以是用花括号括起来的复合语句。

示例程序 **summing.c**

```c
/* summing.c -- 根据用户键入的整数求和 */
#include <stdio.h>

int main(void)
{
    long num;
    long sum = 0L;  /* 把 sum 初始化为 0 */
    int status;
    printf("Please enter an integer to be summed ");
    printf("(q to quit): ");
    status = scanf("%ld", &num);
    while(status == 1) /* == 的意思是 “等于” */
    {
        sum = sum + num;
        printf("Please enter next integer (q to quit): ");
        status = scanf("%ld", &sum);
    }
    printf("Those integers sum to %ld.\n", sum);
    return 0;
}
```

