### E.3　alignof（C++11）

计算机系统可能限制数据在内存中的存储方式。例如，一个系统可能要求double值存储在编号为偶数的内存单元中，而另一个系统可能要求其起始地址为8个整数倍。运算符alignof将类型作为参数，并返回一个整数，指出要求的对齐方式。例如，对齐要求可能决定结构中信息的组织方式，如程序清单E.2所示。

程序清单E.2　align.cpp

```css
// align.cpp -- checking alignment
#include <iostream>
using namespace std;
struct things1
{
    char ch;
    int a;
    double x;
};
struct things2
{
    int a;
    double x;
    char ch;
};
int main()
{
    things1 th1;
    things2 th2;
    cout << “char alignment: “ << alignof(char) << endl;
    cout << “int alignment: “ << alignof(int) << endl;
    cout << “double alignment: “ << alignof(double) << endl;
    cout << “things1 alignment: “ << alignof(things1) << endl;
    cout << “things2 alignment: “ << alignof(things2) << endl;
    cout << “things1 size: “ << sizeof(things1) << endl;
    cout << “things2 size: “ << sizeof(things2) << endl;
    return 0;
}
```

下面是该程序在一个系统中的输出：

```css
char alignment: 1
int alignment: 4
double alignment: 8
things1 alignment: 8
things2 alignment: 8
things1 size: 16
things2 size: 24
```

两个结构的对齐要求都是8。这意味着结构长度将是8的整数倍，这样创建结构数组时，每个元素的起始位置都是8的整数倍。在程序清单E.2中，每个结构的所有成员只占用13位，但结构要求占用的位数为8的整数倍，这意味着需要填充一些位。在每个结构中，double成员的对齐要求为8的整数倍，但在结构thing1和thing2中，成员的排列顺序不同，这导致thing2需要更多的内部填充，以便其边界处于正确的位置。

