[toc]

字节数组类 `QByteArray` 提供一个字节数组，用于存储原始字节。该类在串口通信中经常被使用，因为串口通信数据都是一个一个的 8 位字节流。

### 1. 初始化

通常有两种方法可以初始化 `QByteArray` 类的对象。

第一种方法是通过 `const char*` 将其传递给构造函数。例如：

```cpp
QByteArray ba("Hello");
```

> 注意：系统会将字符串中的 `\0` 字符也添加到 `QByteArray` 中。

第二种方法是使用 `resize()` 设置数组的大小，并初始化每个数组元素。

```cpp
QByteArray ba;
ba.resize(6);
ba[0] = 0x3c;
ba[1] = 0xb8;
ba[2] = 0x64;
ba[3] = 0x18;
ba[4] = 0xca;
```

`QByteArray` 类使用从 0 开始的索引值。在调用 `resize()` 后，新分配的字节具有未定义的值。要将所有字节设置为特定值，可以调用 `fill()` 函数，该函数的原型声明如下：

```cpp
QByteArray &QByteArray::fill(char ch, int size = -1)
```

其中，参数 `ch` 是要给字节数组设置的字符；`size` 如果不是 -1，就表示重新要为字节数组开辟的控件大小。比如：

```cpp
QByteArray ba("Istambul");
ba.fill('o');
// ba = "oooooooo"
ba.fill('X', 2);
// ba = "XX"
```

### 2. 访问某个元素

访问 `QByteArray` 类对象中的某个元素主要有 4 种方式，分别为 `[]`、`at()`、`data[]` 和  `constData[]`。其中 `[]` 和 `data[]` 方式为可读可写，`at[]` 和 `constData[]` 方式仅为可读。如果只是进行读操作，则通过 `at()` 和 `constData[]` 方式的访问速度最快，因为避免了复制处理。

`at[]` 可以比 `operator []()` 更快，就是因为前者不会发生深层复制。

