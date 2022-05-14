`return` 语句表示返回，当把 `return` 语句用在普通的程序代码中时，它表示返回，并且不再执行 `return` 之后的代码。

```c#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("请您输入内容：");
        string inputstr = Console.ReadLine();
        Console.WriteLine(MyStr(inputstr));
    }

    static string MyStr(string str)
    {
        string OutStr;
        OutStr = "你输入的数据是：" + str;
        return OutStr;
    }
}
```

