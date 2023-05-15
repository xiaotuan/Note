`if` 语句的语法如下：

```cpp
if (test-condition)
    statement
```

如果 `test-condition`（测试条件）为 `true`，则程序将执行 statement（语句），后者既可以是一条语句，也可以是语句块。如果测试条件为 false，则程序将跳过语句。和循环测试条件一样，`if` 测试条件也将被强制转换为 `bool` 值，因此 0 将被转换为 `false`，非零为 `true`。

**示例代码：if.cpp**

```cpp
// if.cpp -- using the if statement
#include <iostream>

int main()
{
	using std::cin;	// using declarations
	using std::cout;
	char ch;
	int spaces = 0;
	int total = 0;
	cin.get(ch);
	while (ch != '.')	// quit at end of sentence
	{
		if (ch == ' ')	// check if ch is a space
			++spaces;
		++total;	// done every time
		cin.get(ch);
	}
	cout << spaces << " spaces, " << total;
	cout << " characters total in sentence\n";
	return 0;
}
```

运行结果如下：

```shell
$ g++ if.cpp 
$ ./a.out 
Updated 1 path from the index.
5 spaces, 29 characters total in sentence
```

