可以通过 Class 对象的 `newInstance()` 方法创建类实例：

```java
try {
    String s = String.class.newInstance();
} catch (InstantiationException | IllegalAccessException e) {
    e.printStackTrace();
}
```

`newInstance()` 方法调用默认的构造器初始化新创建的对象。如果这个类没有默认的构造器，就会抛出一个异常。

