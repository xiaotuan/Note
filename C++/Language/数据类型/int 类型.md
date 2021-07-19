[toc]

### 1. 声明 int 变量

```c
int erns;
int hogs, cows, goats;
```

### 2. 初始化变量

```c
int hogs = 21;
int cows = 32, goats = 14;
int dogs, cats = 94;	/* 有效，但是这种格式很糟糕 */
```

> 提示：
>
> 声明为变量创建和标记存储空间，并未其指定初始值。

### 3. int 类型常量

上面示例中出现的整数（21、32、14 和 94）都是整型常量或整型字面量。C 语言把不含小数点和指数的数作为整数。

### 4. 打印 int 值

可以使用 `printf()` 函数打印 `int` 类型的值。`%d` 指明了在一行中打印整数的位置。`%d` 称为转换说明，它指定了 `printf()` 应使用什么格式来显示一个值。

```c
/* print1.c - 演示 printf() 的一些特性 */
#include<stdio.h>

int main(void) 
{
    int ten = 10;
    int two = 2;

    printf("Doing it right: ");
    printf("%d minus %d is %d\n", ten, 2, ten -two);
    printf("Doing it wrong: ");
    printf("%d minus %d is %d\n", ten); // 遗漏 2 个参数

    return 0;
}
```

输出结果如下：

```
Doing it right: 10 minus 2 is 8
Doing it wrong: 10 minus -13964 is 0
```

