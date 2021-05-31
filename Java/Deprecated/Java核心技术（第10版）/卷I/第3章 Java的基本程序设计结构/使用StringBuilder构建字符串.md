首先，构建一个空的字符串构建器：

```java
StringBuilder builder = new StringBuilder();
```

当每次需要添加一部分内容时，就调用 `append` 方法：

```java
builder.append(ch);	// appends a single character
builder.append(str);	// appends a string
```

在需要构建字符串时就调用toString方法，将可以得到一个String对象：

```java
String completedString = builder.toString();
```

> 注释：在 JDK 5.0 中引入 StringBuilder 类。这个类的前身是 StringBuffer，其效率稍有些低，但允许采用多线程的方式执行添加或删除字符的操作。如果所有字符串在一个单线程中编辑（通常都是这样），则应该用 StringBuilder 替代它。这两个类的 API 是相同的。
>