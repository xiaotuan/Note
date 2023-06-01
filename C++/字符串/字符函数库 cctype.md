<center><b>cctype 中的字符函数</b></center>

| 函数名称   | 返回值                                                       |
| ---------- | ------------------------------------------------------------ |
| isalnum()  | 如果参数是字母数字，即字母或数字，该函数返回 true            |
| isalpha()  | 如果参数是字母，该函数返回 true                              |
| iscntrl()  | 如果参数是控制字符，该函数返回 true                          |
| isdigit()  | 如果参数是数字（0 ~ 9），该函数返回 true                     |
| isgraph()  | 如果参数是除空格之外的打印字符，该函数返回 true              |
| islower()  | 如果参数是小写字母，该函数返回 true                          |
| isprint()  | 如果参数是打印字符（包括空格），该函数返回 true              |
| ispunct()  | 如果参数是标点符号，该函数返回 true                          |
| isspace()  | 如果参数是标准空白字符，如空格、进纸、换行符、回车、水平制表符或者垂直制表符，该函数返回 true |
| issupper() | 如果参数是大写字母，该函数返回 true                          |
| isxdigit() | 如果参数是十六进制数字，即 0~9、a~f 或 A~F，该函数返回 true  |
| tolower()  | 如果参数是大写字符，则返回其小写，否则返回该参数             |
| toupper()  | 如果参数是小写字符，则返回其大写，否则返回该参数             |

**示例程序：cctypes.cpp**

```cpp
// cctypes.cpp -- using the ctype.h library
#include <iostream>
#include <cctype>			// prototypes for character functions

int main()
{
	using namespace std;
	cout << "Enter text for analysis, and type @"
			" to terminate input.\n";
			
	char ch;
	int whitespace = 0;
	int digits = 0;
	int chars = 0;
	int punct = 0;
	int others = 0;
	
	cin.get(ch);	 			// get first character
	while (ch != '@')			// test for sentinel
	{
		if (isalpha(ch))		// is it an alphabetic character?
			chars++;
		else if (isspace(ch))	// is it a whitespace character?
			whitespace++;
		else if (isdigit(ch))	// is it a digit?
			digits++;
		else if(ispunct(ch))	// is it punctuation?
			punct++;
		else
			others++;
		cin.get(ch);			// get next character
	}
	cout << chars << " letters, "
		 << whitespace << " whitespace, "
		 << digits << " digits, "
		 << punct << " punctuations, "
		 << others << " others.\n";
	return 0;
}
```

运行结果如下：

```shell
$ g++ cctypes.cpp 
$ ./a.out 
Enter text for analysis, and type @ to terminate input.
AdrenalVision International producer Adrienne Vismonger
announced production of their new 3-D film, a remake of
"My Dinner with Andre," scheduled for 2013. "Wait until
you see the the new scene with an enraged Collossipede!"@
177 letters, 33 whitespace, 5 digits, 9 punctuations, 0 others.
```

