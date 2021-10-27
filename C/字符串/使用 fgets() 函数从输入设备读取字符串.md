可以使用 `fgets()` 函数从输入设备中读取字符串（可以是键盘，也可以是文件），例如：

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[40];
    printf("Please enter you name: ");
    fgets(name, (sizeof name / sizeof(char)) - 1, stdin);
    printf("Hello, %s!", name);

    return 0;
}
```

> 注意：如果是从键盘读取字符串，则 `fget()` 函数会将换行符保存在字符串中。