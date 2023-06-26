[toc]

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

> 注意：`case` 值必须是常量表达式，不允许使用变量。

在 `switch` 语句中，不能删除不同 `case` 中的 `break`。与 `C++` 和 `Java` 编程语言不同，在 `C#` 中，不支持在执行完一个 `case` 实现后自动执行另外一个 `case` 实现（即所谓的贯穿）。但是，虽然不支持自动贯穿，仍可以使用 `goto` 关键字选择另外一个 `case`，从而实现显示贯穿：

```c#
goto case 3;
```

如果多个 `case` 的实现完全相同，则可以先指定多个 `case` ，然后再指定实现：

```c#
switch (country)
{
    case "au":
    case "uk":
    case "us":
        language = "English";
        break;
    case "at":
    case "de":
        language = "German";
        break;
}
```

### 2. switch 语句的模式匹配

在 `switch` 语句中也可以使用模式匹配。下面的代码片段显示了使用常量、类型和关系模式的不同 `case` 选项：

```c#
void SwitchWithPatternMatching(object o) 
{
    switch (o) {
        case null:
            Console.WriteLine("const pattern with null");
            break; 
        case int i when i > 42:
            Console.WriteLine("type pattern with when and a relational pattern");
            break;
        case int:
            Console.WriteLine("type pattern with an int");
           	break;
        case Book b:
            Console.WriteLine($"type pattern with a Book {b.Title}");
            break;
        default:
            break;
    }
}
```

### 2. switch 表达式

接下来的示例显示了一个基于 `enum` 类型的 `switch`。`enum` 类型将整数作为基础，但为不同的值指定了名称。

```c#
enum TrafficLight
{
    Red,
    Amber,
    Green
}
```

到目前为止的 `switch` 语句只是在每个 `case` 中调用了某种操作。当使用 `return` 语句从方法返回时，也可以直接在 `case` 中返回一个值，而不继续执行其余 `case`。

```c#
TrafficLight NextLightClass(TrafficLight light)
{
    switch (light) {
        case TrafficLight.Green:
            return TrafficLight.Amber;
        case TrafficLight.Amber:
            return TrafficLight.Red;
        case TrafficLight.Red:
            return TrafficLight.Green;
        default:
            throw new InvalidOperationException();
    }
}
```

在这种场景中，如果需要基于不同的选项返回值，则可以使用 `C# 8` 新增的 `switch` 表达式。

```c#
TrafficLight NextLightClass(TrafficLight light) => 
    light switch
    {
        TrafficLight.Green => TrafficLight.Amber,
        TrafficLight.Amber => TrafficLight.Red,
        TrafficLight.Red => TrafficLight.Green,
        _ => throw new InvalidOperationException()
    };
```

如果使用 `using static` 指令导入 `enum` 类型 `TrafficLight`，则可以在使用 `enum` 值定义时不添加类型名称，从而进一步实现简化。

```c#
using static TrafficLight;

TrafficLight NextLightClass(TrafficLight light) => 
    light switch
    {
        Green => Amber,
        Amber => Red,
        Red => Green,
        _ => throw new InvalidOperationException()
    };
```

下面的示例使用了模式组合符来组合多种模式：

```c#
string? input = Console.ReadLine();

string result = input switch
{
        "one" => "the input has the value one",
        "two" or "three" => "the input has the value two or three",
        _ => "any other value"
};
```

使用模式组合符时，可以使用 `and`、`or` 和 `not` 关键字组合模式。

