下面来看一个使用 `C++11` 模板类 `array` 的例子。

假设你要使用一个 `array` 对象来存储一年四个季度的开支：

```cpp
std::array<double, 4> expenses;
```

要使用 `array` 类，需要包含头文件 `array`，而名称 `array` 位于名称空间 `std` 中。如果函数来显示 `expenses` 的内容，可按值传递 `expenses`：

```cpp
show(expenses);
```

但如果函数要修改对象 `expenses`，则需要将该对象的地址传递给函数：

```cpp
fill(&expenses);
```

如何声明这两个函数呢？`expenses` 类型为 `array<double, 4>`，因此必须在函数原型中指定这种类型：

```cpp
void show(std::array<double, 4> da);	// da an object
void fill(std::array<double, 4) * pa);	// pa a pointer to an object
```

该程序还包含其他一些功能。首先，它用符号常量替换了 4：

```cpp
const int Seasons = 4;
```

其次，它使用了一个 `const array` 对象，该对象包含 4 个 `string` 对象，用于表示几个季度：

```cpp
const std::array<std::string, Seasons> Snames = 
{"Spring", "Summer", "Fall", "Winter" };
```

**程序清单 arrobj.cpp**

```cpp
// arrobj.cpp -- functions with array objects (C++11)
#include <iostream>
#include <array>
#include <string>

// constant data
const int Seasons = 4;
const std::array<std::string, Seasons> Snames = 
	{ "Spring", "Summer", "Fall", "Winter" };

// function to modify array object
void fill(std::array<double, Seasons> * pa);
// function that uses array object without modifying it
void show(std::array<double, Seasons> da);

int main()
{
	std::array<double, Seasons> expenses;
	fill(&expenses);
	show(expenses);
	return 0;
}

void fill(std::array<double, Seasons> * pa)
{
	using namespace std;
	for (int i = 0; i < Seasons; i++)
	{
		cout << "Enter " << Snames[i] << " expenses: ";
		cin >> (*pa)[i];
	}
}

void show(std::array<double, Seasons> da)
{
	using namespace std;
	double total = 0.0;
	cout << "\nEXPENSES\n";
	for (int i = 0; i < Seasons; i++) 
	{
		cout << Snames[i] << ": $" << da[i] << endl;
		total += da[i];
	}
	cout << "Total Expenses: $" << total << endl;
}
```

运行结果如下：

```shell
$ g++ ./arrobj.cpp -std=c++11 
$ ./a.out 
Enter Spring expenses: 212
Enter Summer expenses: 256
Enter Fall expenses: 208
Enter Winter expenses: 244

EXPENSES
Spring: $212
Summer: $256
Fall: $208
Winter: $244
Total Expenses: $920
```

