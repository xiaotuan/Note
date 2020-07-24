不允许扩展的类被称为 final 类。如果在定义类的时候使用了 final 修饰符就表明这个类是 final  类。声明格式如下所示：

```java
final class Executive extends Manager{
    ...
}
```

类中的方法也可以被声明为 final。如果这样做，子类就不能覆盖这个方法（final 类中的所有方法自动地成为 final 方法）。例如：

```java
class Employee {
    ...
    public final String getName() {
        return name;
    }
}
```

