`DataFlavor` 是由下面两个特性来定义的：

+ `MIME` 类型的名字（比如 `image/gif`）。
+ 用于访问数据的表示类（比如 `java.awt.Image`）。

此外，每一种数据风格都有一个适合人类阅读的名字（比如 "GIF Image"）。

表示类可以用 `IMEI` 类型的 `class` 参数设定，例如：

```java
image/gif;class=java.awt.Image
```

如果没有给定任何 `class` 参数，那么表示类就是 `InputStream`。

为了传递本地的、序列号的和远程的 `Java` 对象，人们定义了如下三个 `IMEI` 类型：

```
application/x-java-jvm-local-objectref
application/x-java-serialized-object
application/x-java-remote-object
```

> 注意：`x-` 前缀表示这时一个试用名，并不是 `IANA` 批准的名字，`IANA` 是负责分配标准的 `MIME` 类型名的机构。

例如，标准的 `stringFlavor` 数据风格是由下面这个 `MIME` 类型描述的：

```
application/x-java-serialized-object;class=java.lang.String
```

可以让剪贴板列出所有可用的风格：

```java
DataFlavor[] flavors = clipboard.getAvailableDataFlavors();
```

也可以在剪贴板上安装一个 `FlavorListener`，当剪贴板上的数据风格集合产生变化时，可以通知风格监听器。

