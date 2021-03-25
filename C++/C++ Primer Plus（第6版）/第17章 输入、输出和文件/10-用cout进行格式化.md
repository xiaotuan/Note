### 17.2.4　用cout进行格式化

ostream插入运算符将值转换为文本格式。在默认情况下，格式化值的方式如下。

+ 对于char值，如果它代表的是可打印字符，则将被作为一个字符显示在宽度为一个字符的字段中。
+ 对于数值整型，将以十进制方式显示在一个刚好容纳该数字及负号（如果有的话）的字段中。
+ 字符串被显示在宽度等于该字符串长度的字段中。
+ 浮点数的默认行为有变化。下面详细说明了老式实现和新式实现之间的区别。
+ 新式：浮点类型被显示为6位，末尾的0不显示（注意，显示的数字位数与数字被存储时精度没有任何关系）。数字以定点表示法显示还是以科学计数法表示（参见第3章），取决于它的值。具体来说，当指数大于等于6或小于等于−5时，将使用科学计数法表示。另外，字段宽度恰好容纳数字和负号（如果有的话）。默认的行为对应于带%g说明符的标准C库函数fprintf()。
+ 老式：浮点类型显示为带6位小数，末尾的0不显示（注意，显示的数字位数与数字被存储时的精度没有任何关系）。数字以定点表示法显示还是以科学计数法表示（参见第3章），取决于它的值。另外，字段宽度恰好容纳数字和负号（如果有的话）。

因为每个值的显示宽度都等于它的长度，因此必须显式地在值之间提供空格；否则，相邻的值将不会被分开。

程序清单17.2演示默认的输出情况，它在每个值后面都显示一个冒号（：），以便可以知道每种情况下的字段宽度。该程序使用表达式1.0/9.0来生成一个无穷小数，以便能够知道打印了多少位。

> **注意：**
> 并非所有的编译器都能生成符合当前C++标准格式的输出。另外，当前标准允许区域性变化。例如，欧洲实现可能遵循欧洲人的风格：使用逗号而不是句点来表示小数点。也就是说，2.54将被写成2，54。区域库（头文件locale）提供了用特定的风格影响（imbuing）输入或输出流的机制，所以同一个编译器能够提供多个区域选项。本章使用美国格式。

程序清单17.2　defaults.cpp

```css
// defaults.cpp -- cout default formats
#include <iostream>
int main()
{
    using std::cout;
    cout << "12345678901234567890\n";
    char ch = 'K';
    int t = 273;
    cout << ch << ":\n";
    cout << t << ":\n";
    cout << -t <<":\n";
    double f1 = 1.200;
    cout << f1 << ":\n";
    cout << (f1 + 1.0 / 9.0) << ":\n";
    double f2 = 1.67E2;
    cout << f2 << ":\n";
    f2 += 1.0 / 9.0;
    cout << f2 << ":\n";
    cout << (f2 * 1.0e4) << ":\n";
    double f3 = 2.3e-4;
    cout << f3 << ":\n";
    cout << f3 / 10 << ":\n";
    return 0;
}
```

程序清单17.2中程序的输出如下：

```css
12345678901234567890
K:
273:
-273:
1.2:
1.31111:
167:
167.111:
1.67111e+006:
0.00023:
2.3e-005:
```

每个值都填充自己的字段。注意，1.200末尾的0没有显示出来，但末尾不带0的浮点值后面将有6个空格。另外，该实现将指数显示为3位，而其他实现可能为两位。

#### 1．修改显示时使用的计数系统

ostream类是从ios类派生而来的，而后者是从ios_base类派生而来的。ios_base类存储了描述格式状态的信息。例如，一个类成员中某些位决定了使用的计数系统，而另一个成员则决定了字段宽度。通过使用控制符（manipulator），可以控制显示整数时使用的计数系统。通过使用ios_base的成员函数，可以控制字段宽度和小数位数。由于ios_base类是ostream的间接基类，因此可以将其方法用于ostream对象（或子代），如cout。

> **注意：**
> ios_base类中的成员和方法以前位于ios类中。现在，ios_base是ios的基类。在新系统中，ios是包含char和wchar_t具体化的模板，而ios_base包含了非模板特性。

