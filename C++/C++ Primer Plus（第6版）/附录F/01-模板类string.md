### 附录F　模板类string

本附录的技术性较强，但如果您只想了解模板类string的功能，可以将重点放在对各种string类方法的描述上。

string类是基于下述模板定义的：

```css
template<class charT, class traits = char_traits<charT>,
                 class Allocator = allocator<charT> >
class basic_string {...};
```

其中，chatT是存储在字符串中的类型；traits参数是一个类，它定义了类型要被表示为字符串时，所必须具备的特征。例如，它必须有length()方法，该方法返回被表示为charT数组的字符串的长度。这种数组结尾用charT(0)值（广义的空值字符）表示。（表达式charT(0)将0转换为charT类型。它可以像类型为char时那样为零，也可以是charT的一个构造函数创建的对象）。这个类还包含用于对值进行比较等操作的方法。Allocator参数是用于处理字符串内存分配的类。默认的allocator<char>模板按标准方式使用new和delete。

有4种预定义的具体化：

```css
typedef basic_string<char> string;
typedef basic_string<char16_t> u16string;
typedef basic_string<char32_t> u32string;
typedef basic_string<wchar_t> wstring;
```

上述具体化又使用下面的具体化：

```css
char_traits<char>
allocator<char>
char_traits<char16_t>
allocator<char_16>
char_traits<char_32>
allocator<char_32>
char_traits<wchar_t>
allocator<wchar_t>
```

除char和wchar_t外，还可以通过定义traits类和使用basic_string模板来为其他一些类型创建一个string类。

