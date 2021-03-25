### 3.4.5　C++11中的auto声明

C++11新增了一个工具，让编译器能够根据初始值的类型推断变量的类型。为此，它重新定义了auto的含义。auto是一个C语言关键字，但很少使用，有关其以前的含义，请参阅第9章。在初始化声明中，如果使用关键字auto，而不指定变量的类型，编译器将把变量的类型设置成与初始值相同：

```css
auto n = 100;      // n is int
auto x = 1.5;      // x is double
auto y = 1.3e12L;  // y is long double
```

然而，自动推断类型并非为这种简单情况而设计的；事实上，如果将其用于这种简单情形，甚至可能让您误入歧途。例如，假设您要将x、y和z都指定为double类型，并编写了如下代码：

```css
auto x = 0.0;  // ok, x is double because 0.0 is double
double y = 0;  // ok, 0 automatically converted to 0.0
auto z = 0;    // oops, z is int because 0 is int
```

显式地声明类型时，将变量初始化0（而不是0.0）不会导致任何问题，但采用自动类型推断时，这却会导致问题。

处理复杂类型，如标准模块库（STL）中的类型时，自动类型推断的优势才能显现出来。例如，对于下述C++98代码：

```css
std::vector<double> scores;
std::vector<double>::iterator pv = scores.begin();
```

C++11允许您将其重写为下面这样：

```css
std::vector<double> scores;
auto pv = scores.begin();
```

本书后面讨论相关的主题时，将再次提到auto的这种新含义。

