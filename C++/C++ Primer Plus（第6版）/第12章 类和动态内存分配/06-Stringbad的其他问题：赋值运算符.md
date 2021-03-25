### 12.1.4　Stringbad的其他问题：赋值运算符

并不是程序清单12.3的所有问题都可以归咎于默认的复制构造函数，还需要看一看默认的赋值运算符。ANSI C允许结构赋值，而C++允许类对象赋值，这是通过自动为类重载赋值运算符实现的。这种运算符的原型如下：

```css
Class_name & Class_name::operator=(const Class_name &);
```

它接受并返回一个指向类对象的引用。例如，StringBad类的赋值运算符的原型如下：

```css
StringBad & StringBad::operator=(const StringBad &);
```

#### 1．赋值运算符的功能以及何时使用它

将已有的对象赋给另一个对象时，将使用重载的赋值运算符：

```css
StringBad headline1("Celery Stalks at Midnight");
...
StringBad knot;
knot = headline1; // assignment operator invoked
```

初始化对象时，并不一定会使用赋值运算符：

```css
StringBad metoo = knot; // use copy constructor, possibly assignment, too
```

这里，metoo是一个新创建的对象，被初始化为knot的值，因此使用复制构造函数。然而，正如前面指出的，实现时也可能分两步来处理这条语句：使用复制构造函数创建一个临时对象，然后通过赋值将临时对象的值复制到新对象中。这就是说，初始化总是会调用复制构造函数，而使用=运算符时也允许调用赋值运算符。

与复制构造函数相似，赋值运算符的隐式实现也对成员进行逐个复制。如果成员本身就是类对象，则程序将使用为这个类定义的赋值运算符来复制该成员，但静态数据成员不受影响。

#### 2．赋值的问题出在哪里

程序清单12.3将headline1赋给knot：

```css
knot = headline1;
```

为knot调用析构函数时，将显示下面的消息：

```css
"Celery Stalks at Midnight" object deleted, 2 left
```

为Headline1调用析构函数时，显示如下消息（有些实现方式在此之前就异常终止了）：

```css
"-|" object deleted, -2 left
```

出现的问题与隐式复制构造函数相同：数据受损。这也是成员复制的问题，即导致headline1.str和knot.str指向相同的地址。因此，当对knot调用析构函数时，将删除字符串“Celery Stalks at Midnight”；当对headline1调用析构函数时，将试图删除前面已经删除的字符串。正如前面指出的，试图删除已经删除的数据导致的结果是不确定的，因此可能改变内存中的内容，导致程序异常终止。要指出的是，如果操作结果是不确定的，则执行的操作将随编译器而异，包括显示独立声明（Declaration of Independence）或释放隐藏文件占用的硬盘空间。当然，编译器开发人员通常不会花时间添加这样的行为。

#### 3．解决赋值的问题

对于由于默认赋值运算符不合适而导致的问题，解决办法是提供赋值运算符（进行深度复制）定义。其实现与复制构造函数相似，但也有一些差别。

+ 由于目标对象可能引用了以前分配的数据，所以函数应使用delete[ ]来释放这些数据。
+ 函数应当避免将对象赋给自身；否则，给对象重新赋值前，释放内存操作可能删除对象的内容。
+ 函数返回一个指向调用对象的引用。

通过返回一个对象，函数可以像常规赋值操作那样，连续进行赋值，即如果S0、S1和S2都是StringBad对象，则可以编写这样的代码：

```css
S0 = S1 = S2;
```

使用函数表示法时，上述代码为：

```css
S0.operator=(S1.operator=(S2));
```

因此，S1.operator=（S2）的返回值是函数S0.operator=()的参数。

因为返回值是一个指向StringBad对象的引用，因此参数类型是正确的。

下面的代码说明了如何为StringBad类编写赋值运算符：

```css
StringBad & StringBad::operator=(const StringBad & st)
{
    if (this == &st)          // object assigned to itself
        return *this;         // all done
    delete [] str;            // free old string
    len = st.len;
    str = new char [len + 1]; // get space for new string
    std::strcpy(str, st.str); // copy the string
    return *this;             // return reference to invoking object
}
```

代码首先检查自我复制，这是通过查看赋值运算符右边的地址（&s）是否与接收对象（this）的地址相同来完成的。如果相同，程序将返回*this，然后结束。第10章介绍过，赋值运算符是只能由类成员函数重载的运算符之一。

如果地址不同，函数将释放str指向的内存，这是因为稍后将把一个新字符串的地址赋给str。如果不首先使用delete运算符，则上述字符串将保留在内存中。由于程序中不再包含指向该字符串的指针，因此这些内存被浪费掉。

接下来的操作与复制构造函数相似，即为新字符串分配足够的内存空间，然后将赋值运算符右边的对象中的字符串复制到新的内存单元中。

上述操作完成后，程序返回*this并结束。

赋值操作并不创建新的对象，因此不需要调整静态数据成员num_strings的值。

将前面介绍的复制构造函数和赋值运算符添加到StringBad类中后，所有的问题都解决了。例如，下面是在完成上述修改后，程序输出的最后几行：

```css
End of main()
"Celery Stalks at Midnight" object deleted, 4 left
"Spinach Leaves Bowl for Dollars" object deleted, 3 left
"Spinach Leaves Bowl for Dollars" object deleted, 2 left
"Lettuce Prey" object deleted, 1 left
"Celery Stalks at Midnight" object deleted, 0 left
```

现在，对象计数是正确的，字符串也没有被损坏。

