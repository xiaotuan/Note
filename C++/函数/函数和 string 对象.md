下面是一个使用 `string` 对象数组的函数示例代码：

**程序清单 topfive.cpp**

```cpp
// topfive.cpp -- handling an array of string objects
#include <iostream>
#include <string>

using namespace std;

const int SIZE = 5;

void display(const string sa[], int n);

int main()
{
	string list[SIZE];	// an array holding 5 string object
	cout << "Enter your " << SIZE << " favorite astronomical sights:\n";
	for (int i = 0; i < SIZE; i++) 
	{
		cout << i + 1 << ": ";
		getline(cin, list[i]);
	}
	
	cout << "Your list:\n";
	display(list, SIZE);
	
	return 0;
}

void display(const string sa[], int n)
{
	for (int i = 0; i  < n; i++)
	{
		cout << i + 1 << ": " << sa[i] << endl;
	}
}
```

运行结果如下：

```
$ g++ topfive.cpp 
$ ./a.out 
Enter your 5 favorite astronomical sights:
1: Orion Nebula 
2: M13
3: Saturn
4: Jupiter
5: Moon
Your list:
1: Orion Nebula
2: M13
3: Saturn
4: Jupiter
5: Moon
```

