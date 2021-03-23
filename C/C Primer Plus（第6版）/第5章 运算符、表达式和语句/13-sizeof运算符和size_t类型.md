#### 5.3.1　 `sizeof` 运算符和 `size_t` 类型

读者在第3章就见过 `sizeof` 运算符。回顾一下， `sizeof` 运算符以字节为单位返回运算对象的大小（在C中，1字节定义为 `char` 类型占用的空间大小。过去，1字节通常是8位，但是一些字符集可能使用更大的字节）。运算对象可以是具体的数据对象（如，变量名）或类型。如果运算对象是类型（如， `float` ），则必须用圆括号将其括起来。程序清单5.8演示了这两种用法。

程序清单5.8　 `sizeof.c` 程序

```c
// sizeof.c -- 使用sizeof运算符
// 使用C99新增的%zd转换说明 -- 如果编译器不支持%zd，请将其改成%u或%lu
#include <stdio.h>
int main(void)
{
     int n = 0;
     size_t intsize;
     intsize = sizeof (int);
     printf("n = %d, n has %zd bytes; all ints have %zd bytes.\n",
               n, sizeof n, intsize);
     return 0;
}
```

C语言规定， `sizeof` 返回 `size_t` 类型的值。这是一个无符号整数类型，但它不是新类型。前面介绍过， `size_t` 是语言定义的标准类型。C有一个 `typedef` 机制（第14章再详细介绍），允许程序员为现有类型创建别名。例如，

```c
typedef double real;
```

这样， `real` 就是 `double` 的别名。现在，可以声明一个 `real` 类型的变量：

```c
real deal; // 使用typedef
```

编译器查看 `real` 时会发现，在 `typedef` 声明中 `real` 已成为 `double` 的别名，于是把 `deal` 创建为 `double` 类型的变量。类似地，C头文件系统可以使用 `typedef` 把 `size_t` 作为 `unsigned int` 或 `unsigned long` 的别名。这样，在使用 `size_t` 类型时，编译器会根据不同的系统替换标准类型。

C99做了进一步调整，新增了 `%zd` 转换说明用于 `printf()` 显示 `size_t` 类型的值。如果系统不支持 `%zd` ，可使用 `%u` 或 `%lu` 代替 `%zd` 。

