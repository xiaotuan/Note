### 10.3.5　改进Stock类

下面将构造函数和析构函数加入到类和方法的定义中。鉴于添加构造函数的重大意义，这里将名称从stock00.h改为stock10.h。类方法放在文件stock10.cpp中。最后，将使用这些资源的程序放在第三个文件中，这个文件名为usestock2.cpp。

#### 1．头文件

程序清单10.4列出了头文件。它将构造函数和析构函数的原型加入到原来的类声明中。另外，它还删除了acquire()函数——现在已经不再需要它了，因为有构造函数。该文件还使用第9章介绍的#ifndef技术来防止多重包含。

程序清单10.4　stock10.h

```css
// stock10.h -- Stock class declaration with constructors, destructor added
#ifndef STOCK10_H_
#define STOCK01_H_
#include <string>
class Stock
{
private:
    std::string company;
    long shares;
    double share_val;
    double total_val;
    void set_tot() { total_val = shares * share_val; }
public:
// two constructors
    Stock(); // default constructor
    Stock(const std::string & co, long n = 0, double pr = 0.0);
    ~Stock(); // noisy destructor
    void buy(long num, double price);
    void sell(long num, double price);
    void update(double price);
    void show();
};
#endif
```

#### 2．实现文件

程序清单10.5提供了方法的定义。它包含了文件stock10.h，以提供类声明（将文件名放在双引号而不是方括号中意味着编译器将源文件所在的目录中搜索它）。另外，程序清单10.5还包含了头文件iostream，以提供I/O支持。该程序清单还使用using声明和限定名称（如std::string）来访问头文件中的各种声明。该文件将构造函数和析构函数的方法定义添加到以前的方法定义中。为让您知道这些方法何时被调用，它们都显示一条消息。这并不是构造函数和析构函数的常规功能，但有助于您更好地了解类是如何使用它们的。

程序清单10.5　stock10.cpp

```css
// stock10.cpp -- Stock class with constructors, destructor added
#include <iostream>
#include "stock10.h"
// constructors (verbose versions)
Stock::Stock() // default constructor
{
    std::cout << "Default constructor called\n";
    company = "no name";
    shares = 0;
    share_val = 0.0;
    total_val = 0.0;
}
Stock::Stock(const std::string & co, long n, double pr)
{
    std::cout << "Constructor using " << co << " called\n";
    company = co;
    if (n < 0)
    {
        std::cout << "Number of shares can’t be negative; "
                    << company << " shares set to 0.\n";
        shares = 0;
    }
    else
        shares = n;
    share_val = pr;
    set_tot();
}
// class destructor
Stock::~Stock() // verbose class destructor
{
    std::cout << "Bye, " << company << "!\n";
}
// other methods
void Stock::buy(long num, double price)
{
     if (num < 0)
    {
        std::cout << "Number of shares purchased can’t be negative. "
            << "Transaction is aborted.\n";
    }
    else
    {
        shares += num;
        share_val = price;
        set_tot();
    }
}
void Stock::sell(long num, double price)
{
    using std::cout;
    if (num < 0)
    {
        cout << "Number of shares sold can’t be negative. "
             << "Transaction is aborted.\n";
    }
    else if (num > shares)
    {
        cout << "You can’t sell more than you have! "
             << "Transaction is aborted.\n";
    }
    else
    {
        shares -= num;
        share_val = price;
        set_tot();
    }
}
void Stock::update(double price)
{
    share_val = price;
    set_tot();
}
void Stock::show()
{
    using std::cout;
    using std::ios_base;
    // set format to #.###
    ios_base::fmtflags orig =
        cout.setf(ios_base::fixed, ios_base::floatfield);
    std::streamsize prec = cout.precision(3);
    cout << "Company: " << company
         << " Shares: " << shares << ‘\n’;
    cout << " Share Price: $" << share_val;
    // set format to #.##
    cout.precision(2);
    cout << " Total Worth: $" << total_val << ‘\n’;
    // restore original format
    cout.setf(orig, ios_base::floatfield);
    cout.precision(prec);
}
```

#### 3．客户文件

程序清单10.6提供了一个测试这些新方法的小程序；由于它只是使用Stock类，因此是Stock类的客户。和stock10.cpp一样，它也包含了文件stock10.h以提供类声明。该程序显示了构造函数和析构函数，它还使用了程序清单10.3调用的格式化命令。要编译整个程序，必须使用第1章和第9章介绍的多文件程序技术。

