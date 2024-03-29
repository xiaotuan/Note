`for` 循环为执行重复的操作提供了循环渐进的步骤。`for` 循环的组成部分完成下面这些步骤：

1. 设置初始值
2. 执行测试，看看循环是否应当继续进行。
3. 执行循环操作。
4. 更新用于测试的值。

`for` 循环的代码形式如下：

```c++
for (initialization; test-expression; update-expression)
{
    body
}
```

例如：

```cpp
// num_test.cpp -- use numeric test in for loop
#include <iostream>

int main()
{
	using namespace std;
	cout << "Enter the starting countdown value: ";
	int limit;
	cin >> limit;
	int i;
	for (i = limit; i; i--)	// quits when i is 0
	{
		cout << "i = " << i << "\n";
	}
	cout << "Done now that i = " << i << "\n";
	return 0;
}
```

在 `initialization` 中声明变量只存在于 `for` 语句中，也就是说，当程序离开循环后，这种变量将消失：

```cpp
for (int i = 0; i < 5; i++)
{
    cout << "C++ knows loops.\n";
}
cout << i << endl;	// oops! i no longer defined
```

`for` 循环需要 3 个表达式（从技术的角度说，它需要 1 条后面跟两个表达式的语句），不过它们可以是空表达式（语句），只有两个分号是必需的。另外，省略 `for` 循环中的测试表达式时，测试结果将为 `true`，因此下面的循环将一致运行下去：

```cpp
for (;;)
    body
```

