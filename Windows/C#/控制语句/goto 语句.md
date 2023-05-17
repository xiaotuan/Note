`goto` 语句用于控制转移到由标签标记的语句。`goto` 语句可以被应用在 `switch` 语句中的 `case` 标签和 `default` 标签，以及标记语句所声明的标签。`goto` 语句的 3 种形式如下所示：

```c#
goto 标签;
goto case 参数表达式;
goto default;
```

例如：

```c#
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("请输入要查找的文字：");
        string inputstr = Console.ReadLine();
        string[] mystr = new string[5];
        mystr[0] = "支付宝";
        mystr[1] = "微信支付";
        mystr[2] = "QQ 支付";
        mystr[3] = "银联";
        mystr[4] = "京东白条";

        for (int i = 0; i < mystr.Length; i++)
        {
            if (mystr[i].Equals(inputstr))
            {
                goto Found;
            }
        }
        Console.WriteLine("您查找的 {0} 不存在！", inputstr);
        goto Finish;
    Found:
        Console.WriteLine("您查找的 {0} 存在！", inputstr);
    Finish:
        Console.WriteLine("查找完毕！");
    }
}
```

