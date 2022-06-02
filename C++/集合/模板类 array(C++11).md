C++ 11 新增了模板类 `array`，它也位于 名称空间 `std` 中。与数组一样，`array` 对象的长度也是固定的，也使用栈（静态内存分配），而不是自由存储区，因此其效率与数组相同。要创建 `array` 对象，需要包含头文件 `array`。`array` 对象的创建语法与 `vector` 稍有不同：

```cpp
#include <array>
...
using namespace std;
array<int, 5> ai;	// create array object of 5 ints
array<double, 4> ad = { 1.2, 2.1, 3.34, 4.3 };
```

推而广之，下面的声明创建一个名为 `arr` 的 `array` 对象，它包含 n_elem 个类型为 typename 的元素：

```cpp
array<typeName, n_elem> arr;
```

与创建 `vector` 对象不同的是，n_elem 不能是变量。

在 C++ 11 中，可将列表初始化用于 `vector` 和 `array` 对象，但在 C++ 98 中，不能对 `vector` 对象这样做。

**示例代码**

```cpp
// choices.cpp -- array variations
#include <iostream>
#include <vector>
#include <array>

int main()
{
    using namespace std;
    // C, original C++
    double a1[4] = { 1.2, 2.4, 3.6, 4.8 };
    // C++98 STL
    vector<double> a2(4);   // create vector with 4 elements
    // no simple way to initialize in C98
    a2[0] = 1.0 / 3.0;
    a2[1] = 1.0 / 5.0;
    a2[2] = 1.0 / 7.0;
    a2[3] = 1.0 / 9.0;
    // C++ 11 -- create and initialize array object
    array<double, 4> a3 = { 3.14, 2.72, 1.62, 1.41 };
    array<double, 4> a4;
    a4 = a3;    // valid for array objects of same size
    // use array notation
    cout << "a1[2]: " << a1[2] << " at " << &a1[2] << endl;
    cout << "a2[2]: " << a2[2] << " at " << &a2[2] << endl;
    cout << "a3[2]: " << a3[2] << " at " << &a3[2] << endl;
    cout << "a4[2]: " << a4[2] << " at " << &a4[2] << endl;
    // misdeed
    a1[-2] = 20.2;
    cout << "a1[-2]: " << a1[-2] << " at " << &a1[-2] << endl;
    cout << "a3[2]: " << a3[2] << " at " << &a3[2] << endl;
    cout << "a4[2]: " << a4[2] << " at " << &a4[2] << endl;

    return 0;
}
```

