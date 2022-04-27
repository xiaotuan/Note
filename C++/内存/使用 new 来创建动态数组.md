[toc]

### 1. 创建动态数组

为数组分配内存的通用格式如下所示：

```cpp
type_name *pointer_name = new type_name[num_elements];
```

在 C++ 中，创建动态数组只要将数组的元素类型和元素数目告诉 `new` 即可。必须在类型名后加上方括号，其中包含元素数目。例如：

```cpp
int *psome = new int[10];	// get a block of 10 ints
```

`new` 运算符返回第一个元素的地址。当程序使用完 `new` 分配的内存块时，应使用 `delete` 释放它们。然而，对于使用 `new` 创建的数组，应使用另一种格式的 `delete` 来释放：

```cpp
delete [] psome;	// free a dynamic array
```

### 2. 使用动态数组

使用 `new` 创建的动态数组可以像使用普通数组那样使用动态数组。例如：

```cpp
// arraynew.cpp -- using the new operator for arrays
#include <iostream>

int main()
{
	using namespace std;
	double *p3 = new double[3];	// space for 3 doubles
	p3[0] = 0.2;	// treat p3 like an array name
	p3[1] = 0.5;
	p3[2] = 0.8;
	cout << "p3[1] is " << p3[1] << ".\n";
	p3 = p3 + 1;	// increment the pointer
	cout << "Now p3[0] is " << p3[0] << " and ";
	cout << "p3[1] is " << p3[1] << ".\n";
	p3 = p3 - 1;	// point back to beginning
	delete[] p3;	// free the memory
	return 0;
}
```

