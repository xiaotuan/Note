### 3.1.3　整型short、int、long和long long

计算机内存由一些叫作位（bit）的单元组成（参见本章后面的旁注“位与字节”）。C++的short、int、long和long long类型通过使用不同数目的位来存储值，最多能够表示4种不同的整数宽度。如果在所有的系统中，每种类型的宽度都相同，则使用起来将非常方便。例如，如果short总是16位，int总是32位，等等。不过生活并非那么简单，没有一种选择能够满足所有的计算机设计要求。C++提供了一种灵活的标准，它确保了最小长度（从C语言借鉴而来），如下所示：

+ short至少16位；
+ int至少与short一样长；
+ long至少32位，且至少与int一样长；
+ long long至少64位，且至少与long一样长。



**位与字节**

计算机内存的基本单元是位（bit）。可以将位看作电子开关，可以开，也可以关。关表示值0，开表示值1。8位的内存块可以设置出256种不同的组合，因为每一位都可以有两种设置，所以8位的总组合数为2×2×2×2×2×2×2×2，即256。因此，8位单元可以表示0～255或者−128～127。每增加一位，组合数便加倍。这意味着可以把16位单元设置成65 536个不同的值，把32位单元设置成4 294 967 296个不同的值，把64位单元设置为18 446 744 073 709 551 616个不同的值。相较之下，unsigned long存储不了地球上当前的人数和银河系的星星数，而long long则可以。

字节（byte）通常指的是8位的内存单元。从这个意义上说，字节指的就是描述计算机内存量的度量单位，1KB等于1024字节，1MB等于1024KB。然而，C++对字节的定义与此不同。C++字节由至少能够容纳实现的基本字符集的相邻位组成，也就是说，可能取值的数目必须等于或超过字符数目。在美国，基本字符集通常是ASCII和EBCDIC字符集，它们都可以用8位来容纳，所以在使用这两种字符集的系统中，C++字节通常包含8位。然而，国际编程可能需要使用更大的字符集，如Unicode，因此有些实现可能使用16位甚至32位的字节。有些人使用术语八位组（octet）表示8位字节。



当前很多系统都使用最小长度，即short为16位，long为32位。这仍然为int提供了多种选择，其宽度可以是16位、24位或32位，同时又符合标准；甚至可以是64位，因为long和long long至少长64位。通常，在老式IBM PC的实现中，int的宽度为16位（与short相同），而在Windows XP、Windows Vista、Windows 7、Macintosh OS X、VAX和很多其他微型计算机的实现中，为32位（与long相同）。有些实现允许选择如何处理int。（读者所用的实现使用的是什么？下面的例子将演示如何在不打开手册的情况下，确定系统的限制。）类型的宽度随实现而异，这可能在将C++程序从一种环境移到另一种环境（包括在同一个系统中使用不同编译器）时引发问题。但只要小心一点（如本章后面讨论的那样），就可以最大限度地减少这种问题。

可以像使用int一样，使用这些类型名来声明变量：

```css
short score;       // creates a type short integer variable
int temperature;   // creates a type int integer variable
long position;     // creates a type long integer variable
```

实际上，short是short int的简称，而long是long int的简称，但是程序设计者们几乎都不使用比较长的形式。

这4种类型（int、short、long和long long）都是符号类型，这意味着每种类型的取值范围中，负值和正值几乎相同。例如，16位的int的取值范围为−32768～+32767。

要知道系统中整数的最大长度，可以在程序中使用C++工具来检查类型的长度。首先，sizeof运算符返回类型或变量的长度，单位为字节（运算符是内置的语言元素，对一个或多个数据进行运算，并生成一个值。例如，加号运算符+将两个值相加）。前面说过，“字节”的含义依赖于实现，因此在一个系统中，两字节的int可能是16位，而在另一个系统中可能是32位。其次，头文件climits（在老式实现中为limits.h）中包含了关于整型限制的信息。具体地说，它定义了表示各种限制的符号名称。例如，INT_MAX为int的最大取值，CHAR_BIT为字节的位数。程序清单3.1演示了如何使用这些工具。该程序还演示了如何初始化，即使用声明语句将值赋给变量。

