### 17.3.3　其他istream类方法

第3章～第5章讨论了get()和getline()方法。您可能还记得，它们提供下面的输入功能：

+ 方法get(char&)和get(void)提供不跳过空白的单字符输入功能；
+ 函数get(char*, int, char)和getline(char*, int, char)在默认情况下读取整行而不是一个单词。

它们被称为非格式化输入函数（unformatted input functions），因为它们只是读取字符输入，而不会跳过空白，也不进行数据转换。

来看一下istream类的这两组成员函数。

#### 1．单字符输入

在使用char参数或没有参数的情况下，get()方法读取下一个输入字符，即使该字符是空格、制表符或换行符。get(char & ch)版本将输入字符赋给其参数，而get(void)版本将输入字符转换为整型（通常是int），并将其返回。

（1）成员函数get(char &)

先来看get(char &)。假设程序中包含如下循环：

```css
int ct = 0;
char ch;
cin.get(ch);
while (ch != '\n')
{
    cout << ch;
    ct++;
    cin.get(ch);
}
cout << ct << endl;
```

接下来，假设提供了如下输入：

```css
I C++ clearly.<Enter>
```

按下回车键后，这行输入将被发送给程序。上述程序片段将首先读取字符I，使用cout显示它，并将ct递增到1。接着，它读取I后面的空格字符，显示它，并将ct递增到2。这一过程将一直继续下去，直到程序将回车键作为换行符处理，并终止循环。这里的重点是，通过使用get(ch)，代码读取、显示并考虑空格和可打印字符。

假设程序试图使用>>：

```css
int ct = 0;
char ch;
cin >> ch;
while (ch != '\n') // FAILS
{
    cout << ch;
    ct++;
    cin >> ch;
}
cout << ct << endl;
```

则代码将首先跳过空格，这样将不考虑空格，因此相应的输出压缩为如下：

```css
IC++clearly.
```

更糟糕的是，循环不会终止！由于抽取运算符跳过了换行符，因此代码不会将换行符赋给ch，所以while循环测试将不会终止循环。

get(char &)成员函数返回一个指向用于调用它的istream对象的引用，这意味着可以拼接get(char &)后面的其他抽取：

```css
char c1, c2, c3;
cin.get(c1).get(c2) >> c3;
```

首先，cin.get(c1)将第一个输入字符赋给c1，并返回调用对象——cin。这样代码缩为cin.get(c2) >> c3，它将第二个输入字符赋给c2。该函数调用返回cin，将代码缩为cin>>c3。这将把下一个非空白字符赋给c3。因此c1和c2的值最后为空格，但c3不是。

如果cin.get(char &)到达文件尾——无论是真正的文件尾，还是通过键盘仿真的文件尾（对于DOS和Windows命令提示符模式，为按下Ctrl + Z；对于UNIX，是在行首按下Ctrl + D），它都不会给其参数赋值。这是完全正确的，因为如果程序到达文件尾，就没有值可供赋给参数了。另外，该方法还调用setstate（failbit），导致cin的测试结果为false：

```css
char ch;
while (cin.get(ch))
{
      // process input
}
```

只要存在有效输入，cin.get(ch)的返回值都将是cin，此时的判定结果为true，因此循环将继续。到达文件尾时，返回值判定为false，循环终止。

（2）成员函数get(void)

get(void)成员函数还读取空白，但使用返回值来将输入传递给程序。因此可以这样使用它：

```css
int ct = 0;
char ch;
ch = cin.get();      // use return value
while (ch != '\n')
{
    cout << ch;
    ct++;
    ch = cin.get();
}
cout << ct << endl;
```

get(void)成员函数的返回类型为int（或某种更大的整型，这取决于字符集和区域）。这使得下面的代码是非法的：

```css
char c1, c2, c3;
cin.get().get() >> c3; // not valid
```

这里，cin.get()将返回一个int值。由于返回值不是类对象，因此不能对它应用成员运算符。因此将出现语法错误。然而，可以在抽取序列的最后使用get()：

```css
char c1;
cin.get(c1).get(); // valid
```

get(void)的返回类型为int，这意味着它后面不能跟抽取运算符。然而，由于cin.get(c1)返回cin，因此它可以放在get()的前面。上述代码将读取第一个输入字符，将其赋给c1，然后读取并丢弃第二个输入字符。

