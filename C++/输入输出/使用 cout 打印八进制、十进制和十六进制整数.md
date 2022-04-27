使用 `cout` 以十进制、八进制或十六进制方式打印整数值，需要使用`dec`、 `oct` 或 `oct` 控制符。例如：

**hexoct2.cpp**

```cpp
// hexoct2.cpp -- display values in hex and octal
#include <iostream>

using namespace std;

int main()
{
	using namespace std;
	int chest = 42;
	int waist = 42;
	int inseam = 42;
	int score = 0x42;

	cout << "Monsieur cuts a striking figure!" << endl;
	cout << "chest = " << chest << " (decimal for 42)" << endl;
	cout << hex;	// manipulator for changing number base
	cout << "waist = " << waist << " (hexadecimal for 42)" << endl;
	cout << oct;	// manipulator for changing number base
	cout << "inseam = " << inseam << " (octal for 42)" << endl;
	cout << dec;	// manipulator for changing number base
	cout << "score = " << score << " (decimal for 0x42" << endl;

	return 0;
}
```

> 注意
>
> 1. 诸如 `cout << hex;` 等代码不会在屏幕上显示任何内容，而只是修改 cout 显示整数的方式。
> 2. 由于标识符 `hex` 位于名称空间 `std` 中，如果省略编译指令 `using`，而使用 `std::cout`、`std::endl`、`std::hex` 和 `std::oct`，则可以将 `hex` 用作变量名。