程序清单3.1　limits.cpp

```css
// limits.cpp -- some integer limits
#include <iostream>
#include <climits>            // use limits.h for older systems
int main()
{
    using namespace std;
    int n_int = INT_MAX;       // initialize n_int to max int value
    short n_short = SHRT_MAX;    // symbols defined in climits file
    long n_long = LONG_MAX;
    long long n_llong = LLONG_MAX;
    // sizeof operator yields size of type or of variable
    cout << "int is " << sizeof (int) << " bytes." << endl;
    cout << "short is " << sizeof n_short << " bytes." << endl;
    cout << "long is " << sizeof n_long << " bytes." << endl;
    cout << "long long is " << sizeof n_llong << " bytes." << endl;
    cout << endl;
    cout << "Maximum values:" << endl;
    cout << "int: " << n_int << endl;
    cout << "short: " << n_short << endl;
    cout << "long: " << n_long << endl;
    cout << "long long: " << n_llong << endl << endl;
    cout << "Minimum int value = " << INT_MIN << endl;
    cout << "Bits per byte = " << CHAR_BIT << endl;
    return 0;
}
```

> **注意：**
> 如果您的系统不支持类型long long，应删除使用该类型的代码行。

下面是程序清单3.1中程序的输出：

```css
int is 4 bytes.
short is 2 bytes.
long is 4 bytes.
long long is 8 bytes.
Maximum values:
int: 2147483647
short: 32767
long: 2147483647
long long: 9223372036854775807
Minimum int value = -2147483648
Bits per byte = 8
```

这些输出来自运行64位Windows 7的系统。

我们来看一下该程序的主要编程特性。

#### 1．运算符sizeof和头文件limits

sizeof运算符指出，在使用8位字节的系统中，int的长度为4个字节。可对类型名或变量名使用sizeof运算符。对类型名（如int）使用sizeof运算符时，应将名称放在括号中；但对变量名（如n_short）使用该运算符，括号是可选的：

```css
cout << "int is " << sizeof (int) << " bytes.\n";
cout << "short is " << sizeof n_short << " bytes.\n";
```

头文件climits定义了符号常量（参见本章后面的旁注“符号常量——预处理器方式”）来表示类型的限制。如前所述，INT_MAX表示类型int能够存储的最大值，对于Windows 7系统，为2 147 483 647。编译器厂商提供了climits文件，该文件指出了其编译器中的值。例如，在使用16位int的老系统中，climits文件将INT_MAX定义为32 767。表3.1对该文件中定义的符号常量进行了总结，其中的一些符号常量与还没有介绍过的类型相关。

<center class="my_markdown"><b class="my_markdown">表3.1　climits中的符号常量</b></center>

| 符 号 常 量 | 表示 |
| :-----  | :-----  | :-----  | :-----  |
| CHAR_BIT | char的位数 |
| CHAR_MAX | char的最大值 |
| CHAR_MIN | char的最小值 |
| SCHAR_MAX | signed char的最大值 |
| SCHAR_MIN | signed char的最小值 |
| UCHAR_MAX | unsigned char的最大值 |
| SHRT_MAX | short的最大值 |
| SHRT_MIN | short的最小值 |
| USHRT_MAX | unsigned short的最大值 |
| INT_MAX | int的最大值 |
| INT_MIN | int的最小值 |
| UINT_MAX | unsigned int的最大值 |
| LONG_MAX | long的最大值 |
| LONG_MIN | long的最小值 |
| ULONG_MAX | unsigned long的最大值 |
| LLONG_MAX | long long的最大值 |
| LLONG_MIN | long long的最小值 |
| ULLONG_MAX | unsigned long long的最大值 |



