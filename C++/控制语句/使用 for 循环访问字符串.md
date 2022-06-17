`for` 循环提供了一种依次访问字符串中每个字符的方式。在下面例子中，可以使用 `string` 对象，也可以使用 `char` 数组，因为它们都让您能够使用数组表示法来访问字符串中的字符。

例如：

```cpp
// forstr1.cpp -- using for with a string
#include <iostream>
#include <string>

int main()
{
	using namespace std;
	cout << "Enter a word: ";
	string word;
	cin >> word;

	// display letters in reverse order
	for (int i = word.size() - 1; i >= 0; i--)
	{
		cout << word[i];
	}
	cout << "\nBye.\n";
	return 0;
}
```

