### I.1.1　使用const而不是#define来定义常量

符号常量可提高代码的可读性和可维护性。常量名指出了其含义，如果要修改它的值，只需定义修改一次，然后重新编译即可。C使用预处理器来创建常量的符号名称。

```css
#define MAX_LENGTH 100
```

这样，预处理器将在编译之前对源代码执行文本置换，即用100替换所有的MAX_LENGTH。

而C++则在变量声明使用限定符const：

```css
const int MAX_LENGTH = 100;
```

这样MAX_LENGTH将被视为一个只读的int变量。

使用const的方法有很多优越性。首先，声明显式指明了类型。使用# define时，必须在数字后加上各种后缀来指出除char、int或double之外的类型。例如，使用100L来表明long类型，使用3.14F来表明float类型。更重要的是，const方法可以很方便地用于复合类型，如下例所示：

```css
const int base_vals[5] = {1000, 2000, 3500, 6000, 10000};
const string ans[3] = {"yes", "no", "maybe"};
```

最后，const标识符遵循变量的作用域规则，因此，可以创建作用域为全局、名称空间或数据块的常量。在特定函数中定义常量时，不必担心其定义会与程序的其他地方使用的全局常量冲突。例如，对于下面的代码：

```css
#define n 5
const int dz = 12;
...
void fizzle()
{
    int n;
    int dz;
    ...
}
```

预处理器将把：

```css
int n;
```

替换为：

```css
int 5;
```

从而导致编译错误。而fizzle()中定义的dz是本地变量。另外，必要时，fizzle()可以使用作用域解析运算符（::），以::dz的方式访问该常量。

虽然C++借鉴了C语言中的关键字const，但C++版本更有用。例如，对于外部const值，C++版本有内部链接，而不是变量和C中const所使用的默认外部链接。这意味着使用const的程序中的每个文件都必须定义该const。这好像增加了工作量，但实际上，它使工作更简单。使用内部链接时，可以将const定义放在工程中的各种文件使用的头文件中。对于外部链接，这将导致编译错误，但对于内部链接，情况并非如此。另外，由于const必须在使用它的文件中定义（在该文件使用的头文件中定义也满足这样的要求），因此可以将const值用作数组长度参数：

```css
const int MAX_LENGTH = 100;
...
double loads[MAX_LENGTH];
for (int i = 0; i < MAX_LENGTH; i++)
    loads[i] = 50;
```

这在C语言中是行不通的，因为定义MAX_LENGTH的声明可能位于一个独立的文件中，在编译时，该文件可能不可用。坦白地说，在C语言中，可以使用static限定符来创建内部链接常量。也就是说，C++通过默认使用static，让您可以少记住一件事。

顺便说一句，修订后的C标准（C99）允许将const用作数组长度，但必须将数组作为一种新式数组——变量数组，而这不是C++标准的一部分。

在控制何时编译头文件方面，# define编译指令仍然很有帮助：

```css
// blooper.h
#ifndef _BLOOPER_H_
#define _BLOOPER_H_
// code goes here
#endif
```

但对于符号常量，习惯上还是使用const，而不是#define。另一个好方法——尤其是在有一组相关的整型常量时——是使用enum：

```css
enum {LEVEL1 = 1, LEVEL2 = 2, LEVEL3 = 4, LEVEL4 = 8};
```

