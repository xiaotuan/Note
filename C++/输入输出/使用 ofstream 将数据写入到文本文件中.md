文件输出的步骤如下：

+ 必须包含头文件 `fstream`。
+ 头文件 `fstream` 定义了一个用于处理输出的 `ofstream` 类。
+ 需要声明一个或多个 `ofstream` 变量（对象），并以自己喜欢的方式对其进行命名，条件是遵守常用的命名规则。
+ 必须指明名称空间 `std`，例如，为引用元素 `ofstream`，必须使用编译指令 `using` 或前缀 `std::`。
+ 需要将 `ofstream` 对象与文件关联起来。为此，方法之一是使用 `open()` 方法。
+ 使用完文件后，应使用方法 `close()` 将其关闭。
+ 可结合使用 `ofstream` 对象和运算符 `<<` 来输出各种类型的数据。

下面演示了如何声明这种对象：

```cpp
ofstream outFile;	// outFile an ofstream object
ofstream fout;	// fout an ofstream object
```

下面演示了如何将这种对象与特定的文件关联起来：

```cpp
outFile.open("fish.txt");	// outFile used to write to the fish.txt file
char filename[50];
cin >> filename;	// user specifies a name
fout.open(filename);	// fout used to read specified file
```

> 注意：方法 `open()` 接受一个 C 风格字符串作为参数，这可以是一个字面字符串，也可以是存储在数组中的字符串。

声明一个 `ofstream` 对象并将其同文件关联起来后，便可以像使用 `cout` 那样使用它。所有可用于 `count` 的操作和方法（如 `<<`、`endl` 和 `setf()` ）都可用于 `ofstream` 对象。

默认情况下，`open()` 将首先截断该文件，即将其长度截断到零——丢弃原有的内容，然后将新的输出加入到该文件中。

> 警告：打开已有的文件，以接受输出时，默认将它其长度截断为零，因此原来的内容将丢失。

**程序清单 outfile.cpp**

```cpp
// outfile.cpp -- writing to a file
#include <iostream>
#include <fstream>		// for file I/O

int main()
{
	using namespace std;
	
	char automobile[50];
	int year;
	double a_price;
	double d_price;
	
	ofstream outFile;		// create object for output
	outFile.open("carinfo.txt");	// associate with a file
	
	cout << "Enter the make and model of automobile: ";
	cin.getline(automobile, 50);
	cout << "Enter the model year: ";
	cin >> year;
	cout << "Enter the original asking price: ";
	cin >> a_price;
	d_price = 0.913 * a_price;
	
	// display information on screen with cout
	
	cout << fixed;
	cout.precision(2);
	cout.setf(ios_base::showpoint);
	cout << "Make and model: " << automobile << endl;
	cout << "Year: " << year << endl;
	cout << "Was asking $" << a_price << endl;
	cout << "Now asking $" << d_price << endl;
	
	// now do exact same things using outFile instead of cout
	
	outFile << fixed;
	outFile.precision(2);
	outFile.setf(ios_base::showpoint);
	outFile << "Make and model: " << automobile << endl;
	outFile << "Year: " << year << endl;
	outFile << "Was asking $" << a_price << endl;
	outFile << "Now asking $" << d_price << endl;
	
	outFile.close();	// done with file
	return 0;
}
```

运行结果如下：

```shell
root@xiaotuan:~/桌面# g++ outfile.cpp 
root@xiaotuan:~/桌面# ./a.out 
Enter the make and model of automobile: Flitz Perky
Enter the model year: 2009
Enter the original asking price: 13500
Make and model: Flitz Perky
Year: 2009
Was asking $13500.00
Now asking $12325.50
```

