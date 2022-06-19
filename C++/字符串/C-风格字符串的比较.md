由于 C++ 将 C-风格字符串视为地址，因此如果使用关系运算符来比较它们，将无法得到满意的结果。相反，应使用 C-风格字符串库中的 `strcmp()` 函数来比较。该函数接受两个字符串地址作为参数。这意味着参数可以是指针、字符串常量或字符数组名。如果两个字符串相同，该函数将返回零；如果第一个字符串按字母顺序排在第二个字符串之前，则 `strcmp()` 将返回一个负数值；如果第一个字符串按字母顺序排在第二个字符串之后，则 `strcmp()` 将返回一个正数值。

```cpp
// forstr2.cpp -- reversing an array
#include <iostream>
#include <cstring>	// prototype for strcmp()

int main()
{
	using namespace std;
	char word[5] = "?ate";
	for (char ch = 'a'; strcmp(word, "mate"); ch++)
	{
		cout << word << endl;
		word[0] = ch;
	}
	cout << "After loop ends, word is " << word << endl;
	return 0;

}
```

C-风格字符串是通过结尾的空值字符定义的，而不是由其所在数组的长度定义的。这意味着两个字符串即使被存储在长度不同的数组中，也可能是相同的：

```cpp
// forstr2.cpp -- reversing an array
#include <iostream>
#include <string>

int main()
{
	using namespace std;
	char big[80] = "Daffy";	// 5 letters plus \0
	char little[6] = "Daffy";	// 5 letters plus \0
	cout << strcmp(big, little);
	return 0;

}
```

虽然不能用关系运算符来比较字符串，但却可以用它们来比较字符，因为字符实际上是整型。例如：

```cpp
for (ch = 'a'; ch <= 'z'; ch++)
{
    cout << ch;
}
```

