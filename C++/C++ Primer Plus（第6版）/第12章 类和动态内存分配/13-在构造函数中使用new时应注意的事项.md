### 12.3　在构造函数中使用new时应注意的事项

至此，您知道使用new初始化对象的指针成员时必须特别小心。具体地说，应当这样做。

+ 如果在构造函数中使用new来初始化指针成员，则应在析构函数中使用delete。
+ new和delete必须相互兼容。new对应于delete，new[ ]对应于delete[ ]。
+ 如果有多个构造函数，则必须以相同的方式使用new，要么都带中括号，要么都不带。因为只有一个析构函数，所有的构造函数都必须与它兼容。然而，可以在一个构造函数中使用new初始化指针，而在另一个构造函数中将指针初始化为空（0或C++11中的nullptr），这是因为delete（无论是带中括号还是不带中括号）可以用于空指针。

NULL、0还是nullptr：以前，空指针可以用0或NULL（在很多头文件中，NULL是一个被定义为0的符号常量）来表示。C程序员通常使用NULL而不是0，以指出这是一个指针，就像使用‘\0’而不是0来表示空字符，以指出这是一个字符一样。然而，C++传统上更喜欢用简单的0，而不是等价的NULL。但正如前面指出的，C++11提供了关键字nullptr，这是一种更好的选择。

+ 应定义一个复制构造函数，通过深度复制将一个对象初始化为另一个对象。通常，这种构造函数与下面类似。

```css
String::String(const String & st)
{
    num_strings++;            // handle static member update if necessary
    len = st.len;             // same length as copied string
    str = new char [len + 1]; // allot space
    std::strcpy(str, st.str); // copy string to new location
}
```

具体地说，复制构造函数应分配足够的空间来存储复制的数据，并复制数据，而不仅仅是数据的地址。另外，还应该更新所有受影响的静态类成员。

+ 应当定义一个赋值运算符，通过深度复制将一个对象复制给另一个对象。通常，该类方法与下面类似：

```css
String & String::operator=(const String & st)
{
    if (this == &st)  // object assigned to itself
        return *this; // all done
    delete [] str;    // free old string
    len = st.len;
    str = new char [len + 1]; // get space for new string
    std::strcpy(str, st.str); // copy the string
    return *this;             // return reference to invoking object
}
```

具体地说，该方法应完成这些操作：检查自我赋值的情况，释放成员指针以前指向的内存，复制数据而不仅仅是数据的地址，并返回一个指向调用对象的引用。

