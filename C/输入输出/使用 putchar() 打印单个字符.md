`putchar()` 函数打印它的参数。例如，下面的语句把字符变量 ch 的值作为字符打印出来：

```c
char ch = getchar();
putchar(ch);
```

该语句与下面的语句效果相同：

```c
char ch = getchar();
printf("%c", ch);
```

