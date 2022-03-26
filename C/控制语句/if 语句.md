if 语句的通用形式如下所示：

```c
if (expression) {
    statement
}
```

如果对 expression 求值为真（非 0），则执行 statement；否则，跳过 statement。与 while 循环一样，statement 可以是一条简单语句或复合语句。例如：

```c
if (score > big) 
    printf("Jackpot!\n");	// 简单语句

if (joe > ron) {	// 复合语句
    joecash++;
    printf("You lose, Ron.\n");
}
```

