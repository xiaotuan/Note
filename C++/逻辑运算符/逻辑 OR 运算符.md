C++ 可以采用逻辑 OR 运算符（||），将两个表达式组合在一起。如果原来表达式中的任何一个或全部都为 true（或非零），则得到的表达式的值为 true；否则，表达式的值为 false。例如：

```cpp
5 == 5 || 5 == 9	// true
5 > 3 || 5 > 10		// true
5 > 8 || 5 < 10		// true
5 < 8 || 5 > 2		// true
5 > 8 || 5 < 2		// false
```

C++ 规定，`||` 运算符是个顺序点。也就是说，先修改左侧的值，再对右侧的值进行判断。另外，如果左侧的表达式为 true，则 C++ 将不会去判断右侧的表达式，因为只要一个表达式为 true，则整个逻辑表达式为 true。

<center><b>|| 运算符</b></center>

|                | expr1 \|\| expr2 的值 |               |
| -------------- | --------------------- | ------------- |
|                | expr1 == true         | expr1 == fase |
| expr2 == true  | true                  | true          |
| expr2 == false | true                  | false         |

**示例代码：or.cpp**

```cpp
// or.cpp -- using the logical OR operator
#include <iostream>
int main()
{
	using namespace std;
	cout << "This program may reformat your hard disk\n"
			"and destroy all your data.\n"
			"Do you wish to continue? <y/n> ";
	char ch;
	cin >> ch;
	if (ch == 'y' || ch == 'Y')	// y or Y
		cout << "You were warned!\a\a\n";
	else if (ch == 'n' || ch == 'N')	// n or N
		cout << "A wise choice ... bye\n";
	else
		cout << "That wasn't a y or n! Apparently you "
				"can't follow\ninstructions, so "
				"I'll trash your disk anyway.\a\a\a\n";
	return 0;
}
```

运行结果如下：

```shell
$ g++ or.cpp
$ ./a.out 
This program may reformat your hard disk
and destroy all your data.
Do you wish to continue? <y/n> N
A wise choice ... bye
```



