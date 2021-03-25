### 12.4.2　返回指向非const对象的引用

两种常见的返回非const对象情形是，重载赋值运算符以及重载与cout一起使用的<<运算符。前者这样做旨在提高效率，而后者必须这样做。

operator=()的返回值用于连续赋值：

```css
String s1("Good stuff");
String s2, s3;
s3 = s2 = s1;
```

在上述代码中，s2.operator=()的返回值被赋给s3。为此，返回String对象或String对象的引用都是可行的，但与Vector示例中一样，通过使用引用，可避免该函数调用String的复制构造函数来创建一个新的String对象。在这个例子中，返回类型不是const，因为方法operator=()返回一个指向s2的引用，可以对其进行修改。

Operator<<()的返回值用于串接输出：

```css
String s1("Good stuff");
cout << s1 << "is coming!";
```

在上述代码中，operator<<（cout, s1）的返回值成为一个用于显示字符串“is coming!”的对象。返回类型必须是ostream &，而不能仅仅是ostream。如果使用返回类型ostream，将要求调用ostream类的复制构造函数，而ostream没有公有的复制构造函数。幸运的是，返回一个指向cout的引用不会带来任何问题，因为cout已经在调用函数的作用域内。

