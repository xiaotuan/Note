### 4.10.2　模板类array（C++11）

vector类的功能比数组强大，但付出的代价是效率稍低。如果您需要的是长度固定的数组，使用数组是更佳的选择，但代价是不那么方便和安全。有鉴于此，C++11新增了模板类array，它也位于名称空间std中。与数组一样，array对象的长度也是固定的，也使用栈（静态内存分配），而不是自由存储区，因此其效率与数组相同，但更方便，更安全。要创建array对象，需要包含头文件array。array对象的创建语法与vector稍有不同：

```css
#include <array>
...
using namespace std;
array<int, 5> ai; // create array object of 5 ints
array<double, 4> ad = {1.2, 2.1, 3.43. 4.3};
```

推而广之，下面的声明创建一个名为arr的array对象，它包含n_elem个类型为typename的元素：

```css
array<typeName, n_elem> arr;
```

与创建vector对象不同的是，n_elem不能是变量。

在C++11中，可将列表初始化用于vector和array对象，但在C++98中，不能对vector对象这样做。