到达文件尾后（不管是真正的文件尾还是模拟的文件尾），cin.get(void)都将返回值EOF—— 头文件iostream提供的一个符号常量。这种设计特性使得可以这样来读取输入：

```css
int ch;
while ((ch = cin.get()) != EOF)
{
    // process input
}
```

这里应将ch的类型声明为int，而不是char，因为值EOF可能无法使用char类型来表示。

第5章更详细地介绍了这些函数，表17.5对单字符输入函数的特性进行了总结。

<center class="my_markdown"><b class="my_markdown">表17.5　cin.get(ch)与cin.get()</b></center>

| 特　征 | cin.get(ch) | ch = cin.get() |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 传输输入字符的方法 | 赋给参数ch | 将函数返回值赋给ch |
| 字符输入时函数的返回值 | 指向istream对象的引用 | 字符编码（int值） |
| 达到文件尾时函数的返回值 | 转换为false | EOF |

#### 2．采用哪种单字符输入形式

假设可以选择>>、get（char &）或get（void），应使用哪一个呢？首先，应确定是否希望跳过空白。如果跳过空白更方便，则使用抽取运算符>>。例如，提供菜单选项时，跳过空白更为方便：

```css
cout << "a. annoy client    b. bill client\n"
     << "c. calm client     d. deceive client\n"
     << "q.\n";
cout << "Enter a, b, c, d, or q: ";
char ch;
cin >> ch;
while (ch != 'q')
{
    switch(ch)
    {
        ...
    }
    cout << "Enter a, b, c, d, or q: ";
    cin >> ch;
}
```

要输入b进行响应，可以键入b并按回车键，这将生成两个字符的响应——b\n。如果使用get()，则必须添加在每次循环中处理\n字符的代码，而抽取运算符可以跳过它（如果使用过C语言进行编程，则可能遇到过使用换行符进行响应为非法的情况。这是个很容易解决的问题，但比较讨厌）。

如果希望程序检查每个字符，请使用get()方法，例如，计算字数的程序可以使用空格来判断单词何时结束。在get()方法中，get(char &)的接口更佳。get(void)的主要优点是，它与标准C语言中的getchar()函数极其类似，这意味着可以通过包含iostream（而不是stdio.h），并用cin.get()替换所有的getchar()，用cout.put(ch)替换所有的putchar(ch)，来将C程序转换为C++程序。

#### 3．字符串输入：getline()、get()和ignore()

接下来复习一下第4章介绍的字符串输入成员函数。getline()成员函数和get()的字符串读取版本都读取字符串，它们的函数特征标相同（这是从更为通用的模板声明简化而来的）：

```css
istream & get(char *, int, char);
istream & get(char *, int);
istream & getline(char *, int, char);
istream & getline(char *, int);
```

第一个参数是用于放置输入字符串的内存单元的地址。第二个参数比要读取的最大字符数大1（额外的一个字符用于存储结尾的空字符，以便将输入存储为一个字符串）。第三个参数指定用作分界符的字符，只有两个参数的版本将换行符用作分界符。上述函数都在读取最大数目的字符或遇到换行符后为止。

例如，下面的代码将字符输入读取到字符数组line中：

```css
char line[50];
cin.get(line, 50);
```

cin.get()函数将在到达第49个字符或遇到换行符（默认情况）后停止将输入读取到数组中。get()和getline()之间的主要区别在于，get()将换行符留在输入流中，这样接下来的输入操作首先看到是将是换行符，而getline()抽取并丢弃输入流中的换行符。

第4章演示了如何使用这两个成员函数的默认格式。现在来看一下接受三个参数的版本，第三个参数用于指定分界符。遇到分界字符后，输入将停止，即使还未读取最大数目的字符。因此，在默认情况下，如果在读取指定数目的字符之前到达行尾，这两种方法都将停止读取输入。和默认情况一样，get()将分界字符留在输入队列中，而getline()不保留。

程序清单17.13演示了getline()和get()是如何工作的，它还介绍了ignore()成员函数。该函数接受两个参数：一个是数字，指定要读取的最大字符数；另一个是字符，用作输入分界符。例如，下面的函数调用读取并丢弃接下来的255个字符或直到到达第一个换行符：

```css
cin.ignore(255, '\n');
```

原型为两个参数提供的默认值为1和EOF，该函数的返回类型为istream &：

```css
istream & ignore(int = 1, int = EOF);
```

默认参数值EOF导致ignore()读取指定数目的字符或读取到文件尾。

