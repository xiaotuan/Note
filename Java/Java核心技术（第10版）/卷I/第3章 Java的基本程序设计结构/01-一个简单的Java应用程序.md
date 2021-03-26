### 3.1 一个简单的 Java 应用程序

下面看一个最简单的 Java 应用程序，它只发送一条消息到控制台窗口中：

**FirstSample.java**

```java
System.out.println("We will not use 'Hello, World!'");
```

Java 中定义类名的规则很宽松。名字必须以字母开头，后面可以跟字母和数字的任意组合。长度基本上没有限制。但是不能使用 Java 保留字。

标准的命名规范为：类名是以大写字母开头的名词。如果名字由多个单词组成，每个单词的第一个字母都应该大写。

源代码的文件名必须与公共类的名字相同，并用 `.java` 作为扩展名。

最后，使用下面这行命令运行这个程序：

```shell
javac FirstSample.java
java FirstSample
```

> 注释：根据 Java 语言规范，main 方法必须声明为 public。