程序清单10.6　usestock1.cpp

```css
// usestok1.cpp -- using the Stock class
// compile with stock10.cpp
#include <iostream>
#include "stock10.h"
int main()
{
  {
    using std::cout;
    cout << "Using constructors to create new objects\n";
    Stock stock1("NanoSmart", 12, 20.0);              // syntax 1
    stock1.show();
    Stock stock2 = Stock ("Boffo Objects", 2, 2.0); // syntax 2
    stock2.show();
    cout << "Assigning stock1 to stock2:\n";
    stock2 = stock1;
    cout << "Listing stock1 and stock2:\n";
    stock1.show();
    stock2.show();
    cout << "Using a constructor to reset an object\n";
    stock1 = Stock("Nifty Foods", 10, 50.0); // temp object
    cout << "Revised stock1:\n";
    stock1.show();
    cout << "Done\n";
  }
    return 0;
}
```

编译程序清单10.4、程序清单10.5和程序清单10.6所示的程序，得到一个可执行程序。下面是使用某个编译器得到的可执行程序的输出：

```css
Using constructors to create new objects
Constructor using NanoSmart called
Company: NanoSmart Shares: 12
  Share Price: $20.00 Total Worth: $240.00
Constructor using Boffo Objects called
Company: Boffo Objects Shares: 2
  Share Price: $2.00 Total Worth: $4.00
Assigning stock1 to stock2:
Listing stock1 and stock2:
Company: NanoSmart Shares: 12
  Share Price: $20.00 Total Worth: $240.00
Company: NanoSmart Shares: 12
  Share Price: $20.00 Total Worth: $240.00
Using a constructor to reset an object
Constructor using Nifty Foods called
Bye, Nifty Foods!
Revised stock1:
Company: Nifty Foods Shares: 10
  Share Price: $50.00 Total Worth: $500.00
Done
Bye, NanoSmart!
Bye, Nifty Foods!
```

使用某些编译器编译该程序时，该程序输出的前半部分可能如下（比前面多了一行）：

```css
Using constructors to create new objects
Constructor using NanoSmart called
Company: NanoSmart Shares: 12
  Share Price: $20.00 Total Worth: $240.00
Constructor using Boffo Objects called
Bye, Boffo Objects! << additional line
Company: Boffo Objects Shares: 2
  Share Price: $2.00 Total Worth: $4.00
...
```

下一小节将解释输出行“Bye, Boffo Objects!”。

> **提示：**
> 您可能注意到了，在程序清单10.6中，main()的开头和末尾多了一个大括号。诸如stock1和stock2等自动变量将在程序退出其定义所属代码块时消失。如果没有这些大括号，代码块将为整个main()，因此仅当main()执行完毕后，才会调用析构函数。在窗口环境中，这意味着将在两个析构函数调用前关闭，导致您无法看到最后两条消息。但添加这些大括号后，最后两个析构函数调用将在到达返回语句前执行，从而显示相应的消息。

#### 4．程序说明

程序清单10.6中的下述语句：

```css
Stock stock1("NanoSmart", 12, 20.0);
```

创建一个名为stock1的Stock对象，并将其数据成员初始化为指定的值：

```css
Constructor using NanoSmart called
Company: NanoSmart Shares: 12
```

下面的语句使用另一种语法创建并初始化一个名为stock2的对象：

```css
stock2:
Stock stock2 = Stock ("Boffo Objects", 2, 2.0);
```

C++标准允许编译器使用两种方式来执行第二种语法。一种是使其行为和第一种语法完全相同：

```css
Constructor using Boffo Objects called
Company: Boffo Objects Shares: 2
```

另一种方式是允许调用构造函数来创建一个临时对象，然后将该临时对象复制到stock2中，并丢弃它。如果编译器使用的是这种方式，则将为临时对象调用析构函数，因此生成下面的输出：

```css
Constructor using Boffo Objects called
Bye, Boffo Objects!
Company: Boffo Objects Shares: 2
```

生成上述输出的编译器可能立刻删除临时对象，但也可能会等一段时间，在这种情况下，析构函数的消息将会过一段时间才显示。

