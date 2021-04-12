### 3.5.4　for/in循环

另一种for循环是for/in循环，它适用于任何可迭代的数据类型，但在大多数情况下，都将其用于数组和对象。下面的示例通过将for/in循环用于一个简单数组演示了其语法和行为：

```go
var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
for (var idx in days){
 　print("It's " + days[idx] + "\n");
}
```

注意到在循环的每次迭代中都调整了变量idx，使其从第一个数组索引依次变为最后一个索引。该循环的输出如下：

```go
It's Monday
It's Tuesday
It's Wednesday
It's Thursday
It's Friday
```

