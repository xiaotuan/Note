#### 4.4.6　 `printf()` 和 `scanf()` 的*修饰符

`printf()` 和 `scanf()` 都可以使用*修饰符来修改转换说明的含义。但是，它们的用法不太一样。首先，我们来看 `printf()` 的*修饰符。

如果你不想预先指定字段宽度，希望通过程序来指定，那么可以用*修饰符代替字段宽度。但还是要用一个参数告诉函数，字段宽度应该是多少。也就是说，如果转换说明是 `%` * `d` ，那么参数列表中应包含*和 `d` 对应的值。这个技巧也可用于浮点值指定精度和字段宽度。程序清单 `4.16` 演示了相关用法。

程序清单4.16　 `varwid.c` 程序

```c
/* varwid.c -- 使用变宽输出字段 */
#include <stdio.h>
int main(void)
{
     unsigned width, precision;
     int number = 256;
     double weight = 242.5;
     printf("Enter a field width:\n");
     scanf("%d", &width);
     printf("The number is :%*d:\n", width, number);
     printf("Now enter a width and a precision:\n");
     scanf("%d %d", &width, &precision);
     printf("Weight = %*.*f\n", width, precision, weight);
     printf("Done!\n");
     return 0;
}
```

变量 `width` 提供字段宽度， `number` 是待打印的数字。因为转换说明中*在 `d` 的前面，所以在 `printf()` 的参数列表中， `width` 在 `number` 的前面。同样， `width` 和 `precision` 提供打印 `weight` 的格式化信息。下面是一个运行示例：

```c
Enter a field width:
6
The number is :   256:
Now enter a width and a precision:
8 3
Weight =  242.500
Done!

```

这里，用户首先输入 `6` ，因此 `6` 是程序使用的字段宽度。类似地，接下来用户输入 `8` 和 `3` ，说明字段宽度是 `8` ，小数点后面显示 `3` 位数字。一般而言，程序应根据 `weight` 的值来决定这些变量的值。

`scanf()` 中*的用法与此不同。把*放在 `%` 和转换字符之间时，会使得 `scanf()` 跳过相应的输入项。程序清单 `4.17` 就是一个例子。

程序清单4.17　 `skip2.c` 程序

```c
/* skiptwo.c -- 跳过输入中的前两个整数 */
#include <stdio.h>
int main(void)
{
     int n;
     printf("Please enter three integers:\n");
     scanf("%*d %*d %d", &n);
     printf("The last integer was %d\n", n);
     return 0;
}
```

程序清单 `4.17` 中的 `scanf()` 指示：跳过两个整数，把第 `3` 个整数拷贝给 `n` 。下面是一个运行示例：

```c
Please enter three integers:
2013 2014 2015
The last integer was 2015

```

在程序需要读取文件中特定列的内容时，这项跳过功能很有用。

