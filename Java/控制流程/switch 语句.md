[toc]

### 1. switch 语句

在处理多个选项时，可以使用 `switch` 语句，例如：

```java
Scanner in = new Scanner(System.in);
System.out.print("Select an option (1, 2, 3, 4) ");
int choice = in.nextInt();
switch (choice) {
    case 1:
        ...
        break;
      
    case 2:
        ...
        break;
    
    case 3:
        ...
        break;
       
    case 4:
        ...
        break;
        
    default:
        // bad input
        ....
        break;
}
```

`switch` 语句将从与选项值相匹配的 `case` 标签处开始执行直到遇到 `break` 语句，或者执行到 `switch` 语句的结束处为止。如果没有相匹配的 `case` 标签，而有 `default` 子句，就执行这个子句。

> 提示
>
> 有可能触发多个 `case` 分支。如果在 `case` 分支语句的末尾没有 `break` 语句，那么就会接着执行下一个 `case` 分支语句。

### 2. case 标签的值

`case` 标签可以是：

+ 类型为 char、byte、short 或 int 的常量表达式
+ 枚举常量
+ 从 Java SE 7 开始，case 标签还可以是字符串字面量。

当 `switch` 语句中使用枚举常量时，不必在每个标签中指明枚举名，可以由 `switch` 的表达式值确定。例如：

```java
Size sz = ...;
switch (sz) {
    case SMALL:	// no need to use Size.SMALL
        ...
        break;
        
    ...
}
```

