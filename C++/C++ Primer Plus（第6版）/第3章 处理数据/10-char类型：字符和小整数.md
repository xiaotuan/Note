### 3.1.8　char类型：字符和小整数

下面介绍最后一种整型：char类型。顾名思义，char类型是专为存储字符（如字母和数字）而设计的。现在，存储数字对于计算机来说算不了什么，但存储字母则是另一回事。编程语言通过使用字母的数值编码解决了这个问题。因此，char类型是另一种整型。它足够长，能够表示目标计算机系统中的所有基本符号——所有的字母、数字、标点符号等。实际上，很多系统支持的字符都不超过128个，因此用一个字节就可以表示所有的符号。因此，虽然char最常被用来处理字符，但也可以将它用做比short更小的整型。

在美国，最常用的符号集是ASCII字符集（参见附录C）。字符集中的字符用数值编码（ASCII码）表示。例如，字符A的编码为65，字母M的编码为77。为方便起见，本书在示例中使用的是ASCII码。然而，C++实现使用的是其主机系统的编码——例如，IBM大型机使用EBCDIC编码。ASCII和EBCDIC都不能很好地满足国际需要，C++支持的宽字符类型可以存储更多的值，如国际Unicode字符集使用的值。本章稍后将介绍wchar_t类型。

程序清单3.5使用了char类型。

程序清单3.5　chartype.cpp

```css
// chartype.cpp -- the char type
#include <iostream>
int main()
{
    using namespace std;
    char ch;          // declare a char variable
    cout << "Enter a character: " << endl;
    cin >> ch;
    cout << "Hola! ";
    cout << "Thank you for the " << ch << " character." << endl;
    return 0;
}
```

同样，\n在C++中表示换行符。下面是该程序的输出：

```css
Enter a character:
M
Hola! Thank you for the M character.
```

有趣的是，程序中输入的是M，而不是对应的字符编码77。另外，程序将打印M，而不是77。通过查看内存可以知道，77是存储在变量ch中的值。这种神奇的力量不是来自char类型，而是来自cin和cout，这些工具为您完成了转换工作。输入时，cin将键盘输入的M转换为77；输出时，cout将值77转换为所显示的字符M；cin和cout的行为都是由变量类型引导的。如果将77存储在int变量中，则cout将把它显示为77（也就是说，cout显示两个字符7）。程序清单3.6说明了这一点，该程序还演示了如何在C++中书写字符字面值：将字符用单引号括起，如'M'（注意，示例中没有使用双引号。C++对字符用单引号，对字符串使用双引号。cout对象能够处理这两种情况，但正如第4章将讨论的，这两者有天壤之别）。最后，程序引入了cout的一项特性——cout.put()函数，该函数显示一个字符。

程序清单3.6　morechar.cpp

```css
// morechar.cpp -- the char type and int type contrasted
#include <iostream>
int main()
{
    using namespace std;
    char ch = 'M';           // assign ASCII code for M to ch
    int i = ch;              // store same code in an int
    cout << "The ASCII code for " << ch << " is " << i << endl;
    cout << "Add one to the character code:" << endl;
    ch = ch + 1;             // change character code in ch
    i = ch;                  // save new character code in i
    cout << "The ASCII code for " << ch << " is " << i << endl;
    // using the cout.put() member function to display a char
    cout << "Displaying char ch using cout.put(ch): ";
    cout.put(ch);
    // using cout.put() to display a char constant
    cout.put('!');
    cout << endl << "Done" << endl;
    return 0;
}
```

下面是程序清单3.6中程序的输出：

```css
The ASCII code for M is 77
Add one to the character code:
The ASCII code for N is 78
Displaying char ch using cout.put(ch): N!
Done
```

#### 1．程序说明

在程序清单3.6中，‘M’表示字符M的数值编码，因此将char变量ch初始化为‘M’，将把ch设置为77。然后，程序将同样的值赋给int变量i，这样ch和i的值都是77。接下来，cout把ch显示为M，而把i显示为77。如前所述，值的类型将引导cout选择如何显示值——这是智能对象的另一个例子。

