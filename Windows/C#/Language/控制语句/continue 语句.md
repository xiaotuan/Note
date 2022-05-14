`continue` 语句只能应用于 `while`、`do...while`、`for` 或 `foreach` 语句中，用来忽略循环语句块内位于其后面的代码而直接开始一次新的循环。当多个  `while`、`do...while`、`for` 或 `foreach` 语句嵌套时，`continue` 语句只能使直接包含它的循环语句开始一次新的循环。

```c#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        for (int i = 0; i < 4; i++)
        {
            Console.WriteLine("\n 第 {0} 次循环：", i + 1);
            for (int j = 0; j < 20; j++)
            {
                if (j % 2 == 0)
                {
                    continue;
                }
                Console.Write(j + " ");
            }
            Console.WriteLine();
        }
    }
}
```

