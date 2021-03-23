#### 7.2.3　多重选择 `else` 　 `if` 

现实生活中我们经常有多种选择。在程序中也可以用 `else` 　 `if` 扩展 `if` 　 `else` 结构模拟这种情况。来看一个特殊的例子。电力公司通常根据客户的总用电量来决定电费。下面是某电力公司的电费清单，单位是千瓦时（kWh）：

```c
首 360kWh:         $0.13230/kWh
续 108kWh:         $0.15040/kWh
续 252kWh:         $0.30025/kWh
超过 720kWh:       $0.34025/kWh
```

如果对用电管理感兴趣，可以编写一个计算电费的程序。程序清单7.4是完成这一任务的第1步。

程序清单7.4　 `electric.c` 程序

```c
// electric.c -- 计算电费
#include <stdio.h>
#define RATE1   0.13230               // 首次使用 360 kwh 的费率
#define RATE2   0.15040               // 接着再使用 108 kwh 的费率
#define RATE3   0.30025               // 接着再使用 252 kwh 的费率
#define RATE4   0.34025               // 使用超过 720kwh 的费率
#define BREAK1  360.0                 // 费率的第1个分界点
#define BREAK2  468.0                 // 费率的第2个分界点
#define BREAK3  720.0                 // 费率的第3个分界点
#define BASE1   (RATE1 * BREAK1)      // 使用360kwh的费用
#define BASE2  (BASE1 + (RATE2 * (BREAK2 - BREAK1)))   // 使用468kwh的费用
#define BASE3  (BASE2 + (RATE3 *(BREAK3 - BREAK2)))    // 使用720kwh的费用
int main(void)
{
     double kwh;                       // 使用的千瓦时
     double bill;                      // 电费
     printf("Please enter the kwh used.\n");
     scanf("%lf", &kwh);               // %lf对应double类型
     if (kwh <= BREAK1)
          bill = RATE1 * kwh;
     else if (kwh <= BREAK2)           // 360～468 kwh    
          bill = BASE1 + (RATE2 * (kwh - BREAK1));
     else if (kwh <= BREAK3)           // 468～720 kwh
          bill = BASE2 + (RATE3 * (kwh - BREAK2));
     else                              // 超过 720 kwh               
          bill = BASE3 + (RATE4 * (kwh - BREAK3));
     printf("The charge for %.1f kwh is $%1.2f.\n", kwh, bill);
     return 0;
}
```

该程序的输出示例如下：

```c
Please enter the kwh used.
580
The charge for 580.0 kwh is $97.50.

```

程序清单7.4用符号常量表示不同的费率和费率分界点，以便把常量统一放在一处。这样，电力公司在更改费率以及费率分界点时，更新数据非常方便。 `BASE1` 和 `BASE2` 根据费率和费率分界点来表示。一旦费率或分界点发生了变化，它们也会自动更新。预处理器是不进行计算的。程序中出现 `BASE1` 的地方都会被替换成 `0.13230` * `360.0` 。不用担心，编译器会对该表达式求值得到一个数值（ `47.628` ），以便最终的程序代码使用的是 `47.628` 而不是一个计算式。

程序流简单明了。该程序根据 `kwh` 的值在3个公式之间选择一个。特别要注意的是，如果 `kwh` 大于 `360` ，程序只会到达第1个 `else` 。因此， `else` 　 `if (kwh <= BREAK2)` 这行相当于要求 `kwh` 在 `360` ～ `482` 之间，如程序注释所示。类似地，只有当 `kwh` 的值超过 `720` 时，才会执行最后的 `else` 。最后，注意 `BASE1` 、 `BASE2` 和 `BASE3` 分别代表 `360` 、 `468` 和 `720` 千瓦时的总费用。因此，当电量超过这些值时，只需要加上额外的费用即可。

实际上， `else` 　 `if` 是已学过的 `if` 　 `else` 语句的变式。例如，该程序的核心部分只不过是下面代码的另一种写法：

```c
if (kwh <= BREAK1)
     bill = RATE1 * kwh;
else
     if (kwh <= BREAK2)            // 360～468 kwh
          bill = BASE1 + (RATE2 * (kwh - BREAK1));
     else    
          if (kwh <= BREAK3)        // 468～720 kwh
               bill = BASE2 + (RATE3 * (kwh - BREAK2));
          else                      // 超过720 kwh
               bill = BASE3 + (RATE4 * (kwh - BREAK3));
```

也就是说，该程序由一个 `if else` 语句组成， `else` 部分包含另一个 `if else` 语句，该 `if else` 语句的 `else` 部分又包含另一个 `if else` 语句。第2个 `if else` 语句嵌套在第 1个 `if` 　 `else` 语句中，第3个 `if` 　 `else` 语句嵌套在第2个 `if` 　 `else` 语句中。回忆一下，整个 `if` 　 `else` 语句被视为一条语句，因此不必把嵌套的 `if` 　 `else` 语句用花括号括起来。当然，花括号可以更清楚地表明这种特殊格式的含义。

这两种形式完全等价。唯一不同的是使用空格和换行的位置不同，不过编译器会忽略这些。尽管如此，第1种形式还是好些，因为这种形式更清楚地显示了有4种选择。在浏览程序时，这种形式让读者更容易看清楚各项选择。在需要时要缩进嵌套的部分，例如，必须测试两个单独的量时。本例中，仅在夏季对用电量超过720kWh的用户加收10%的电费，就属于这种情况。

可以把多个 `else` 　 `if` 语句连成一串使用，如下所示（当然，要在编译器的限制范围内）：

```c
if (score < 1000)
     bonus = 0;
else if (score < 1500)
     bonus = 1;
else if (score < 2000)
     bonus = 2;
else if (score < 2500)
     bonus = 4;
else
     bonus = 6;
```

（这可能是一个游戏程序的一部分， `bonus` 表示下一局游戏获得的光子炸弹或补给。）

对于编译器的限制范围，C99标准要求编译器最少支持127层套嵌。