**符号常量——预处理器方式**

climits文件中包含与下面类似的语句行：

```css
#define INT_MAX 32767
```

在C++编译过程中，首先将源代码传递给预处理器。在这里，#define和#include一样，也是一个预处理器编译指令。该编译指令告诉预处理器：在程序中查找INT_MAX，并将所有的INT_MAX都替换为32767。因此#define编译指令的工作方式与文本编辑器或字处理器中的全局搜索并替换命令相似。修改后的程序将在完成这些替换后被编译。预处理器查找独立的标记（单独的单词），跳过嵌入的单词。也就是说，预处理器不会将PINT_MAXTM替换为P32767IM。也可以使用#define来定义自己的符号常量（参见程序清单3.2）。然而，#define编译指令是C语言遗留下来的。C++有一种更好的创建符号常量的方法（使用关键字const，将在后面的一节讨论），所以不会经常使用#define。然而，有些头文件，尤其是那些被设计成可用于C和C++中的头文件，必须使用#define。



#### 2．初始化

初始化将赋值与声明合并在一起。例如，下面的语句声明了变量n_int，并将int的最大取值赋给它：

```css
int n_int = INT_MAX;
```

也可以使用字面值常量来初始化。可以将变量初始化为另一个变量，条件是后者已经定义过。甚至可以使用表达式来初始化变量，条件是当程序执行到该声明时，表达式中所有的值都是已知的：

```css
int uncles = 5;                  // initialize uncles to 5
int aunts = uncles;              // initialize aunts to 5
int chairs = aunts + uncles + 4; // initialize chairs to 14
```

如果将uncles的声明移到语句列表的最后，则另外两条初始化语句将变得非法，因为这样一来，当程序试图对其他变量进行初始化时，uncles的值是未知的。

前面的初始化语法来自C语言，C++还有另一种C语言没有的初始化语法：

```css
int owls = 101;       // traditional C initialization, sets owls to 101
int wrens(432);       // alternative C++ syntax, set wrens to 432
```

> **警告：**
> 如果不对函数内部定义的变量进行初始化，该变量的值将是不确定的。这意味着该变量的值将是它被创建之前，相应内存单元保存的值。

如果知道变量的初始值应该是什么，则应对它进行初始化。将变量声明和赋值分开，可能会带来瞬间悬而未决的问题：

```css
short year;          // what could it be?
year = 1492;         // oh
```

然而，在声明变量时对它进行初始化，可避免以后忘记给它赋值的情况发生。

#### 3．C++11初始化方式

还有另一种初始化方式，这种方式用于数组和结构，但在C++98中，也可用于单值变量：

```css
int hamburgers = {24}; // set hamburgers to 24
```

将大括号初始化器用于单值变量的情形还不多，但C++11标准使得这种情形更多了。首先，采用这种方式时，可以使用等号（=），也可以不使用：

```css
int emus{7}; // set emus to 7
int rheas = {12}; // set rheas to 12
```

其次，大括号内可以不包含任何东西。在这种情况下，变量将被初始化为零：

```css
int rocs = {}; // set rocs to 0
int psychics{}; // set psychics to 0
```

最后，这有助于更好地防范类型转换错误，这个主题将在本章末尾讨论。

为何需要更多的初始化方法？有充分的理由吗？原因是让新手更容易学习C++，这可能有些奇怪。以前，C++使用不同的方式来初始化不同的类型：初始化类变量的方式不同于初始化常规结构的方式，而初始化常规结构的方式又不同于初始化简单变量的方式；通过使用C++新增的大括号初始化器，初始化常规变量的方式与初始化类变量的方式更像。C++11使得可将大括号初始化器用于任何类型（可以使用等号，也可以不使用），这是一种通用的初始化语法。以后，教材可能介绍使用大括号进行初始化的方式，并出于向后兼容的考虑，顺便提及其他初始化方式。

