`C++` 的 `switch` 语句能够更容易地从大型列表中进行选择。下面是 `switch` 语句的通用格式：

```cpp
switch (integer-expression)
{
    case label1:
        statement(s)
    case label2:
        statement(s)
    ...
    default: statement(s)
}
```

执行到 `switch` 语句时，程序将跳到使用 `integer-expression` 的值标记的那一行。`integer-expression` 必须是一个结果为整数值的表达式。另外，每个标签都必须是整数常量表达式。最常见的标签是 `int` 或 `char` 常量，也可以是枚举量。如果 `integer-expression` 不与任何标签匹配，则程序将跳到标签为 `default` 的那一行。`default` 标签是可选的，如果被省略，而又没有匹配的标签，则程序将跳到 `switch` 后面的语句处执行。

程序跳转到 `switch` 中特定代码行后，将依次执行之后的所有语句，除非有明确的其他指示。程序不会在执行到下一个 `case` 处自动停止，要让程序执行完一组特定语句后停止，必须使用 `break` 语句。这将导致程序跳转到 `switch` 后面的语句处执行。

**示例程序：switch.cpp**

```cpp
// switch.cpp -- using the switch statement
#include <iostream>

using namespace std;

void showmenu();	// function prototypes
void report();
void comfort();

int main()
{
	showmenu();
	int choice;
	cin >> choice;
	while (choice != 5)
	{
		switch(choice)
		{
			case 1:
				cout << "\a\n";
				break;
			case 2:
				report();
				break;
			case 3:
				cout << "The boss was in all day.\n";
				break;
			case 4:
				comfort();
				break;
			default:
				cout << "That's not a choice.\n";
		}
		showmenu();
		cin >> choice;
	}
	cout << "Bye!\n";
	return 0;
}

void showmenu()
{
	cout << "Please enter 1, 2, 3, 4, or 5:\n"
			"1) alarm			2) report\n"
			"3) alibi			4) comfort\n"
			"5) quit\n";
}

void report() 
{
	cout << "It's been an excellent week for business.\n"
			"Sales are up 120%. Expenses are down 35%.\n";
}

void comfort()
{
	cout << "Your employees think you are the finest CEO\n"
			"in the industry. The board of directors think\n"
			"you are the finest CEO in the industry.\n";
}
```

运行结果如下：

```shell
$ g++ switch.cpp 
$ ./a.out 
Please enter 1, 2, 3, 4, or 5:
1) alarm			2) report
3) alibi			4) comfort
5) quit
1

Please enter 1, 2, 3, 4, or 5:
1) alarm			2) report
3) alibi			4) comfort
5) quit
2
It's been an excellent week for business.
Sales are up 120%. Expenses are down 35%.
Please enter 1, 2, 3, 4, or 5:
1) alarm			2) report
3) alibi			4) comfort
5) quit
3
The boss was in all day.
Please enter 1, 2, 3, 4, or 5:
1) alarm			2) report
3) alibi			4) comfort
5) quit
4
Your employees think you are the finest CEO
in the industry. The board of directors think
you are the finest CEO in the industry.
Please enter 1, 2, 3, 4, or 5:
1) alarm			2) report
3) alibi			4) comfort
5) quit
5
Bye!
```

**1. 将枚举量用作标签**

通常，`cin` 无法识别枚举类型，因此该程序要求用户选择选项时输入一个整数。当 `switch` 语句将 `int` 值和枚举量标签进行比较时，将枚举量提升为 `int`。另外，在 `while` 循环测试条件中，也会将枚举量提升为 `int` 类型。

**示例代码：enum.cpp**

```cpp
// enum.cpp -- using enum
#include <iostream>

// create named constants for 0 - 6
enum { red, orange, yellow, green, blue, violet, indigo };

int main()
{
	using namespace std;
	cout << "Enter color code (0-6): ";
	int code;
	cin >> code;
	while (code >= red && code <= indigo)
	{
		switch (code)
		{
			case red:
				cout << "Her lips were red.\n";
				break;
			
			case orange:
				cout << "Her hair was orange.\n";
				break;
				
			case yellow:
				cout << "Her shoes were yellow.\n";
				break;
				
			case green:
				cout << "Her nails were green.\n";
				break;
				
			case blue:
				cout << "Her sweatsuit was blue.\n";
				break;
			
			case violet:
				cout << "Her eyes were violet.\n";
				break;
				
			case indigo:
				cout << "Her mood was indigo.\n";
				break;
		}
		cout << "Enter color code (0-6): ";
		cin >> code;
	}
	cout << "Bye\n";
	return 0;
}
```

运行结果如下：

```shell
$ g++ enum.cpp 
$ ./a.out 
Enter color code (0-6): 3
Her nails were green.
Enter color code (0-6): 5
Her eyes were violet.
Enter color code (0-6): 2
Her shoes were yellow.
Enter color code (0-6): 8
Bye
```

