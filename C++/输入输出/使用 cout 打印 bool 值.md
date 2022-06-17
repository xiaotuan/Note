通常，`cout` 在显示 `bool` 值之前将它们转换为 `int`，但 `cout.setf`（`ios::boolalpha`）函数调用设置了一个标记，该标记命令 `cout` 显示 `true` 和 `false`，而不是 1 和 0。

> 注意：老式 C++ 实现可能要求使用 `ios::boolalpha`，而不是 `ios_base::boolapha` 来作为 `cout.setf()` 的参数。有些老式实现甚至无法识别这种形式。

例如：

```cpp
// express.cpp -- values of expressions
#include <iostream>

int main()
{
	using namespace std;
	int x;

	cout << "The expression x = 1000 has the value ";
	cout << (x = 100) << endl;
	cout << "Now x = " << x << endl;
	cout << "The expression x < 3 has the value ";
	cout << (x < 3) << endl;
	cout << "The expression x > 3 has the value ";
	cout << (x > 3) << endl;
	cout.setf(ios_base::boolalpha);	// a newer c++ feature
	cout << "The expression x < 3 has the value ";
	cout << (x < 3) << endl;
	cout << "The expression x > 3 has the value ";
	cout << (x > 3) << endl;
	return 0;
}
```

