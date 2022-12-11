可以访问外围浏览器的两个区域：状态栏和 Web 页面显示区，这都要使用 `AppletContext` 接口的方法。

可以用 `showStatus` 方法在浏览器底部的状态栏中显示一个字符串。例如：

```java
showStatus("Loading data ... please wait");
```

>   提示：从经验来看，`showStatus` 的作用有限。浏览器也会经常使用状态栏，它会用类似 "Applet running" 之类的话覆盖原先的消息。

可以用 `showDocument` 方法告诉浏览器显示一个不同的 Web 页面。有很多方法可以达到这个目的。最简单的方法是调用 `showDocument` 并提供一个参数，即你想要显示的 URL：

```java
URL u = new URL("http://horstmann.com/index.html");
getAppletContext().showDocument(u);
```

这个调用的问题在于，它会在当前页面所在的同一个窗口中打开新 Web 页面，因此会替换你的 applet。要返回原来的 applet，用户必须点击浏览器的后退按钮。

可以在 `showDocumtent` 调用中提供第二个参数告诉浏览器在另一个窗口中显示文档。

<center><b>showDocument 方法</b></center>

| 目标参数     | 位置                                                         |
| ------------ | ------------------------------------------------------------ |
| "_self" 或无 | 在当前框架中显示文档                                         |
| "_parent"    | 在父框架中显示文档                                           |
| "_top"       | 在最顶层框架中显示文档                                       |
| "_blank"     | 在新的未命名顶层窗口中显示文档                               |
| 其他字符串   | 在指定框架中显示。如果不存在指定名字的框架，则打开一个新窗口，并指定为这个窗口的名字 |