来看如何设置显示整数时使用的计数系统。要控制整数以十进制、十六进制还是八进制显示，可以使用dec、hex和oct控制符。例如，下面的函数调用将cout对象的计数系统格式状态设置为十六进制：

```css
hex(cout);
```

完成上述设置后，程序将以十六进制形式打印整数值，直到将格式状态设置为其他选项为止。注意，控制符不是成员函数，因此不必通过对象来调用。

虽然控制符实际上是函数，但它们通常的使用方式为：

```css
cout << hex;
```

ostream类重载了<<运算符，这使得上述用法与函数调用hex（cout）等价。控制符位于名称空间std中。程序清单17.3演示了这些控制符的用法，它以3种不同的计数系统显示了一个整数的值及其平方。注意，可以单独使用控制符，也可将其作为一系列插入的组成部分。

程序清单17.3　manip.cpp

```css
// manip.cpp -- using format manipulators
#include <iostream>
int main()
{
    using namespace std;
    cout << "Enter an integer: ";
    int n;
    cin >> n;
    cout << "n n*n\n";
    cout << n << " " << n * n << " (decimal)\n";
// set to hex mode
    cout << hex;
    cout << n << " ";
    cout << n * n << " (hexadecimal)\n";
// set to octal mode
    cout << oct << n << " " << n * n << " (octal)\n";
// alternative way to call a manipulator
    dec(cout);
    cout << n << " " << n * n << " (decimal)\n";
    return 0;
}
```

下面程序清单17.3中程序的运行情况：

```css
Enter an integer: 13
n     n*n
13     169 (decimal)
d     a9 (hexadecimal)
15      251 (octal)
13      169 (decimal)
```

#### 2．调整字段宽度

您可能已经注意到，在程序清单17.3的输出中各列并没有对齐，这是因为数字的字段宽度不相同。可以使用width成员函数将长度不同的数字放到宽度相同的字段中，该方法的原型为：

```css
int width();
int width(int i);
```

第一种格式返回字段宽度的当前设置；第二种格式将字段宽度设置为i个空格，并返回以前的字段宽度值。这使得能够保存以前的值，以便以后恢复宽度值时使用。

width()方法只影响将显示的下一个项目，然后字段宽度将恢复为默认值。例如，请看下面的语句：

```css
cout << '#';
cout.width(12);
cout << 12 << "#" << 24 << "#\n";
```

由于width()是成员函数，因此必须使用对象（这里为cout）来调用它。输出语句生成的输出如下：

```css
#     12#24#
```

12被放到宽度为12个字符的字段的最右边，这被称为右对齐。然后，字段宽度恢复为默认值，并将两个#符号以及24放在宽度与它们的长度相等的字段中。

> **警告：**
> width()方法只影响接下来显示的一个项目，然后字段宽度将恢复为默认值。

C++永远不会截短数据，因此如果试图在宽度为2的字段中打印一个7位值，C++将增宽字段，以容纳该数据（在有些语言中，如果数据长度与字段宽度不匹配，将用星号填充字段。C/C++的原则是：显示所有的数据比保持列的整洁更重要。C++视内容重于形式）。程序清单17.4演示了width()成员函数是如何工作的。

程序清单17.4　width.cpp

```css
// width.cpp -- using the width method
#include <iostream>
int main()
{
    using std::cout;
    int w = cout.width(30);
    cout << "default field width = " << w << ":\n";
    cout.width(5);
    cout << "N" <<':';
    cout.width(8);
    cout << "N * N" << ":\n";
    for (long i = 1; i <= 100; i *= 10)
    {
        cout.width(5);
        cout << i <<':';
        cout.width(8);
        cout << i * i << ":\n";
    }
    return 0;
}
```

程序清单17.4中程序的输出如下：

```css
     default field width = 0:
  N:   N * N:
  1:       1:
10:      100:
100:   10000:
```

在上述输出中，值在字段中右对齐。输出中包含空格，也就是说，cout通过加入空格来填满整个字段。右对齐时，空格被插入到值的左侧。用来填充的字符叫作填充字符（fill character）。右对齐是默认的。

