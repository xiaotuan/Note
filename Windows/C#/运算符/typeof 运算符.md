`typeof` 运算符用于获得系统原型对象的类型，也就是 `Type` 对象。`Type` 类包含关于值类型和引用类型的信息。

**示例：**

```c#
namespace CShapeTest
{
    class CShapeTest
    {
        static void Main(string[] args)
        {
            Type mytype = typeof(string);
            Console.WriteLine("类型：{0}", mytype);
            Console.ReadLine();
        }
    }
}
```

运行结果：

```
类型：System.String
```

