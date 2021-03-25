### 16.7.2　模板initializer_list（C++11）

模板initializer_list是C++11新增的。您可使用初始化列表语法将STL容器初始化为一系列值：

```css
std::vector<double> payments {45.99, 39.23, 19.95, 89.01};
```

这将创建一个包含4个元素的容器，并使用列表中的4个值来初始化这些元素。这之所以可行，是因为容器类现在包含将initializer_list<T>作为参数的构造函数。例如，vector<double>包含一个将initializer_list<double>作为参数的构造函数，因此上述声明与下面的代码等价：

```css
std::vector<double> payments({45.99, 39.23, 19.95, 89.01});
```

这里显式地将列表指定为构造函数参数。

通常，考虑到C++11新增的通用初始化语法，可使用表示法{}而不是()来调用类构造函数：

```css
shared_ptr<double> pd {new double}; // ok to use {} instead of ()
```

但如果类也有接受initializer_list作为参数的构造函数，这将带来问题：

```css
std::vector<int> vi{10}; // ??
```

这将调用哪个构造函数呢？

```css
std::vector<int> vi(10);    // case A: 10 uninitialized elements
std::vector<int> vi({10}); // case B: 1 element set to 10
```

答案是，如果类有接受initializer_list作为参数的构造函数，则使用语法{}将调用该构造函数。因此在这个示例中，对应的是情形B。

所有initializer_list元素的类型都必须相同，但编译器将进行必要的转换：

```css
std::vector<double> payments {45.99, 39.23, 19, 89};
// same as std::vector<double> payments {45.99, 39.23, 19.0, 89.0};
```

在这里，由于vector的元素类型为double，因此列表的类型为initializer_list<double>，所以19和89被转换为double。

但不能进行隐式的窄化转换：

```css
std::vector<int> values = {10, 8, 5.5}; // narrowing, compile-time error
```

在这里，元素类型为int，不能隐式地将5.5转换为int。

除非类要用于处理长度不同的列表，否则让它提供接受initializer_list作为参数的构造函数没有意义。例如，对于存储固定数目值的类，您不想提供接受initializer_list作为参数的构造函数。在下面的声明中，类包含三个数据成员，因此没有提供initializer_list作为参数的构造函数：

```css
class Position
{
private:
    int x;
    int y;
    int z;
public:
    Position(int xx = 0, int yy = 0, int zz = 0)
             : x(xx), y(yy), z(zz) {}
    // no initializer_list constructor
    ...
};
```

这样，使用语法{}时将调用构造函数Position(int, int, int)：

```css
Position A = {20, -3}; // uses Position(20,-3,0)
```

