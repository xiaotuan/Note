使用 `std::count` 打印消息的格式如下所示：

```cpp
std::cout << "要打印的消息";
```

例如：

```cpp
#include <iostream>

int main()
{
  using namespace std;
  cout << "Come up and C++ me some time.";
  cout << endl;
  cout << "You won't regret it!" << endl;
  return 0;
}
```

`endl` 表示换行。打印字符串时，`cout` 不会自动移到下一行。也可以使用 C 语言符号 `\n` 进行换行：

```c++
cout << "What's next?\n";	// \n means start a new line
```

`endl` 和 `\n` 的区别是：`endl` 确保程序继续运行前刷新输出，而 `\n` 不能提供这样的保证。
