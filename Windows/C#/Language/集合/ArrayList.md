[toc]

> 注意：程序中使用 `ArrayList` 类时，需要在命名空间区域添加 `using System.Collections;`。

`ArrayList` 类位于 `System.Collections` 命名空间下，它可以动态地添加和删除元素。可以将 `ArrayList` 类看作扩充了功能的数组，但它并不等同于数组。

### 1. ArrayList 构造器

`ArrayList` 提供了 3 个构造器：

（1）默认的构造器，将会以默认（16位）的大小来初始化内部的数组。构造器格式如下所示：

```c#
public ArrayList();
```

例如：

```c#
using System.Collections;

ArrayList List = new ArrayList();
```

（2）用一个 `ICollection` 对象来构造，并将该集合的元素添加到 `ArrayList` 中。构造器格式如下所示：

```c#
public ArrayList(ICollection);
```

例如：

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
ArrayList List = new ArrayList(arr);
```

（3）用指定的大小初始化内部的数组。构造器格式如下所示：

```c#
using System.Collections;

public ArrayList(int);
```

例如：

```c#
using System.Collections;

ArrayList List = new ArrayList(10);
for (int i = 0; i < List.Count; i++)
{
    List.Add(i);
}
```

### 2. ArrayList 常用属性

| 属性           | 说明                                            |
| -------------- | ----------------------------------------------- |
| Capacity       | 获取或设置 ArrayList 可包含的元素数             |
| Count          | 获取 ArrayList 中实际包含的元素数               |
| IsFixedSize    | 获取一个值，该值指示 ArrayList 是否具有固定大小 |
| IsReadOnly     | 获取一个值，该值指示 ArrayList 是否为只读       |
| IsSynchronized | 获取一个值，该值指示是否同步对 ArrayList 的访问 |
| Item           | 获取或设置指定索引处的元素                      |
| SyncRoot       | 获取可用于同步 ArrayList 访问的对象。           |

### 3. 添加元素

向 `ArrayList` 集合中添加元素时，可以使用 `ArrayList` 类提供的 `Add()` 方法和 `Insert()` 方法。

#### 3.1 Add() 方法

`Add()` 方法用来将对象添加到 `ArrayList` 集合的结尾处，其语法格式如下所示：

```c#
public virtual int Add(Object value);
```

> 提示：`ArrayList` 允许 `null` 值作为有效值，并且允许重复元素。

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList List = new ArrayList(arr);
List.Add(7);
```

#### 3.2 Insert() 方法

`Insert()` 方法用来将元素插入 `ArrayList` 集合的指定索引处，其语法格式如下所示：

```c#
public virtual void Insert(int index, Object value);
```

例如：

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList List = new ArrayList(arr);
List.Insert(3, 7);
```

#### 3.3 InsertRange() 方法

`InsertRange()` 方法允许将一维数组插入到指定位置。

### 4. 删除元素

在 `ArrayList` 集合中删除元素时，可以使用 `ArrayList` 类提供的 `Clear()` 方法、`Remove()` 方法、`RemoveAt()` 方法和 `RemoveRange()` 方法。

#### 4.1 Clear() 方法

`Clear()` 方法用来从 `ArrayList` 中移除所有元素，其语法格式如下所示：

```c#
public virtual void Clear();
```

例如：

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList List = new ArrayList(arr);
List.Clear();
```

#### 4.2 Remove() 方法

`Remove()` 方法用来从 `ArrayList` 中移除特定对象的第一个匹配项，其语法格式如下所示：

```c#
public virtual void Remove(Object obj);
```

> 提示：在删除 `ArrayList` 中的元素时，如果不包含指定对象，则 `ArrayList` 将保持不变。

例如：

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList List = new ArrayList(arr);
List.Remove(3);
```

#### 4.3 RemoveAt() 方法

`RemoveAt()` 方法用来移除 `ArrayList` 的指定索引处的元素，其语法格式如下所示：

```c#
public virtual void RemoveAt(int index);
```

例如：

```c#
using System.Collections;

int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList List = new ArrayList(arr);
List.RemoveAt(3);
```

#### 4.4 RemoveRange() 方法

`RemoveRange()` 方法用来从 `ArrayList` 中移除一定范围的元素，其语法格式如下所示：

```c#
public virtual void RemoveRange(int index, int count);
```

> 注意：在 `RemoveRange()` 方法中参数 count 的长度不能超出数组的总长度减去参数 index 的值。

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        int[] arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        ArrayList List = new ArrayList(arr);
        Console.WriteLine("原 ArrayList 集合：");
        foreach (int i in List)
        {
            Console.Write(i.ToString() + " ");
        }
        Console.WriteLine();
        List.RemoveRange(0, 5);
        Console.WriteLine("删除元素后的 ArrayList 集合：");
        foreach (int i in List)
        {
            Console.Write(i.ToString() + " ");
        }
    }

}
```

### 5. 遍历 ArrayList

`ArrayList` 集合的遍历与数组类似，都可以使用 `foreach` 语句。例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        ArrayList list = new ArrayList();
        list.Add("TM");
        list.Add("C# 从入门到精通");
        foreach (string str in list)
        {
            Console.WriteLine(str);
        }
    }

}
```

### 6. 查找元素

查找 `ArrayList` 集合中的元素时，可以使用 `ArrayList` 类提供的 `Contains()` 方法、`IndexOf()` 方法和 `LastIndexOf()` 方法。`IndexOf()` 方法和 `LastIndexOf()` 方法的用法与  string 字符串类的同名方法的用法基本相同。

`Contains()` 方法用来确定某元素是否在 `ArrayList` 集合中，其语法格式如下所示：

```c#
public virtual bool Contains(Object item);
```

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        int[] arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        ArrayList List = new ArrayList(arr);
        Console.Write(List.Contains(2));
    }

}
```

