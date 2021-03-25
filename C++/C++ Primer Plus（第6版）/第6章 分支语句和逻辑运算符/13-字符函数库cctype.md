### 6.3　字符函数库cctype

C++从C语言继承了一个与字符相关的、非常方便的函数软件包，它可以简化诸如确定字符是否为大写字母、数字、标点符号等工作，这些函数的原型是在头文件cctype（老式的风格中为ctype.h）中定义的。例如，如果ch是一个字母，则isalpha（ch）函数返回一个非零值，否则返回0。同样，如果ch是标点符号（如逗号或句号），函数ispunct（ch）将返回true。（这些函数的返回类型为int，而不是bool，但通常bool转换让您能够将它们视为bool类型。）

使用这些函数比使用AND和OR运算符更方便。例如，下面是使用AND和OR来测试字符ch是不是字母字符的代码：

```css
if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
```

与使用isalpha()相比：

```css
if (isalpha(ch))
```

isalpha()不仅更容易使用，而且更通用。AND/OR格式假设A-Z的字符编码是连续的，其他字符的编码不在这个范围内。这种假设对于ASCII码来说是成立的，但通常并非总是如此。

程序清单6.8演示一些ctype库函数。具体地说，它使用isalpha()来检查字符是否为字母字符，使用isdigits()来测试字符是否为数字字符，如3，使用isspace()来测试字符是否为空白，如换行符、空格和制表符，使用ispunct()来测试字符是否为标点符号。该程序还复习了if else if结构，并在一个while循环中使用了cin.get（char）。

程序清单6.8　cctypes.cpp

```css
// cctypes.cpp -- using the ctype.h library
#include <iostream>
#include <cctype> // prototypes for character functions
int main()
{
    using namespace std;
    cout << "Enter text for analysis, and type @"
            " to terminate input.\n";
    char ch;
    int whitespace = 0;
    int digits = 0;
    int chars = 0;
    int punct = 0;
    int others = 0;
    cin.get(ch);              // get first character
    while (ch != '@')         // test for sentinel
    {
        if(isalpha(ch))       // is it an alphabetic character?
            chars++;
        else if(isspace(ch))  // is it a whitespace character?
            whitespace++;
        else if(isdigit(ch))  // is it a digit?
            digits++;
        else if(ispunct(ch))  // is it punctuation?
            punct++;
        else
            others++;
        cin.get(ch);          // get next character
    }
    cout << chars << " letters, "
         << whitespace << " whitespace, "
         << digits << " digits, "
         << punct << " punctuations, "
         << others << " others.\n";
    return 0;
}
```

下面是该程序的运行情况。注意，空白字符计数中包括换行符：

```css
Enter text for analysis, and type @ to terminate input.
AdrenalVision International producer Adrienne Vismonger
announced production of their new 3-D film, a remake of
"My Dinner with Andre," scheduled for 2013. "Wait until
you see the the new scene with an enraged Collossipede!"@
177 letters, 33 whitespace, 5 digits, 9 punctuations, 0 others.
```

表6.4对cctype软件包中的函数进行了总结。有些系统可能没有表中列出的一些函数，也可能还有在表中没有列出的一些函数。

<center class="my_markdown"><b class="my_markdown">表6.4　cctype中的字符函数</b></center>

| 函 数 名 称 | 返　回　值 |
| :-----  | :-----  | :-----  | :-----  |
| isalnum() | 如果参数是字母数字，即字母或数字，该函数返回true |
| isalpha() | 如果参数是字母，该函数返回true |
| iscntrl() | 如果参数是控制字符，该函数返回true |
| isdigit() | 如果参数是数字（0～9），该函数返回true |
| isgraph() | 如果参数是除空格之外的打印字符，该函数返回true |
| islower() | 如果参数是小写字母，该函数返回true |
| isprint() | 如果参数是打印字符（包括空格），该函数返回true |
| ispunct() | 如果参数是标点符号，该函数返回true |
| isspace() | 如果参数是标准空白字符，如空格、进纸、换行符、回车、水平制表符或者垂直制表符，该函数返回true |
| isupper() | 如果参数是大写字母，该函数返回true |
| isxdigit() | 如果参数是十六进制数字，即0～9、a～f或A～F，该函数返回true |
| tolower() | 如果参数是大写字符，则返回其小写，否则返回该参数 |
| toupper() | 如果参数是小写字符，则返回其大写，否则返回该参数 |

