`printf()` 函数的返回值是打印字符的个数。如果有输出错误，`printf()` 则返回一个负值（`printf()` 的旧版本会返回不同的值）。

```c
#include <stdio.h>

int main(void)
{
    int bph2o = 212;
    int rv;
    rv = printf("%d F is water's boiling point.\n", bph2o);
    printf("The printf() function printed %d characters.\n", rv);
    
    return 0;
}
```

