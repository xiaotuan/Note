#### B.5.1　断言： `assert.h` 

`assert.h` 头文件中把 `assert()` 定义为一个宏。在包含 `assert.h` 头文件之前定义宏标识符 `NDEBUG` ，可以禁用 `assert()` 宏。通常用一个关系表达式或逻辑表达式作为 `assert()` 的参数，如果运行正常，那么程序在执行到该点时，作为参数的表达式应该为真。表B.5.1描述了 `assert()` 宏。

<center class="my_markdown"><b class="my_markdown">表B.5.1　断言宏</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void assert(int exprs);` | 如果 `exprs` 为 `1` （或真），宏什么也不做。如果 `exprs` 为 `0` （或假）， `assert()` 就显示该表达式和其所在的行号和文件名。然后， `assert()` 调用 `abort()` |

C11新增了 `static_assert` 宏，展开为 `_Static_assert` 。 `_Static_assert` 是一个关键字，被认为是一种声明形式。它以这种方式提供一个编译时检查：

```c
_Static_assert( 常量表达式,字符串字面量);
```

如果对常量表达式求值为 `0` ，编译器会给出一条包含字符串字面量的错误消息；否则，没有任何效果。

