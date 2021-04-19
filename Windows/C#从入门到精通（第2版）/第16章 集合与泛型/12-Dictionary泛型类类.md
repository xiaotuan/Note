### 16.3.3　Dictionary<K,V>类

在System.Collections.Generic命名空间中，与HashTable相对应的泛型集合是Dictionary<K,V>，其存储数据的方式和哈希表相似，通过键/值来保存元素，并具有泛型的全部特征，编译时检查类型约束，读取时无需进行类型转换。定义Dictionary<K,V>泛型集合中的方法如下。

```c
Dictionary<K,V> 泛型集合名=new Dictionary<K,V>();
```

其中“K”为占位符，具体定义时用存储键“Key”的数据类型代替，“V”同样也是占位符，用元素的值“Value”的数据类型代替，这样在定义该集合时，就声明了存储元素的键和值的数据类型，保证了类型的安全性。

在【范例16-2】中，对HashTable的定义可以改为使用Dictionary<K,V>来实现。代码如下。

```c
Dictionary<string, string> openWith =  new Dictionary<string, string>();
//创建泛型集合Dictionary对象
```

在这个Dictionary<K,V>的声明中，“<string,string>”中的第1个string表示集合中Key的类型，第2个string表示Value的类型。

```c
01  //创建一个泛型Dictionary集合openWith
02  Dictionary<string, string> openWith =  new Dictionary<string, string>();
03  openWith.Add("txt", "notepad.exe");    //添加键/值对到哈希表中，键不能重复
04  openWith.Add("bmp", "paint.exe");      //添加键/值对到哈希表中，键不能重复
```

