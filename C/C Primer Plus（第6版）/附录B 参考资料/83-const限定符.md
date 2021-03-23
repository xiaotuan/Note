#### B.9.3　 `const` 限定符

在C中，全局的 `const` 具有外部链接，但是在C++中，具有内部链接。也就是说，下面C++的声明：

```c
const double PI = 3.14159;
```

相当于下面C中的声明：

```c
static const double PI = 3.14159;
```

假设这两条声明都在所有函数的外部。C++规则的意图是为了在头文件更加方便地使用 `const` 。如果 `const` 变量是内部链接，每个包含该头文件的文件都会获得一份 `const` 变量的备份。如果 `const` 变量是外部链接，就必须在一个文件中进行定义式声明，然后在其他文件中使用关键字 `extern` 进行引用式声明。

顺带一提，C++可以使用关键字 `extern` 使一个 `const` 值具有外部链接。所以两种语言都可以创建内部链接和外部链接的 `const` 变量。它们的区别在于默认使用哪种链接。

另外，在C++中，可以用 `const` 来声明普通数组的大小：

```c
const int ARSIZE = 100;
double loons[ARSIZE]; /* 在C++中，与double loons[100];相同 */
```

当然，也可以在C99中使用相同的声明，不过这样的声明会创建一个变长数组。

在C++中，可以使用 `const` 值来初始化其他 `const` 变量，但是在C中不能这样做：

```c
const double RATE = 0.06;            // C++和C都可以
const double STEP = 24.5;            // C++和C都可以
const double LEVEL = RATE * STEP;    // C++可以，C不可以
```

