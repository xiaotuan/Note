### 4.3　string类简介

ISO/ANSI C++98标准通过添加string类扩展了C++库，因此现在可以string类型的变量（使用C++的说法是对象）而不是字符数组来存储字符串。您将看到，string类使用起来比数组简单，同时提供了将字符串作为一种数据类型的表示方法。

要使用string类，必须在程序中包含头文件string。string类位于名称空间std中，因此您必须提供一条using编译指令，或者使用std::string来引用它。string类定义隐藏了字符串的数组性质，让您能够像处理普通变量那样处理字符串。程序清单4.7说明了string对象与字符数组之间的一些相同点和不同点。

程序清单4.7　strtype1.cpp

```css
// strtype1.cpp -- using the C++ string class
#include <iostream>
#include <string>                  // make string class available
int main()
{
    using namespace std;
    char charr1[20];               // create an empty array
    char charr2[20] = "jaguar";    // create an initialized array
    string str1;                   // create an empty string object
    string str2 = "panther";       // create an initialized string
    cout << "Enter a kind of feline: ";
    cin >> charr1;
    cout << "Enter another kind of feline: ";
    cin >> str1;                  // use cin for input
    cout << "Here are some felines:\n";
    cout << charr1 << " " << charr2 << " "
         << str1 << " " << str2    // use cout for output
         << endl;
    cout << "The third letter in " << charr2 << " is "
         << charr2[2] << endl;
    cout << "The third letter in " << str2 << " is "
         << str2[2] << endl;       // use array notation
    return 0;
}
```

下面是该程序的运行情况：

```css
Enter a kind of feline: ocelot
Enter another kind of feline: tiger
Here are some felines:
ocelot jaguar tiger panther
The third letter in jaguar is g
The third letter in panther is n
```

从这个示例可知，在很多方面，使用string对象的方式与使用字符数组相同。

+ 可以使用C-风格字符串来初始化string对象。
+ 可以使用cin来将键盘输入存储到string对象中。
+ 可以使用cout来显示string对象。
+ 可以使用数组表示法来访问存储在string对象中的字符。

程序清单4.7表明，string对象和字符数组之间的主要区别是，可以将string对象声明为简单变量，而不是数组：

```css
string str1;              // create an empty string object
string str2 = "panther";  // create an initialized string
```

类设计让程序能够自动处理string的大小。例如，str1的声明创建一个长度为0的string对象，但程序将输入读取到str1中时，将自动调整str1的长度：

```css
cin >> str1;           // str1 resized to fit input
```

这使得与使用数组相比，使用string对象更方便，也更安全。从理论上说，可以将char数组视为一组用于存储一个字符串的char存储单元，而string类变量是一个表示字符串的实体。

