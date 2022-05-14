`do...while` 循环语句与 `while` 循环语句类似，它们之间的区别是：`while` 语句为先判断条件是否成立再执行循环体；而 `do...while` 循环语句则先执行一次循环后，再判断条件是否成立。也就是说 `do...while` 循环语句中 `{}` 中的程序段至少被执行一次。

`do...while` 循环语句基本形式如下所示：

```c#
do
{
    语句块;
} while(布尔表达式);
```

例如：

```c#
class Program
{
    static void Main(string[] args)
    {
        string[] MyArray = new string[3] { "世界杯", "欧洲杯", "欧冠" };
        int i = 0;
        do
        {
            Console.WriteLine(MyArray[i++]); 
        } while (i < MyArray.Length);
    }
}
```

