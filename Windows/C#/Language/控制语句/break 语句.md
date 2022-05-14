[toc]

`break` 语句只能应用在 `switch`、`while`、`do...while`、`for` 或 `foreach` 语句中，当多个 `switch`、`while`、`do...while`、`for` 或 `foreach` 语句互相嵌套时，`break` 语句只应用于最里层的语句。如果要穿越多个嵌套层，则必须使用 `goto` 语句。

### 1. break 语句在 switch 语句中的应用

```C#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        int i = Convert.ToInt32(DateTime.Today.DayOfWeek);
        switch (i)
        {
            case 1:
                Console.WriteLine("今天是星期一");
                break;

            case 2:
                Console.WriteLine("今天是星期二");
                break;

            case 3:
                Console.WriteLine("今天是星期三");
                break;

            case 4:
                Console.WriteLine("今天是星期四");
                break;

            case 5:
                Console.WriteLine("今天是星期五");
                break;

            case 6:
                Console.WriteLine("今天是星期六");
                break;

            case 0:
                Console.WriteLine("今天是星期日");
                break;
        }
    }
}
```

### 2. break 语句在 for 语句中的应用

```c#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        for (int i = 0; i < 4; i++)
        {
            Console.WriteLine("\n 第 {0} 次循环：", i + 1);
            for (int j = 0; j < 200; j++)
            {
                if (j == 12)
                {
                    break;
                }
                Console.Write(j + " ");
            }
        }
    }
}
```



