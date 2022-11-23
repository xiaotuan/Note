假设一个按钮监听器需要执行以下调用：

```java
frame.loadData();
```

`EventHandler` 类可以用下面的调用创建这样一个监听器：

```java
ActionListener listener = EventHandler.create(ActionListener.class, frame, "loadData");
```

这种方法现在已经成为历史。利用 lambda 表达式，可以更容易地使用以下调用：

```java
event -> frame.loadData();
```

`EventHandler` 机制的效率也不高，而且笔记容易出错。它使用反射来调用方法。出于这个原因，`EventHandler.create` 调用的第二个参数必须属于一个公有类。否则，反射机制就无法确定和调用目标方法。