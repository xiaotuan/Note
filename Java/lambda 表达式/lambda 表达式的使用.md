[toc]

### 1. 一种 lambda 表达式形式

下面使用一种 lambda 表达式的形式：

**有参形式**

```java
(参数类型1 参数1, 参数类型2 参数2, ...) -> {
    表达式
}
```

**无参形式**

```java
() -> {
    表达式式
}
```

例如：

```java
import java.util.Arrays;

public class JavaTest {

	public static void main(String[] args) {
		String[] friends = { "Peter", "Paul", "Mary" };
        // Comparator 接口
		Arrays.sort(friends,(String o1, String o2) -> {
			return o1.length() - o2.length();
		});
		System.out.println(Arrays.toString(friends));
		
        // Runnable 接口
		new Thread(() -> {
			System.out.println("Thread print info.");
		}).start();
	}

}
```

### 2. 自动推导参数类型的 lambda 表达式

如果可以推导出一个 lambda 表达式的参数类型，则可以忽略其类型。例如，Comparator 接口的 lambda 表达式如下所示：

```java
// Comparator 接口
(first, second) -> {	// Same as (String.first, String second)
    return first.length() - second.length();
}
```

> 提示
>
> 如果 lambda 表达式只有一条语句，可以简写成如下形式：
>
> ```java
> // Comparator 接口
> (first, second) -> first.length() - second.length()
> ```

如果方法只有一个参数，而且这个参数的类型可以推导得出，那么甚至还可以省略小括号：

```java
// ActionListener 接口
new Timer(1000, event -> System.out.println("The time is " + new Date())).start();
```

> 提示
>
> 无需指定 lambda 表达式的返回类型。lambda 表达式的返回类型总是会由上下文推导得出。如果一个 lambda 表达式只在某些分支返回一个值，而在另外一些分支不返回值，这是不合法的。例如，`(int x) -> { if (x >= 0) return 1; }` 就不合法。

### 3. 方法引用

有时，可能已经有现成的方法可以完成你想要传递到其他代码的某个动作。例如，假设你希望只要出现一个定时器事件就打印这个事件对象。当然，为此也可以调用：

```java
Timer t = new Timer(1000, event -> System.out.println(event));
```

但是，如果直接把 println 方法传递到 Timer 构造器就更好了。具体做法如下：

```java
Timer t = new Timer(1000, System.out::println);
```

表达式 `System.out::println` 是一个方法引用， 它等价于 lambda 表达式 `x -> System.out.println(x)`。

可以在方法引用中使用 this 参数。例如，`this::equals` 等同于 `x -> this.equals(x)`。使用 super 也是合法的。下面的方法表达式：

```java
super::instanceMethod
```

### 4. 构造器引用

构造器引用与方法引用很类似，只不过方法名为 new。例如，`Person::new` 是 Person 构造器的一个引用。具体使用那个构造器取决于上下文。

### 5. 键提取器

Comparator 接口的静态 comparing 方法取一个 “键提取器” 函数，它将类型 T 映射为一个可比较的类型。对要比较的对象应用这个函数，然后对返回的键完成比较。例如：

```java
Arrays.sort(people, Comparator.comparing(Person::getName));
```

可以把比较器与 thenComparing 方法串起来。例如：

```java
Arrays.sort(people, Comparator.comparing(Person::getLastName)
           .thenComparing(Person::getFirstName));
```

如果两个人的姓相同，就会使用第二个比较器。