[toc]

### 1. StringBuilder 类的定义

`StringBuilder` 类有 6 种不同的构造方法，其中一种语法格式如下所示：

```c#
using System.Text;

public StringBuilder(string value, int cap);
```

+ value：`StringBuilder` 对象引用的字符串。
+ cap：设定 `StringBuilder` 对象的初始大小。

### 2. String Builder 类的使用

`StringBuilder` 类存在于 `System.Text` 命名空间中，如果要创建 `StringBuilder` 对象，首先必须引用此命名空间。

<center><b>StringBuilder 类中常用的方法及说明</b></center>

| 方法         | 说明                                                      |
| ------------ | --------------------------------------------------------- |
| Append       | 将文本或字符串追加到指定对象的末尾                        |
| AppendFormat | 自定义变量的格式并将这些值追加到 StringBuilder 对象的末尾 |
| Insert       | 将字符串或对象添加当前 StringBuilder 对象中的指定位置     |
| Remove       | 从当前 StringBuilder 对象中移除指定数量的字符             |
| Replace      | 用另一个指定的字符来替换 StringBuilder 对象内的字符       |

例如：

```C#
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int Num = 1000;
        StringBuilder honorvsiaomi = new StringBuilder("荣耀自称科技标杆", 100);
        honorvsiaomi.Append("VS 小米死磕高性价比");
        Console.WriteLine(honorvsiaomi.ToString());
        honorvsiaomi.AppendFormat("{0:C}", Num);
        honorvsiaomi.Insert(0, "PK: ");
        Console.WriteLine(honorvsiaomi.ToString());
        honorvsiaomi.Remove(21, honorvsiaomi.Length - 21);
        Console.WriteLine(honorvsiaomi.ToString());
        honorvsiaomi.Replace("PK", "相爱相杀");
        Console.WriteLine(honorvsiaomi.ToString());
    }
}
```

