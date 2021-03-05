[toc]

**程序清单4.7 strtype1.cpp**

```cpp
// strtype1.cpp -- using the C++ string class
#include <iostream>
#include <string>	// make string class available

int main() 
{
	using namespace std;
	char charr1[20];			// create an empty array
	char charr2[20] = "jaguar";	// create an initialized array
	string str1;				// create an empty string object
	string str2 = "panther";	// create an initialized string

	cout << "Enter a kind of feline: ";
	cin >> charr1;
	cout << "Enter another kind of feline: ";
	cin >> str1;				// use cin for input
	cout << "Here are some felines:\n";
	cout << charr1 << " " << charr2 << " "
		<< str1 << " " << str2	// use cout for output
		<< endl;
	cout << "The third letter in " << charr2 << " is "
		<< charr2[2] << endl;
	cout << "The third letter in " << str2 << " is "
		<< str2[2] << endl;		// use array notation
	
	return 0;
}
```

输出结果如下所示：

```console
Enter a kind of feline: ocelot
Enter another kind of feline: tiger
Here are some felines:
ocelot jaguar tiger panther
The third letter in jaguar is g
The third letter in panther is n
```

### 1. C++ 11 字符串初始化

C++ 11 允许将列表初始化用于 C 风格字符串和 string 对象：

```cpp
char first_date[] = {"Le Chapon Dodu"};
char second_date[] {"The Elegant Plate"};
string third_date = {"The Bread Bowl"};
string fourth_date = {"Hank's Fine Eats"};
```

### 2. 赋值、拼接和附加

可以将一个 string 对象赋给另一个 string 对象：

```cpp
char charr1[20];			// create an empty array
char charr2[20] = "jaguar";	// create an initialized array
string str1;				// create an empty string object
string str2 = "panther";	// create an initialized string
charr1 = charr2;			// INVALID, no array assignment
str1 = str2;				// VALID, objectassignment ok
```

可以使用运算符 + 将两个 string  对象合并起来，还可以使用运算符 += 将字符串附加到 string 对象的末尾。

```cpp
string str3;
str3 = str1 + str2;		// assign str3 the joined strings
str1 += str2;			// add str2 to the end of str1
```

**程序清单4.8 strtype2.cpp**

```cpp
// strtype2.cpp -- assigning, adding, and appending
#include <iostream>
#include <string>			// make string class available

int main()
{
	using namespace std;
	string s1 = "penguin";
	string s2, s3;

	cout << "You can assign one string object to another: s2 = s1 \n";
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

输出结果如下所示：

```console
You can assign one string object to another: s2 = s1
s1: penguin, s2: penguin
You can assign a C-style string to a string object.
s2 = "buzzard"
s2: buzzard
You can concatenate strings: s3 = s1 + s2
s3: penguinbuzzard
You can append strings.
s1 += s2 yields s1 = penguinbuzzard
s2 += " for a day" yields s2 = buzzard for a day
```

### 3. string 类的其他操作

头文件 cstring （以前为 string.h）提供了对字符串操作的函数。

**程序清单 4.9 strtype3.cpp**

```cpp
// strtype3.cpp -- more string class features
#include <iostream>
#include <string>			// make string class available
#include <cstring>			// C-style string library

int main()
{
	using namespace std;
	char charr1[20];
	char charr2[20] = "jaguar";
	string str1;
	string str2 = "panther";

	// assignment for string objects and character arrays
	str1 = str2;			// copy str2 to str1
	// strcpy(charr1, charr2);	// strcpy 被认为是不安全的，需要使用 strcpy_s 替代
	strcpy_s(charr1, charr2);	// copy charr2 to charr1

	// appending for string objects and character arrays
	str1 += " paste";		//add paste to end of str1
	// strcat(charr1, " juice"); // strcat 被认为是不安全的，需要使用 strcat_s 替代
	strcat_s(charr1, " juice");	// add juice to end of charr1

	// finding the length of a string object and a C-style string
	int len1 = str1.size();	// obtain length of str1
	int len2 = strlen(charr1);	// obtain length of charr1

	cout << "The string " << str1 << " contains "
		<< len1 << " characters.\n";
	cout << "The string " << charr1 << " contains "
		<< len2 << " characters.\n";

	return 0;
}
```

输出结果如下所示：

```console
The string panther paste contains 13 characters.
The string jaguar juice contains 12 characters.
```

使用字符串数组时，总是存在目标数组过小，无法存储指定信息的危险，如下面的示例所示：

```cpp
char site[10] = "house";
strcat(site, " of pancakes");	// memory problem
```

函数 strcat() 试图将全部 12 个字符复制到数组 site 中，这将覆盖相邻的内存。C 函数库提供了与 strcat() 和 strcpy() 类似的函数——strncat() 和 strncpy() ，它们接受指出目标数组最大允许长度的第三个参数。

### 4. string 类 I/O

可以使用 cin 和运算符 >> 来将输入存储到 string 对象中，使用 cout 和运算符 << 来显示对象。

**程序清单4.10 strtype4.cpp**

```cpp
// strtype4.cpp -- line input
#include <iostream>
#include <string>			// make string class available
#include <cstring>			// C-style string library

