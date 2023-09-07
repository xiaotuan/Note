[toc]

### 1. Hashtable 概述

`Hashtable` 通常称为哈希表，它表示键/值对的集合，这些键/值对根据键的哈希代码进行组织。它的每个元素都是一个存储在 `DictionaryEntry` 对象中的键/值对。键不能为空引用，但值可以。

`Hashtable` 的构造函数有多种，这里介绍两种最常用的：

+ 使用默认的初始容量、加载因子、哈希代码提供程序和比较器来初始化 `Hashtable` 类的新的空实例，语法如下：

  ```c#
  public Hashtable()
  ```

+ 使用指定的初始容量、默认加载因子、默认哈希代码提供程序和默认比较器来初始化 `Hashtable` 类的新的空实例，语法如下：

  ```c#
  public Hashtable(int capacity)
  ```

`Hashtable` 常用属性及说明如下表所示：

| 属性             | 说明                                              |
| ---------------- | ------------------------------------------------- |
| `Count`          | 获取包含在 `Hashtable` 中的键/值对的数目          |
| `IsFixedSize`    | 获取一个值，该值指示 `Hashtable` 是否具有固定大小 |
| `IsReadOnly`     | 获取一个值，该值指示 `Hashtable` 是否具有固定大小 |
| `IsSynchronized` | 获取一个值，该值指示是否同步对 `Hashtable` 的访问 |
| `Item`           | 获取或设置与指定的键相关联的值                    |
| `Keys`           | 获取包含 `Hashtable` 中的键的 `ICollection`       |
| `SyncRoot`       | 获取可用于同步 `Hashtable` 访问的对象             |
| `Values`         | 获取包含 `Hashtable` 中的值的 `ICollection`       |

### 2. Hashtable 元素的添加

向 `Hashtable` 中添加元素时，可以使用 `Hashtable` 类提供的 `Add()` 方法，其语法格式如下：

```c#
public virtual void Add(Object key, Object value)
```

```c#
Hashtable hashtable = new Hashtable();
hashtable.Add("id", "BH0001");
hashtable.Add("name", "TM");
hashtable.Add("sex", "男");
Console.WriteLine(hashtable.Count);
```

### 3. Hashtable 元素的删除

在 `Hashtable` 中删除元素时，可以使用 `Hashtable` 类提供的 `Clear()` 方法和 `Remove()` 方法。

1. Clear() 方法

   `Clear()` 方法用来从 `Hashtable` 中移除所有元素。

   ```c#
   Hashtable hashtable = new Hashtable();
   hashtable.Add("id", "BH0001");
   hashtable.Add("name", "TM");
   hashtable.Add("sex", "男");
   hashtable.Clear();
   Console.WriteLine(hashtable.Count);
   ```

2. Remove() 方法

   `Remove()` 方法用来从 `Hashtable` 中移除带有指定键的元素，其语法格式如下：

   ```C#
   public virtual void Remove(Object key)
   ```

   ```C#
   Hashtable hashtable = new Hashtable();
   hashtable.Add("id", "BH0001");
   hashtable.Add("name", "TM");
   hashtable.Add("sex", "男");
   hashtable.Remove("sex");
   Console.WriteLine(hashtable.Count);
   ```

### 3. Hashtable 的遍历

可以使用 `foreach` 语句遍历 `Hashtable` 中的元素。

```c#
using System.Collections;

class CShapeTest
{
    static void Main(string[] args)
    {
        Hashtable hashtable = new Hashtable();
        hashtable.Add("id", "BH0001");
        hashtable.Add("name", "TM");
        hashtable.Add("sex", "男");
        foreach (DictionaryEntry dicEntry in hashtable)
        {
            Console.WriteLine("\t" + dicEntry.Key + "\t " + dicEntry.Value);
        }
    }
}
```

### 5. Hashtable 元素的查找

在 `Hashtable` 中查找元素时，可以使用 `Hashtable` 类提供的 `Contains()` 方法、`ContainsKey()` 方法和 `ContainsValue()` 方法。

1. Contains() 方法

   `Contains()` 方法用来确定 `Hashtable` 中是否包含特定键。

   ```C#
   Hashtable hashtable = new Hashtable();
   hashtable.Add("id", "BH0001");
   hashtable.Add("name", "TM");
   hashtable.Add("sex", "男");
   Console.WriteLine(hashtable.Contains("id"));
   ```

   > 提示：`ContainsKey()` 方法和 `Contains()` 方法实现的功能、语法都相同。

2. ContainsValue() 方法

   `ContainsValue()` 方法用来确定 `Hashtable` 中是否包含特定值。

   ```c#
   Hashtable hashtable = new Hashtable();
   hashtable.Add("id", "BH0001");
   hashtable.Add("name", "TM");
   hashtable.Add("sex", "男");
   Console.WriteLine(hashtable.ContainsValue("男"));
   ```

   