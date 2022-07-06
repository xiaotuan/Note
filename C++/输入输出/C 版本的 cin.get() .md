C 语言中的字符 I/O 函数 —— `getchar()` 和 `putchar()`，它们仍然使用，只要像在 C 语言中那样包含头文件 `stdio.h` （或新的 `cstdio`）即可。也可以使用 `istream` 和 `ostream` 类中类似功能的成员函数。

不接受任何参数的 `cin.get()` 成员函数返回输入中的下一个字符。也就是说，可以这样使用它：

```cpp
ch = cin.get();
```

该函数的工作方式与 `C` 语言中的 `getchar()` 相似，将字符编码作为 `int` 值返回；而 `cin.get(ch)` 返回一个对象，而不是读取的字符。同样，可以使用 `cout.put()` 函数来显示字符：

```cpp
cout.put(ch);
```

该函数的工作方式类似 `C` 语言中的 `putchar()`，只不过其参数类型为 `char`，而不是  `int`。

> 注意：最初，`put()` 成员只有一个原型 —— `put(char)`。可以传递一个 `int` 参数给它，该参数将被强制转换为 `char`。C++ 标准还要求只有一个原型。然而，有些 C++ 实现都提供了 3 个原型：`put(char)`、`put(signed char)` 和 `put(unsigned char)`。在这些实现中，给 `put()` 传递一个 `int` 参数将导致错误消息，因为转换 `int` 的方式不止一种。使用显示强制类型转换的原型（如 `cin.put(char(ch))`）可使用 `int` 参数。

例如：

```cpp
int ch;	// for compatibility with EOF value
ch = cin.get();
while (ch != EOF)
{
    cout.put(ch);	// cout.put(char(ch)) for some implementations
    ++count;
    ch = cin.get();
}
```

关于使用 `cin.get()`还有一个微妙而重要的问题。由于 EOF 表示的不是有效字符编码，因此可能不与 `char` 类型兼容。例如，在有些系统中，`char` 类型是没有符号的，因此 `char` 变量不可能为 EOF 值（-1）。由于这种原因，如果使用 `cin.get()`（没有参数）并测试 EOF，则必须将返回值赋给 int 变量，而不是 `char` 变量。另外，如果将 `ch` 的类型声明为 `int`，而不是 `char`，则必须在显示 `ch` 时将其强制转换为 `char` 类型。

例如：

```cpp
// textin4.cpp -- reading chars with cin.get()
#include <iostream>

int main(void)
{
	using namespace std;
	int ch;	// should be int, not char
	int count = 0;

	while ((ch = cin.get()) != EOF)	// test for end-of-file
	{
		cout.put(char(ch));
		++count;
	}
	cout << endl << count << " characters read\n";
	return 0;
}
```