注意，在程序清单17.4中，第一条cout语句显示字符串时，字段宽度被设置为30，但在显示w的值时，字段宽度不是30。这是由于width()方法只影响接下来被显示的一个项目。另外，w的值为0。这是由于cout.width（30）返回的是以前的字段宽度，而不是刚设置的值。为0表明，默认的字段宽度为0。由于C++总会增长字段，以容纳数据，因此这种值适用于所有的数据。最后，程序使用width()来对齐列标题和数据，方法是将第1列宽度设置为5个字符，将第2列的宽度设置为8个字符。

#### 3．填充字符

在默认情况下，cout用空格填充字段中未被使用的部分，可以用fill()成员函数来改变填充字符。例如，下面的函数调用将填充字符改为星号：

```css
cout.fill('*');
```

这对于检查打印结果，防止接收方添加数字很有用。程序清单17.5演示了该成员函数的用法。

程序清单17.5　fill.cpp

```css
// fill.cpp -- changing fill character for fields
#include <iostream>
int main()
{
    using std::cout;
    cout.fill('*');
    const char * staff[2] = { "Waldo Whipsnade", "Wilmarie Wooper"};
    long bonus[2] = {900, 1350};
    for (int i = 0; i < 2; i++)
    {
        cout << staff[i] << ": $";
        cout.width(7);
        cout << bonus[i] << "\n";
    }
    return 0;
}
```

下面是程序清单17.5中程序的输出：

```css
Waldo Whipsnade: $****900
Wilmarie Wooper: $***1350
```

注意，与字段宽度不同的是，新的填充字符将一直有效，直到更改它为止。

#### 4．设置浮点数的显示精度

浮点数精度的含义取决于输出模式。在默认模式下，它指的是显示的总位数。在定点模式和科学模式下（稍后将讨论），精度指的是小数点后面的位数。已经知道，C++的默认精度为6位（但末尾的0将不显示）。precision()成员函数使得能够选择其他值。例如，下面语句将cout的精度设置为2：

```css
cout.precision(2);
```

和width()的情况不同，但与fill()类似，新的精度设置将一直有效，直到被重新设置。程序清单17.6准确地说明了这一点。

程序清单17.6　precise.cpp

```css
// precise.cpp -- setting the precision
#include <iostream>
int main()
{
    using std::cout;
    float price1 = 20.40;
    float price2 = 1.9 + 8.0 / 9.0;
    cout << "\"Furry Friends\" is $" << price1 << "!\n";
    cout << "\"Fiery Fiends\" is $" << price2 << "!\n";
    cout.precision(2);
    cout << "\"Furry Friends\" is $" << price1 << "!\n";
    cout << "\"Fiery Fiends\" is $" << price2 << "!\n";
    return 0;
}
```

下面是程序清单17.6中程序的输出：

```css
"Furry Friends" is $20.4!
"Fiery Fiends" is $2.78889!
"Furry Friends" is $20!
"Fiery Fiends" is $2.8!
```

注意，第3行没有打印小数点及其后面的内容。另外，第4行显示的总位数为2位。

#### 5．打印末尾的0和小数点

对于有些输出（如价格或栏中的数字），保留末尾的0将更为美观。例如，对于程序清单17.6的输出，$20.40将比$20.4更美观。iostream系列类没有提供专门用于完成这项任务的函数，但ios_base类提供了一个setf()函数（用于set标记），能够控制多种格式化特性。这个类还定义了多个常量，可用作该函数的参数。例如，下面的函数调用使cout显示末尾小数点：

```css
cout.setf(ios_base::showpoint);
```

使用默认的浮点格式时，上述语句还将导致末尾的 0 被显示出来。也就是说，如果使用默认精度（6位）时，cout不会将2.00显示为2，而是将它显示为2.00000。程序清单17.7在程序清单17.6中添加了这条语句。

您可能对表示法ios_base::showpoint有疑问，showpoint是ios_base类声明中定义的类级静态常量。类级意味着如果在成员函数定义的外面使用它，则必须在常量名前面加上作用域运算符（::）。因此ios_base::showpoint指的是在ios_base类中定义的一个常量。

