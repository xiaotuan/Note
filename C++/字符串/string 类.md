[toc]

### 1. string 类

ISO/ANSI C++98 标准通过添加 `string`  类扩展了 C++ 库。要使用 `string` 类，必须在程序中包含头文件 `string`。`string` 类位于命名空间 std 中，因此必须提供一条 using 编译指令，或者使用 `std::string` 来引用它。

```cpp
// strtype1.cpp -- using the C++ string class
#include <iostream>
#include <string>	// make string class available
int main()
{
	using namespace std;
	char charr1[20];	// create an empty array
	char charr2[20] = "jaguar";	// create an initialized array
	string str1;	// create an empty string object
	string str2 = "panther";	// create an initialized string

	cout << "Enter a kind of feline: ";
	cin >> charr1;
	cout << "Enter another kind of feline: ";
	cin >> str1;	// use cin for input
	cout << "Here are some felines:\n";
	cout << charr1 << " " << charr2 << " "
		<< str1 << " " << str2	// use cout for output
		<< endl;
	cout << "The third letter in " << charr2 << " is "
		<< charr2[2] << endl;
	cout << "The third letter in " << str2 << " is "
		<< str2[2] << endl;	// use array notation

	return 0;
}
```

### 2. 初始化 string 变量

#### 2.1 C 风格初始化

+ 可以使用 C - 风格字符串来初始化 `string` 对象。
+ 可以使用 `cin` 来将键盘输入存储到 `string` 对象中。

```cpp
string str1;	// create an empty string object
string str2 = "panther";	// create an initialized string

cin >> str1;	// use cin for input
```

#### 2.2 C++11 字符串初始化

可以使用列表初始化方式初始化 `string` 对象：

```cpp
string third_date = { "The Bread Bowl" };
string fourth_date { "Hank's Fine Eats" };
```

### 3. 赋值

可以将一个 `string` 对象赋给另一个 `string` 对象：

```cpp
string str1;
string str2 = "panther";	// create an initialized string
str1 = str2;	// VALID, object assignment OK
```

### 4. 字符串拼接

可以使用运算符 `+` 将两个 `string` 对象合并起来，还可以使用运算符 `+=` 将字符串附加到 `string` 对象的末尾。

```cpp
// strtype2.cpp -- assigning, adding, and appending
#include <iostream> 
#include <string>	// make string class available

int main()
{
	using namespace std;
	string s1 = "penguin";
	string s2, s3;

	cout << "You can assign one string object to another: s2 = s1\n";
	s2 = s1;
	cout << "s1: " << s1 << ", s2: " << s2 << endl;
	cout << "You can assign a C-style string to a string object.\n";
	cout << "s2 = \"buzzard\"\n";
	s2 = "buzzard";
	cout << "s2: " << s2 << endl;
	cout << "You can concatenate strings: s3 = s1 + s2\n";
	s3 = s1 + s2;
	cout << "s3: " << s3 << endl;
	cout << "You can append strings.\n";
	s1 += s2;
	cout << "s1 += s2 yields s1 = " << s1 << endl;
	s2 += " for a day";
	cout << "s2 += \" for a day\" yields s2 = " << s2 << endl;

	return 0;
}
```

### 5. string 类的其他操作

对于 C- 风格字符串，程序员使用 C 语言库中的函数来完成这些任务。头文件 `cstring`（以前为 `string.h` ）提供了这些函数。

```cpp
// strtype3.cpp -- more string class features
#include <iostream>
#include <string>	// make string class available
#include <cstring>	// C-style string library

int main()
{
	using namespace std;
	char charr1[20];
	char charr2[20] = "jaguar";
	string str1;
	string str2 = "panther";

	// assignment for string objects and character arrays
	str1 = str2;	// copy str2 to str1
	strcpy_s(charr1, charr2);	// copy charr2 to charr1

	// appending for string objects and character arrays
	str1 += " paste";	// add paste to end of str1
	strcat_s(charr1, " juice");	// add juice to end of charr1

	// finding the length of a string object and a C-style string
	size_t len1 = str1.size();	// obtain length of str1
	size_t len2 = strlen(charr1);	// obtain length of charr1

	cout << "The string " << str1 << " contains "
		<< len1 << " characters.\n";
	cout << "The string " << charr1 << " contains "
		<< len2 << " characters.\n";

	return 0;
}
```

### 6. string  类 I/O

可以使用 `cin` 和运算符 `>>` 来将输入存储到 `string` 对象中，使用 `cout` 和运算符 `<<` 来显示 `string` 对象，其语法与处理 C-风格字符串相同。但读取一行的语法与 C-风格字符串不同，使用的是 `getline()` 函数。

```cpp
// strtype4.cpp -- line input
#include <iostream>
#include <string>	// make string class available
#include <cstring>	// C-style string library

int main()
{
	using namespace std;
	char charr[20];
	string str;

	cout << "Length of string in charr before input: "
		<< strlen(charr) << endl;
	cout << "Length of string in str before input: "
		<< str.size() << endl;
	cout << "Enter a line of text:\n";
	cin.getline(charr, 20);	// indicate maximum length
	cout << "You entered: " << charr << endl;
	cout << "Enter another line of text:\n";
	getline(cin, str);	// cin now an argument; no length specifier
	cout << "You entered: " << str << endl;
	cout << "Length of string in charr after input: "
		<< strlen(charr) << endl;
	cout << "Length of string in str after input: "
		<< str.size() << endl;

	return 0;
}
```

