`new` 运算符用于创建一个新的类型实例，它有以下 3 中形式：

+ 对象创建表达式，用于创建一个类类型或值类型的实例。
+ 数组创建表达式，用于创建一个数组类型实例。
+ 代表创建表达式，用于创建一个新的代表类型实例。

**示例：**

```c#
namespace CShapeTest
{
    class CShapeTest
    {
        static void Main(string[] args)
        {
            string[] phone = new string[5];
            phone[0] = "华为 Mate 40";
            phone[1] = "荣耀 V40";
            phone[2] = "小米11";
            phone[3] = "VIVO X60";
            phone[4] = "OPPO Reno5";
            Console.WriteLine(phone[0]);
            Console.WriteLine(phone[1]);
            Console.WriteLine(phone[2]);
            Console.WriteLine(phone[3]);
            Console.WriteLine(phone[4]);
            Console.ReadLine();
        }
    }
}
```