int main()
{
	using namespace std;
	char charr[20];
	string str;

	cout << "Length of string in charr before input: "
		<< strlen(charr) << endl;
	cout << "Length of string in str before input: "
		<< str.size() << endl;
	cout << "Enter a line of text: \n";
	cin.getline(charr, 20);	// indicate maximum length
	cout << "You entered: " << charr << endl;
	cout << "Enter another line of text:\n";
	getline(cin, str);		// cin now an argument; no lenght specifier
	cout << "You entered: " << str << endl;
	cout << "Length of string in charr after input: "
		<< strlen(charr) << endl;
	cout << "Length of string in str after input: "
		<< str.size() << endl;

	return 0;
}
```

输出结果如下所示：

```console
Length of string in charr before input: 31
Length of string in str before input: 0
Enter a line of text:
peanut butter
You entered: peanut butter
Enter another line of text:
blueberry jam
You entered: blueberry jam
Length of string in charr after input: 13
Length of string in str after input: 13
```

在用户输入之前，该程序指出数组 charr 中的字符串长度为 31，这比该数组的长度要大。因为未初始化的数组的内容是未定义的，函数 strlen() 从数组的第一个元素开始计算字节数，知道遇到空字符位置。对于未被初始化的数据，第一个空字符的储蓄位置是随机的，因此得到的数组长度很可能都不同。

函数 getline() 是 istream 类的一个类方法，第一个参数是目标数组；第二个参数是数组长度。

### 5.其他形式的字符串字面量

除 char 类型外，C++ 还有类型 wchar_t；而 C++11 新增了类型 char16_t 和 char32_t。对于这些类型的字符串字面量，C++分别使用前缀 L、u 和 U 表示，下面是一个如何使用这些前缀的例子：

```cpp
wchar_t title[] = L"Chief Astrogator";	// w_char string
char16_t name[] = u"Felonia Ripova";	// char_16 string
char32_t car[] = U"Humber Super Snipe";	// char_32 string
```

C++11 还支持 Unicode 字符编码 UTF-8。C++ 使用前缀 u8 来表示这种类型的字符串字面值。

C++11 新增的另一种类型是原始（raw）字符串。在原始字符串中，字符表示的就是自己，例如，序列 \n 不表示换行符，而表示两个常规字符——斜杠和 n。原始字符串将 `"(` 和 `)"` 用作定界符，并使用前缀 R 来标识原始字符串：

```cpp
cout << R"(Jim "King" Tutt uses "\n" instend of endl.)" << '\n';
```

上述代码将显示如下内容：

```console
Jim "King" Tutt uses "\n" instend of endl.
```

如果要在原始字符串中包含 )"，该如何办呢？原始字符串语法允许您在表示字符串开头的 " 和 ( 之间添加其他字符，这意味着表示字符串结尾的 " 和 ) 之间也必须包含这些字符。因此，使用 `R"+*(` 标识原始字符串的开头时，必须使用 `)+*"` 标识原始字符串的结尾。例如：

```cpp
cout << R"+*("(who wouldn't?)", she whispered.)+*" << endl;
```

将显示如下内容：

```console
"(who wouldn't?)", she whispered.
```

> 自定义定界符时，在默认定界符之间添加任意数量的基本字符，但空格、左括号、右括号、斜杠和控制字符（如制表符和换行符）除外。