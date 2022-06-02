将 `new` 用于结构由两步组成：创建结构和访问其成员。要创建结构，需要同时使用结构类型和 `new`。例如：

```cpp
inflatable *ps = new inflatable;
```

创建动态结构时，不能将成员运算符句点用于结构名，因为这种结构没有名称，只是知道它的地址。C++ 专门为这种情况提供了一个运算符：箭头成员运算符（`->`）。例如：

```cpp
ps->price;
```

> 提示：有时，C++新手在指定结构成员时，搞不清楚何时应使用句点运算符，何时应使用箭头运算符。如果结构标识符是结构名，则使用句点运算符；如果标识符是指向结构的指针，则使用箭头运算符。

另一种访问结构成员的方法是，如果 `ps` 是指向结构的指针，则 `*ps` 就是被执行的值——结构本身。由于 `*ps` 是一个结构，因此 `(*ps).price` 是该结构的 `price` 成员。C++ 的运算符优先规则要求使用括号。

**示例代码**

```cpp
// newstrct.cpp -- using new with a structure
#include <iostream>

struct inflatable // structure definition
{
    char name[20];
    float volume;
    double price;
};

int main()
{
    using namespace std;
    inflatable* ps = new inflatable;    // alloc memory for structure
    cout << "Enter name of inflatable item: ";
    cin.get(ps->name, 20);  // method 1 for member access
    cout << "Enter volume in cubic feet: ";
    cin >> (*ps).volume;    // method 2 for member access
    cout << "Enter price: $";
    cin >> ps->price;
    cout << "Name: " << (*ps).name << endl; // method 2
    cout << "Volume: " << ps->volume << " cubic feet\n";    // method 1
    cout << "Price: $" << ps->price << endl;    // method 1
    delete ps;  // free memory used by structure
    return 0;
}

```

