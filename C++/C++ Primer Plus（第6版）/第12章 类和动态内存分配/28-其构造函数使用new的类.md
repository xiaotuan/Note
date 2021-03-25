### 12.6.3　其构造函数使用new的类

如果类使用new运算符来分配类成员指向的内存，在设计时应采取一些预防措施（前面总结了这些预防措施，应牢记这些规则，这是因为编译器并不知道这些规则，因此无法发现错误）。

+ 对于指向的内存是由new分配的所有类成员，都应在类的析构函数中对其使用delete，该运算符将释放分配的内存。
+ 如果析构函数通过对指针类成员使用delete来释放内存，则每个构造函数都应当使用new来初始化指针，或将它设置为空指针。
+ 构造函数中要么使用new []，要么使用new，而不能混用。如果构造函数使用的是new[]，则析构函数应使用delete []；如果构造函数使用的是new，则析构函数应使用delete。
+ 应定义一个分配内存（而不是将指针指向已有内存）的复制构造函数。这样程序将能够将类对象初始化为另一个类对象。这种构造函数的原型通常如下：

```css
className(const className &)
```

+ 应定义一个重载赋值运算符的类成员函数，其函数定义如下（其中c_pointer是c_name的类成员，类型为指向type_name的指针）。下面的示例假设使用new []来初始化变量c_pointer：

```css
c_name & c_name::operator=(const c_name & cn)
{
    if (this == & cn)
        return *this; // done if self-assignment
    delete [] c_pointer;
    // set size number of type_name units to be copied
    c_pointer = new type_name[size];
    // then copy data pointed to by cn.c_pointer to
    // location pointed to by c_pointer
    ...
    return *this;
}
```

