### 附录B　sort函数

我们可以利用C++中的排序函数sort，对古董的重量进行从小到大排序。要使用此函数，只需引入头文件：

```c
#include <algorithm>
```

语法描述为：

```c
sort(begin, end)// 参数begin, end表示一个范围，分别为待排序数组的首地址和尾地址。
```

例如：

```c
//mysort1
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
 int a[10]={7,4,5,23,2,73,41,52,28,60},i;
 for(i=0;i<10;i++)
   cout<<a[i]<<" ";
 cout<<endl;
 sort(a,a+10);
 for(i=0;i<10;i++)
  cout<<a[i]<<" ";
 return 0;
}
```

输出结果为：

```c
7 4 5 23 2 73 41 52 28 60
2 4 5 7 23 28 41 52 60 73
```

sort（a，a+10）将把数组a按升序排序，因为sort函数默认为升序。可能有人会问：怎么样用它降序排列呢？这就是下一个讨论的内容。

（1）自己编写compare函数

一种是自己编写一个比较函数来实现，接着调用含3个参数的sort：

```c
sort(begin,end,compare) //两个分别为待排序数组的首地址和尾地址。
//最后一个参数compare表示比较的类型
```

例如：

```c
//mysort2
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
bool compare(int a,int b)
{
       return a<b;   //升序排列，如果改为return a>b，则为降序
}
int main()
{
     int a[10]={7,4,5,23,2,73,41,52,28,60},i;
     for(i=0;i<10;i++)
       cout<<a[i]<<" ";
     cout<<endl;
     sort(a,a+10,compare);
     for(i=0;i<10;i++)
       cout<<a[i]<<" ";
     return 0;
}
```

输出结果为：

```c
7 4 5 23 2 73 41 52 28 60
2 4 5 7 23 28 41 52 60 73
```

（2）利用functional标准库

其实对于这么简单的任务（类型支持“<”“>”等比较运算符），完全没必要自己写一个类出来。标准库里已经有现成可用的，就在functional里，在头文件引用include进来即可。

```c
#include<functional>
```

functional提供了如下的基于模板的比较函数对象。

+ equal_to<Type>：等于。
+ not_equal_to<Type>：不等于。
+ greater<Type>：大于。
+ greater_equal<Type>：大于等于。
+ less<Type>：小于。
+ less_equal<Type>：小于等于。

对于这个问题来说，greater和less就足够了，可以直接拿来用。

+ 升序：sort(begin,end,less<data-type>())。
+ 降序：sort(begin,end,greater<data-type>())。

```c
//mysort3
#include<cstdio>
#include<iostream>
#include<functional>
#include<algorithm>
using namespace std;
int main()
{
     int a[10]={7,4,5,23,2,73,41,52,28,60},i;
     for(i=0;i<10;i++)
       cout<<a[i]<<" ";
     cout<<endl;
     sort(a,a+10,greater<int>());//从大到小排序
     for(i=0;i<10;i++)
       cout<<a[i]<<" ";
     return 0;
}
```

输出结果为：

```c
7 4 5 23 2 73 41 52 28 60
73 60 52 41 28 23 7 5 4 2
```