程序清单17.7　showpt.cpp

```css
// showpt.cpp -- setting the precision, showing trailing point
#include <iostream>
int main()
{
    using std::cout;
    using std::ios_base;
    float price1 = 20.40;
    float price2 = 1.9 + 8.0 / 9.0;
    cout.setf(ios_base::showpoint);
    cout << "\"Furry Friends\" is $" << price1 << "!\n";
    cout << "\"Fiery Fiends\" is $" << price2 << "!\n";
    cout.precision(2);
    cout << "\"Furry Friends\" is $" << price1 << "!\n";
    cout << "\"Fiery Fiends\" is $" << price2 << "!\n";
    return 0;
}
```

下面是使用当前C++格式时，程序清单17.7中程序的输出：

```css
"Furry Friends" is $20.4000!
"Fiery Fiends" is $2.78889!
"Furry Friends" is $20.!
"Fiery Fiends" is $2.8!
```

在上述输出中，第一行显示了；第三行显示了小数点，但没有显示末尾的0，这是因为精度被设置为2，而小数点前面已经包含两位。

#### 6．再谈setf()

setf()方法控制了小数点被显示时其他几个格式选项，因此来仔细研究一下它。ios_base类有一个受保护的数据成员，其中的各位（这里叫作标记）分别控制着格式化的各个方面，例如计数系统、是否显示末尾的0等。打开一个标记称为设置标记（或位），并意味着相应的位被设置为1。位标记是编程开关，相当于设置DIP开关以配置计算机硬件。例如，hex、dec和oct控制符调整控制计数系统的3个标记位。setf()函数提供了另一种调整标记位的途径。

setf()函数有两个原型。第一个为：

```css
fmtflags setf(fmtflags);
```

其中，fmtflags是bitmask类型（参见后面的“注意”）的typedef名，用于存储格式标记。该名称是在ios_base类中定义的。这个版本的setf()用来设置单个位控制的格式信息。参数是一个fmtflags值，指出要设置哪一位。返回值是类型为fmtflags的数字，指出所有标记以前的设置。如果打算以后恢复原始设置，则可以保存这个值。应给setf()传递什么呢？如果要第11位设置为1，则可以传递一个第11位为1的数字。返回值的第11位将被设置为1。对位进行跟踪好像单调乏味（实际上也是这样）。然而，您不必作做这项工作，ios_base类定义了代表位值的常量，表17.1列出了其中的一些定义。

<center class="my_markdown"><b class="my_markdown">表17.1　格式常量</b></center>

| 常　量 | 含　义 |
| :-----  | :-----  | :-----  | :-----  |
| ios_base ::boolalpha | 输入和输出bool值，可以为true或false |
| ios_base ::showbase | 对于输出，使用C++基数前缀（0，0x） |
| ios_base ::showpoint | 显示末尾的小数点 |
| ios_base ::uppercase | 对于16进制输出，使用大写字母，E表示法 |
| ios_base ::showpos | 在正数前面加上+ |

> **注意：**
> bitmask类型是一种用来存储各个位值的类型。它可以是整型、枚举，也可以是STL bitset容器。这里的主要思想是，每一位都是可以单独访问的，都有自己的含义。iostream软件包使用bitmask来存储状态信息。

由于这些格式常量都是在ios_base类中定义，因此使用它们时，必须加上作用域解析运算符。也就是说，应使用ios_base ::uppercase，而不是uppercase。如果不想使用using编译指令或using声明，可以使用作用域运算符来指出这些名称位于名称空间std中。修改将一直有效，直到被覆盖为止。程序清单17.8演示了如何使用其中一些常量。

程序清单17.8　setf.cpp

```css
// setf.cpp -- using setf() to control formatting
#include <iostream>
int main()
{
    using std::cout;
    using std::endl;
    using std::ios_base;
    int temperature = 63;
    cout << "Today's water temperature: ";
    cout.setf(ios_base::showpos); // show plus sign
    cout << temperature << endl;
    cout << "For our programming friends, that's\n";
    cout << std::hex << temperature << endl; // use hex
    cout.setf(ios_base::uppercase); // use uppercase in hex
    cout.setf(ios_base::showbase);  // use 0X prefix for hex
    cout << "or\n";
    cout << temperature << endl;
    cout << "How " << true << "! oops -- How ";
    cout.setf(ios_base::boolalpha);
    cout << true << "!\n";
    return 0;
}
```

