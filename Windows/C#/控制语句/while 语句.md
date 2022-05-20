`while` 语句的语法格式如下所示：

```c#
while (布尔表达式)
{
    语句块;
}
```

例如：

```c#
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("现在互联网主要在线支付方式：");
        string[] Players = new string[] { "支付宝", "微信支付", "QQ 支付", "银联", "京东白条" };
        int i = 0;
        while (i < Players.Length)
        {
            Console.WriteLine(Players[i]);
            i++;
        }
    }
}
```

在 `while` 语句的嵌入语句块中，`break` 语句用于将控制转到 `while` 语句的结束点，而 `continue` 语句可用于将控制直接转到下一次循环。

> 提示：在循环语句中，可以通过 `goto`、`return` 或 `throw` 语句退出。

例如：

```c#
class Program
{
    static void Main(string[] args)
    {
        int s = 0, num = 80;
        while (s < num)
        {
            s++;
            if (s > 40)
            {
                break;
            }
            if ((s % 2) == 0)
            {
                continue;
            }
            Console.WriteLine(s);
        }
    }
}
```

