#### B.8.3　 `STDC FP_CONTRACT` 编译指示

一些浮点数处理器可以把有多个运算符的浮点表达式合并成一个运算。例如，处理器只需一步就求出下面表达式的值：

```c
x*y - z
```

这加快了运算速度，但是减少了运算的可预测性。 `STDC FP_CONTRACT` 编译指示允许用户开启或关闭这个特性。默认状态取决于实现。

为特定运算关闭合并特性，然后再开启，可以这样做：

```c
#pragma STDC FP_CONTRACT OFF
val = x * y - z;
#pragma STDC FP_CONTRACT ON
```

