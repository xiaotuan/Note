虽然 C-风格字符串和 `string` 对象的用途几乎相同，但与数组相比，`string` 对象与结构更相似。如果需要多个字符串，可以声明一个 `string` 对象数组，而不是二维 `char` 数组。

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
	cout << "Enter your " << SIZE << " favorite astronomical sights: \n";
	for (int i = 0; i < SIZE; i++)
	{
		cout << i + 1 << ": ";
		getline(cin, list[i]);
	}
	
	cout << "Your list: \n";
	display(list, SIZE);
	
	return 0;
}

void display(const string sa[], int n)
{
	for (int i = 0; i < n; i++)
		cout << i + 1 << ": " << sa[i] << endl;
}
```

运行结果如下：

```shell
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