示例代码：

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QByteArray bal("Hello");
    if ('\0' == bal[5])
        printf("bal[5]=\'\\0\'\n");

    QByteArray ba;
    ba.resize(6);
    ba[0] = 0x3c;
    ba[1] = 0xb8;
    ba[2] = 0x64;
    ba[3] = 0x18;
    ba[4] = 0xca;
    ba.data()[5] = 0x31;
    qDebug() << "[]" << ba[2];  // [] d
    qDebug() << "at() " << ba.at(2);    // at() d
    qDebug() << "data() " << ba.data()[2];  // data() d
    qDebug() << "constData() " << ba.constData()[2];    // constData() d
    qDebug() << "constData() " << ba.constData()[5];    // constData() 1

    return a.exec();
}
```

运行结果如下：

```
bal[5]='\0'
[] d
at()  d
data()  d
constData()  d
constData()  1
```

### 3. 截取子字节数组

要一次提取多个字节，可使用函数 `left()`、`right()` 或 `mid()`。

（1）函数 `left()` 返回从索引 0 位置开始、长度为 `len` 的子字节数组，该函数的原型声明如下：

```cpp
QByteArray left(int len);
```

如果 `len` 大于原来整个字节数组的长度，则返回整个字节数组：

```cpp
QByteArray x("Pineapple");
QByteArray y = x.left(4);
// y == "Pine"
```

（2）函数 `right()` 用来获取从字节数组最后一个字节数据开始，向前面截取 `len` 个字节并返回截取的字节数组。该函数的原型声明如下：

```cpp
QByteArray right(int len);
```

如果 `len` 大于原来整个字节数组的长度，则返回整个字节数组：

```cpp
QByteArray x("Prineapple");
QByteArray y = x.right(5);
// y == "apple"
```

（3）函数 `mid()` 返回从指定索引位置开始，向右边（即后面）长度为 `len` 的字节数组。该函数的原型声明如下：

```cpp
QByteArray mid(int pos, int len = -1);
```

其中，参数 `pos` 表示开始截取的索引，索引值从 0 开始；`len` 表示要截取的字节数组的长度，如果 `len` 为 -1（默认值）或 `pos + len` 大于原字节数组的长度，则返回从 `pos` 开始一直到右边剩下的全部字节数组。

```cpp
QByteArray x("Five pineapples");
QByteArray y = x.mid(5, 4);	// y == "pine"
QByteArray z = x.mid(5);	// z == "pineapples"
```

### 4. 获取字节数组的大小

可以用成员函数 `size`、`length` 和 `count` 来获取字节数组的大小。除了名字不同， 这 3 个函数是等同的，函数的原型声明如下：

```cpp
int size();
int length();
int count();
```

`size()` 函数的用法如下：

```cpp
QByteArray ba("Hello");
int n = ba.size();	// n == 5
```

> 提示：`size()` 并不包含字符串末尾自动添加的 `\0`。另外，如果以字符串形式初始化，中间有 `\0`，则 `size()` 不会统计 `\0` 及其后面的字符。
>
> ```cpp
> QByteArray ba2("He\0llo");
> int n = ba2.size();	// n == 2
> ```
>
> 通过 `resize` 分配空间，然后通过逐个赋值来进行初始化的话，中间某个字节数据是 `\0`，并不会被 `size()` 函数截断。比如：
>
> ```cpp
> QByteArray ba3;
> ba3.resize(6);
> ba3[0] = 0x3c;
> ba3[1] = '\0';
> ba3[2] = 0x64;
> ba3[3] = 0x18;
> ba3[4] = 0xca;
> ba3.data()[5] = 0x31;
> n = ba3.size();	// n == 6
> ```

### 5. 数据转换与处理

#### 5.1 Hex 转换（十六进制转换）

`QByteArray` 类的公有静态函数 `QByteArray::fromHex` 可以把十六进制编码的数据转换为字符（`char`）类型的数据，并存储到 `QByteArray` 类对象中。该函数的原型声明如下：

```cpp
QByteArray fromHex(const QByteArray &hexEncoded);
```

其中，参数 `hexEncoded` 是十六进制编码的字节数组。由于该函数并不检查参数的有效性，因此遇到非十六进制数据则直接略过，然后继续处理剩余的数据：

```cpp
QByteArray text = QByteArray::fromHex("517420697320677265617421");
text.data();	// returns "Qt is great!""
```

与 `fromHex()` 相逆的函数是 `toHex()`，该函数将字节数组中十六进制的数值编码转化为字符，它的原型声明如下：

```cpp
QByteArray toHex();
```

例如：

```cpp
QByteArray ba;
ba.resize(3);
ba[0] = 0x30;
ba[1] = 0x31;
ba[2] = 0x32;
qDebug() << ba.toHex();	// return "303132"
```

#### 5.2 数值转换与输出

`QByteArray` 类的公有静态函数 `number` 可以将数据显示成二进制、十六进制、显示科学记数和指定小数位数值，该函数的原型声明如下：

```cpp
QByteArray number(int n, int base = 10);
```

其中，参数 `n` 是要转变的整数；`base` 是要进行转换的进制，进制取值范围为 2 到 36，即从二进制到三十六机制。例如：

```cpp
int n = 63;
qDebug() << QByteArray::number(n);	// returns "63"
qDebug() << QByteArray::number(n, 16);	// return "3f"
qDebug() << QByteArray::number(n, 16).toUpper();	// returns "3F"
qDebug() << QByteArray::number(n, 2);	// returns "111111"
qDebug() << QByteArray::number(n, 8);	// return "77"
```

`setNum()` 函数也是将某个整数转为某种进制的字符数组，函数的原型声明如下：

```cpp
QByteArray & setNum(int n, int base = 10);
```

例如：

```cpp
QByteArray ba;
int n = 63;
ba.setNum(n);	// ba = "63"
ba.setNum(n, 16);	// ba = "3f"
```

因为 `setNum()` 不是静态函数，所以要用对象来调用。

除了整数之外，还能把数值按指定格式和小数位转换输出，所调用的函数依旧是 `number()`，只不过参数形式变了：

```cpp
QByteArray number(double n, char f = 'g', int prec = 6);
```

其中，参数 `n` 是要进行转换的实数；`f` 表示转换格式，取值如下：

+ `e`：采用指数法表示实数，此时实数的格式如 [-]9.9e[+|-]999。
+ `E`：格式同 `e`，不过 `E` 要大写。
+ `f`：普通小数表示法，此时格式如 [-]9.9。
+ `g`：使用 `e` 或 `f` 格式，第三个参数表示有效数字位的个数。
+ `G`：使用 `E` 或 `f` 格式，第三个参数表示有效数字位的个数。

当参数 `f` 为 `e`、`E` 或 `f` 时，`prec` 表示十进制小数点后小数部分的位数；当 `f` 为 `g` 或 `G` 时，`prec` 表示有效数字位数的最大数目。注意，小数位要四舍五入。

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QByteArray ba1 = QByteArray::number(12345.6, 'E', 3);
    QByteArray ba2 = QByteArray::number(12345.6, 'c', 3);
    QByteArray ba3 = QByteArray::number(12345.6, 'f', 3);
    QByteArray ba4 = QByteArray::number(12345.6, 'g', 3);
    QByteArray ba5 = QByteArray::number(12345.6, 'G', 3);
    qDebug() << ba1;
    qDebug() << ba2;
    qDebug() << ba3;
    qDebug() << ba4;
    qDebug() << ba5;

    return a.exec();
}
```

