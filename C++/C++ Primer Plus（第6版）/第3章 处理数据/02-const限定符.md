C++ 有一种更好的处理符号常量的方法，这种方法旧式使用 const 关键子来修改变量声明和初始化。例如，假设需要一个表示一年中月份数的符号常量，请在程序中输入下面这行代码：

```cpp
const int Months = 12;	// Months is symbolic constant for 12
```

一种常见的做法是将名称的首写字母大写，以提醒您 Months 是个常量。创建常量的通用格式如下：

```cpp
const type name = value;
```

注意，应在声明中对 const 进行初始化。下面的代码不好：

```cpp
const int toes;	// value of toes undefined at this point
toes = 10;	// to late!
```

如果在声明常量时没有提供值，则该常量的值将是不确定的，且无法修改。

const 与 #define的对比，首先，它能够明确指定类型。其次，可以使用 C++ 的作用域规则将定义限定在特定的函数或文件中。第三，可以将 const 用于更复杂的类型。

ANSI C 也使用 const 限定符，这是从 C++ 借鉴来的。C++ 版本稍微有些不同。区别之一是作用域规则；另一个主要的区别是，在 C++ （而不是 C）中可以用 const 值来声明数组长度。