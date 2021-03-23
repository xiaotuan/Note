#### 6.7.1　当 `Zeno` 遇到 `for` 循环

接下来，我们看看 `for` 循环和逗号运算符如何解决古老的悖论。希腊哲学家Zeno曾经提出箭永远不会达到它的目标。首先，他认为箭要到达目标距离的一半，然后再达到剩余距离的一半，然后继续到达剩余距离的一半，这样就无穷无尽。Zeno认为箭的飞行过程有无数个部分，所以要花费无数时间才能结束这一过程。不过，我们怀疑Zeno是自愿甘做靶子才会得出这样的结论。

我们采用一种定量的方法，假设箭用1秒钟走完一半的路程，然后用1/2秒走完剩余距离的一半，然后用1/4秒再走完剩余距离的一半，等等。可以用下面的无限序列来表示总时间：

```c
1 + 1/2 + 1/4 + 1/8 + 1/16 +....
```

程序清单6.14中的程序求出了序列前几项的和。变量 `power_of_two` 的值分别是 `1.0` 、 `2.0` 、 `4.0` 、 `8.0` 等。

程序清单6.14　 `zeno.c` 程序

```c
/* zeno.c -- 求序列的和 */
#include <stdio.h>
int main(void)
{
     int t_ct;       // 项计数
     double time, power_of_2;
     int limit;
     printf("Enter the number of terms you want: ");
     scanf("%d", &limit);
     for (time = 0, power_of_2 = 1, t_ct = 1; t_ct <= limit;
                                    t_ct++, power_of_2 *= 2.0)
     {
          time += 1.0 / power_of_2;
          printf("time = %f when terms = %d.\n", time, t_ct);
     }
     return 0;
}
```

下面是序列前15项的和：

```c
Enter the number of terms you want: 15
time = 1.000000 when terms = 1.
time = 1.500000 when terms = 2.
time = 1.750000 when terms = 3.
time = 1.875000 when terms = 4.
time = 1.937500 when terms = 5.
time = 1.968750 when terms = 6.
time = 1.984375 when terms = 7.
time = 1.992188 when terms = 8.
time = 1.996094 when terms = 9.
time = 1.998047 when terms = 10.
time = 1.999023 when terms = 11.
time = 1.999512 when terms = 12.
time = 1.999756 when terms = 13.
time = 1.999878 when terms = 14.
time = 1.999939 when terms = 15.

```

不难看出，尽管不断添加新的项，但是总和看起来变化不大。就像程序输出显示的那样，数学家的确证明了当项的数目接近无穷时，总和无限接近 `2.0` 。假设 `S` 表示总和，下面我们用数学的方法来证明一下：

```c
S = 1 + 1/2 + 1/4 + 1/8 + ...
```

这里的省略号表示“等等”。把 `S` 除以 `2` 得：

```c
S/2 = 1/2 + 1/4 + 1/8 + 1/16 + ...
```

第1个式子减去第2个式子得：

```c
S - S/2 = 1 +1/2 -1/2 + 1/4 -1/4 +...
```

除了第1个值为 `1` ，其他的值都是一正一负地成对出现，所以这些项都可以消去。只留下：

```c
S/2 = 1
```

然后，两侧同乘以 `2` ，得：

```c
S = 2
```

从这个示例中得到的启示是，在进行复杂的计算之前，先看看数学上是否有简单的方法可用。

程序本身是否有需要注意的地方？该程序演示了在表达式中可以使用多个逗号运算符，在 `for` 循环中，初始化了 `time` 、 `power_of_2` 和 `count` 。构建完循环条件之后，程序本身就很简短了。

