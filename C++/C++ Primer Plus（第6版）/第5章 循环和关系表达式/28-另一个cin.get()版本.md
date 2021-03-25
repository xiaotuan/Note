### 5.5.5　另一个cin.get()版本

“怀旧”的C语言用户可能喜欢C语言中的字符I/O函数——getchar()和putchar()，它们仍然适用，只要像在C语言中那样包含头文件stdio.h（或新的cstdio）即可。也可以使用istream和ostream类中类似功能的成员函数，来看看这种方式。

不接受任何参数的cin.get()成员函数返回输入中的下一个字符。也就是说，可以这样使用它：

```css
ch = cin.get();
```

该函数的工作方式与C语言中的getchar()相似，将字符编码作为int值返回；而cin.get(ch)返回一个对象，而不是读取的字符。同样，可以使用cout.put()函数（参见第3章）来显示字符：

```css
cout.put(ch);
```

该函数的工作方式类似C语言中的putchar()，只不过其参数类型为char，而不是int。

> **注意：**
> 最初，put()成员只有一个原型——put(char)。可以传递一个int参数给它，该参数将被强制转换为char。C++标准还要求只有一个原型。然而，有些C++实现都提供了3个原型：put(char)、put(signed char)和put(unsigned char)。在这些实现中，给put()传递一个int参数将导致错误消息，因为转换int的方式不止一种。使用显式强制类型转换的原型（如cin.put(char(ch))）可使用int参数。

为成功地使用cin.get()，需要知道其如何处理EOF条件。当该函数到达EOF时，将没有可返回的字符。相反，cin.get()将返回一个用符号常量EOF表示的特殊值。该常量是在头文件iostream中定义的。EOF值必须不同于任何有效的字符值，以便程序不会将EOF与常规字符混淆。通常，EOF被定义为值−1，因为没有ASCII码为−1的字符，但并不需要知道实际的值，而只需在程序中使用EOF即可。例如，程序清单5.18的核心是这样：

```css
char ch;
cin.get(ch);
while (cin.fail() == false) // test for EOF
{
    cout << ch;
    ++count;
    cin.get(ch);
}
```

可以使用int ch，并用cin.get()代替cin.get(char)，用cout.put()代替cout，用EOF测试代替cin.fail()测试：

```css
int ch; /// for compatibility with EOF value
ch = cin.get();
while (ch != EOF)
{
    cout.put(ch); // cout.put(char(ch)) for some implementations
    ++count;
    ch = cin.get();
}
```

如果ch是一个字符，则循环将显示它。如果ch为EOF，则循环将结束。

> **提示：**
> 需要知道的是，EOF不表示输入中的字符，而是指出没有字符。

除了当前所做的修改外，关于使用cin.get()还有一个微妙而重要的问题。由于EOF表示的不是有效字符编码，因此可能不与char类型兼容。例如，在有些系统中，char类型是没有符号的，因此char变量不可能为EOF值（−1）。由于这种原因，如果使用cin.get()（没有参数）并测试EOF，则必须将返回值赋给int变量，而不是char变量。另外，如果将ch的类型声明为int，而不是char，则必须在显示ch时将其强制转换为char类型。

程序清单5.19将程序清单5.18进行了修改，使用了cin.get()方法。它还通过将字符输入与while循环测试合并在一起，使代码更为简洁。

程序清单5.19　textin4.cpp

```css
// textin4.cpp -- reading chars with cin.get()
#include <iostream>
int main(void)
{
    using namespace std;
    int ch;                                // should be int, not char
    int count = 0;
    while ((ch = cin.get()) != EOF)  // test for end-of-file
    {
        cout.put(char(ch));
        ++count;
    }
    cout << endl << count << " characters read\n";
    return 0;
}
```

> **注意：**
> 有些系统要么不支持来自键盘的模拟EOF，要么支持地不完善，在这种情况下，上述示例将无法正常运行。如果使用cin.get()来锁住屏幕直到可以阅读它，这将不起作用，因为检测EOF时将禁止进一步读取输入。然而，可以使用程序清单5.14那样的计时循环来使屏幕停留一段时间。还可使用第17章将介绍的cin.clear()来重置输入流。

下面是该程序的运行情况：

```css
The sullen mackerel sulks in the shadowy shallows.
The sullen mackerel sulks in the shadowy shallows.
Yes, but the blue bird of happiness harbors secrets.<ENTER>
Yes, but the blue bird of happiness harbors secrets.
<CTRL>+<Z><ENTER>
104 characters read
```

下面分析一下循环条件：

```css
while ((ch = cin.get()) != EOF)
```

子表达式ch=cin.get()两端的括号导致程序首先计算该表达式。为此，程序必须首先调用cin.get()函数，然后将该函数的返回值赋给ch。由于赋值语句的值为左操作数的值，因此整个子表达式变为ch的值。如果这个值是EOF，则循环将结束，否则继续。该测试条件中所有的括号都是必不可少的。如果省略其中的一些括号：

```css
while (ch = cin.get() != EOF)
```

由于!=运算符的优先级高于=，因此程序将首先对cin.get()的返回值和EOF进行比较。比较的结果为false或true，而这些bool值将被转换为0或1，并本质赋给ch。

另一方面，使用cin.get(ch)（有一个参数）进行输入时，将不会导致任何类型方面的问题。前面讲过，cin.get(char)函数在到达EOF时，不会将一个特殊值赋给ch。事实上，在这种情况下，它不会将任何值赋给ch。ch不会被用来存储非char值。表5.3总结了cin.get(char)和cin.get()之间的差别。

<center class="my_markdown"><b class="my_markdown">表5.3　cin.get(ch)与cin.get()</b></center>

| 属　性 | cin.get(ch) | ch=cin.get() |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 传递输入字符的方式 | 赋给参数ch | 将函数返回值赋给ch |
| 用于字符输入时函数的返回值 | istream对象（执行bool转换后为true） | int类型的字符编码 |
| 到达EOF时函数的返回值 | istream对象（执行bool转换后为false） | EOF |

那么应使用cin.get()还是cin.get(char)呢？使用字符参数的版本更符合对象方式，因为其返回值是istream对象。这意味着可以将它们拼接起来。例如，下面的代码将输入中的下一个字符读入到ch1中，并将接下来的一个字符读入到ch2中：

```css
cin.get(ch1).get(ch2);
```

这是可行的，因为函数调用cin.get(ch1)返回一个cin对象，然后便可以通过该对象调用get(ch2)。

get()的主要用途是能够将stdio.h的getchar()和putchar()函数转换为iostream的cin.get()和cout.put()方法。只要用头文件iostream替换stdio.h，并用作用相似的方法替换所有的getchar()和putchar()即可。（如果旧的代码使用int变量进行输入，而所用的实现包含put()的多个原型，则必须做进一步的调整。）

