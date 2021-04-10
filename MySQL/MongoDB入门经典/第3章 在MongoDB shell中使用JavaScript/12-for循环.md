### 3.5.3　for循环

JavaScript for循环让您能够使用一条for语句执行代码指定的次数。for语句将三条语句合并成一个代码块，其语法如下：

```go
for (assignment; condition; update;){
 　code to be executed;
}
```

执行循环时，for语句这样使用这三条语句。

+ assignment：只在循环开始时执行，以后不再执行。这条语句用于初始化在循环中用作条件的变量。
+ condition：在循环的每次迭代中都检查。如果为true，就执行循环，否则结束循环。
+ update：在每次迭代中，在循环中的代码执行完毕后都执行它。这条语句通常递增condition语句使用的计数器。

下面的示例演示了for循环。它不仅演示了基本的for循环，还演示了可将一个循环嵌套在另一个循环中：

```go
for (var x=1; x<=3; x++){
 　for (var y=1; y<=3; y++){
 　 　print(x + " X " + y + " = " + (x*y) + "\n");
 　}
}
```

这个循环在控制台中的输出如下：

```go
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
```