由于ch实际上是一个整数，因此可以对它使用整数操作，如加1，这将把ch的值变为78。然后，程序将i重新设置为新的值（也可以将i加1）。cout再次将这个值的char版本显示为字符，将int版本显示为数字。

C++将字符表示为整数这一事实，使得操纵字符值很容易。不必使用笨重的转换函数在字符和ASCII码之间来回转换。

即使通过键盘输入的数字也被视为字符。请看下面的代码：

```css
char ch;
cin >> ch;
```

如果您输入5并按回车键，上述代码将读取字符“5”，并将其对应的字符编码（ASCII编码53）存储到变量ch中。请看下面的代码：

```css
int n;
cin >> n;
```

如果您也输入5并按回车键，上述代码将读取字符“5”，将其转换为相应的数字值5，并存储到变量n中。

最后，该程序使用函数cout.put()显示变量ch和一个字符常量。

#### 2．成员函数cout.put()

cout.put()到底是什么东西？其名称中为何有一个句点？函数cout.put()是一个重要的C++ OOP概念——成员函数——的第一个例子。类定义了如何表示和控制数据。成员函数归类所有，描述了操纵类数据的方法。例如类ostream有一个put()成员函数，用来输出字符。只能通过类的特定对象（例如这里的cout对象）来使用成员函数。要通过对象（如cout）使用成员函数，必须用句点将对象名和函数名称（put()）连接起来。句点被称为成员运算符。cout.put()的意思是，通过类对象cout来使用函数put()。第10章介绍类时将更详细地介绍这一点。现在，您接触的类只有istream和ostream，可以通过使用它们的成员函数来熟悉这一概念。

cout.put()成员函数提供了另一种显示字符的方法，可以替代<<运算符。现在读者可能会问，为何需要cout.put()。答案与历史有关。在C++的Release 2.0之前，cout将字符变量显示为字符，而将字符常量（如‘M’和‘N’）显示为数字。问题是，C++的早期版本与C一样，也把字符常量存储为int类型。也就是说，‘M’的编码77将被存储在一个16位或32位的单元中。而char变量一般占8位。下面的语句从常量‘M’中复制8位（左边的8位）到变量ch中：

```css
char ch = 'M';
```

遗憾的是，这意味着对cout来说，‘M’和ch看上去有天壤之别，虽然它们存储的值相同。因此，下面的语句将打印$字符的ASCII码，而不是字符$：

```css
cout << '$';
```

但下面的语句将打印字符$：

```css
cout.put('$');
```

在Release 2.0之后，C++将字符常量存储为char类型，而不是int类型。这意味着cout现在可以正确处理字符常量了。

cin对象有几种不同的方式可以读取输入的字符。通过使用一个利用循环来读取几个字符的程序，读者可以更容易地领会到这一点。因此在第5章介绍了循环后，我们再来讨论这个主题。

#### 3．char字面值

在C++中，书写字符常量的方式有多种。对于常规字符（如字母、标点符号和数字），最简单的方法是将字符用单引号括起。这种表示法代表的是字符的数值编码。例如，ASCII系统中的对应情况如下：

+ 'A'为65，即字符A的ASCII码；
+ 'a'为97，即字符a的ASCII码；
+ '5'为53，即数字5的ASCII码；
+ ' '为32，即空格字符的ASCII码；
+ '!'为33，即惊叹号的ASCII码。

这种表示法优于数值编码，它更加清晰，且不需要知道编码方式。如果系统使用的是EBCDIC，则A的编码将不是65，但是'A'表示的仍然是字符A。

