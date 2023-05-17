`for` 语句用于计算一个初始化序列，然后当某个条件为真时，重复执行嵌套语句并计算一个迭代表达式序列；如果为假，则终止循环，退出 `for` 循环。

`for` 语句的基本形式如下所示：

```C#
for (初始化表达式; 条件表达式; 迭代表达式)
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
        int[] myint = new int[10];
        for (int i = 0; i < myint.Length; i++)
        {
            myint[i] = i;
        }
        for (int i = 0; i < myint.Length; i++)
        {
            Console.WriteLine("myint[{0}] 的值是：{1}", i, myint[i]);
        }
    }
}
```

