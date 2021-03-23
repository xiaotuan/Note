### 7.8　 `goto` 语句

早期版本的BASIC和FORTRAN所依赖的 `goto` 语句，在C中仍然可用。但是C和其他两种语言不同，没有 `goto` 语句C程序也能运行良好。Kernighan和Ritchie提到 `goto` 语句“易被滥用”，并建议“谨慎使用，或者根本不用”。首先，介绍一下如何使用 `goto` 语句；然后，讲解为什么通常不需要它。

`goto` 语句有两部分： `goto` 和标签名。标签的命名遵循变量命名规则，如下所示：

```c
goto part2;
```

要让这条语句正常工作，函数还必须包含另一条标为 `part2` 的语句，该语句以标签名后紧跟一个冒号开始：

```c
part2: printf("Refined analysis:\n");
```

