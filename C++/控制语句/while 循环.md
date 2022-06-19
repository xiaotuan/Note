`while` 循环时没有初始化和更新部分的 `for` 循环，它只有测试条件和循环体：

```cpp
while (test-condition)
    body
```

例如：

```cpp
// while.cpp -- introducing the while loop
#include <iostream>

const int ArSize = 20;

int main()
{
	using namespace std;
	char name[ArSize];
	cout << "Your first name, please: ";
	cin >> name;
	cout << "Here is your name, verticalized and ASCIIized:\n";
	int i = 0;	// start at beginning for string
	while (name[i] != '\0')	// process to end of string
	{
		cout << name[i] << ": " << int(name[i]) << endl;
		i++;	// don't forget this step
	}
	return 0;
}
```

不同于 C-风格字符串，`string` 对象不适用空字符来标记字符串末尾，因此要将上面程序转换为使用 `string` 类的版本，只需用 `string` 对象替换 `char` 数组即可。例如：

```cpp
// while.cpp -- introducing the while loop
#include <iostream>
#include <string>

int main()
{
	using namespace std;
	string name;
	cout << "Your first name, please: ";
	cin >> name;
	cout << "Here is your name, verticalized and ASCIIized:\n";
	int i = 0;	// start at beginning for string
	while (name[i] != '\0')	// process to end of string
	{
		cout << name[i] << ": " << int(name[i]) << endl;
		i++;	// don't forget this step
	}
	return 0;
}
```

