`if else` 语句的通用格式如下：

```cpp
if (test-condition)
    statement1
else
    statement2
```

如果测试条件为 true 或非零，则程序将执行 statement1，跳过 statement2；如果测试条件为 false 或 0，则程序将跳过 statement1。

`if else` 中的两种操作都必须是一条语句。如果需要多条语句，需要永大括号将它们括起来，组成一个块语句。

```cpp
if (ch == 'Z')
{	// if true block
    zorro++;
    cout << "Another Zorro candidate\n";
} else {	// if false block
    dull++;
    cout << "Not a Zorro candidate\n";
}
```

**示例代码：ifelse.cpp**

```cpp
// ifelse.cpp -- using the if else statement
#include <iostream>

int main()
{
	char ch;
	
	std::cout << "Type, and I shall repeat.\n";
	std::cin.get(ch);
	while (ch != '.')
	{
		if (ch == '\n')
			std::cout << ch;	// done if newline
		else
			std::cout << ++ch;	// done otherwise
		std::cin.get(ch);
	}
	// try ch + 1 instend of ++ch for interesting effect
	std::cout << "\nPlease excuse the slight confusion.\n";
	// std::cin.get();
	// std::cin.get();
	return 0;
}
```

运行结果如下：

```shell
$ g++ ifelse.cpp
$ ./a.out 
Type, and I shall repeat.
An ineffable joy suffused me as I beheld
Bo!jofggbcmf!kpz!tvggvtfe!nf!bt!J!cfifme
the wonders of modern computing.
uif!xpoefst!pg!npefso!dpnqvujoh
Please excuse the slight confusion.
```

