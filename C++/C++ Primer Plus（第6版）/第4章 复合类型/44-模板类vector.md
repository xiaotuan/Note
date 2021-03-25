### 4.10.1　模板类vector

模板类vector类似于string类，也是一种动态数组。您可以在运行阶段设置vector对象的长度，可在末尾附加新数据，还可在中间插入新数据。基本上，它是使用new创建动态数组的替代品。实际上，vector类确实使用new和delete来管理内存，但这种工作是自动完成的。

这里不深入探讨模板类意味着什么，而只介绍一些基本的实用知识。首先，要使用vector对象，必须包含头文件vector。其次，vector包含在名称空间std中，因此您可使用using编译指令、using声明或std::vector。再次，模板使用不同的语法来指出它存储的数据类型。最后，vector类使用不同的语法来指定元素数。下面是一些示例：

```css
#include <vector>
...
using namespace std;
vector<int> vi;        // create a zero-size array of int
int n;
cin >> n;
vector<double> vd(n); // create an array of n doubles
```

其中，vi是一个vector<int>对象，vd是一个vector<double>对象。由于vector对象在您插入或添加值时自动调整长度，因此可以将vi的初始长度设置为零。但要调整长度，需要使用vector包中的各种方法。

一般而言，下面的声明创建一个名为vt的vector对象，它可存储n_elem个类型为typeName的元素：

```css
vector<typeName> vt(n_elem);
```

其中参数n_elem可以是整型常量，也可以是整型变量。

