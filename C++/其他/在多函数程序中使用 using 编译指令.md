可以通过将编译指令放在函数的外面，且位于需要使用该命名空间的所有函数的前面，来使所有函数都可以访问该命名空间，例如：

```c++
// ourfunc1.cpp -- repositioning the using directive

#include <iostream>

using namespace std;	// affects all function definitions in this file

void simon(int);

int main()
{
	simon(3);
	cout << "Pick an integer: ";
	int count;
	cin >> count;
	simon(count);
	cout << "Done!" << endl;
	return 0;
}

void simon(int n)
{
	cout << "Simon says touch your toes " << n << " times." << endl;
}
```

