可以通过修改更新表达式来修改步长。例如：

```cpp
// bigstep.cpp -- count as directed
#include <iostream>

int main()
{
	using std::cout;	// a using declaration
	using std::cin;
	using std::endl;
	cout << "Enter an integer: ";
	int by;
	cin >> by;
	cout << "Counting by " << by << "s:\n";
	for (int i = 0; i < 100; i = i + by)
	{
		cout << i << endl;
	}
	return 0;
}
```

