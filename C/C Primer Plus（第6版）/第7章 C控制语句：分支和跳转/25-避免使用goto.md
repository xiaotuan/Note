#### 7.8.1　避免使用 `goto` 

原则上，根本不用在C程序中使用 `goto` 语句。但是，如果你曾经学过FORTRAN或BASIC（ `goto` 对这两种语言而言都必不可少），可能还会依赖用 `goto` 来编程。为了帮助你克服这个习惯，我们先概述一些使用 `goto` 的常见情况，然后再介绍C的解决方案。

+ 处理包含多条语句的 `if` 语句：

```c
if (size > 12)
     goto a;
goto b;
a: cost = cost * 1.05;
flag = 2;
b: bill = cost * flag;
```

对于以前的BASIC和FORTRAN，只有直接跟在 `if` 条件后面的一条语句才属于 `if` ，不能使用块或复合语句。我们把以上模式转换成等价的C代码，标准C用复合语句或块来处理这种情况：

```c
if (size > 12)
{
     cost = cost * 1.05;
     flag = 2;
}
bill = cost * flag;
```

+ 二选一：

```c
if (ibex > 14)
     goto a;
sheds = 2;
goto b;
a: sheds= 3;
b: help = 2 * sheds;
```

C通过 `if` 　 `else` 表达二选一更清楚：

```c
if (ibex > 14)
     sheds = 3;
else
     sheds = 2;
help = 2 * sheds;
```

实际上，新版的BASIC和FORTRAN已经把else纳入新的语法中。

+ 创建不确定循环：

```c
readin: scanf("%d", &score);
if (score < O)
    goto stage2;
lots of statements
goto readin;
stage2: more stuff;
```

C用 `while` 循环代替：

```c
scanf("%d", &score);
while (score >= 0)
{
    lots of statements
    scanf("%d", &score);
}
more stuff;
```

+ 跳转至循环末尾，并开始下一轮迭代。C使用 `continue` 语句代替。
+ 跳出循环。C使用 `break` 语句。实际上， `break` 和 `continue` 是 `goto` 的特殊形式。使用 `break` 和 `continue` 的好处是：其名称已经表明它们的用法，而且这些语句不使用标签，所以不用担心把标签放错位置导致的危险。
+ 胡乱跳转至程序的不同部分。简而言之，不要这样做！

但是，C程序员可以接受一种 `goto` 的用法——出现问题时从一组嵌套循环中跳出（一条 `break` 语句只能跳出当前循环）：

```c
while (funct > 0)
{
     for (i = 1; i <= 100; i++)
          {
          for (j = 1; j <= 50; j++)
          {
               其他语句
               if (问题)
                   goto help;
               其他语句
          }
          其他语句
     }
     其他语句
}
其他语句
help: 语句
```

从其他例子中也能看出，程序中使用其他形式比使用 `goto` 的条理更清晰。当多种情况混在一起时，这种差异更加明显。哪些 `goto` 语句可以帮助 `if` 语句？哪些可以模仿 `if` 　 `else` ？哪些控制循环？哪些是因为程序无路可走才不得已放在那里？过度地使用 `goto` 语句，会让程序错综复杂。如果不熟悉 `goto` 语句，就不要使用它。如果已经习惯使用 `goto` 语句，试着改掉这个毛病。讽刺地是，虽然C根本不需要 `goto` ，但是它的 `goto` 比其他语言的 `goto` 好用，因为C允许在标签中使用描述性的单词而不是数字。



**小结：程序跳转**

**关键字：**  `break` 、 `continue` 、 `goto`

**一般注解：**

这3种语句都能使程序流从程序的一处跳转至另一处。

`break`
**语句：**

所有的循环和 `switch` 语句都可以使用 `break` 语句。它使程序控制跳出当前循环或 `switch` 语句的剩余部分，并继续执行跟在循环或 `switch` 后面的语句。

**示例：**

```c
switch (number)
{
     case 4: printf("That's a good choice.\n");
             break;
     case 5: printf("That's a fair choice.\n");
             break;
     default: printf("That's a poor choice.\n");
}
```

`continue`
**语句：**

所有的循环都可以使用 `continue` 语句，但是 `switch` 语句不行。 `continue` 语句使程序控制跳出循环的剩余部分。对于 `while` 或 `for` 循环，程序执行到 `continue` 语句后会开始进入下一轮迭代。对于 `do` 　 `while` 循环，对出口条件求值后，如有必要会进入下一轮迭代。

**示例：**

```c
while ((ch = getchar()) != '\n')
{
     if (ch == ' ')
          continue;
     putchar(ch);
     chcount++;
}
```

以上程序段把用户输入的字符再次显示在屏幕上，并统计非空格字符。

`goto`
**语句：**

`goto` 语句使程序控制跳转至相应标签语句。冒号用于分隔标签和标签语句。标签名遵循变量命名规则。标签语句可以出现在 `goto` 的前面或后面。

**形式：**

```c
goto label ;
     .
     .
     .
label : statement

```

**示例：**

```c
top : ch = getchar();
     .
     .
     .
if (ch != 'y')
goto top;
```



