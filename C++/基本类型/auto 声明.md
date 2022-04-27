C++11新增了一个工具， 让编译器能够根据初始值的类型推断变量的类型。 为此， 它重新定义了 `auto` 的含义。 `auto` 是一个C语言关键字， 但很少使用。

在初始化声明中， 如果使用关键字 `auto`， 而不指定变量的类型， 编译器将把变量的类型设置成与初始值相同：  

```cpp
auto n = 100;	// n is int
auto x = 1.5;	// x is double
auto y = 1.3e12L;	// y is long double
```

