使用 `using` 指令引入命名空间的基本形式为：

```c#
using 命名空间名;
```

例如：

```c#
using N1;   // 使用 using 指令引入命名空间 N1

namespace Test02
{
    class Program
    {
        static void Main(string[] args)
        {
            A oa = new A(); // 实例化 N1 中的类 A
            oa.MyIs();  // 调用类 A 中的 MyIs() 方法
        }
    }
}

namespace N1    // 建立命名空间 N1
{
    class A // 实例化命名空间 N1 中的类 A
    {
        public void MyIs()
        {
            Console.WriteLine("吴京登顶中国电影票房第一人"); // 输出字符串
            Console.WriteLine();
        }
    }
}
```

使用 `using` 语句引用静态方法或变量的格式如下：

```c#
using static 名称空间.静态方法或变量;
```

例如：

```c#
using static System.Console;
```

