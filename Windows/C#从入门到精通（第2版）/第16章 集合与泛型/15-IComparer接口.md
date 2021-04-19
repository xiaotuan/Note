### 16.4.1　IComparer<T>接口

泛型接口也具有一般接口的共同特点，即在接口中可以包含字段、属性、方法和索引器，但都不能够实现。泛型接口IComparer<T>定义了为比较两个对象而实现的方法。其定义如下。

```c
01  public interface IComparer<T>
02  {
03          int Compare(T x,T y);        //比较两个对象x和y的方法
04  }
```

类型参数“T”是要比较的对象的类型。Compare方法用于比较两个对象并返回一个值，指示一个对象是小于、等于还是大于另一个对象。参数x是要比较的第1个对象，y是要比较的第2个对象，均属于类型T。如果返回值大于0，则x>y；如果返回值小于0，则x<y；如果返回值等于0，则x=y。

IComparer<T>泛型接口主要的作用是作为参数传入Sort()方法，实现对象比较方式的排序。Sort方法的语法如下。

```c
public void Sort（IComparer<T> comparer）
```

在【范例16-1】中已经使用了IComparer接口实现按照客户姓名进行排序的方法，在下面的范例中，我们将改为使用IComparer<T>来实现同样的功能。

**【范例16-3】 改写范例【16-1】 ，利用List<T>编写一个管理客户地址簿的应用程序。**

（1）在Visual Studio 2013中新建C#控制台程序，项目名为“CustomerInfoList”，然后添加一个新类到项目中，类名为CustomerInfo，表示客户。其代码和【范例16-1】中的CustomerInfo.cs代码一样，只是对下面的这条语句做了些修改（代码16-3-1.txt）。

```c
private static ArrayList CustomerList = new ArrayList();
```

将上句中的ArrayList类型改为用泛型集合List来定义，改后如下。

```c
private static List<CustomerInfo> CustomerList = new List<CustomerInfo>();
```

（2）使用IComparer<T>泛型接口实现按照客户姓名进行排序的方法（代码16-3-2.txt）。

```c
01  class CustomerNameCompare : IComparer<CustomerInfo>  //按照客户姓名进行排序的方法
02  {        //自定义排序，实现IComparer接口按照客户姓名降序排序
03          public int Compare(CustomerInfo x, CustomerInfo y)        //按照客户姓名降序排序的方法
04          {
05                  return (x.Name .CompareTo(y.Name )); //返回按照客户姓名比较的结果
06          } 
07  }
```

> <img src="https://cdn.ptpress.cn/pubcloud/5B0A982E/ushu/N19937/online/FBOL6c69757cf0cda/Images/10.png" style="width:84px;  height: 95px; " width="7%" class="my_markdown"/>
> **提示**
> 在Compare方法中降序排列时使用y.CompareTo(x)写法，升序排列时使用x.CompareTo(y)写法实现。

（3）其他代码不变。

**【运行结果】**

输出结果和【范例16-1】相同。

**【范例分析】**

在【范例16-3】的步骤（1）中，CustomerInfo类中改用List<T>泛型集合类，用于存储客户的信息代替原来的ArrayList，执行的时候不需要装箱和拆箱，能提高执行的效率。