运行结果如下：

```
"1.235E+04"
"12345.600"
"12345.600"
"1.23e+04"
"1.23E+04"
```

### 6. 字母大小写的转换

`QByteArray` 类对象若为带大小写字母的字符串，可调用函数 `toUpper()` 和 `toLower()` 实现字母大小写的转换。它们的原型声明如下：

```cpp
QByteArray toUpper();
QByteArray toLower();
```

例如：

```cpp
QByteArray x("Qt by THE QT COMPANY");
QByteArray y = x.toUpper();
// y == "QT BY THE QT COMPANY"
```

`QByteArray` 类还提供了判断是大写字母还是小写字母的成员函数 `isUpper` 和 `isLower`，它们的原型声明如下：

```cpp
bool isLower();
bool isUpper();
```

### 7. 字符串数值转为各类数值

`QByteArray` 类对象的字符若都为数值，则可通过 `to*` 函数转为各种类型的数据，例如：

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QByteArray strInt("1234");
    bool ok0;
    qDebug() << strInt.toInt(); // return 1234

    // return 4660，默认是把 strInt 的内容作为十六进制数的 1234，因而对应的十进制数值为 4660
    qDebug() << strInt.toInt(&ok0, 16);

    QByteArray string("1234.56");
    bool ok1;
    qDebug() << string.toInt(); // return 0, 小数均视为 0
    qDebug() << string.toInt(&ok1, 16); // return 0, 小数均视为 0
    qDebug() << string.toFloat();   // return 1234.56
    qDebug() << string.toDouble();  // return 1234.56

    QByteArray str("FF");
    bool ok2;
    qDebug() << str.toInt(&ok2, 16);    // return 255, ok2 == true
    qDebug() << str.toInt(&ok2, 10);    // return 0, ok == false,转为十进制失败

    return a.exec();
}
```

运行结果如下：

```
1234
4660
0
0
1234.56
1234.56
255
0
```

### 8. QByteArray 与 char* 互转

成员函数 `data` 可以返回指向字节数组中存储数据的指针。该函数的原型声明如下：

```cpp
char *data();
```

该指针可用于访问和修改组成数组的元素。

如果要把 `char*` 转为 `QString`，可以直接作为参数传入 `QByteArray` 类的构造函数中：

```cpp
QByteArray ba("Hello world");
QString str(ba);
```

例如：

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QByteArray ba("Hello world");
    char* data = ba.data(); // 返回一个指向字节数组 ba 的指针，指向第一个字符
    qDebug() << ba.data();  // 打印整个字符
    while (*data)
    {
        cout << "[" << *data << "], ";
        ++data;
    }

    return a.exec();
}
```

运行结果如下：

```
Hello world
[H], [e], [l], [l], [o], [ ], [w], [o], [r], [l], [d],
```

### 9. QByteArray 与 std::string 互转

`QByteArray` 类提供的成员函数 `toStdString()` 可以将字节数组转为 `string`，该函数的原型声明如下：

```cpp
std::string toStdString();
```

与该函数相反的函数是静态成员函数 `fromStdString()`，它将 `string` 数据转为字节数组，该函数的原型声明如下：

```cpp
static inline QByteArray fromStdString(const std::string &s);
```

### 10. 与字符 QString 互转

`QString` 转 `QByteArray` 的代码如下：

```cpp
QString str = QString("Hello world!");
QByteArray arr = str.toLatin1();
```

`QByteArray` 转 `QString` 的代码如下：

```cpp
QByteArray arr("Hello world!");
QString str = arr;
```

### 11.  QByteArray 与自定义结构体之间的转化

