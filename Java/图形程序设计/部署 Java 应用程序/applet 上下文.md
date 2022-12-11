要与浏览器通信，applet 可以调用 `getAppletContext` 方法。这个方法会返回一个实现 `AppletContext` 接口的对象。可以认为 `AppletContext` 接口的具体实现是 `applet` 与外围浏览器之间的一个通信渠道。除了 `getAudioClip` 和 `getImage` 之外，`AppletContext` 接口还包含很多有用的方法。

一个 Web 页面可以包含多个 applet。如果一个 Web 页面包含来自同一个 codebase 的多个 applet，它们可以相互通信。

如果为 HTML 文件中的各个 applet 指定 name 属性，可以使用 `AppletContext` 接口的 `getApplet` 方法来得到这个 applet 的一个引用。

```html
<applet code="Chart.class" width="100" height="100" name="Chart1">
    
</applet>
```

则以下调用：

```java
Applet char1 = getAppletContext().getApplet("Chart1");
```

会提供这个 applet 的一个引用。假设 `Chart` 类中有一个方法可以接受新数据并重绘图表，可以通过适当的类型转换来调用这个方法：

```java
((Chart) chart1).setData(3, "Earth", 9000);
```

还可以列出一个 Web 页面上的所有 applet，不论它们是否有 name 属性。`getApplets` 方法会返回一个枚举对象。下面给出一个循环，它会打印当前页面上所有 applet 的类名：

```java
Enumeration<Applet> e = getAppletContext().getApplets();
while (e.hasMoreElements()) {
    Applet a = e.nextElement();
    System.out.println(a.getClass().getName());
}
```

applet 不能与不同 Web 页面上的其他 applet 通信。