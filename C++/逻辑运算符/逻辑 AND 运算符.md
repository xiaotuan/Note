逻辑 AND 运算符（&&），也是将两个表达式组合成一个表达式。仅当原来的两个表达式都为 true 时，得到的表达式的值才为 true。例如：

```cpp
5 == 5 && 4 == 4	// true
5 == 3 && 4 == 4	// false
```

&& 运算符也是顺序点，它将首先判定左侧，并且在右侧被判定之前产生所有的副作用。如果左侧为 false，则整个逻辑表达式必须为 false，在这种情况下，C++ 将不会再对右侧进行判定。

<center><b>&& 运算符</b></center>

|                | expr1 && expr2 的值 |                |
| -------------- | ------------------- | -------------- |
|                | expr1 == true       | extr1 == false |
| expr2 == true  | true                | false          |
| expr2 == false | false               | false          |

**示例代码：and.cpp**

```cpp
// and.cpp -- using the logical AND operator
#include <iostream>
const int ArSize = 6;
int main()
{
	using namespace std;
	float naaq[ArSize];
	cout << "Enter the NAAQs (New Age Awareness Quotients) "
		 << "of\nyour neighbors. Program terminates "
		 << "when you make\n" << ArSize << " entries "
		 << "or enter a negative value.\n";
		
	int i = 0;
	float temp;
	cout << "First value: ";
	cin >> temp;
	while (i < ArSize && temp >= 0) 	// 2 quitting criteria
	{
		naaq[i] = temp;
		++i;
		if (i < ArSize)	// room left in the array,
		{
			cout << "Next value: ";
			cin >> temp;	// so get next value
		}
	}
	if (i == 0)
	{
		cout << "No data--bye\n";
	} else {
		cout << "Enter your NAAQ: ";
		float you;
		cin >> you;
		int count = 0;
		for (int j = 0; j < i; j++) 
		{
			if (naaq[j] > you)
			{
				++count;
			}
		}
		cout << count;
		cout << " of your neighbors have greater awareness of\n"
			 << "the New Age than you do.\n";
	}
	return 0;
}
```

运行结果如下：

```shell
$ g++ and.cpp
$ ./a.out
Enter the NAAQs (New Age Awareness Quotients) of
your neighbors. Program terminates when you make
6 entries or enter a negative value.
First value: 28
Next value: 72
Next value: 15
Next value: 6
Next value: 130
Next value: 145
Enter your NAAQ: 50
3 of your neighbors have greater awareness of
the New Age than you do.
```