有些字符不能直接通过键盘输入到程序中。例如，按回车键并不能使字符串包含一个换行符；相反，程序编辑器将把这种键击解释为在源代码中开始新的一行。其他一些字符也无法从键盘输入，因为C++语言赋予了它们特殊的含义。例如，双引号字符用来分隔字符串字面值，因此不能把双引号放在字符串字面值中。对于这些字符，C++提供了一种特殊的表示方法——转义序列，如表3.2所示。例如，\a表示振铃字符，它可以使终端扬声器振铃。转义序列\n表示换行符，\”将双引号作为常规字符，而不是字符串分隔符。可以在字符串或字符常量中使用这些表示法，如下例所示：

```css
char alarm = '\a';
cout << alarm << "Don't do that again!\a\n";
cout << "Ben \"Buggsie\" Hacker\nwas here!\n";
```

最后一行的输出如下：

```css
Ben "Buggsie" Hacker
was here!
```

<center class="my_markdown"><b class="my_markdown">表3.2　C++转义序列的编码</b></center>

| 字 符 名 称 | ASCII符号 | C++代码 | 十进制ASCII码 | 十六进制ASCII码 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 换行符 | NL (LF) | \n | 10 | 0xA |
| 水平制表符 | HT | \t | 9 | 0x9 |
| 垂直制表符 | VT | \v | 11 | 0xB |
| 退格 | BS | \b | 8 | 0x8 |
| 回车 | CR | \r | 13 | 0xD |
| 振铃 | BEL | \a | 7 | 0x7 |
| 反斜杠 | \ | \ | 92 | 0x5C |
| 问号 | ? | \? | 63 | 0x3F |
| 单引号 | ' | \ ' | 39 | 0x27 |
| 双引号 | " | \ " | 34 | 0x22 |

注意，应该像处理常规字符（如Q）那样处理转义序列（如\n）。也就是说，将它们作为字符常量时，应用单引号括起；将它们放在字符串中时，不要使用单引号。

转义序列的概念可追溯到使用电传打字机与计算机通信的时代，现代系统并非都支持所有的转义序列。例如，输入振铃字符时，有些系统保持沉默。

换行符可替代endl，用于在输出中重起一行。可以以字符常量表示法（‘\n’）或字符串方式（“\n”）使用换行符。下面三行代码都将光标移到下一行开头：

```css
cout << endl;    // using the endl manipulator
cout << '\n';    // using a character constant
cout << "\n";    // using a string
```

可以将换行符嵌入到较长的字符串中，这通常比使用endl方便。例如，下面两条cout语句的输出相同：

```css
cout << endl << endl << "What next?" << endl << "Enter a number:" << endl;
cout << "\n\nWhat next?\nEnter a number:\n";
```

显示数字时，使用endl比输入“\n”或‘\n’更容易些，但显示字符串时，在字符串末尾添加一个换行符所需的输入量要少些：

```css
cout << x << endl;    // easier than cout << x << "\n";
cout << "Dr. X.\n";   // easier than cout << "The Dr. X." << endl;
```

最后，可以基于字符的八进制和十六进制编码来使用转义序列。例如，Ctr+Z的ASCII码为26，对应的八进制编码为032，十六进制编码为0x1a。可以用下面的转义序列来表示该字符：\032或\0x1a。将这些编码用单引号括起，可以得到相应的字符常量，如'\032'，也可以将它们放在字符串中，如"hi\x1a there"。

> **提示：**
> 在可以使用数字转义序列或符号转义序列（如\0x8和\b）时，应使用符号序列。数字表示与特定的编码方式（如ASCII码）相关，而符号表示适用于任何编码方式，其可读性也更强。

程序清单3.7演示了一些转义序列。它使用振铃字符来提请注意，使用换行符使光标前进，使用退格字符使光标向左退一格（Houdini曾经在只使用转义序列的情况下，绘制了一幅哈得逊河图画；他无疑是一位转义序列艺术大师）。

程序清单3.7　bondini.cpp

```css
// bondini.cpp -- using escape sequences
#include <iostream>
int main()
{
    using namespace std;
    cout << "\aOperation \"HyperHype\" is now activated!\n";
    cout << "Enter your agent code:________\b\b\b\b\b\b\b\b";
    long code;
    cin >> code;
    cout << "\aYou entered " << code << "...\n";
    cout << "\aCode verified! Proceed with Plan Z3!\n";
    return 0;
}
```

