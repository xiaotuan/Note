#### 4.3.1　 `const` 限定符

`C90` 标准新增了 `const` 关键字，用于限定一个变量为只读<sup class="my_markdown">[2]</sup>。其声明如下：

```c
const int MONTHS = 12; // MONTHS在程序中不可更改，值为12
```

这使得 `MONTHS` 成为一个只读值。也就是说，可以在计算中使用 `MONTHS` ，可以打印 `MONTHS` ，但是不能更改 `MONTHS` 的值。 `const` 用起来比 `#define` 更灵活，第 `12` 章将讨论与 `const` 相关的内容。

