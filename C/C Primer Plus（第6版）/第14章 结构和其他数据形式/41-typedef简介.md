### 14.12　 `typedef` 简介

`typedef` 工具是一个高级数据特性，利用 `typedef` 可以为某一类型自定义名称。这方面与 `#define` 类似，但是两者有3处不同：

+ 与 `#define` 不同， `typedef` 创建的符号名只受限于类型，不能用于值。
+ `typedef` 由编译器解释，不是预处理器。
+ 在其受限范围内， `typedef` 比 `#define` 更灵活。

下面介绍 `typedef` 的工作原理。假设要用 `BYTE` 表示1字节的数组。只需像定义个 `char` 类型变量一样定义 `BYTE` ，然后在定义前面加上关键字 `typedef` 即可：

```c
typedef unsigned char BYTE;
```

随后，便可使用 `BYTE` 来定义变量：

```c
BYTE x, y[10], * z;
```

该定义的作用域取决于 `typedef` 定义所在的位置。如果定义在函数中，就具有局部作用域，受限于定义所在的函数。如果定义在函数外面，就具有文件作用域。

通常， `typedef` 定义中用大写字母表示被定义的名称，以提醒用户这个类型名实际上是一个符号缩写。当然，也可以用小写：

```c
typedef unsigned char byte;
```

`typedef` 中使用的名称遵循变量的命名规则。

为现有类型创建一个名称，看上去真是多此一举，但是它有时的确很有用。在前面的示例中，用 `BYTE` 代替 `unsigned char` 表明你打算用 `BYTE` 类型的变量表示数字，而不是字符码。使用 `typedef` 还能提高程序的可移植性。例如，我们之前提到的 `sizeof` 运算符的返回类型： `size_t` 类型，以及 `time()` 函数的返回类型： `time_t` 类型。C标准规定 `sizeof` 和 `time()` 返回整数类型，但是让实现来决定具体是什么整数类型。其原因是，C标准委员会认为没有哪个类型对于所有的计算机平台都是最优选择。所以，标准委员会决定建立一个新的类型名（如， `time_t` ），并让实现使用 `typedef` 来设置它的具体类型。以这样的方式，C标准提供以下通用原型：

```c
time_t time(time_t *);
```

`time_t` 在一个系统中是 `unsigned long` ，在另一个系统中可以是 `unsigned long long` 。只要包含 `time.h` 头文件，程序就能访问合适的定义，你也可以在代码中声明 `time_t` 类型的变量。

`typedef` 的一些特性与 `#define` 的功能重合。例如：

```c
#define BYTE unsigned char
```

这使预处理器用 `BYTE` 替换 `unsigned char` 。但是也有 `#define` 没有的功能：

```c
typedef char * STRING;
```

没有 `typedef` 关键字，编译器将把 `STRING` 识别为一个指向 `char` 的指针变量。有了 `typedef` 关键字，编译器则把 `STRING` 解释成一个类型的标识符，该类型是指向 `char` 的指针。因此：

```c
STRING name, sign;
```

相当于：

```c
char * name, * sign;
```

但是，如果这样假设：

```c
#define STRING char *
```

然后，下面的声明：

```c
STRING name, sign;
```

将被翻译成：

```c
char * name, sign;
```

这导致只有 `name` 才是指针。

还可以把 `typedef` 用于结构：

```c
typedef struct complex {
     float real;
     float imag;
} COMPLEX;
```

然后便可使用 `COMPLEX` 类型代替 `complex` 结构来表示复数。使用 `typedef` 的第1个原因是：为经常出现的类型创建一个方便、易识别的类型名。例如，前面的例子中，许多人更倾向于使用 `STRING` 或与其等价的标记。

用 `typedef` 来命名一个结构类型时，可以省略该结构的标签：

```c
typedef struct {double x; double y;} rect;
```

假设这样使用 `typedef` 定义的类型名：

```c
rect r1 = {3.0, 6.0};
rect r2;
```

以上代码将被翻译成：

```c
struct {double x; double y;} r1= {3.0, 6.0};
struct {double x; double y;} r2;
r2 = r1;
```

这两个结构在声明时都没有标记，它们的成员完全相同（成员名及其类型都匹配），C认为这两个结构的类型相同，所以 `r1` 和 `r2` 间的赋值是有效操作。

使用 `typedef` 的第2个原因是： `typedef` 常用于给复杂的类型命名。例如，下面的声明：

```c
typedef char (* FRPTC ()) [5];
```

把 `FRPTC` 声明为一个函数类型，该函数返回一个指针，该指针指向内含5个 `char` 类型元素的数组（参见下一节的讨论）。

使用 `typedef` 时要记住， `typedef` 并没有创建任何新类型，它只是为某个已存在的类型增加了一个方便使用的标签。以前面的 `STRING` 为例，这意味着我们创建的 `STRING` 类型变量可以作为实参传递给以指向 `char` 的指针作为形参的函数。

通过结构、联合和 `typedef` ，C提供了有效处理数据的工具和处理可移植数据的工具。

