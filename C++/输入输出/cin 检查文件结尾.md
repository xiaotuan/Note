如果输入来自于文件，则可以使用一种功能强大技术——检测文件尾（EOF)。

很多操作系统都允许通过键盘来模拟文件尾条件。在 `Unix` 中，可以在行首按下 <kbd>Ctrl</kbd> + <kbd>D</kbd> 来实现；在 `Windows` 命令提示符模式下，可以在任意位置按 <kbd>Ctrl</kbd> + <kbd>Z</kbd> 和 <kbd>Enter</kbd>。

检测到 EOF 后，`cin` 将两位（ `eofbit` 和 `failbit` ）都设置为 1。可以通过成员函数 `eof()` 来查看 `eofbit` 是否被设置；如果检测到 EOF，则 `cin.eof()` 将返回 `bool` 值 `true`，否则返回 `false`。同样，如果 `eofbit` 或 `failbit` 被设置为 1，则 `fail()` 成员函数返回 `true`，否则返回 `false`。注意，`eof()` 和 `fail()` 方法报告最近读取的结果；也就是说，它们在事后报告，而不是预先报告。因此应将 `cin.eof()` 或 `cin.fail()` 测试放在读取后。

> 警告：当 `cin` 方法检测到 `EOF` 时，将设置 `cin` 对象中一个指示 `EOF` 条件标记。设置这个标记后，`cin` 将不读取输入，再次调用 `cin` 也不管用。`cin.clear()` 方法可能清除 EOF 标记，使输入继续进行。在有些系统中，按 <kbd>Ctrl</kbd>+<kbd>Z</kbd> 实际上将结束输入和输出，而 `cin.clear()` 将无法恢复输入和输出。

例如：

```cpp
// textin3.cpp -- reading chars to end of file
#include <iostream>

int main()
{
	using namespace std;
	char ch;
	int count = 0;
	cin.get(ch);	// attempt to read a char
	while (cin.fail() == false)	// test for EOF
	{
		cout << ch;	// echo character
		++count;
		cin.get(ch);	// attempt to read another char
	}
	cout << endl << count << " characters read\n";
	return 0;
}
```

然而， `istream` 类提供了一个可以将 `istream` 对象转换成 `bool` 值的函数；当 `cin` 出现在需要 `bool` 值的地方时，该转换函数将被调用。这意味着可以将上述 `while` 测试改写为这样：

```cpp
while (cin)	// while input is successful
```

最后，由于 `cin.get(char)` 的返回值为 `cin`，因此可以将循环精简成这种格式：

```cpp
while (cin.get(ch))	// while input is successful
{
    ... // do stuff
}
```