在 `Socket` 网络编程中，网络数据一般是 `uchar` 类型，在 `Qt` 中则可以使用 `QByteArray` 类。`QByteArray` 类在 `QSocket` 共享库中，根据 C++ 中 `char*` 数据与结构体之间的映射可以实现结构体与 `QByteArray` 的转化。下面来看一段代码：

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>
#include <stdlib.h>

typedef struct Feader {
    int channel;
    int type;
} Header;

typedef struct Msg {
    Header header;
    char content[128];
    friend QDebug operator << (QDebug os, Msg msg) {
        os << "(" << " channel: " << msg.header.channel << " type: " <<
              msg.header.type << " content: " << msg.content << " )";
        return os;
    }
} Msg;

typedef struct PeerMsg {
    PeerMsg(const int &ip, const int &por) {
        ipV4 = ip;
        port = por;
    }
    int ipV4;
    int port;
    friend QDebug operator << (QDebug os, PeerMsg msg) {
        os << "( " << " ipV4: " << QString::number(msg.ipV4)
           << " port: " << QString::number(msg.port) << " )";
        return os;
    }
} PeerMsg;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    Msg msg;
    msg.header.channel = 1001;
    msg.header.type = 1;
    strcpy(msg.content, "ABCDEFG");

    qDebug() << msg;
    QByteArray array;
    array.append((char*)&msg, sizeof(msg)); // 把结构体转为 QByteArray
    Msg *getMsg = (Msg*) array.data();
    qDebug() << *getMsg;

    QByteArray totalByte;
    PeerMsg peerMsg(123456, 10086);
    totalByte.append((char*)&peerMsg, sizeof(PeerMsg));
    totalByte.append(array, array.size());

    PeerMsg *getByte = (PeerMsg*)totalByte.data();  // 把 QByteArray 转为结构体
    qDebug() << *getByte;
    QByteArray contentmsg = totalByte.right(totalByte.size() - sizeof(*getByte));
    Msg *getMsg2 = (Msg*)contentmsg.data();
    qDebug() << *getMsg2;

    return a.exec();
}
```

运行结果如下：

```
(  channel:  1001  type:  1  content:  ABCDEFG  )
(  channel:  1001  type:  1  content:  ABCDEFG  )
(   ipV4:  "123456"  port:  "10086"  )
(  channel:  1001  type:  1  content:  ABCDEFG  )
```

### 12. 判断是否为空

可以使用函数 `isEmpty()` 来判断字节数组是否为空，原型声明如下：

```cpp
bool isEmpty();
```

如果字节数组的 `size` 为 0，则返回 `true`，否则返回 `false`。例如：

```cpp
QByteArray().isEmpty();	// return true
QByteArray("").isEmpty();	// return true
QByteArray("abc").isEmpty();	// return false
```

### 13. 向前搜索和向后搜索

函数 `indexOf()` 返回该字节数组中第一次出现字节数组的索引位置，从索引位置向前搜索。如果找到，则返回第一次出现的索引位置，如果没有找到，则返回 -1。例如：

```cpp
QByteArray x("sticky question");
QByteArray y("sti");
x.indexOf(y);	// returns 0
x.indexOf(y, 1);	// returns 10
x.indexof(y, 10);	// returns 10
x.indexOf(y, 11);	// returns -1
```

`indexOf()` 还可以搜索 `char*` 和 `QString` 类型的数据，例如：

```cpp
QByteArray ba("ABCBA");
ba.indexOf("B");	// returns 1
ba.indexOf("B", 1);	// returns 1
ba.indexOf("B", 2);	// returns 3
ba.indexOf("X");	// return -1
```

`lastIndexOf()` 函数是向后搜索。

### 14. 插入

函数 `insert()` 可以在某个索引位置上插入字节数组，例如：

```cpp
QByteArray ba("Meal");
ba.insert(1, QByteArray("ontr"));
// ba == "Montreal"
```

此外，也可以在某个位置插入一个或多个字符，有两个函数，这两个函数的原型声明如下：

```cpp
QByteArray & QByteArray::insert(int i, char ch);
QByteArray & insert(int i, int count, char ch);
```

另外，还有一种重载形式，就是插入 `char*` 类型的数据，有两种函数的原型声明形式：

```cpp
QByteArray & insert(int i, const char *str);
QByteArray & QByteArray::insert(int i, const char *str, int len);
```

第一种形式不带长度，插入全部 `str`；第二种形式带长度 `len`，`len` 表示 `str` 中的 `len` 个字节。

此外，Qt 还提供了 `prepend()` 函数，该函数在原字符串开头插入另一个字符串。