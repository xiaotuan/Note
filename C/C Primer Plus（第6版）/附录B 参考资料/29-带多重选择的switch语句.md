#### B.4.6　带多重选择的switch语句

**关键字：**
`switch`

**一般注解：**

程序控制根据 `expression` 的值跳转至相应的 `case` 标签处。然后，程序流执行剩下的所有语句，除非执行到 `break` 语句进行重定向。 `expression` 和 `case` 标签都必须是整数值（包括 `char` 类型），标签必须是常量或完全由常量组成的表达式。如果没有 `case` 标签与 `expression` 的值匹配，控制则转至标有 `default` 的语句（如果有的话）；否则，控制将转至紧跟在 `switch` 语句后面的语句。控制转至特定标签后，将执行 `switch` 语句中其后的所有语句，除非到达 `switch` 末尾，或执行到 `break` 语句。

**形式：**

```c
switch ( expression )
{
     case label1 : statement1//使用break跳出switch
     case label2 : statement2
     default     : statement3
}

```

可以有多个标签语句， `default` 语句可选。

**示例：**

```c
switch (value)
{
     case 1 : find_sum(ar, n);
              break;
     case 2 : show_array(ar, n);
              break;
     case 3 : puts("Goodbye!");
              break;
     default : puts("Invalid choice, try again.");
               break;
}
switch (letter)
{
     case 'a' :
     case 'e' : printf("%d is a vowel\n", letter);
     case 'c' :
     case 'n' : printf("%d is in \"cane\"\n", letter);
     default : printf("Have a nice day.\n");
}
```

如果 `letter` 的值是 `'a'` 或 `'e'` ，就打印这3条消息；如果 `letter` 的值是 `'c'` 或 `'n'` ，则只打印后两条消息； `letter` 是其他值时，值打印最后一条消息。

