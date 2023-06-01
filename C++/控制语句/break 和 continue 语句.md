`break` 和 `continue` 语句都使程序能够跳过部分代码。可以在 `switch` 语句或任何循环中使用 `break` 语句，使程序跳到 `switch` 或循环后面的语句处执行。`continue` 语句用于循环中，让程序跳过循环体中余下的代码，并开始新一轮循环。

**示例代码：jump.cpp**

```cpp
// jump.cpp -- using continue and break
#include <iostream>

const int ArSize = 80;

int main()
{
	using namespace std;
	
	char line[ArSize];
	int spaces = 0;
	
	cout << "Enter a line of text:\n";
	cin.get(line, ArSize);
	cout << "Complete line:\n" << line << endl;
	cout << "Line through first period:\n";
	for (int i = 0; line[i] != '\0'; i++)
	{
		cout << line[i];	// display character
		if (line[i] == '.')	// quit if it's a period
			break;
		if (line[i] != ' ')	// skip rest of loop
			continue;
		spaces++;
	}
	cout << "\n" << spaces << " spaces\n";
	cout << "Done.\n";
	return 0;
}
```

运行结果如下：

```shell
$ g++ jump.cpp 
$ ./a.out 
Enter a line of text:
Let's do lunch today. You can pay!
Complete line:
Let's do lunch today. You can pay!
Line through first period:
Let's do lunch today.
3 spaces
Done.
```

