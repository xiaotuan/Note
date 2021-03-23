#### 9.1.8　使用 `return` 从函数中返回值

前面介绍了如何把信息从主调函数传递给被调函数。反过来，函数的返回值可以把信息从被调函数传回主调函数。为进一步说明，我们将创建一个返回两个参数中较小值的函数。由于函数被设计用来处理 `int` 类型的值，所以被命名为 `imin()` 。另外，还要创建一个简单的 `main()` ，用于检查 `imin()` 是否正常工作。这种被设计用于测试函数的程序有时被称为驱动程序（driver），该驱动程序调用一个函数。如果函数成功通过了测试，就可以安装在一个更重要的程序中使用。程序清单9.3演示了这个驱动程序和返回最小值的函数。

程序清单9.3　 `lesser.c` 程序

```c
/* lesser.c -- 找出两个整数中较小的一个 */
#include <stdio.h>
int imin(int, int);
int main(void)
{
     int evil1, evil2;
     printf("Enter a pair of integers (q to quit):\n");
     while (scanf("%d %d", &evil1, &evil2) == 2)
     {
          printf("The lesser of %d and %d is %d.\n",
                   evil1, evil2, imin(evil1, evil2));
          printf("Enter a pair of integers (q to quit):\n");
     }
     printf("Bye.\n");
     return 0;
}
int imin(int n, int m)
{
     int min;
     if (n < m)
          min = n;
     else
          min = m;
     return min;
}
```

回忆一下， `scanf()` 返回成功读取数据的个数，所以如果输入不是两个整数会导致循环终止。下面是一个运行示例：

```c
Enter a pair of integers (q to quit):
509 333
The lesser of 509 and 333 is 333.
Enter a pair of integers (q to quit):
-9393 6
The lesser of -9393 and 6 is -9393.
Enter a pair of integers (q to quit):
q
Bye.

```

关键字 `return` 后面的表达式的值就是函数的返回值。在该例中，该函数返回的值就是变量 `min` 的值。因为 `min` 是 `int` 类型的变量，所以 `imin()` 函数的类型也是 `int` 。

变量 `min` 属于 `imin()` 函数私有，但是 `return` 语句把 `min` 的值传回了主调函数。下面这条语句的作用是把 `min` 的值赋给 `lesser:`

```c
lesser = imin(n,m);
```

是否写成下面这样：

```c
imin(n,m);
lesser = min;
```

不能。因为主调函数甚至不知道 `min` 的存在。记住， `imin()` 中的变量是 `imin()` 的局部变量。函数调用 `imin(evil1, evil2)` 只是把两个变量的值拷贝了一份。

返回值不仅可以赋给变量，也可以被用作表达式的一部分。例如，可以这样：

```c
answer = 2 * imin(z, zstar) + 25;
printf("%d\n", imin(-32 + answer, LIMIT));
```

返回值不一定是变量的值，也可以是任意表达式的值。例如，可以用以下的代码简化程序示例：

```c
/* 返回最小值的函数，第2个版本 */
imin(int n,int m)
{
     return (n < m) ? n : m;
}
```

条件表达式的值是 `n` 和 `m` 中的较小者，该值要被返回给主调函数。虽然这里不要求用圆括号把返回值括起来，但是如果想让程序条理更清楚或统一风格，可以把返回值放在圆括号内。

如果函数返回值的类型与函数声明的类型不匹配会怎样？

```c
int what_if(int n)
{
     double z = 100.0 / (double) n;
     return z; // 会发生什么？
}
```

实际得到的返回值相当于把函数中指定的返回值赋给与函数类型相同的变量所得到的值。因此在本例中，相当于把 `z` 的值赋给 `int` 类型的变量，然后返回 `int` 类型变量的值。例如，假设有下面的函数调用：

```c
result = what_if(64);
```

虽然在 `what_if()` 函数中赋给 `z` 的值是 `1.5625` ，但是 `return` 语句返回 `int` 类型的值 `1` 。

使用 `return` 语句的另一个作用是，终止函数并把控制返回给主调函数的下一条语句。因此，可以这样编写 `imin()` ：

```c
/*返回最小值的函数，第3个版本*/
imin(int n,int m)
{
     if (n < m)
          return n;
     else
          return m;
}
```

许多C程序员都认为只在函数末尾使用一次 `return` 语句比较好，因为这样做更方便浏览程序的人理解函数的控制流。但是，在函数中使用多个 `return` 语句也没有错。无论如何，对用户而言，这3个版本的函数用起来都一样，因为所有的输入和输出都完全相同，不同的是函数内部的实现细节。下面的版本也没问题：

```c
/*返回最小值的函数，第4个版本*/
imin(int n, int m)
{
     if (n < m)
          return n;
     else
          return m;
     printf("Professor Fleppard is like totally a fopdoodle.\n");
}
```

`return` 语句导致 `printf()` 语句永远不会被执行。如果Fleppard教授在自己的程序中使用这个版本的函数，可能永远不知道编写这个函数的学生对他的看法。

另外，还可以这样使用 `return` ：

```c
return;
```

这条语句会导致终止函数，并把控制返回给主调函数。因为 `return` 后面没有任何表达式，所以没有返回值，只有在 `void` 函数中才会用到这种形式。

