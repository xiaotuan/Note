考虑下面这个例子：

```java
public static void repeatMessage(String text, int delay) {
    ActionListener listener = event -> {
        System.out.println(text);
        Toolkit.getDefaultToolkit().beep();
    };
    new Timer(delay, listener).start();
}
```

在上面的例子中，lambda 表达式有 1 个自有变量 text。表达式 lambda 表达式的数据结构必须存储自由变量的值。我们说它被 lambda 表达式捕获。

在 lambda 表达式中，只能引用值不会改变的变量。例如，下面的做法是不合法的：

```java
public static void countDown(int start, int delay) {
    ActionListener listener = event -> {
        start--;	// Error: Can't mutate captured variable
        System.out.println(start);
    };
    new Timer(delay, listener).start();
}
```

如果在 lambda 表达式中引用变量，而这个变量可能在外部改变，这也是不合法的。例如：

```java
public static void repeat(String text, int count) {
    for (int i = 1; i <= count; i++) {
        ActionListener listener = event -> {
            System.out.println(i + ": " + text);	// Error: Cannot refer to changing
        };
        new Timer(1000, listener).start();
    }
}
```

lambda 表达式的体与嵌套块有相同的作用域。这里同样适用命名冲突和遮蔽的有关规则。在 lambda 表达式中声明与一个局部变量同名的参数或局部变量是不合法的。

```java
Path first = Paths.get("/usr/bin");
Comparator<String> comp = (first, second) -> first.length() - second.length();	// Error: Variable first already defined
```

lambda 表达式中同样也不能有同名的局部变量。

在一个 lambda 表达式中使用 this 关键字时，是指创建这个 lambda 表达式的方法的 this 参数。例如：

```java
public class Application() {
    public void init() {
        ActionListener listener = event -> {
            System.out.println(this.toString());
        }
    }
}
```

表达式 `this.toString()` 会调用 Application 对象的 toString 方法，而不是 ActionListener 实例的方法。