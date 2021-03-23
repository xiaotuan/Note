### 12.5　ANSI C类型限定符

我们通常用类型和存储类别来描述一个变量。C90还新增了两个属性：恒常性（constancy）和易变性（volatility）。这两个属性可以分别用关键字 `const` 和 `volatile` 来声明，以这两个关键字创建的类型是限定类型（qualified type）。C99标准新增了第3个限定符： `restrict` ，用于提高编译器优化。C11标准新增了第4个限定符： `_Atomic` 。C11提供一个可选库，由 `stdatomic.h` 管理，以支持并发程序设计，而且 `_Atomic` 是可选支持项。

C99为类型限定符增加了一个新属性：它们现在是幂等的（idempotent）！这个属性听起来很强大，其实意思是可以在一条声明中多次使用同一个限定符，多余的限定符将被忽略：

```c
const const const int n = 6; // 与 const int n = 6;相同
```

有了这个新属性，就可以编写类似下面的代码：

```c
typedef const int zip;
const zip q = 8;
```

