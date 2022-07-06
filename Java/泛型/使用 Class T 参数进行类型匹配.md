有时，匹配泛型方法中的 `Class<T>` 参数的类型变量很有实用价值。下面是一个标志的示例：

```java
public static <T> Pair<T> makePair(Class<T> c) throws InstantiationException, IllegalAccessException {
    return new Pair<>(c.getInstance(), c.newInstance());
}
```

如果调用

```java
makePair(Employee.class);
```

`Employee.class` 是类型 `Class<Employee>` 的一个对象。`makePair` 方法的类型参数 T 同 `Employee` 匹配，并且编译器可以推断出这个方法将返回一个 `Pair<Employee>`。