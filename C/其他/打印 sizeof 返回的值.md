可以使用 `%zd` 转换说明打印 `sizeof` 返回的值，例如：

```c
#include <stdio.h>

int main(void)
{
    char name[40];
    printf("name array size is %zd.", sizeof(name));

    return 0;
}
```