下面是程序清单17.8中程序的输出：

```css
Today's water temperature: +63
For our programming friends, that's
3f
or
0X3F
How 0X1! oops -- How true!
```

注意，仅当基数为10时才使用加号。C++将十六进制和八进制都视为无符号的，因此对它们，无需使用符号（然而，有些C++实现可能仍然会显示加号）。

第二个setf()原型接受两个参数，并返回以前的设置：

```css
fmtflags setf(fmtflags , fmtflags );
```

函数的这种重载格式用于设置由多位控制的格式选项。第一参数和以前一样，也是一个包含了所需设置的fmtflags值。第二参数指出要清除第一个参数中的哪些位。例如，将第3位设置为1表示以10为基数，将第4位设置为1表示以8为基数，将第5位设置为1表示以16为基数。假设输出是以10为基数的，而要将它设置为以16为基数，则不仅需要将第5位设置为1，还需要将第3位设置为0——这叫作清除位（clearing the bit）。聪明的十六进制控制符可自动完成这两项任务。使用函数setf()时，要做的工作多些，因为要用第二参数指出要清除哪些位，用第一参数指出要设置哪位。这并不像听上去那么复杂，因为ios_base类为此定义了常量（如表17.2所示）。具体地说，要修改基数，可以将常量ios_base::basefield用作第二参数，将ios_base ::hex用作第一参数。也就是说，下面的函数调用与使用十六进制控制符的作用相同：

```css
cout.setf(ios_base::hex, ios_base::basefield);
```

<center class="my_markdown"><b class="my_markdown">表17.2　setf(long, long)的参数</b></center>

| 第二个参数 | 第一个参数 | 含　义 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| ios_base ::basefield | ios_base ::dec | 使用基数10 |
| ios_base ::oct | 使用基数8 |
| ios_base ::hex | 使用基数16 |
| ios_base ::floatfield | ios_base ::fixed | 使用定点计数法 |
| ios_base ::scientific | 使用科学计数法 |
| ios_base ::adjustfield | ios_base ::left | 使用左对齐 |
| ios_base ::right | 使用右对齐 |
| ios_base ::internal | 符号或基数前缀左对齐，值右对齐 |

ios_base类定义了可按这种方式处理的3组格式标记。每组标记都由一个可用作第二参数的常量和两三个可用作第一参数的常量组成。第二参数清除一批相关的位，然后第一参数将其中一位设置为1。表17.2列出了用作setf()的第二参数的常量的名称、可用作第一参数的相关常量以及它们的含义。例如，要选择左对齐，可将ios_base ::adjustfield用作第二参数，将ios_base ::left作为第一参数。左对齐意味着将值放在字段的左端，右对齐则表示将值放在字段的右端。内部对齐表示将符号或基数前缀放在字段左侧，余下的数字放在字段的右侧（遗憾的是，C++没有提供自对齐模式）。

定点表示法意味着使用格式123.4来表示浮点值，而不管数字的长度如何，科学表示法则意味着使用格式1.23e04，而不考虑数字的长度。如果您熟悉C语言中printf()的说明符，则可能知道，默认的C++模式对应于%g说明符，定点表示法对应于%f说明符，而科学表示法对应于%e说明符。

在C++标准中，定点表示法和科学表示法都有下面两个特征：

+ 精度指的是小数位数，而不是总位数；
+ 显示末尾的0。

setf()函数是ios_base类的一个成员函数。由于这个类是ostream类的基类，因此可以使用cout对象来调用该函数。例如，要左对齐，可使用下面的调用：

```css
ios_base::fmtflags old = cout.setf(ios::left, ios::adjustfield);
```

要恢复以前的设置，可以这样做：

```css
cout.setf(old, ios::adjustfield);
```

程序清单17.9是一个使用两个参数的setf()的示例。

