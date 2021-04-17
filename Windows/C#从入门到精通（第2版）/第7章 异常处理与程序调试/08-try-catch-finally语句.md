### 7.3.2　try-catch-finally语句

除了try-catch语句，C#异常处理语句还有try-catch-finally语句，语法如下。

```c
try
{
      可能出现异常的语句序列；
}
catch(异常类型 异常对象)             
{
      对可能出现的异常进行处理；        
}
finally
{        
最后要执行的代码，进行必要的清理操作，以释放资源
}
```

与try-catch语句相比，try-catch-finally语句多了一个finally块，无论try块的语句执行过程中是否发生异常，finally块中的语句都将得到执行，finally块的执行在try块和catch块之后。finally块可以包含执行清理的代码，例如，可以在finally块中关闭在try块中打开的连接或者打开的文件。

例如，在try块中打开文件，由于发生异常导致文件未被正常关闭，则需要在finally块中关闭文件。此外，在try-catch语句后边的语句也可以放到finally块内，例7-1可以改为：

```c
01  try
02  {        
03          //打开文件
04          int x = int.Parse(Console.ReadLine());    //输入整型值
05          int y = 10;
06          int z = y / x;
07           //关闭文件
08  }
09  catch(Exception e)                      //捕获异常，参数为异常类Exception的对象e
10  {
11          Console.WriteLine(e.Message);   //输出被捕获的异常对象e的Message属性值
12  }
13  finallly
14  { 
15          //关闭文件 
16          Console.ReadKey();
17  }
```

