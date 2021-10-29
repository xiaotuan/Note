[toc]

### 方法1

使用多个 `printf()` 语句。

### 方法2

使用反斜杠（`\`）和 <kbd>Enter</kbd> 键组合来断行。这使得光标移至下一行，而且字符串中不会包含换行符。

### 方法3

ANSI C 引入的字符串连接。在两个用双引号括起来的字符串之间用空白隔开，C 编译器会把多个字符串看作是一个字符串。

### 示例代码

```c
#include <stdio.h>

int main(void)
{
    printf("Here's one way to print a");
    printf("long string.\n");
    printf("Here's another way to print a \
long string.\n");
    printf("Here's the newest way to print a "
        "long string.\n");

    return 0;
}
```



