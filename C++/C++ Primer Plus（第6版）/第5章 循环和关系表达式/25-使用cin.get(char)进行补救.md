### 5.5.2　使用cin.get(char)进行补救

通常，逐个字符读取输入的程序需要检查每个字符，包括空格、制表符和换行符。cin所属的istream类（在iostream中定义）中包含一个能够满足这种要求的成员函数。具体地说，成员函数cin.get(ch)读取输入中的下一个字符（即使它是空格），并将其赋给变量ch。使用这个函数调用替换cin>>ch，可以修补程序清单5.16的问题。程序清单5.17列出了修改后的代码。

程序清单5.17　textin2.cpp

```css
// textin2.cpp -- using cin.get(char)
#include <iostream>
int main()
{
    using namespace std;
    char ch;
    int count = 0;
    cout << "Enter characters; enter # to quit:\n";
    cin.get(ch);       // use the cin.get(ch) function
    while (ch != ‘#’)
    {
        cout << ch;
        ++count;
        cin.get(ch);  // use it again
    }
    cout << endl << count << " characters read\n";
    return 0;
}
```

下面是该程序的运行情况：

```css
Enter characters; enter # to quit:
Did you use a #2 pencil?
Did you use a
14 characters read
```

现在，该程序回显了每个字符，并将全部字符计算在内，其中包括空格。输入仍被缓冲，因此输入的字符个数仍可能比最终到达程序的要多。

如果熟悉C语言，可能以为这个程序存在严重的错误！cin.get(ch)调用将一个值放在ch变量中，这意味着将修改该变量的值。在C语言中，要修改变量的值，必须将变量的地址传递给函数。但程序清单5.17调用cin.get()时，传递的是ch，而不是&ch。在C语言中，这样的代码无效，但在C++中有效，只要函数将参数声明为引用即可。引用是C++在C语言的基础上新增的一种类型。头文件iostream将cin.get(ch)的参数声明为引用类型，因此该函数可以修改其参数的值。我们将在第8章中详细介绍。同时，C语言行家可以松一口气了——通常，在C++中传递的参数的工作方式与在C语言中相同。然而，cin.get(ch)不是这样。

