`switch` 语句的语法格式如下所示：

```c#
switch (表达式)
{
    case 常量表达式: 
        语句块;
        break;
        
    case 常量表达式:
        语句块;
        break;
        ....
    case 常量表达式:
        语句块;
        break;
        
    default:
        语句块;
        break;
}
```

在 `switch` 语句中，表达式的类型必须是 `sbyte`、`byte`、`short`、`ushort`、`int`、`uint`、`long`、`ulong`、`char`、`string` 或者枚举类型中的一种。

例如：

```C#
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("请输入要查询的录取分数线（比如民办本科、艺术类本科、体育类本科、二本、一本）");
        string strNum = Console.ReadLine();
        switch (strNum)
        {
            case "民办本科":
                Console.WriteLine("民办本科录取分数线：350");
                break;

            case "艺术类本科":
                Console.WriteLine("艺术类本科录取分数线：290");
                break;

            case "体育类本科":
                Console.WriteLine("体育类本科录取分数线：280");
                break;

            case "二本":
                Console.WriteLine("二本录取分数线：445");
                break;

            case "一本":
                Console.WriteLine("一本录取分数线：555");
                break;

            default:
                Console.WriteLine("你输入的查询信息有误！");
                break;
        }
    }
}
```

或者：

```C#
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("请您输入一个月份：");
        int MyMonth = int.Parse(Console.ReadLine());
        string MySeason;
        switch (MyMonth)
        {
            case 12:
            case 1:
            case 2:
                MySeason = "您输入的月份属于冬季！";
                break;

            case 3:
            case 4:
            case 5:
                MySeason = "您输入的月份属于春季！";
                break;

            case 6:
            case 7:
            case 8:
                MySeason = "您输入的月份属于夏季！";
                break;

            case 9:
            case 10:
            case 11:
                MySeason = "您输入的月份属于秋季！";
                break;

            default:
                MySeason = "月份输入错误！";
                break;
        }
        Console.WriteLine(MySeason);    
    }
}
```

