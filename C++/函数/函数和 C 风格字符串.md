[toc]

C-风格字符串由一些列字符组成，以空值字符结尾。

### 1. 将 C-风格字符串作为参数的函数

假设要将字符串作为参数传递给函数，则表示字符串的方式有三种：

+ `char` 数组；
+ 用引号括起来的字符串常量（也称字符串字面值）；
+ 被设置为字符串的地址的 `char` 指针。

但上述 3 种选择的类型都是 `char` 指针（准确地说是 `char*`），因此可以将其作为字符串处理函数的参数：

``` cpp
char ghost[15] = "galloping";
char * str = "galumphing";
int n1 = strlen(ghost);			// ghost is &ghost[0]
int n2 = strlen(str);			// pointer to char
int n3 = strlen("ganboling");	// address of string
```

C-风格字符串与常规 `char` 数组之间的一个重要区别是，字符串有内置的结束字符（包含字符，但不以空值字符结尾的 `char` 数组只是数组，而不是字符串）。这意味着不必将字符串长度作为参数传递给函数，而函数可以使用循环依次检查字符串中的每个字符，知道遇到结尾的空字符为止。

**程序清单 strgfun.cpp**

```cpp
// strgfun.cpp -- functions with a string argument
#include <iostream>

unsigned int c_in_str(const char * str, char ch);

int main()
{
	using namespace std;
	char mmm[15] = "minimum";	// string in an array
	// some systems require preceding char with static to
	// enable array initialization
	
	char *wail = "ululate";		// wail points to string
	
	unsigned int ms = c_in_str(mmm, 'm');
	unsigned int us = c_in_str(wail, 'u');
	cout << ms << " m characters in " << mmm << endl;
	cout << us << " u characters in " << wail << endl;
	return 0;
}

// this function counts the number of ch characters
// in the string str
unsigned int c_in_str(const char * str, char ch)
{
	unsigned int count = 0;
	
	while (*str)	// quit when *str is '\0'
	{
		if (*str == ch)
		{
			count++;
		}
		str++;	// move pointer to next char
	}
	return count;
}
```

运行结果如下：

```
$ g++ strgfun.cpp 
strgfun.cpp: In function ‘int main()’:
strgfun.cpp:13:15: warning: deprecated conversion from string constant to ‘char*’ [-Wwrite-strings]
  char *wail = "ululate";  // wail points to string
               ^
$ ./a.out 
3 m characters in minimum
2 u characters in ululate
```

> 注意：
>
> 已弃用从字符串常量到' char* '的转换。原因是：
>
> 1. 主程序初始化字符串，是字符串常量，该字符串的内存分配至全局的 `const` 内存区。
> 2. 而 `char*` 声明了一个指针，而这个指针指向的是全局的 `const` 内存去，`const` 内存区不是想改就改的。所以，如果你一定要写这块内存的话，那就是一个非常严重的内存错误。

当然，可以在函数头中使用数组表示法，而不声明 `str`：

```cpp
unsigned int c_in_str(const char str[], char ch)	// also okay
```

### 2. 返回 C 风格字符串的函数

函数无法返回一个字符串，但可以返回字符串的地址，这样做的效率更高。

**程序清单 strgback.cpp**

```cpp
// strgback.cpp -- a function that returns a pointer to char
#include <iostream>

char * buildstr(char c, int n);	// prototype

int main()
{
	using namespace std;
	int times;
	char ch;
	
	cout << "Enter a character: ";
	cin >> ch;
	cout << "Enter a integer: ";
	cin >> times;
	char *ps = buildstr(ch, times);
	cout << ps << endl;
	delete [] ps;	// free memory
	ps = buildstr('+', 20);		// reuse pointer
	cout << ps << "-DONE-" << ps << endl;
	delete [] ps;	// free memory
	return 0;
}

// builds string made of n c characters
char * buildstr(char c, int n)
{
	char * pstr = new char[n + 1];
	pstr[n] = '\0';	// terminate string
	while (n-- > 0)
		pstr[n] = c;	// fill reset of string
	return pstr;
}
```

运行结果如下：

```
$ g++ strgback.cpp 
$ ./a.out 
Enter a character: V 
Enter a integer: 46
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
++++++++++++++++++++-DONE-++++++++++++++++++++
```

> 注意：变量 `pstr` 的作用域为 `buildstr` 函数内，因此该函数结束时，`pstr`（而不是字符串）使用的内存将被释放。但由于函数返回了 `pstr` 的值，因此程序仍可以通过 `main()` 中的指针 `ps` 来访问新建的字符串。
>
> 当该字符串不再需要时，应该使用 `delete` 释放该字符串占用的内存。（使用 `new` 分配的内存，需要使用 `delete` 释放内存）
