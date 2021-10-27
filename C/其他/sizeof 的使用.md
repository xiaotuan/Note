如果 `sizeof` 的运算对象是类型时，必须使用圆括号将其括起来，例如：

```c
sizeof(int)
sizeof(double)
```

如果 `sizeof` 的运算对象是变量或常量时，既可以使用圆括号将其括起来，也可以不用，但推荐都使用圆括号括起来，例如：

```c
char name[40]
sizeof name
sizeof(name)
sizeof 6.28
sizeof(6.28)
```

