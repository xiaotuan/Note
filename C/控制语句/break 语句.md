程序执行到循环中的 `break` 语句时，会终止包含它的循环，并继续执行下一阶段。如果 `break` 语句位于嵌套循环内，它只会影响包含它的当前循环。`break` 还可用于因其他原因退出循环的情况。例如：

```c
/* break.c -- 使用 break 退出循环 */
#include <stdio.h>

int main(void)
{
    float length, width;
    printf("Enter the length of the rectangle:\n");
    while (scanf("%f", &length) == 1)
    {
        printf("Length = %0.2f:\n", length);
        printf("Enter its width:\n");
        if (scanf("%f", &width) != 1) 
        {
            break;
        }
        printf("Width = %0.2f:\n", width);
        printf("Area = %0.2f:\n", length * width);
        printf("Enter the length of the rectangle:\n");
    }
    printf("Done.\n");
    return 0;
}
```

