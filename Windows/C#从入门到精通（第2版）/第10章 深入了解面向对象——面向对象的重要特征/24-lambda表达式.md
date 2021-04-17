### 10.6.2　lambda表达式

lambda 表达式是一种可用于创建委托或表达式目录树类型的匿名函数。 通过使用 lambda 表达式，可以写入可作为参数传递或作为函数调用值返回的本地函数。lambda 表达式对于编写 LINQ 查询表达式特别有用。若要创建lambda 表达式，需要在lambda 运算符 => 左侧指定输入参数（如果有），然后在另一侧输入表达式或语句块。

**【范例10-6】 lambda 表达式 x => x * x 指定名为 x 的参数并返回x 的平方值。 代码10-6-1.txt展示如何将此表达式分配给委托类型。**

```c
01  using System.Linq.Expressions;
02  namespace ConsoleApplication1
03  {
04          class Program
05          {
06                  static void Main(string[] args)
07                  {
08                          Expression<del> myET = x => x * x;
09                  }
10          }
11  }
```

**【范例分析】**

在【范例10-6】中，请注意委托签名具有一个 int 类型的隐式类型输入参数，并返回 int。 可以将 lambda 表达式转换为该类型的委托，因为该表达式也具有一个输入参数 (x)，以及一个编译器可隐式转换为 int 类型的返回值。使用输入参数“5”调用委托时，它将返回结果“25”。

表达式位于 => 运算符右侧的 lambda 表达式称为“表达式 lambda”。 表达式 lambda 广泛用于表达式树（C# 和 Visual Basic）的构造。 表达式 lambda 会返回表达式的结果，并采用以下基本形式。

```c
(input parameters) => expression;
```

仅当 lambda 只有一个输入参数时，括号才是可选的。否则括号是必需的。使用空括号指定零个输入参数，括号内的两个或更多输入参数使用逗号加以分隔。当编译器难以或无法推断输入类型时，需要显式地指定类型。

语句 lambda 与表达式 lambda 表达式类似，只是语句括在大括号中。

```c
 (input parameters) => {statement;}
```

通过使用 async 和 await 关键字，可以轻松创建包含异步处理的 lambda 表达式和语句。

**【范例10-7】 Windows 窗体示例包含一个调用和等待异步方法 ExampleMethodAsync 的事件处理程序。**

```c
01  public partial class Form1 : Form
02  {
03      public Form1()
04      {
05          InitializeComponent();
06      }
07      private async void button1_Click(object sender, EventArgs e)
08      {
09          await ExampleMethodAsync();// ExampleMethodAsync returns a Task.
10          textBox1.Text += "\r\nControl returned to Click event handler.\r\n";
11      }
12      async Task ExampleMethodAsync()
13      {
14          await Task.Delay(1000); // 模拟异步进程的任务返回
15      }
16  }
```

**【拓展训练】**

修改【范例10-4】，使用lambda（拓展代码10-4-1.txt）表达式实现委托，进行数组排序。代码如下，运行结果不变。

```c
01  public delegate bool SortDelegate(int[] x);                  //定义委托SortDelegate
02  static void Main(string[] args)
03  {
04          int[] arr = new int[] { 8, 9, 5, 7, 2, 1, 4, 5, 6 }; //待排序的数组
05          Console.WriteLine("排序前的数组元素是");
06          foreach (int i in arr)
07          {  Console.Write("{0}  ", i);  }            //输出排序前的数组元素，以便进行比较
08                  // 用lambda表达式实例化委托
09                  SortDelegate mydelegate = array=>{  //匿名委托{}中的代码实现排序
10                          for (int i = array.GetUpperBound(0); i >= 0; i--)//循环实现冒泡排序
11                          {         //冒泡排序
12                                  for (int j = 0; j <= i; j++)
13                                  if (array[j] <= array[i])
14                                  { //如果array[j] 不大于array[i]，再交换二者的值
15                                          int temp = array[j];
16                                          array[j] = array[i];
17                                          array[i] = temp;
18                                  }
19                          }
20                          return true;
21                  };
22          mydelegate(arr);                            //调用委托进行排序
23          Console.WriteLine("排序后的数组元素是");
24          foreach (int i in arr)                      //输出排序后的数组元素
25          {Console.Write("{0}  ", i);  }
26  }
```

第9行使用lambda表达式实现委托执行冒泡排序算法，运行结果不变。

