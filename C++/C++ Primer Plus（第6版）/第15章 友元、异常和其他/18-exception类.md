### 15.3.8　exception类

C++异常的主要目的是为设计容错程序提供语言级支持，即异常使得在程序设计中包含错误处理功能更容易，以免事后采取一些严格的错误处理方式。异常的灵活性和相对方便性激励着程序员在条件允许的情况下在程序设计中加入错误处理功能。总之，异常是这样一种特性：类似于类，可以改变您的编程方式。

较新的C++编译器将异常合并到语言中。例如，为支持该语言，exception头文件（以前为exception.h或except.h）定义了exception类，C++可以把它用作其他异常类的基类。代码可以引发exception异常，也可以将exception类用作基类。有一个名为what()的虚拟成员函数，它返回一个字符串，该字符串的特征随实现而异。然而，由于这是一个虚方法，因此可以在从exception派生而来的类中重新定义它：

```css
#include <exception>
class bad_hmean : public std::exception
{
public:
    const char * what() { return "bad arguments to hmean()"; }
...
};
class bad_gmean : public std::exception
{
public:
    const char * what() { return "bad arguments to gmean()"; }
...
};
```

如果不想以不同的方式处理这些派生而来的异常，可以在同一个基类处理程序中捕获它们：

```css
try {
...
}
catch(std::exception & e)
{
    cout << e.what() << endl;
...
}
```

否则，可以分别捕获它们。

C++库定义了很多基于exception的异常类型。

#### 1．stdexcept异常类

头文件stdexcept定义了其他几个异常类。首先，该文件定义了logic_error和runtime_error类，它们都是以公有方式从exception派生而来的：

```css
class logic_error : public exception {
public:
explicit logic_error(const string& what_arg);
...
};
class domain_error : public logic_error {
public:
explicit domain_error(const string& what_arg);
...
};
```

注意，这些类的构造函数接受一个string对象作为参数，该参数提供了方法what()以C-风格字符串方式返回的字符数据。

这两个新类被用作两个派生类系列的基类。异常类系列logic_error描述了典型的逻辑错误。总体而言，通过合理的编程可以避免这种错误，但实际上这些错误还是可能发生的。每个类的名称指出了它用于报告的错误类型：

+ domain_error；
+ invalid_argument；
+ length_error；
+ out_of_bounds。

每个类独有一个类似于logic_error的构造函数，让您能够提供一个供方法what()返回的字符串。

数学函数有定义域（domain）和值域（range）。定义域由参数的可能取值组成，值域由函数可能的返回值组成。例如，正弦函数的定义域为负无穷大到正无穷大，因为任何实数都有正弦值；但正弦函数的值域为−1到+1，因为它们分别是最大和最小正弦值。另一方面，反正弦函数的定义域为−1到+1，值域为−π到+ π。如果您编写一个函数，该函数将一个参数传递给函数std::sin()，则可以让该函数在参数不在定义域−1到+1之间时引发domain_error异常。

异常invalid_argument指出给函数传递了一个意料外的值。例如，如果函数希望接受一个这样的字符串：其中每个字符要么是‘0’要么是‘1’，则当传递的字符串中包含其他字符时，该函数将引发invalid_argument异常。

异常length_error用于指出没有足够的空间来执行所需的操作。例如，string类的append()方法在合并得到的字符串长度超过最大允许长度时，将引发length_error异常。

异常out_of_bounds通常用于指示索引错误。例如，您可以定义一个类似于数组的类，其operator() [ ]在使用的索引无效时引发out_of_bounds异常。

接下来，runtime_error异常系列描述了可能在运行期间发生但难以预计和防范的错误。每个类的名称指出了它用于报告的错误类型：

+ range_error；
+ overflow_error；
+ underflow_error。

每个类独有一个类似于runtime_error的构造函数，让您能够提供一个供方法what()返回的字符串。

下溢（underflow）错误在浮点数计算中。一般而言，存在浮点类型可以表示的最小非零值，计算结果比这个值还小时将导致下溢错误。整型和浮点型都可能发生上溢错误，当计算结果超过了某种类型能够表示的最大数量级时，将发生上溢错误。计算结果可能不再函数允许的范围之内，但没有发生上溢或下溢错误，在这种情况下，可以使用range_error异常。

一般而言，logic_error系列异常表明存在可以通过编程修复的问题，而runtime_error系列异常表明存在无法避免的问题。所有这些错误类有相同的常规特征，它们之间的主要区别在于：不同的类名让您能够分别处理每种异常。另一方面，继承关系让您能够一起处理它们（如果您愿意的话）。例如，下面的代码首先单独捕获out_of_bounds异常，然后统一捕获其他logic_error系列异常，最后统一捕获exception异常、runtime_error系列异常以及其他从exception派生而来的异常：

```css
try {
...
}
catch(out_of_bounds & oe) // catch out_of_bounds error
{...}
catch(logic_error & oe)   // catch remaining logic_error family
{...}
catch(exception & oe)     // catch runtime_error, exception objects
{...}
```

如果上述库类不能满足您的需求，应该从logic_error或runtime_error派生一个异常类，以确保您异常类可归入同一个继承层次结构中。

#### 2．bad_alloc异常和new

对于使用new导致的内存分配问题，C++的最新处理方式是让new引发bad_alloc异常。头文件new包含bad_alloc类的声明，它是从exception类公有派生而来的。但在以前，当无法分配请求的内存量时，new返回一个空指针。

程序清单15.13演示了最新的方法。捕获到异常后，程序将显示继承的what()方法返回的消息（该消息随实现而异），然后终止。

程序清单15.13　newexcp.cpp

```css
// newexcp.cpp -- the bad_alloc exception
#include <iostream>
#include <new>
#include <cstdlib> // for exit(), EXIT_FAILURE
using namespace std;
struct Big
{
    double stuff[20000];
};
int main()
{
    Big * pb;
    try {
        cout << "Trying to get a big block of memory:\n";
        pb = new Big[10000]; // 1,600,000,000 bytes
        cout << "Got past the new request:\n";
    }
    catch (bad_alloc & ba)
    {
        cout << "Caught the exception!\n";
        cout << ba.what() << endl;
        exit(EXIT_FAILURE);
    }
    cout << "Memory successfully allocated\n";
    pb[0].stuff[0] = 4;
    cout << pb[0].stuff[0] << endl;
    delete [] pb;
    return 0;
}
```

下面该程序在某个系统中的输出：

```css
Trying to get a big block of memory:
Caught the exception!
std::bad_alloc
```

在这里，方法what()返回字符串“std::bad_alloc”。

如果程序在您的系统上运行时没有出现内存分配问题，可尝试提高请求分配的内存量。

#### 3．空指针和new

很多代码都是在new在失败时返回空指针时编写的。为处理new的变化，有些编译器提供了一个标记（开关），让用户选择所需的行为。当前，C++标准提供了一种在失败时返回空指针的new，其用法如下：

```css
int * pi = new (std::nothrow) int;
int * pa = new (std::nowthrow) int[500];
```

使用这种new，可将程序清单15.13的核心代码改为如下所示：

```css
Big * pb;
pb = new (std::nothrow) Big[10000]; // 1,600,000,000 bytes
if (pb == 0)
{
    cout << "Could not allocate memory. Bye.\n";
    exit(EXIT_FAILURE);
}
```

