for 循环的格式如下：

```
for (initialize; test; update) 
{
	statement
}
```

for 语句使用 3 个表达式控制循环过程，分别用分号隔开。initialize 表达式在执行 for 语句之前只执行一次；然后对 test 表达式求值，如果表达式为真（或非零），执行循环一次；接着对 update 表达式求值，并再次检查 test 表达式。

示例程序 **sweetie.c**

```c
// sweetie.c -- 使用 for 循环的计数循环
#include <stdio.h>

int main(void)
{
    const int NUMBER = 22;
    int count;
    for (count = 1; count <= NUMBER; count++) {
        printf("Be my Valentine!\n");
    }
    return 0;
}
```

