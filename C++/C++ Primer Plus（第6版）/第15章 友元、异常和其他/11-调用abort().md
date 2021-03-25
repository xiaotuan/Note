### 15.3.1　调用abort()

对于这种问题，处理方式之一是，如果其中一个参数是另一个参数的负值，则调用abort()函数。Abort()函数的原型位于头文件cstdlib（或stdlib.h）中，其典型实现是向标准错误流（即cerr使用的错误流）发送消息abnormal program termination（程序异常终止），然后终止程序。它还返回一个随实现而异的值，告诉操作系统（如果程序是由另一个程序调用的，则告诉父进程），处理失败。abort()是否刷新文件缓冲区（用于存储读写到文件中的数据的内存区域）取决于实现。如果愿意，也可以使用exit()，该函数刷新文件缓冲区，但不显示消息。程序清单15.7是一个使用abort()的小程序。

程序清单15.7　error1.cpp

```css
//error1.cpp -- using the abort() function
#include <iostream>
#include <cstdlib>
double hmean(double a, double b);
int main()
{
    double x, y, z;
    std::cout << "Enter two numbers: ";
    while (std::cin >> x >> y)
    {
        z = hmean(x,y);
        std::cout << "Harmonic mean of " << x << " and " << y
            << " is " << z << std::endl;
        std::cout << "Enter next set of numbers <q to quit>: ";
    }
    std::cout << "Bye!\n";
    return 0;
}
double hmean(double a, double b)
{
    if (a == -b)
    {
        std::cout << "untenable arguments to hmean()\n";
    std::abort();
    }
    return 2.0 * a * b / (a + b);
}
```

程序清单15.7中程序的运行情况如下：

```css
Enter two numbers: 3 6
Harmonic mean of 3 and 6 is 4
Enter next set of numbers <q to quit>: 10 -10
untenable arguments to hmean()
abnormal program termination
```

注意，在hmean()中调用abort()函数将直接终止程序，而不是先返回到main()。一般而言，显示的程序异常中断消息随编译器而异，下面是另一种编译器显示的消息：

```css
This application has requested the Runtime to terminate it
in an unusual way. Please contact the application's support
team for more information.
```

为了避免异常终止，程序应在调用hmean()函数之前检查x和y的值。然而，依靠程序员来执行这种检查是不安全的。

