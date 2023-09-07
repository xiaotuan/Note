[toc]

### 1. ArrayList 类概述

`ArrayList` 类位于 `System.Collections` 命名空间下，它可以动态添加和删除元素。

`ArrayList` 提供了 3 个构造函数：

+ 默认构造函数，将会以默认的大小来初始化内部数组。构造函数格式如下：

  ```c#
  public ArrayList();
  ```

  示例：

  ```c#
  ArrayList list = new ArrayList();
  for (int i = 0; i < 10; i++) {
      list.Add(i);
  }
  ```

+ 用一个 `ICollection` 对象来构造，并将该集合的元素添加到 `ArrayList` 中。构造器格式如下：

  ```C#
  public ArrayList(ICollection);
  ```

  示例：

  ```c#
  int[] arr = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
  ArrayList list = new ArrayList(arr);
  ```

+ 用指定的大小初始化内部数组。构造器格式如下：

  ```C#
  public ArrayList(int);
  ```

  示例：

  ```c#
  ArrayList list = new ArrayList(10);
  for (int i = 0; i < list.Count; i++) {
      list.Add(i);
  }
  ```

`ArrayList` 常用属性及说明如下表所示：

| 属性             | 说明                                              |
| ---------------- | ------------------------------------------------- |
| `Capacity`       | 获取或设置 `ArrayList` 可包含的元素数             |
| `Count`          | 获取 `ArrayList` 中实际包含的元素数               |
| `IsFixedSize`    | 获取一个值，该值指示 `ArrayList` 是否具有固定大小 |
| `IsReadOnly`     | 获取一个值，该值指示 `ArrayList` 是否为只读       |
| `IsSynchronized` | 获取一个值，该值指示是否同步对 `ArrayList` 的访问 |
| `Item`           | 获取或设置指定索引处的元素                        |
| `SyncRoot`       | 获取可用于同步 `ArrayList` 访问的对象             |

### 2. ArrayList 元素的添加

向 `ArrayList` 集合中添加元素时，可以使用 `ArrayList` 类的 `Add()` 方法和 `Insert()` 方法：

1. Add() 方法

   `Add()` 方法用来将对象添加到 `ArrayList` 集合的结尾处。

   > 提示：`ArrayList` 允许 `null` 值作为有效值，并且允许重复的元素。

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.Add(7);
   ```

2. Insert() 方法

   `Insert()` 方法用来将元素插入 `ArrayList` 集合的指定索引处，其语法格式如下：

   ```c#
   public virtual void Insert(int index, Object value)
   ```

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.Insert(3, 7);
   ```

### 3. ArrayList 元素的删除

在 `ArrayList` 集合中删除元素时，可以使用 `ArrayList` 类提供的 `Clear()` 方法、`Remove()` 方法、`RemoveAt()` 方法和 `RemoveRange()` 方法。

1. Clear() 方法

   `Clear()` 方法用来从 `ArrayList` 中移除所有元素。

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.Clear();
   ```

2. Remove() 方法

   `Remove()` 方法用来从 `ArrayList` 中移除特定对象的第一个匹配项。

   > 注意：在删除 `ArrayList` 中的元素时，如果不包含指定对象，则 `ArrayList` 将保持不变。

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.Remove(3);
   ```

3. RemoveAt() 方法

   `RemoveAt()` 方法用来从`ArrayList` 中移除指定索引处的元素。

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.RemoveAt(3);
   ```

4. RemoveRange() 方法

   `RemoveRange()` 方法用来从 `ArrayList` 中移除一定范围的元素，其语法格式如下：

   ```c#
   public virtual void RemoveRange(int index, int count)
   ```

   > 警告：在 `RemoveRange()` 方法中，参数 `count` 的长度不能超出数组的总长度减去参数 `index` 的值。

   示例：

   ```c#
   int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
   ArrayList list = new ArrayList(arr);
   list.RemoveAt(3, 2);
   ```

### 4. ArrayList 的遍历

可以使用 `foreach` 语句遍历 `ArrayList` 集合。

```c#
using System.Collections;

class CShapeTest
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

### 5. ArrayList 元素的查找

查找 `ArrayList` 集合中的元素时，可以使用 `ArrayList` 类提供的 `Contains()` 方法、`IndexOf()` 方法和 `LastIndexOf()` 方法。

```c#
int[] arr = new int[] { 1, 2, 3, 4, 5, 6 };
ArrayList list = new ArrayList(arr);
Console.Write(list.Contains(2));
```