下面的语句表明可以将一个对象赋给同类型的另一个对象：

```css
stock2 = stock1; // object assignment
```

与给结构赋值一样，在默认情况下，给类对象赋值时，将把一个对象的成员复制给另一个。在这个例子中，stock2原来的内容将被覆盖。

> **注意：**
> 在默认情况下，将一个对象赋给同类型的另一个对象时，C++将源对象的每个数据成员的内容复制到目标对象中相应的数据成员中。

构造函数不仅仅可用于初始化新对象。例如，该程序的main()中包含下面的语句：

```css
stock1 = Stock("Nifty Foods", 10, 50.0);
```

stock1对象已经存在，因此这条语句不是对stock1进行初始化，而是将新值赋给它。这是通过让构造程序创建一个新的、临时的对象，然后将其内容复制给stock1来实现的。随后程序调用析构函数，以删除该临时对象，如下面经过注释后的输出所示：

```css
Using a constructor to reset an object
Constructor using Nifty Foods called     >> temporary object created
Bye, Nifty Foods!                            >> temporary object destroyed
Revised stock1:
Company: Nifty Foods Shares: 10           >> data now copied to stock1
  Share Price: $50.00 Total Worth: $500.00
```

有些编译器可能要过一段时间才删除临时对象，因此析构函数的调用将延迟。

最后，程序显示了下面的内容：

```css
Done
Bye, NanoSmart!
Bye, Nifty Foods!
```

函数main()结束时，其局部变量（stock1和stock2）将消失。由于这种自动变量被放在栈中，因此最后创建的对象将最先被删除，最先创建的对象将最后被删除（“NanoSmart”最初位于stock1中，但随后被传输到stock2中，然后stock1被重置为“Nifty Food”）。

输出表明，下面两条语句有根本性的差别：

```css
Stock stock2 = Stock ("Boffo Objects", 2, 2.0);
stock1 = Stock("Nifty Foods", 10, 50.0); // temporary object
```

第一条语句是初始化，它创建有指定值的对象，可能会创建临时对象（也可能不会）；第二条语句是赋值。像这样在赋值语句中使用构造函数总会导致在赋值前创建一个临时对象。

> **提示：**
> 如果既可以通过初始化，也可以通过赋值来设置对象的值，则应采用初始化方式。通常这种方式的效率更高。

#### 5．C++11列表初始化

在C++11中，可将列表初始化语法用于类吗？可以，只要提供与某个构造函数的参数列表匹配的内容，并用大括号将它们括起：

```css
Stock hot_tip = {"Derivatives Plus Plus", 100, 45.0};
Stock jock {"Sport Age Storage, Inc"};
Stock temp {};
```

在前两个声明中，用大括号括起的列表与下面的构造函数匹配：

```css
Stock::Stock(const std::string & co, long n = 0, double pr = 0.0);
```

因此，将使用该构造函数来创建这两个对象。创建对象jock时，第二个和第三个参数将为默认值0和0.0。第三个声明与默认构造函数匹配，因此将使用该构造函数创建对象temp。

另外，C++11还提供了名为std::initialize_list的类，可将其用作函数参数或方法参数的类型。这个类可表示任意长度的列表，只要所有列表项的类型都相同或可转换为相同的类型，这将在第16章介绍。

#### 6．const成员函数

请看下面的代码片段：

```css
const Stock land = Stock("Kludgehorn Properties");
land.show();
```

对于当前的C++来说，编译器将拒绝第二行。这是什么原因呢？因为show()的代码无法确保调用对象不被修改——调用对象和const一样，不应被修改。我们以前通过将函数参数声明为const引用或指向const的指针来解决这种问题。但这里存在语法问题：show()方法没有任何参数。相反，它所使用的对象是由方法调用隐式地提供的。需要一种新的语法——保证函数不会修改调用对象。C++的解决方法是将const关键字放在函数的括号后面。也就是说，show()声明应像这样：

```css
void show() const; // promises not to change invoking object
```

同样，函数定义的开头应像这样：

```css
void stock::show() const // promises not to change invoking object
```

以这种方式声明和定义的类函数被称为const成员函数。就像应尽可能将const引用和指针用作函数形参一样，只要类方法不修改调用对象，就应将其声明为const。从现在开始，我们将遵守这一规则。

