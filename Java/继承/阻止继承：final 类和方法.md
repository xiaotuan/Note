[toc]

### 1. final 类

不允许扩展的类被称为 final 类。如果在定义类的时候使用了 final 修饰符就表明这个类是 final 类。

```java
public final class Excutive extends Manager {
    ...
}
```

### 2. final 方法

类中的特定方法也可以被声明为 final，子类不能覆盖这个方法（final 类中的所有方法自动地成为 final 方法）。

```java
public class Employee {
    ...
    public final String getName() {
        return name;
    }
    ...
}
```

### 3. final 变量

类中的域也可以被声明为 final。对于 final 域来说，构造对象之后就不允许改变它们的值了。不过，如果将一个类声明为 final ，只有其中的方法自动地成为 final ，而不包括域。

