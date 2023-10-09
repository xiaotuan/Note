使用 `ifstream` 读取文本文件步骤如下：

+ 必须包含头文件 `fstream`。
+ 头文件 `fstream` 定义了一个用于处理输入的 `ifstream` 类。
+ 需要声明一个或多个 `ifstream` 变量（对象），并以自己喜欢的方式对其进行命名，条件是遵守常用的命名规则。
+ 必须指明名称空间 `std`；例如，为引用元素 `ifstream`，必须使用编译指令 `using` 或前缀 `std::`。
+ 需要将 `ifstream` 对象与文件关联起来。为此，方法之一是使用 `open()` 方法。
+ 使用完文件后，应使用 `close()` 方法将其关闭。
+ 可结合使用 `ifstream` 对象和运算符 `>>` 来读取各种类型的数据。
+ 可以使用 `ifstream` 对象和 `get()` 方法来读取一个字符，使用 `ifstream` 对象和 `getline()` 来读取一行字符。
+ 可以结合使用 `ifstream` 和 `eof()`、`fail()` 等方法来判断输入是否成功。
+ `ifstream` 对象本身被用作测试条件时，如果最后一个读取操作成功，它将被转换为布尔值 `true`，否则被转换为 `false`。

下面演示了如何声明这种对象：

```cpp
ifstream inFile;	// inFile an ifstream object
ifstream fin;		// fin an ifstream object
```

下面演示了如何将这种对象与特定的文件关联起来：

```cpp
inFile.open("bowling.txt");		// inFile used to read bowling.txt file
char filename[50];
cin >> filename;	// user specifies a name
fin.open(filename);	// fin used to read specified file
```

> 注意：方法 `open()` 接受一个 C 风格字符串作为参数，这可以是一个字面字符串，也可以是存储在数组中的字符串。

> 提示：所有可用于 `cin` 的操作和方法都可用于 `ifstream` 对象。

如果试图打开一个不存在的文件用于输入，情况将如何呢？这种错误将导致后面使用 `ifstream` 对象进行输入时失败。检查文件是否被成功打开的首选方法是使用方法 `is_open()`，为此，可以使用类似于下面的代码：

```cpp
inFile.open("bowling.txt");
if (!inFile.is_open()) {
    exit(EXIT_FAILURE);
}
```

> 提示：函数 `exit()` 的原型是在头文件 `cstdlib` 中定义的，在该头文件中，还定义了一个用于同操作系统通信的参数值 `EXIT_FAILURE`。
>
> 方法 `is_open()` 是 C++ 中相对较新的内容。如果读者的编译器不支持它，可使用较老的方法 `good()` 来代替。

读取文件时，有几点需要检查。首先，程序读取文件时不应超过 `EOF`。如果最后一次读取数据时遇到 `EOF`，方法 `eof()` 将返回 `true`。其次，程序可能遇到类型不匹配的情况。如果最后一次读取操作中发生了类型不匹配的情况，方法 `fail()` 将返回 `true`（如果遇到了 `EOF`，该方法也将返回 `true`）。最后，可能出现意外的问题，如文件受损或硬件故障。如果最后一次读取文件时发生了这样的问题，方法 `bad()` 将返回 `true`。不要分别检查这些情况，一种更简单的方法是使用 `good()` 方法，该方法在没有发生任何错误时返回 `true`：

```cpp
while (inFile.good())	// while input good and not at EOF
{
    ...
}
```

方法 `good()` 指出最后一次读取输入的操作是否成功，这一点至关重要。这意味着应该在执行读取输入的操作后，立刻应用这种测试。鉴于以下事实，可以对上述代码进行精简：表达式 `inFile >> value` 的结果为 `inFile.good()`，而在需要一个 `bool` 值的情况下，`inFile` 的结果为 `inFile.good()`，即 `true` 或 `false`。下面示例程序中的循环结构替换可以替换为如下结构：

```cpp
// abbreviated file-reading loop design
// omit pre-loop input
while (inFile >> value)	// read and test for success
{
    // loop body goes here
    // omit end-of-loop input
}
```



**程序清单 sumafile.cpp**

```cpp
// sumafile.cpp -- functions with an array argument
#include <iostream>
#include <fstream>	// file I/O support
#include <cstdlib>	// support for exit()

const int SIZE = 60;

int main()
{
	using namespace std;
	char filename[SIZE];
	ifstream inFile;	// object for handling file input
	cout << "Enter name of data file: ";
	cin.getline(filename, SIZE);
	inFile.open(filename);	// associate inFile with a file
	if (!inFile.is_open()) {	// failed to open file
		cout << "Could not open file " << filename << endl;
		cout << "Program terminating.\n";
		exit(EXIT_FAILURE);
	}
	double value;
	double sum = 0.0;
	int count = 0;	// number of items read
	
	inFile >> value;	// get first value
	while (inFile.good()) {	// while input good and not at EOF
		++count;	// one more item read
		sum += value;	// calculate running total
		inFile >> value;	// get next value
	}
	if (inFile.eof()) {
		cout << "End of file reached.\n";
	} else if (inFile.fail()) {
		cout << "Input terminated by data mismatch.\n";
	} else {
		cout << "Input terminated for unknown reason.\n";
	}
	if (count == 0) {
		cout << "No data processed.\n";
	} else {
		cout << "Items read: " << count << endl;
		cout << "Sum: " << sum << endl;
		cout << "Average: " << sum / count << endl;
	}
	inFile.close();	// finished with the file
	return 0;
}
```

要运行上面程序，首先需要创建一个包含数字的文本文件。假设该文件名为 `scores.txt`，包含的内容如下：

```
18 19 18.5 13.5 14
16 19.5 20 18 12 18.5
17.5
```

运行结果如下：

```shell
root@xiaotuan:~/桌面# g++ sumafile.cpp 
root@xiaotuan:~/桌面# ./a.out 
Enter name of data file: scores.txt
End of file reached.
Items read: 12
Sum: 204.5
Average: 17.0417
```

