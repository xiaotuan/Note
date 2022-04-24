`goto` 语句有两部分：`goto` 和标签名。标签的命名遵循变量命名规则，如下所示：

```c
goto part2;
```

要让这条语句正常工作，函数还必须包含另一条标为 part2 的语句，该语句可以标签名后紧跟一个冒号开始：

```c
part2: printf("Refined analysis:\n");
```

例如：

```c
#include <stdio.h>

int main(void)
{
    int ibex = 15;
    int help = 8;
    int sheds = 3;
    if (ibex > 14)
    {
        goto a;
    }
    a: sheds = 3;
    b: help = 2 * sheds;
    printf("sheds: %d, help: %d\n", sheds, help);
    return 0;
}
```

执行结果如下所示：

```
sheds: 3, help: 6
```

