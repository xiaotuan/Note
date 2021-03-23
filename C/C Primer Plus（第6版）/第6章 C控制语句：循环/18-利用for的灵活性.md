#### 6.5.1　利用 `for` 的灵活性

虽然 `for` 循环看上去和FORTRAN的 `DO` 循环、Pascal的 `FOR` 循环、BASIC的 `FOR...NEXT` 循环类似，但是 `for` 循环比这些循环灵活。这些灵活性源于如何使用 `for` 循环中的3个表达式。以前面程序示例中的 `for` 循环为例，第1个表达式给计数器赋初值，第2个表达式表示计数器的范围，第3个表达式递增计数器。这样使用 `for` 循环确实很像其他语言的循环。除此之外， `for` 循环还有其他9种用法。

+ 可以使用递减运算符来递减计数器：

```c
/* for_down.c */
#include <stdio.h>
int main(void)
{
     int secs;
     for (secs = 5; secs > 0; secs--)
          printf("%d seconds!\n", secs);
     printf("We have ignition!\n");
     return 0;
}
```

该程序输出如下：

```c
5 seconds!
4 seconds!
3 seconds!
2 seconds!
1 seconds!
We have ignition!
```

+ 可以让计数器递增2、10等：

```c
/* for_13s.c */
#include <stdio.h>
int main(void)
{
     int n; // 从2开始，每次递增13
     for (n = 2; n < 60; n = n + 13)
          printf("%d \n", n);
     return 0;
}
```

每次循环 `n` 递增 `13` ，程序的输出如下：

```c
 2
15
28
41
54
```

+ 可以用字符代替数字计数：

```c
/* for_char.c */
#include <stdio.h>
int main(void)
{
     char ch;
     for (ch = 'a'; ch <= 'z'; ch++)
          printf("The ASCII value for %c is %d.\n", ch, ch);
     return 0;
}
```

该程序假定系统用ASCII码表示字符。由于篇幅有限，省略了大部分输出：

```c
The ASCII value for a is 97.
The ASCII value for b is 98.
...
The ASCII value for x is 120.
The ASCII value for y is 121.
The ASCII value for z is 122.
```

该程序能正常运行是因为字符在内部是以整数形式存储的，因此该循环实际上仍是用整数来计数。

+ 除了测试迭代次数外，还可以测试其他条件。在for_cube程序中，可以把：

```c
for (num = 1; num <= 6; num++)
```

替换成：

```c
for (num = 1; num*num*num <= 216; num++)
```

如果与控制循环次数相比，你更关心限制立方的大小，就可以使用这样的测试条件。

+ 可以让递增的量几何增长，而不是算术增长。也就是说，每次都乘上而不是加上一个固定的量：

```c
/* for_geo.c */
#include <stdio.h>
int main(void)
{
     double debt;
     for (debt = 100.0; debt < 150.0; debt = debt * 1.1)
          printf("Your debt is now $%.2f.\n", debt);
     return 0;
}
```

该程序中，每次循环都把 `debt` 乘以 `1.1` ，即 `debt` 的值每次都增加 `10%` ，其输出如下：

```c
Your debt is now $100.00.
Your debt is now $110.00.
Your debt is now $121.00.
Your debt is now $133.10.
Your debt is now $146.41.
```

+ 第3个表达式可以使用任意合法的表达式。无论是什么表达式，每次迭代都会更新该表达式的值。

```c
/* for_wild.c */
#include <stdio.h>
int main(void)
{
     int x;
     int y = 55;
     for (x = 1; y <= 75; y = (++x * 5) + 50)
          printf("%10d %10d\n", x, y);
     return 0;
}
```

该循环打印 `x` 的值和表达式 `++x * 5 + 50` 的值，程序的输出如下：

```c
1           55
2           60
3           65
4           70
5           75
```

注意，测试涉及 `y` ，而不是 `x` 。 `for` 循环中的3个表达式可以是不同的变量（注意，虽然该例可以正常运行，但是编程风格不太好。如果不在更新部分加入代数计算，程序会更加清楚）。

+ 可以省略一个或多个表达式（但是不能省略分号），只要在循环中包含能结束循环的语句即可。

```c
/* for_none.c */
#include <stdio.h>
int main(void)
{
     int ans, n;
     ans = 2;
     for (n = 3; ans <= 25;)
          ans = ans * n;
     printf("n = %d; ans = %d.\n", n, ans);
     return 0;
}
```

该程序的输出如下：

```c
n = 3; ans = 54.
```

该循环保持 `n` 的值为 `3` 。变量 `ans` 开始的值为 `2` ，然后递增到 `6` 和 `18` ，最终是 `54` （ `18` 比 `25` 小，所以 `for` 循环进入下一次迭代， `18` 乘以 `3` 得 `54` ）。顺带一提，省略第2个表达式被视为真，所以下面的循环会一直运行：

```c
for (; ; )
     printf("I want some action\n");
```

+ 第1个表达式不一定是给变量赋初值，也可以使用 `printf()` 。记住，在执行循环的其他部分之前，只对第1个表达式求值一次或执行一次。

```c
/* for_show.c */
#include <stdio.h>
int main(void)
{
     int num = 0;
     for (printf("Keep entering numbers!\n"); num != 6;)
          scanf("%d", &num);
     printf("That's the one I want!\n");
     return 0;
}
```

该程序打印第1行的句子一次，在用户输入 `6` 之前不断接受数字：

```c
Keep entering numbers!
3
5
8
6
That's the one I want!

```

+ 循环体中的行为可以改变循环头中的表达式。例如，假设创建了下面的循环：

```c
for (n = 1; n < 10000; n = n + delta)
```

如果程序经过几次迭代后发现 `delta` 太小或太大，循环中的 `if` 语句（详见第7章）可以改变 `delta` 的大小。在交互式程序中，用户可以在循环运行时才改变 `delta` 的值。这样做也有危险的一面，例如，把 `delta` 设置为 `0` 就没用了。

总而言之，可以自己决定如何使用 `for` 循环头中的表达式，这使得在执行固定次数的循环外，还可以做更多的事情。接下来，我们将简要讨论一些运算符，使 `for` 循环更加有用。



**小结： `for` 语句**

**关键字：**
`for`

**一般注解：**

`for` 语句使用3个表达式控制循环过程，分别用分号隔开。 `initialize` 表达式在执行 `for` 语句之前只执行一次；然后对 `test` 表达式求值，如果表达式为真（或非零），执行循环一次；接着对 `update` 表达式求值，并再次检查 `test` 表达式。 `for` 语句是一种入口条件循环，即在执行循环之前就决定了是否执行循环。因此， `for` 循环可能一次都不执行。 `statement` 部分可以是一条简单语句或复合语句。

**形式：**

`for ( initialize; test; update )`

`statement`

在`test`为假或0之前，重复执行`statement`部分。

**示例：**

```c
for (n = 0; n < 10 ; n++)
     printf(" %d %d\n", n, 2 * n + 1);
```



