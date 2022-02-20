C99 专门针对真/假值这种类型的变量新增了 `_Bool` 类型。`-Bool` 类型的变量只能存储 1（真）或 0（假）。

示例程序 **boolean.c**

```c
// boolean.c -- 使用 _Bool 类型的变量 variable
#include <stdio.h>

int main(void)
{
    long num;
    long sum = 0L;
    _Bool input_is_good;
    printf("Please enter an integer to be summed ");
    printf("(q to quit): ");
    input_is_good = (scanf("%ld", &num) == 1);
    while (input_is_good)
    {
        sum = sum + num;
        printf("Please enter next integer (q to quit): ");
        input_is_good = (scanf("%ld", &num) == 1);
    }
    printf("Those integers sum to %ld.\n", sum);
    return 0;
}
```

