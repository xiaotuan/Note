### 3.1.9　bool类型

ANSI/ISO C++标准添加了一种名叫bool的新类型（对C++来说是新的）。它的名称来源于英国数学家George Boole，是他开发了逻辑律的数学表示法。在计算中，布尔变量的值可以是true或false。过去，C++和C一样，也没有布尔类型。在第5章和第6章中将会看到，C++将非零值解释为true，将零解释为false。然而，现在可以使用bool类型来表示真和假了，它们分别用预定义的字面值true和false表示。也就是说，可以这样编写语句：

```css
bool is_ready = true;
```

字面值true和false都可以通过提升转换为int类型，true被转换为1，而false被转换为0：

```css
int ans = true; // ans assigned 1
int promise = false; // promise assigned 0
```

另外，任何数字值或指针值都可以被隐式转换（即不用显式强制转换）为bool值。任何非零值都被转换为true，而零被转换为false：

```css
bool start = -100; // start assigned true
bool stop = 0; // stop assigned false
```

在第6章介绍if语句后，示例中将经常使用数据类型bool。

