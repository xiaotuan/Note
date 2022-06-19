如果使用 `string` 类字符串而不是 C-f风格字符串，比较起来将简单些，因为类设计让您能够使用关系运算符进行比较。例如：

```cpp
// compstr2.cpp -- comparing strings using arrays
#include <iostream>
#include <string>	// string class

int main()
{
	using namespace std;
	string word = "?ate";
	for (char ch = 'a'; word != "mate"; ch++)
	{
		cout << word << endl;
		word[0] = ch;
	}
	cout << "After loop ends, word is " << word << endl;
	return 0;
}
```

