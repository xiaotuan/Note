[toc]

`Hashtable` 通常称为哈希表，它表示键/值对的集合，这些键/值对根据键的哈希代码进行组织。它的每个元素都是一个存储在 `DictionaryEntry` 对象中的键/值对。键不能为空引用，但值可以。

### 1. 构造函数

（1）使用默认的初始容量、加载因子、哈希代码提供程序和比较器来初始化 `Hashtable` 类的新的空实例，语法格式如下所示：

```c#
public Hashtable()
```

（2）使用指定的初始容量、默认加载因子、默认哈希代码提供程序和默认比较器来初始化 `Hashtable` 类的新的空实例，语法格式如下所示：

```c#
public Hashtable(int capacity);
```

### 2. ArrayList 常用属性

| 属性           | 说明                                            |
| -------------- | ----------------------------------------------- |
| Count          | 获取包含在 Hashtable 中键/值对的数目            |
| IsFixedSize    | 获取一个值，该值指示 Hashtable 是否具有固定大小 |
| IsReadOnly     | 获取一个值，该值指示 Hashtable 是否为只读       |
| IsSynchronized | 获取一个值，该值指示是否同步对 Hashtable 的访问 |
| Item           | 获取或设置指定键相关联的值                      |
| Keys           | 获取包含 Hashtable 中的键的 ICollection         |
| SyncRoot       | 获取可用于同步 Hashtable 访问的对象。           |
| Values         | 获取包含 Hashtable 中的值的 ICollection         |

### 3. 添加元素

向 `Hashtable` 中添加元素时，可以使用 `Hashtable` 类提供的 `Add()` 方法。

`Add()` 方法用来将带有指定键和值的元素添加到 `Hashtable` 中，其语法格式如下所示：

```c#
public virtual void Add(Object key, Object value);
```

> 提示：如果指定了 `Hashtable` 的初始容量，则不用限定向 `Hashtable` 对象中添加的因子个数。容量会根据加载的因子自动增加。

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        Console.WriteLine(hashtable.Count);
    }

}
```

### 4. 删除元素

在 `Hashtable` 中删除元素时，可以使用 `Hashtable` 类提供的 `Clear()` 方法和 `Remove()` 方法。

#### 4.1 Clear() 方法

`Clear()` 方法用来从 `Hashtable` 中移除所有元素，其语法格式如下所示：

```c#
public virtual void Clear();
```

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        hashtable.Clear();
        Console.WriteLine(hashtable.Count);
    }

}
```

#### 4.2 Remove() 方法

`Remove()` 方法用来从 `Hashtable` 中移除带有指定键的元素，其语法格式如下所示：

```c#
public virtual void Remove(Object key);
```

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        hashtable.Remove("sex");
        Console.WriteLine(hashtable.Count);
    }

}
```

### 5. 遍历 Hashtable

可以使用 `foreach` 语句遍历 `Hashtable` 。这里需要注意的是，由于 `Hashtable` 中的元素是一个键/值对，因此需要使用 `DictionaryEntry` 结构来进行遍历。例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        Console.WriteLine("\t 键\t 值");
        foreach (DictionaryEntry entry in hashtable)
        {
            Console.WriteLine("\t " + entry.Key + "\t " + entry.Value);
        }
    }

}
```

### 6. 查找元素

在 `Hashtable` 中查找元素时，可以使用 `Hashtable` 类提供的 `Contains()` 方法、`ContainsKey()` 方法和 `ContainsValue()` 方法。

#### 6.1 Contains() 方法

`Contains()` 方法用来确定 `Hashtable` 中是否包含特定键，其语法格式如下所示：

```c#
public virtual bool Contains(Object key);
```

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        Console.WriteLine(hashtable.Contains("id"));
    }

}
```

#### 6.2 ContainsValue() 方法

`ContainsValue()` 方法用来确定 `Hashtable` 中是否包含特定值，其语法格式如下所示：

```c#
public virtual bool ContainsValue(Object value);
```

例如：

```c#
using System.Collections;

class Program
{

    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        Console.WriteLine(hashtable.ContainsValue("id"));
    }

}
```

