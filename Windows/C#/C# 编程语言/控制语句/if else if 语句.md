`if ... else if` 语句的语法格式如下所示：

```c#
if (条件表达式1) 
{
    语句序列1
}
else if (条件表达式2)
{
    语句序列2
}
...
else if (条件表达式n)
{
    语句序列n
}
```

例如：

```c#
class Program
{
    static void Main(string[] args)
    {
        const int i = 18;
        const int j = 30;
        const int k = 50;
        int YouAge = 0;
        Console.WriteLine("请输入你的年龄：");
        YouAge = int.Parse(Console.ReadLine());
        if (YouAge <= i)
        {
            Console.WriteLine("您的年龄还小，要努力奋斗哦!");
        }
        else if (YouAge > i && YouAge <= j)
        {
            Console.WriteLine("您现在的阶段正式努力奋斗的黄金阶段！");
        }
        else if (YouAge > j && YouAge <= k)
        {
            Console.WriteLine("您现在的阶段正是人生的黄金阶段！");
        }
        else
        {
            Console.WriteLine("最美不过夕阳红！");
        }
    }
}
```

