考虑下面这个简单的方法，它的参数个数是可变的：

```java
public static <T> void addAll(Collection<T> coll, T... ts) {
    for (t : ts) {
        coll.add(t);
    }
}
```

应该记得，实际上参数 ts  是一个数组，包含提供的所有实参。

现在考虑以下调用：

```java
Collection<Pair<String>> table = ...;
Pair<String> pair1 = ...;
Pair<String> pair2 = ...;
addAll(table, pair1, pair2);
```

为了调用这个方法，`Java` 虚拟机必须建立一个 `Pair<String>` 数组，这就违反了前面的规则。不过，对于这种情况，规则有所放松，你只会得到一个警告，而不是错误。

可以采用两种方法来抑制这个警告。一种方法是为包含 `addAll` 调用的方法增加注解 `@SuppressWarnings("unchecked")`。或者在 `Java SE 7` 中，还可以用 `@SafeVarargs` 直接标注 `addAll` 方法：

```java
@SafeVarargs
public static <T> void addAll(Collection<T> coll, T... ts)
```

现在就可以提供泛型类型来调用这个方法了。对于只需要读取参数数组的所有方法，都可以使用这个注解，这仅限于最常见的用例。

> 提示：可以使用 `@SafeVarargs` 标注来消除创建泛型数组的有关限制，方法如下：
>
> ```java
> @SafeVarargs static <E> E[] array(E... array) { return array; }
> ```
>
> 现在可以调用：
>
> ```java
> Pair<String>[] table = array(pair1, pair2);
> ```
>
> 这看起来很方便，不过隐藏着危险。以下代码：
>
> ```java
> Object[] objarray = table;
> objarray[0] = new Pair<Employee>();
> ```
>
> 能顺利运行而不会出现 `ArrayStoreException` 异常（因为数组存储之后检查擦除的类型），但在处理 `table[0]` 时你会在别处得到一个异常。



