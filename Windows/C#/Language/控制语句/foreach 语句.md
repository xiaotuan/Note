`foreach` 语句用于枚举一个集合的元素，并对该集合中的每个元素执行一次嵌入语句。但是 `foreach` 语句不应用于更改集合内容，以避免产生不可预知的错误。

`foreach` 语句的基本形式如下所示：

```c#
foreach(类型 迭代变量名 in 集合类型表达式)
{
    语句块;
}
```

例如：

```C#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        ArrayList alt = new ArrayList();
        alt.Add("流浪地球");
        alt.Add("疯狂的外星人");
        alt.Add("飞驰人生");
        alt.Add("新喜剧之王");
        alt.Add("廉政风云");
        Console.WriteLine("2019 春节档热门上映电影: ");
        foreach (string InternetName in alt)
        {
            Console.WriteLine(InternetName);
        }
    }
}
```

