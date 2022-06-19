`do while` 循环时出口条件循环。这意味着这种循环将首先执行循环体，然后再判定测试表达式，决定是否应继续执行循环。如果条件为 `false`，则循环终止；否则，进入新一轮的执行和测试。这样的循环通常至少执行一次，因为其程序流必须经过循环体后才能到达测试条件。下面是其语法：

```cpp
do
    body;
while (test-expression);
```

例如：

```cpp
// dowhile.cpp -- exit-condition loop
#include <iostream>

int main()
{
	using namespace std;
	int n;

	cout << "Enter numbers in the range 1-10 to find ";
	cout << "my favorite number\n";
	do
	{
		cin >> n;	// execute body
	} while (n != 7);	// then test
	cout << "Yes, 7 is my favorite.\n";
	return 0;
}
```

