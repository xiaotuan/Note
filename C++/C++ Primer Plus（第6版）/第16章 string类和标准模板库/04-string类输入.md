### 16.1.2　string类输入

对于类，很有帮助的另一点是，知道有哪些输入方式可用。对于C-风格字符串，有3种方式：

```css
char info[100];
cin >> info;             // read a word
cin.getline(info, 100);  // read a line, discard \n
cin.get(info, 100);      // read a line, leave \n in queue
```

对于string对象，有两种方式：

```css
string stuff;
cin >> stuff;        // read a word
getline(cin, stuff); // read a line, discard \n
```

两个版本的getline()都有一个可选参数，用于指定使用哪个字符来确定输入的边界：

```css
cin.getline(info,100,':'); // read up to :, discard :
getline(stuff, ':');       // read up to :, discard :
```

在功能上，它们之间的主要区别在于，string版本的getline()将自动调整目标string对象的大小，使之刚好能够存储输入的字符：

```css
char fname[10];
string lname;
cin >> fname;            // could be a problem if input size > 9 characters
cin >> lname;            // can read a very, very long word
cin.getline(fname, 10);  // may truncate input
getline(cin, fname);     // no truncation
```

自动调整大小的功能让string版本的getline()不需要指定读取多少个字符的数值参数。

在设计方面的一个区别是，读取C-风格字符串的函数是istream类的方法，而string版本是独立的函数。这就是对于C-风格字符串输入，cin是调用对象；而对于string对象输入，cin是一个函数参数的原因。这种规则也适用于>>形式，如果使用函数形式来编写代码，这一点将显而易见：

```css
cin.operator>>(fname);  // ostream class method
operator>>(cin, lname); // regular function
```

下面更深入地探讨一下string输入函数。正如前面指出的，这两个函数都自动调整目标string的大小，使之与输入匹配。但也存在一些限制。第一个限制因素是string对象的最大允许长度，由常量string::npos指定。这通常是最大的unsigned int值，因此对于普通的交互式输入，这不会带来实际的限制；但如果您试图将整个文件的内容读取到单个string对象中，这可能成为限制因素。第二个限制因素是程序可以使用的内存量。

string版本的getline()函数从输入中读取字符，并将其存储到目标string中，直到发生下列三种情况之一：

+ 到达文件尾，在这种情况下，输入流的eofbit将被设置，这意味着方法fail()和eof()都将返回true；
+ 遇到分界字符（默认为\n），在这种情况下，将把分界字符从输入流中删除，但不存储它；
+ 读取的字符数达到最大允许值（string::npos和可供分配的内存字节数中较小的一个），在这种情况下，将设置输入流的failbit，这意味着方法fail()将返回true。

输入流对象有一个统计系统，用于跟踪流的错误状态。在这个系统中，检测到文件尾后将设置eofbit寄存器，检测到输入错误时将设置failbit寄存器，出现无法识别的故障（如硬盘故障）时将设置badbit寄存器，一切顺利时将设置goodbit寄存器。第17章将更深入地讨论这一点。

string版本的operator>>()函数的行为与此类似，只是它不断读取，直到遇到空白字符并将其留在输入队列中，而不是不断读取，直到遇到分界字符并将其丢弃。空白字符指的是空格、换行符和制表符，更普遍地说，是任何将其作为参数来调用isspace()时，该函数返回ture的字符。

本书前面有多个控制台string输入示例。由于用于string对象的输入函数使用输入流，能够识别文件尾，因此也可以使用它们来从文件中读取输入。程序清单16.2是一个从文件中读取字符串的简短示例，它假设文件中包含用冒号字符分隔的字符串，并使用指定分界符的getline()方法。然后，显示字符串并给它们编号，每个字符串占一行。

程序清单16.2　strfile.cpp

```css
// strfile.cpp -- read strings from a file
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
int main()
{
    using namespace std;
    ifstream fin;
    fin.open("tobuy.txt");
    if (fin.is_open() == false)
    {
        cerr << "Can't open file. Bye.\n";
        exit(EXIT_FAILURE);
    }
    string item;
    int count = 0;
    getline(fin, item, ':');
    while (fin) // while input is good
    {
        ++count;
        cout << count <<": " << item << endl;
        getline(fin, item,':');
    }
    cout << "Done\n";
    fin.close();
    return 0;
}
```

下面是文件tobuy.txt的内容：

```css
sardines:chocolate ice cream:pop corn:leeks:
cottage cheese:olive oil:butter:tofu:
```

通常，对于程序要查找的文本文件，应将其放在可执行程序或项目文件所在的目录中；否则必须提供完整的路径名。在Windows系统中，C-风格字符串中的转义序列\表示一个斜杠：

```css
fin.open("C:\\CPP\\Progs\\tobuy.txt"); // file = C:\CPP\Progs\tobuy.txt
```

下面是程序清单16.2中程序的输出：

```css
1: sardines
2: chocolate ice cream
3: pop corn
4: leeks
5:
cottage cheese
6: olive oil
7: butter
8: tofu
9:
Done
```

注意，将:指定为分界字符后，换行符将被视为常规字符。因此文件tobuy.txt中第一行末尾的换行符将成为包含“cottage cheese”的字符串中的第一个字符。同样，第二行末尾的换行符是第9个输入字符串中唯一的内容。