该函数返回调用对象，这使得能够拼接函数调用，如下所示：

```css
cin.ignore(255, '\n').ignore(255, '\n');
```

其中，第一个ignore()方法读取并丢弃一行，第二个调用读取并丢弃另一行，因此一共读取了两行。

现在来看一看程序清单17.13。

程序清单17.13　get_gun.cpp

```css
// get_fun.cpp -- using get() and getline()
#include <iostream>
const int Limit = 255;
int main()
{
    using std::cout;
    using std::cin;
    using std::endl;
    char input[Limit];
    cout << "Enter a string for getline() processing:\n";
    cin.getline(input, Limit, '#');
    cout << "Here is your input:\n";
    cout << input << "\nDone with phase 1\n";
    char ch;
    cin.get(ch);
    cout << "The next input character is " << ch << endl;
    if (ch != '\n')
        cin.ignore(Limit, '\n'); // discard rest of line
    cout << "Enter a string for get() processing:\n";
    cin.get(input, Limit, '#');
    cout << "Here is your input:\n";
    cout << input << "\nDone with phase 2\n";
    cin.get(ch);
    cout << "The next input character is " << ch << endl;
    return 0;
}
```

下面是程序清单17.13中程序的运行情况：

```css
Enter a string for getline() processing:
Please pass
me a #3 melon!
Here is your input:
Please pass
me a
Done with phase 1
The next input character is 3
Enter a string for get() processing:
I still
want my #3 melon!
Here is your input:
I still
want my
Done with phase 2
The next input character is #
```

注意，getline()函数将丢弃输入中的分界字符#，而get()函数不会。

#### 4．意外字符串输入

get(char *, int)和getline()的某些输入形式将影响流状态。与其他输入函数一样，这两个函数在遇到文件尾时将设置eofbit，遇到流被破坏（如设备故障）时将设置badbit。另外两种特殊情况是无输入以及输入到达或超过函数调用指定的最大字符数。下面来看这些情况。

对于上述两个方法，如果不能抽取字符，它们将把空值字符放置到输入字符串中，并使用setstate()设置failbit。方法在什么时候无法抽取字符呢？一种可能的情况是输入方法立刻到达了文件尾。对于get(char *, int)来说，另一种可能是输入了一个空行：

```css
char temp[80];
while (cin.get(temp,80)) // terminates on empty line
     ...
```

有意思的是，空行并不会导致getline()设置failbit。这是因为getline()仍将抽取换行符，虽然不会存储它。如果希望getline()在遇到空行时终止循环，则可以这样编写：

```css
char temp[80];
while (cin.getline(temp,80) && temp[0] != '\0') // terminates on empty line
```

现在假设输入队列中的字符数等于或超过了输入方法指定的最大字符数。首先，来看getline()和下面的代码：

```css
char temp[30];
while (cin.getline(temp,30))
```

getline()方法将从输入队列中读取字符，将它们放到temp数组的元素中，直到（按测试顺序）到达文件尾、将要读取的字符是换行符或存储了29个字符为止。如果遇到文件尾，则设置eofbit；如果将要读取的字符是换行符，则该字符将被读取并丢弃；如果读取了29个字符，并且下一个字符不是换行符，则设置failbit。因此，包含30个或更多字符的输入行将终止输入。

现在来看get(char *, int)方法。它首先测试字符数，然后测试是否为文件尾以及下一个字符是否是换行符。如果它读取了最大数目的字符，则不设置failbit标记。然而，由此可以知道终止读取是否是由于输入字符过多引起的。可以用peek()（参见下一节）来查看下一个输入字符。如果它是换行符，则说明get()已读取了整行；如果不是换行符，则说明get()是在到达行尾前停止的。这种技术对getline()不适用，因为getline()读取并丢弃换行符，因此查看下一个字符无法知道任何情况。然而，如果使用的是get()，则可以知道是否读取了整个一行。下一节将介绍这种方法的一个例子。另外，表17.6总结了这些行为。

<center class="my_markdown"><b class="my_markdown">表17.6　输入行为</b></center>

| 方　法 | 行　为 |
| :-----  | :-----  | :-----  | :-----  |
| getline(char *, int) | 如果没有读取任何字符（但换行符被视为读取了一个字符），则设置failbit | 如果读取了最大数目的字符，且行中还有其他字符，则设置failbit |
| get(char *, int) | 如果没有读取任何字符，则设置failbit |

