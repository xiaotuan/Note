首先，要使用 `vector` 对象，必须包含头文件 `vector`。其次，`vector` 包含在名称空间 `std` 中，因此您可以使用 `using` 编译指令、`using` 声明或 `std::vector`。第三，模板使用不同的语法来指出它存储的数据类型。第四，`vector` 类使用不同的语法来指定元素数。下面是一些示例：

```cpp
#include <vector>
...
using namespace std;
vector<int> vi;	// create a zero-size array of int
int n;
cin >> n;
vector<double> vd(n);	// create an array of n doubles
```

一般而言，下面的声明创建一个名为 `vt` 的 `vector` 对象，它可存储 `n_elem` 个类型为 typeName 的元素：

```cpp
vector<typeName> vt(n_elem);
```

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

