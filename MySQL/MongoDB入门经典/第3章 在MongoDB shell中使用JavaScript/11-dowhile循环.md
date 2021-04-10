### 3.5.2　do/while循环

另一种while循环是do/while循环，它在您要先执行循环中的代码一次，再检查表达式时很有用。

例如，下面的do/while循环将不断执行，直到day的值为Wednesday：

```go
var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
var i=0;
do{
 　var day=days[i++];
 　print("It's " + day + "\n");
} while (day != "Wednesday");
```

该循环在控制台中的输出如下：

```go
It's Monday
It's Tuesday
It's Wednesday
```

