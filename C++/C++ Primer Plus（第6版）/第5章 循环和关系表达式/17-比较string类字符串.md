### 5.1.15　比较string类字符串

如果使用string类字符串而不是C-风格字符串，比较起来将简单些，因为类设计让您能够使用关系运算符进行比较。这之所以可行，是因为类函数重载（重新定义）了这些运算符。第12章将介绍如何将这种特性加入到类设计中，但从应用的角度说，读者现在只需知道可以将关系运算符用于string对象即可。程序清单5.12是在程序清单5.11的基础上修改而成的，它使用的是string对象而不是char数组。

程序清单5.12　compstr2.cpp

```css
// compstr2.cpp -- comparing strings using arrays
#include <iostream>
#include <string> // string class
int main()
{
    using namespace std;
    string word = "?ate";
    for (char ch = ‘a’; word != "mate"; ch++)
    {
        cout << word << endl;
        word[0] = ch;
    }
    cout << "After loop ends, word is " << word << endl;
    return 0;
}
```

该程序的输出与程序清单5.11相同。

**程序说明**

在程序清单5.12中，下面的测试条件使用了一个关系运算符，该运算符的左边是一个string对象，右边是一个C-风格字符串：

```css
word != "mate"
```

string类重载运算符!=的方式让您能够在下述条件下使用它：至少有一个操作数为string对象，另一个操作数可以是string对象，也可以是C-风格字符串。

string类的设计让您能够将string对象作为一个实体（在关系型测试表达式中），也可以将其作为一个聚合对象，从而使用数组表示法来提取其中的字符。

正如您看到的，使用C-风格字符串和string对象可获得相同的结果，但使用string对象更简单、更直观。

最后，和前面大多数for循环不同，此循环不是计数循环。也就是说，它并不对语句块执行指定的次数。相反，此循环将根据情况（word为“mate”）来确定是否停止。对于这种测试，C++程序通常使用while循环，下面来看看这种循环。

