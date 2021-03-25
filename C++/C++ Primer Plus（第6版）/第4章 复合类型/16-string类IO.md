### 4.3.4　string类I/O

正如您知道的，可以使用cin和运算符>>来将输入存储到string对象中，使用cout和运算符<<来显示string对象，其句法与处理C-风格字符串相同。但每次读取一行而不是一个单词时，使用的句法不同，程序清单4.10说明了这一点。

程序清单4.10　strtype4.cpp

```css
// strtype4.cpp -- line input
#include <iostream>
#include <string>           // make string class available
#include <cstring>          // C-style string library
int main()
{
    using namespace std;
    char charr[20];
    string str;
    cout << "Length of string in charr before input: "
         << strlen(charr) << endl;
    cout << "Length of string in str before input: "
         << str.size() << endl;
    cout << "Enter a line of text:\n";
    cin.getline(charr, 20);  // indicate maximum length
    cout << "You entered: " << charr << endl;
    cout << "Enter another line of text:\n";
    getline(cin, str);       // cin now an argument; no length specifier
    cout << "You entered: " << str << endl;
    cout << "Length of string in charr after input: "
         << strlen(charr) << endl;
    cout << "Length of string in str after input: "
         << str.size() << endl;
    return 0;
}
```

下面是一个运行该程序时的输出示例：

```css
Length of string in charr before input: 27
Length of string in str before input: 0
Enter a line of text:
peanut butter
You entered: peanut butter
Enter another line of text:
blueberry jam
You entered: blueberry jam
Length of string in charr after input: 13
Length of string in str after input: 13
```

在用户输入之前，该程序指出数组charr中的字符串长度为27，这比该数组的长度要大。这里有两点需要说明。首先，未初始化的数组的内容是未定义的；其次，函数strlen()从数组的第一个元素开始计算字节数，直到遇到空字符。在这个例子中，在数组末尾的几个字节后才遇到空字符。对于未被初始化的数据，第一个空字符的出现位置是随机的，因此您在运行该程序时，得到的数组长度很可能与此不同。

另外，用户输入之前，str中的字符串长度为0。这是因为未被初始化的string对象的长度被自动设置为0。

下面是将一行输入读取到数组中的代码：

```css
cin.getline(charr, 20);
```

这种句点表示法表明，函数getline()是istream类的一个类方法（还记得吗，cin是一个istream对象）。正如前面指出的，第一个参数是目标数组；第二个参数数组长度，getline()使用它来避免超越数组的边界。

下面是将一行输入读取到string对象中的代码：

```css
getline(cin,str);
```

这里没有使用句点表示法，这表明这个getline()不是类方法。它将cin作为参数，指出到哪里去查找输入。另外，也没有指出字符串长度的参数，因为string对象将根据字符串的长度自动调整自己的大小。

那么，为何一个getline()是istream的类方法，而另一个不是呢？在引入string类很久之前，C++就有istream类。因此istream的设计考虑到了诸如double和int等基本C++数据类型，但没有考虑string类型，所以istream类中，有处理double、int和其他基本类型的类方法，但没有处理string对象的类方法。

由于istream类中没有处理string对象的类方法，因此您可能会问，下述代码为何可行呢？

```css
cin >> str; // read a word into the str string object
```

像下面这样的代码使用istream类的一个成员函数：

```css
cin >> x; // read a value into a basic C++ type
```

但前面处理string对象的代码使用string类的一个友元函数。有关友元函数及这种技术为何可行，将在第11章介绍。另外，您可以将cin和cout用于string对象，而不用考虑其内部工作原理。