> **注意：**
> 程序清单17.9中的程序使用了一个数学函数，有些C++系统不自动搜索数学库。例如，有些UNIX系统要求这样做：

```css
$ CC setf2.C -lm
```

> -lm选项命令链接程序搜索数学库。同样，有些使用g++的Linux系统也要求这样做。

程序清单17.9　setf2.cpp

```css
// setf2.cpp -- using setf() with 2 arguments to control formatting
#include <iostream>
#include <cmath>
int main()
{
    using namespace std;
   // use left justification, show the plus sign, show trailing
    // zeros, with a precision of 3
    cout.setf(ios_base::left, ios_base::adjustfield);
    cout.setf(ios_base::showpos);
    cout.setf(ios_base::showpoint);
    cout.precision(3);
    // use e-notation and save old format setting
    ios_base::fmtflags old = cout.setf(ios_base::scientific,
        ios_base::floatfield);
    cout << "Left Justification:\n";
    long n;
    for (n = 1; n <= 41; n+= 10)
    {
        cout.width(4);
        cout << n << "|";
        cout.width(12);
        cout << sqrt(double(n)) << "|\n";
    }
    // change to internal justification
    cout.setf(ios_base::internal, ios_base::adjustfield);
    // restore default floating-point display style
    cout.setf(old, ios_base::floatfield);
    cout << "Internal Justification:\n";
    for (n = 1; n <= 41; n+= 10)
    {
        cout.width(4);
        cout << n << "|";
        cout.width(12);
        cout << sqrt(double(n)) << "|\n";
    }
    // use right justification, fixed notation
    cout.setf(ios_base::right, ios_base::adjustfield);
    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout << "Right Justification:\n";
    for (n = 1; n <= 41; n+= 10)
    {
        cout.width(4);
        cout << n << "|";
        cout.width(12);
        cout << sqrt(double(n)) << "|\n";
    }
    return 0;
}
```

下面是程序清单17.9中程序的输出：

```css
Left Justification:
+1  |+1.000e+00 |
+11 |+3.317e+00 |
+21 |+4.583e+00 |
+31 |+5.568e+00 |
+41 |+6.403e+00 |
Internal Justification:
+  1|+      1.00|
+ 11|+      3.32|
+ 21|+      4.58|
+ 31|+      5.57|
+ 41|+      6.40|
Right Justification:
 +1|      +1.000|
+11|      +3.317|
+21|      +4.583|
+31|      +5.568|
+41|      +6.403|
```

注意到精度3让默认的浮点显示（在这个程序中用于内部对齐）总共显示3位，而定点模式和科学模式只显示3位小数（e表示法的指数位数取决于实现）。

调用setf()的效果可以通过unsetf()消除，后者的原型如下：

```css
void unsetf(fmtflags mask);
```

其中，mask是位模式。mask中所有的位都设置为1，将使得对应的位被复位。也就是说，setf()将位设置为1，unsetf()将位恢复为0。例如：

```css
cout.setf(ios_base::showpoint);       // show trailing decimal point
cout.unsetf(ios_base::boolshowpoint); // don't show trailing decimal point
cout.setf(ios_base::boolalpha);        // display true, false
cout.unsetf(ios_base::boolalpha);    // display 1, 0
```

您可能注意到了，没有专门指示浮点数默认显示模式的标记。系统的工作原理如下：仅当只有定点位被设置时使用定点表示法；仅当只有科学位被设置时使用科学表示法；对于其他组合，如没有位被设置或两位都被设置时，将使用默认模式。因此，启用默认模式的方法之一如下：

```css
cout.setf(0, ios_base::floatfield); // go to default mode
```

第二个参数关闭这两位，而第一个参数不设置任何位。一种实现同样目标的简捷方式是，使用参数ios::floatfield来调用函数unsetf()：

```css
cout.unsetf(ios_base::floatfield); // go to default mode
```

如果已知cout处于定点状态，则可以使用参数ios_base::fixed调用函数unsetf()来切换到默认模式；然而，无论cout的当前状态如何，使用参数ios_base::floatfield调用函数unsetf()都将切换到默认模式，因此这是一种更好的选择。