> **注意：**
> 有些基于ANSI C之前的编译器的C++系统不能识别\a。对于使用ASCII字符集的系统，可以用\007替换\a。有些系统的行为可能有所不同，例如可能将\b显示为一个小矩形，而不是退格，或者在退格时删除，还可能忽略\a。

运行程序清单3.7中的程序时，将在屏幕上显示下面的文本：

```css
Operation "HyperHype" is now activated!
Enter your agent code:________
```

打印下划线字符后，程序使用退格字符将光标退到第一个下划线处。读者可以输入自己的密码，并继续。下面是完整的运行情况：

```css
Operation "HyperHype" is now activated!
Enter your agent code:42007007
You entered 42007007...
Code verified! Proceed with Plan Z3!
```

#### 4．通用字符名

C++实现支持一个基本的源字符集，即可用来编写源代码的字符集。它由标准美国键盘上的字符（大写和小写）和数字、C语言中使用的符号（如{和=）以及其他一些字符（如换行符和空格）组成。还有一个基本的执行字符集，它包括在程序执行期间可处理的字符（如可从文件中读取或显示到屏幕上的字符）。它增加了一些字符，如退格和振铃。C++标准还允许实现提供扩展源字符集和扩展执行字符集。另外，那些被作为字母的额外字符也可用于标识符名称中。也就是说，德国实现可能允许使用日耳曼语的元音变音，而法国实现则允许使用重元音。C++有一种表示这种特殊字符的机制，它独立于任何特定的键盘，使用的是通用字符名（universal character name）。

通用字符名的用法类似于转义序列。通用字符名可以以\u或\U打头。\u后面是8个十六进制位，\U后面则是16个十六进制位。这些位表示的是字符的ISO 10646码点（ISO 10646是一种正在制定的国际标准，为大量的字符提供了数值编码，请参见本章后面的“Unicode和ISO 10646”）。

如果所用的实现支持扩展字符，则可以在标识符（如字符常量）和字符串中使用通用字符名。例如，请看下面的代码：

```css
int k\u00F6rper;
cout << "Let them eat g\u00E2teau.\n";
```

ö的ISO 10646码点为00F6，而â的码点为00E2。因此，上述C++代码将变量名设置为körper，并显示下面的输出：

```css
Let them eat gâteau.
```

如果系统不支持ISO 10646，它将显示其他字符或gu00E2teau，而不是â。

实际上，从易读性的角度看，在变量名中使用\u00F6没有多大意义，但如果实现的扩展源字符集包含ö，它可能允许您从键盘输入该字符。

请注意，C++使用术语“通用编码名”，而不是“通用编码”，这是因为应将\u00F6解释为“Unicode码点为U-00F6的字符”。支持Unicode的编译器知道，这表示字符ö，但无需使用内部编码00F6。无论计算机使用是ASCII还是其他编码系统，都可在内部表示字符T；同样，在不同的系统中，将使用不同的编码来表示字符ö。在源代码中，可使用适用于所有系统的通用编码名，而编译器将根据当前系统使用合适的内部编码来表示它。



**Unicode和ISO 10646**

Unicode提供了一种表示各种字符集的解决方案——为大量字符和符号提供标准数值编码，并根据类型将它们分组。例如，ASCII码为Unicode的子集，因此在这两种系统中，美国的拉丁字符（如A和Z）的表示相同。然而，Unicode还包含其他拉丁字符，如欧洲语言使用的拉丁字符、来自其他语言（如希腊语、西里尔语、希伯来语、切罗基语、阿拉伯语、泰语和孟加拉语）中的字符以及象形文字（如中国和日本的文字）。到目前为止，Unicode可以表示109000多种符号和90多个手写符号（script），它还在不断发展中。

Unicode给每个字符指定一个编号——码点。Unicode码点通常类似于下面这样：U-222B。其中U表示这是一个Unicode字符，而222B是该字符（积分正弦符号）的十六进制编号。

国际标准化组织（ISO）建立了一个工作组，专门开发ISO 10646——这也是一个对多种语言文本进行编码的标准。ISO 10646小组和Unicode小组从1991年开始合作，以确保他们的标准同步。



#### 5．signed char和unsigned char

与int不同的是，char在默认情况下既不是没有符号，也不是有符号。是否有符号由C++实现决定，这样编译器开发人员可以最大限度地将这种类型与硬件属性匹配起来。如果char有某种特定的行为对您来说非常重要，则可以显式地将类型设置为signed char 或unsigned char：

```css
char fodo;          // may be signed, may be unsigned
unsigned char bar;  // definitely unsigned
signed char snark;  // definitely signed
```

如果将char用作数值类型，则unsigned char和signed char之间的差异将非常重要。unsigned char类型的表示范围通常为0～255，而signed char的表示范围为−128到127。例如，假设要使用一个char变量来存储像200这样大的值，则在某些系统上可以，而在另一些系统上可能不可以。但使用unsigned char可以在任何系统上达到这种目的。另一方面，如果使用char变量来存储标准ASCII字符，则char有没有符号都没关系，在这种情况下，可以使用char。

#### 6．wchar_t

程序需要处理的字符集可能无法用一个8位的字节表示，如日文汉字系统。对于这种情况，C++的处理方式有两种。首先，如果大型字符集是实现的基本字符集，则编译器厂商可以将char定义为一个16位的字节或更长的字节。其次，一种实现可以同时支持一个小型基本字符集和一个较大的扩展字符集。8位char可以表示基本字符集，另一种类型wchar_t（宽字符类型）可以表示扩展字符集。wchar_t类型是一种整数类型，它有足够的空间，可以表示系统使用的最大扩展字符集。这种类型与另一种整型（底层[underlying]类型）的长度和符号属性相同。对底层类型的选择取决于实现，因此在一个系统中，它可能是unsigned short，而在另一个系统中，则可能是int。

cin和cout将输入和输出看作是char流，因此不适于用来处理wchar_t类型。iostream头文件的最新版本提供了作用相似的工具——wcin和wcout，可用于处理wchar_t流。另外，可以通过加上前缀L来指示宽字符常量和宽字符串。下面的代码将字母P的wchar_t版本存储到变量bob中，并显示单词tall的wchar_t版本：

```css
wchar_t bob = L'P';       // a wide-character constant
wcout << L"tall" << endl; // outputting a wide-character string
```

在支持两字节wchar_t的系统中，上述代码将把每个字符存储在一个两个字节的内存单元中。本书不使用宽字符类型，但读者应知道有这种类型，尤其是在进行国际编程或使用Unicode或ISO 10646时。

#### 7．C++11新增的类型：char16_t和char32_t

随着编程人员日益熟悉Unicode，类型wchar_t显然不再能够满足需求。事实上，在计算机系统上进行字符和字符串编码时，仅使用Unicode码点并不够。具体地说，进行字符串编码时，如果有特定长度和符号特征的类型，将很有帮助，而类型wchar_t的长度和符号特征随实现而异。因此，C++11新增了类型char16_t和char32_t，其中前者是无符号的，长16位，而后者也是无符号的，但长32位。C++11使用前缀u表示char16_t字符常量和字符串常量，如u‘C’和u“be good”；并使用前缀U表示char32_t常量，如U‘R’和U“dirty rat”。类型char16_t与\u00F6形式的通用字符名匹配，而类型char32_t与\U0000222B形式的通用字符名匹配。前缀u和U分别指出字符字面值的类型为char16_t和char32_t：

```css
char16_t ch1 = u'q'; // basic character in 16-bit form
char32_t ch2 = U'/U0000222B'; // universal character name in 32-bit form
```

与wchar_t一样，char16_t和char32_t也都有底层类型—— 一种内置的整型，但底层类型可能随系统而异。

