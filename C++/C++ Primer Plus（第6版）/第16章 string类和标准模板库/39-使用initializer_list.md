### 16.7.3　使用initializer_list

要在代码中使用initializer_list对象，必须包含头文件initializer_list。这个模板类包含成员函数begin()和end()，您可使用这些函数来访问列表元素。它还包含成员函数size()，该函数返回元素数。程序清单16.22是一个简单的initializer_list使用示例，它要求编译器支持C++11新增的initializer_list。

程序清单16.22　ilist.cpp

```css
// ilist.cpp -- use initializer_list (C++11 feature)
#include <iostream>
#include <initializer_list>
double sum(std::initializer_list<double> il);
double average(const std::initializer_list<double> & ril);
int main()
{
    using std::cout;
    cout << "List 1: sum = " << sum({2,3,4})
         <<", ave = " << average({2,3,4}) << '\n';
    std::initializer_list<double> dl = {1.1, 2.2, 3.3, 4.4, 5.5};
    cout << "List 2: sum = " << sum(dl)
         <<", ave = " << average(dl) << '\n';
    dl = {16.0, 25.0, 36.0, 40.0, 64.0};
    cout << "List 3: sum = " << sum(dl)
         <<", ave = " << average(dl) << '\n';
    return 0;
}
double sum(std::initializer_list<double> il)
{
    double tot = 0;
    for (auto p = il.begin(); p !=il.end(); p++)
        tot += *p;
    return tot;
}
double average(const std::initializer_list<double> & ril)
{
    double tot = 0;
    int n = ril.size();
    double ave = 0.0;
    if (n > 0)
    {
        for (auto p = ril.begin(); p !=ril.end(); p++)
            tot += *p;
        ave = tot / n;
    }
    return ave;
}
```

该程序的输出如下：

```css
List 1: sum = 9, ave = 3
List 2: sum = 16.5, ave = 3.3
List 3: sum = 181, ave = 36.2
```

**程序说明**

可按值传递initializer_list对象，也可按引用传递，如sum()和average()所示。这种对象本身很小，通常是两个指针（一个指向开头，一个指向末尾的下一个元素），也可能是一个指针和一个表示元素数的整数，因此采用的传递方式不会带来重大的性能影响。STL按值传递它们。

函数参数可以是initializer_list字面量，如{2, 3, 4}，也可以是initializer_list变量，如dl。

initializer_list的迭代器类型为const，因此您不能修改initializer_list中的值：

```css
*dl.begin() = 2011.6; // not allowed
```

但正如程序清单16.22演示的，可以将一个initializer_list赋给另一个initializer_list：

```css
dl = {16.0, 25.0, 36.0, 40.0, 64.0}; // allowed
```

然而，提供initializer_list类的初衷旨在让您能够将一系列值传递给构造函数或其他函数。