#### 7．标准控制符

使用setf()不是进行格式化的、对用户最为友好的方法，C++提供了多个控制符，能够调用setf()，并自动提供正确的参数。前面已经介绍过dec、hex和oct，这些控制符（多数都不适用于老式C++实现）的工作方式都与hex相似。例如，下面的语句打开左对齐和定点选项：

```css
cout << left << fixed;
```

表17.3列出了这些控制符以及其他一些控制符。

<center class="my_markdown"><b class="my_markdown">表17.3　一些标准控制符</b></center>

| 控　制　符 | 调　用 |
| :-----  | :-----  | :-----  | :-----  |
| boolalpha | setf(ios_base::boolalpha) |
| noboolalpha | unset(ios_base::noboolalpha) |
| showbase | setf(ios_base::showbase) |
| noshowbase | unsetf(ios_base::showbase) |
| showpoint | setf(ios_base::showpoint) |
| noshowpoint | unsetf(ios_base::showpoint) |
| showpos | setf(ios_base::showpos) |
| noshowpos | unsetf(ios_base::showpos) |
| uppercase | setf(ios_base::uppercase) |
| nouppercase | unsetf(ios_base::uppercase) |
| internal | setf(ios_base::internal,ios_base::adjustfield) |
| left | setf(ios_base::left,ios_base::adjustfield) |
| right | setf(ios_base::right,ios_base::adjustfield) |
| dec | setf(ios_base::dec,ios_base::basefield) |
| hex | setf(ios_base::hex,ios_base::basefield) |
| oct | setf(ios_base::oct,ios_base::basefield) |
| fixed | setf(ios_base::fixed,ios_base::floatfield) |
| scientific | setf(ios_base::scientific,ios_base::floatfield) |

> **提示：**
> 如果系统支持这些控制符，请使用它们；否则，仍然可以使用setf()。

#### 8．头文件iomanip

使用iostream工具来设置一些格式值（如字段宽度）不太方便。为简化工作，C++在头文件iomanip中提供了其他一些控制符，它们能够提供前面讨论过的服务，但表示起来更方便。3个最常用的控制符分别是setprecision()、setfill()和setw()，它们分别用来设置精度、填充字符和字段宽度。与前面讨论的控制符不同的是，这3个控制符带参数。setprecision()控制符接受一个指定精度的整数参数；setfill() 控制符接受一个指定填充字符的char参数；setw()控制符接受一个指定字段宽度的整数参数。由于它们都是控制符，因此可以用cout语句连接起来。这样，setw()控制符在显示多列值时尤其方便。程序清单17.10演示了这一点，它对于每一行输出，都多次修改了字段宽度和填充字符，同时使用了一些较新的标准控制符。

> **注意：**
> 有些C++系统不自动搜索数学库。前面说过，有些UNIX系统要求使用如下命令选项来访问数学库：

```css
$ CC iomanip.C -lm
```

程序清单17.10　iomanip.cpp

```css
// iomanip.cpp -- using manipulators from iomanip
// some systems require explicitly linking the math library
#include <iostream>
#include <iomanip>
#include <cmath>
int main()
{
    using namespace std;
    // use new standard manipulators
    cout << fixed << right;
    // use iomanip manipulators
    cout << setw(6) << "N" << setw(14) << "square root"
         << setw(15) << "fourth root\n";
    double root;
    for (int n = 10; n <=100; n += 10)
    {
        root = sqrt(double(n));
        cout << setw(6) << setfill('.') << n << setfill(' ')
              << setw(12) << setprecision(3) << root
              << setw(14) << setprecision(4) << sqrt(root)
              << endl;
    }
    return 0;
}
```

下面是程序清单17.10中程序的输出：

```css
     N square root fourth root
....10     3.162      1.7783
....20     4.472      2.1147
....30     5.477      2.3403
....40     6.325      2.5149
....50     7.071      2.6591
....60     7.746      2.7832
....70     8.367      2.8925
....80     8.944      2.9907
....90     9.487      3.0801
...100    10.000      3.1623
```

现在可以生成几乎完全对齐的列了。使用fixed控制符导致显示末尾的0。

