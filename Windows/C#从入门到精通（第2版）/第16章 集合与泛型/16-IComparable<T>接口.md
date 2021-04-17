### 16.4.2　IComparable<T>接口

IComparable<T>也是常用的泛型接口。泛型接口IComparable<T>的功能和接口IComparable相似，规定了一个没有实现的方法CompareTo(Object obj)，语法如下。

```c
public interface IComparable
{
        int CompareTo(Object obj) ;
}
```

此接口中的CompareTo用于比较对象的大小。如果一个类实现了该接口中的这个方法，说明这个类的对象是可以比较大小的。如果当前对象小于obj，返回值小于0；如果当前对象大于obj，返回值大于0；如果当前对象等于obj，返回值等于0。

**【范例16-4】 使用IComparable<T>实现比较对象的大小的功能。**

（1）新建控制台程序，项目名为“CustomerInfoListExt”，然后添加一个新类到项目中，类名为CustomerInfo，表示客户信息并实现IComparable接口（代码16-4-1.txt）。

```c
01  class CustomerInfo:IComparable<CustomerInfo>  //实现IComparable接口的类CustomerInfo
02  {        
03         private String id;             //表示客户ID的字段
04         private String name;           //表示客户姓名的字段
05         private String address;        //表示客户地址的字段
06         public CustomerInfo() { }      //无参数构造函数
07         public CustomerInfo(String myid, string myname, string myaddress)
08         {        //有参数构造函数
09             id = myid;
10             name = myname;
11             address = myaddress;
12         }
13         public String ID              //表示客户ID的属性
14         {
15             set { id = value; }
16             get { return id; }
17         }
18         public String Name           //表示客户姓名的属性
19         {
20             get { return name; }
21             set { name = value; }
22         }
23         public String Address        //表示客户地址的属性
24         {
25             get { return address; }
26             set { address = value; }
27         } 
28         public int CompareTo(CustomerInfo objCustomer)       //按照姓名比较对象大小的方法
29         {     //实现IComparable<T>的比较方法，按照姓名比较对象大小
30             return this.Name .CompareTo (objCustomer.Name ); //返回按照姓名比较的结果
31         }
32  }
```

（2）在Program的Main中添加以下测试代码（代码16-4-2.txt）并测试。

```c
01  //实例化CustomerInfo，向List<T>中添加对象
02  CustomerInfo aCustomerInfo1 = new CustomerInfo(“Id0001”, “李四", "河南郑州市");
03  CustomerInfo aCustomerInfo2 = new CustomerInfo("Id0002", "王五", "湖南长沙市");
04  if (aCustomerInfo1 .CompareTo (aCustomerInfo2 )>0)   //按照姓名比较两个对象的大小
05         Console .WriteLine ("{0}的姓名比{1}的姓名排列靠前",aCustomerInfo1.Name ,
            aCustomerInfo2.Name );
06  else 
07          Console .WriteLine ("{0}的姓名比{1}的姓名排列靠前后",aCustomerInfo1.Name ,
            aCustomerInfo2.Name );
08  Console.ReadKey();
```

**【运行结果】**

单击工具栏中的<img src="https://cdn.ptpress.cn/pubcloud/5B0A982E/ushu/N19937/online/FBOL6c69757cf0cda/Images/300.png" style="width:24px;  height: 22px; " width="16" class="my_markdown"/>
按钮，输出结果如下图所示。

![301.png](../images/301.png)
