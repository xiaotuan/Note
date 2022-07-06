现在，`Class` 类是泛型的。例如，`String.class` 实际上是一个 `Class<String>` 类的对象（事实上，是唯一的对象）。

类型参数十分有用，这是因为它允许 `Class<T>` 方法的返回类型更加具有针对性。下面 `Class<T>` 中的方法就使用了类型参数：

```java
T newInstance()
T cast(Object obj)
T[] getEnumConstants()
Class<? super T> getSuperClass()
Constructor<T> getConstructor(Class... parameterTypes)
Constructor<T> getDeclaredConstructor(Class... parameterTypes)
```

`newInstance` 方法返回一个实例，这个实例所属的类由默认的构造器获得。它的返回类型目前被声明为 T，其类型与 `Class<T>` 描述的类相同，这样就免除了类型转换。

如果给定的类型确实是 T 的一个子类型，`cast` 方法就会返回一个现在声明为类型 T 的对象，否则，抛出一个 `BadCastException` 异常。

如果这个类不是 `enum` 类或类型 T 的枚举值的数值，`getEnumConstants` 方法将返回 null。

最后，`getConstructor` 和 `getDeclaredConstructor` 方法返回一个 `Constructor<T>` 对象。`Constructor` 类也已经变成泛型，以便 `newInstance` 方法有一个正确的返回类型。