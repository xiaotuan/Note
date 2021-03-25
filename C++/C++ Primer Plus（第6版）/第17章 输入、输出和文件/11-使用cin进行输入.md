### 17.3　使用cin进行输入

现在来介绍输入，即如何给程序提供数据。cin对象将标准输入表示为字节流。通常情况下，通过键盘来生成这种字符流。如果键入字符序列2011，cin对象将从输入流中抽取这几个字符。输入可以是字符串的一部分、int值、float值，也可以是其他类型。因此，抽取还涉及了类型转换。cin对象根据接收值的变量的类型，使用其方法将字符序列转换为所需的类型。

通常，可以这样使用cin：

```css
cin >> value_holder;
```

其中，value_holder为存储输入的内存单元，它可以是变量、引用、被解除引用的指针，也可以是类或结构的成员。cin解释输入的方式取决于value_holder的数据类型。istream类（在iostream头文件中定义）重载了抽取运算符>>，使之能够识别下面这些基本类型：

+ signed char &；
+ unsigned char &；
+ char &；
+ short &；
+ unsigned short &；
+ int &；
+ unsigned int &；
+ long &；
+ unsigned long &；
+ long long &（C++11）；
+ unsigned long long &（C++11）；
+ float &；
+ double &；
+ long double &。

这些运算符函数被称为格式化输入函数（formatted input functions），因为它们可以将输入数据转换为目标指定的格式。

典型的运算符函数的原型如下：

```css
istream & operator>>(int &);
```

参数和返回值都是引用。引用参数（参见第8章）意味着下面这样的语句将导致operator>>()函数处理变量staff_size本身，而不是像常规参数那样处理它的副本：

```css
cin >> staff_size;
```

由于参数类型为引用，因此cin能够直接修改用作参数的变量的值。例如，上述语句将直接修改变量staff_size的值。稍后将介绍引用返回值的重要意义。首先来看抽取运算符的类型转换方面。对于上述列出的各种类型的参数，抽取运算符将字符输入转换为指定类型的值。例如，假设staff_size的类型为int，则编译器将：

```css
cin >> staff_size;
```

与下面的原型匹配：

```css
istream & operator>>(int &);
```

对应于上述原型的函数将读取发送给程序的字符流（假设为字符2、3、1、8和4）。对于使用2字节int的系统来说，函数将把这些字符转换为整数23184的2字节二进制表示。如果staff_size的类型为double，则cin将使用operator >> (double &)将上述输入转换为值23184.0的8字节浮点表示。

顺便说一句，可以将hex、oct和dec控制符与cin一起使用，来指定将整数输入解释为十六进制、八进制还是十进制格式。例如，下面的语句将输入12或0x12解释为十六进制的12或十进制的18，而将ff或FF解释为十进制的255：

```css
cin >> hex;
```

istream类还为下列字符指针类型重载了>>抽取运算符：

+ signed char *；
+ char *；
+ unsigned char *。

对于这种类型的参数，抽取运算符将读取输入中的下一个单词，将它放置到指定的地址，并加上一个空值字符，使之成为一个字符串。例如，假设有这样一段代码：

```css
cout << "Enter your first name:\n";
char name[20];
cin >> name;
```

如果通过键入Liz来进行响应，则抽取运算符将把字符Liz\0放到name数组中（\0表示末尾的空值字符）。name标识符是一个char数组名，可作为数组第一个元素的地址，这使name的类型为char *（指向char的指针）。

每个抽取运算符都返回调用对象的引用，这使得能够将输入拼接起来，就像拼接输出那样：

```css
char name[20];
float fee;
int group;
cin >> name >> fee >> group;
```

其中，cin>>name返回的cin对象成了处理fee的对象。

