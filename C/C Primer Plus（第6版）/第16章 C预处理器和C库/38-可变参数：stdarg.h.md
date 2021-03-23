### 16.14　可变参数： `stdarg.h` 

本章前面提到过变参宏，即该宏可以接受可变数量的参数。 `stdarg.h` 头文件为函数提供了一个类似的功能，但是用法比较复杂。必须按如下步骤进行：

1．提供一个使用省略号的函数原型；

2．在函数定义中创建一个 `va_list` 类型的变量；

3．用宏把该变量初始化为一个参数列表；

4．用宏访问参数列表；

5．用宏完成清理工作。

接下来详细分析这些步骤。这种函数的原型应该有一个形参列表，其中至少有一个形参和一个省略号：

```c
void f1(int n, ...);　　　          　// 有效
int f2(const char * s, int k, ...);  // 有效
char f3(char c1, ..., char c2);      // 无效，省略号不在最后
double f3(...);　　　　　             // 无效，没有形参
```

最右边的形参（即省略号的前一个形参）起着特殊的作用，标准中用 `parmN` 这个术语来描述该形参。在上面的例子中，第1行 `f1()` 中 `parmN` 为 `n` ，第2行 `f2()` 中 `parmN` 为 `k` 。传递给该形参的实际参数是省略号部分代表的参数数量。例如，可以这样使用前面声明的 `f1()` 函数：

```c
f1(2, 200, 400);　　　   // 2个额外的参数
f1(4, 13, 117, 18, 23);　// 4个额外的参数
```

接下来，声明在 `stdarg.h` 中的 `va_list` 类型代表一种用于存储形参对应的形参列表中省略号部分的数据对象。变参函数的定义起始部分类似下面这样：

```c
double sum(int lim,...)
{
　　 va_list ap;　//声明一个存储参数的对象
```

在该例中， `lim` 是 `parmN` 形参，它表明变参列表中参数的数量。

然后，该函数将使用定义在 `stdarg.h` 中的 `va_start()` 宏，把参数列表拷贝到 `va_list` 类型的变量中。该宏有两个参数： `va_list` 类型的变量和 `parmN` 形参。接着上面的例子讨论， `va_list` 类型的变量是 `ap` ， `parmN` 形参是 `lim` 。所以，应这样调用它：

```c
va_start(ap, lim);　// 把ap初始化为参数列表
```

下一步是访问参数列表的内容，这涉及使用另一个宏 `va_arg()` 。该宏接受两个参数：一个 `va_list` 类型的变量和一个类型名。第1次调用 `va_arg()` 时，它返回参数列表的第1项；第2次调用时返回第2项，以此类推。表示类型的参数指定了返回值的类型。例如，如果参数列表中的第1个参数是 `double` 类型，第2个参数是 `int` 类型，可以这样做：

```c
double tic;
int toc;
...
tic = va_arg(ap, double);　// 检索第1个参数
toc = va_arg(ap, int);　 　//检索第2个参数
```

注意，传入的参数类型必须与宏参数的类型相匹配。如果第1个参数是 `10.0` ，上面 `tic` 那行代码可以正常工作。但是如果参数是 `10` ，这行代码可能会出错。这里不会像赋值那样把 `double` 类型自动转换成 `int` 类型。

最后，要使用 `va_end()` 宏完成清理工作。例如，释放动态分配用于存储参数的内存。该宏接受一个 `va_list` 类型的变量：

```c
va_end(ap);　// 清理工作
```

调用 `va_end(ap)` 后，只有用 `va_start` 重新初始化 `ap` 后，才能使用变量 `ap` 。

因为 `va_arg()` 不提供退回之前参数的方法，所以有必要保存 `va_list` 类型变量的副本。C99新增了一个宏用于处理这种情况： `va_copy()` 。该宏接受两个 `va_list` 类型的变量作为参数，它把第2个参数拷贝给第1个参数：

```c
va_list ap;
va_list apcopy;
double tic;
int toc;
...
va_start(ap, lim); 　　    // 把ap初始化为一个参数列表
va_copy(apcopy, ap);　   　// 把apcopy作为ap的副本
tic = va_arg(ap, double);　// 检索第1个参数
toc = va_arg(ap, int);　　 // 检索第2个参数
```

此时，即使删除了 `ap` ，也可以从 `apcopy` 中检索两个参数。

程序清单16.21中的程序示例中演示了如何创建这样的函数，该函数对可变参数求和。 `sum()` 的第1个参数是待求和项的数目。

程序清单16.21　 `varargs.c` 程序

```c
//varargs.c -- use variable number of arguments
#include <stdio.h>
#include <stdarg.h>
double sum(int, ...);
int main(void)
{
　　 double s, t;
　　 s = sum(3, 1.1, 2.5, 13.3);
　　 t = sum(6, 1.1, 2.1, 13.1, 4.1, 5.1, 6.1);
　　 printf("return value for "
　　　　　"sum(3, 1.1, 2.5, 13.3):　　　　　　　　%g\n", s);
　　 printf("return value for "
　　　　　"sum(6, 1.1, 2.1, 13.1, 4.1, 5.1, 6.1): %g\n", t);
　　 return 0;
}
double sum(int lim, ...)
{
　　 va_list ap;　　　  　 　// 声明一个对象存储参数
　　 double tot = 0;
　　 int i;
　　 va_start(ap, lim);　　　// 把ap初始化为参数列表
　　 for (i = 0; i < lim; i++)
　　　　　tot += va_arg(ap, double);　// 访问参数列表中的每一项
　　 va_end(ap);　　　            　　// 清理工作
　　 return tot;
}
```

下面是该程序的输出：

```c
return value for sum(3, 1.1, 2.5, 13.3):　　　           16.9
return value for sum(6, 1.1, 2.1, 13.1, 4.1, 5.1, 6.1):　31.6
```

查看程序中的运算可以发现，第1次调用 `sum()` 时对3个数求和，第2次调用时对6个数求和。

总而言之，使用变参函数比使用变参宏更复杂，但是函数的应用范围更广。

