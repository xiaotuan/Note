在 C 语言中，可以用库函数 `malloc()` 来分配内存；在 C++ 中仍然可以这样做，但  C++ 还有更好的方法—— new 运算符。下面是一个这样的示例：

```cpp
int *pn = new int;
```

`new int` 告诉程序，需要适合存储 `int` 的内存。`new` 运算符根据类型来确定需要多少字节的内存。然后，它找到这样的内存，并返回其地址。接下来，将地址赋给 `pn`，`pn` 是被声明为指向 `int` 的指针。

为一个数据对象（可以是结构，也可以是基本类型）获得并指定分配内存的通用格式如下：

```cpp
typeName *pointer_name = new typeName;
```

> 说明：`new` 分配的内存块通常与常规变量声明分配的内存块不同。常规变量的值都存储在被称为栈（stack）的内存区域中，而 `new` 从被称为堆（heap）或自由存储区（free store）的内存区域分配内存。

> **内存被耗尽？**
>
> 计算机可能会由于没有足够的内存而无法满足 `new` 的请求。在这种情况下，`new` 通常会引发异常；而在较老的实现中，`new` 将返回 0。在 C++ 中，值为 0 的指针被称为空指针（null pointer）。C++ 确保空指针不会执行有效的数据，因此它常被用来表示运算符或函数失败。

示例代码：

```cpp
// use_new.cpp -- using the new operator
#include <iostream>

int main()
{
    using namespace std;
    int nights = 1001;
    int* pt = new int;  // allocate space for an int 
    *pt = 1001; // store a value there

    cout << "nights value = ";
    cout << nights << ": location " << &nights << endl;
    cout << "int ";
    cout << "value = " << *pt << ": location = " << pt << endl;

    double* pd = new double;    // allocate space for a double
    *pd = 10000001.0;   // store a double there

    cout << "double ";
    cout << "value = " << *pd << ": location = " << pd << endl;
    cout << "location of pointer pd: " << &pd << endl;
    cout << "size of pt =" << sizeof(pt);
    cout << ": size of *pt = " << sizeof(*pt) << endl;
    cout << "size of pd = " << sizeof pd;
    cout << ": size of *pd = " << sizeof(*pd) << endl;

    delete pt;
    delete pd;

    return 0;
}
```

