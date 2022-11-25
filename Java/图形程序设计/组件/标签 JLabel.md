标签是容纳文本的组件，它们没有任何的修饰（例如没有边缘），也不能响应用户输入。可以利用标签标识组件。

`JLabel` 的构造器允许指定初始文本和图标，也可以选择内容的排列方式。可以用 Swing Constants 接口中的常量来指定排列方式。在这个接口中定义了几个很有用的常量，如 LEFT、RIGHT、CENTER、NORTH、EAST 等。`JLabel` 是实现这个接口的一个 Swing 类。因此，可以指定右对齐标签：

```java
JLabel label = new JLabel("User name: ", SwingConstants.RIGHT);
```

利用 `setText` 和 `setIcon` 方法可以在运行期间设置标签的文本和图标。

> 提示：可以在按钮、标签和菜单项上使用无格式文本或 `HTML` 文本。我们不推荐在按钮上使用 HTML 文本——这样会影响观感。但是 HTML 文本在标签中是非常有效的。只要简单地将标签字符串放置在 `<html>...</html>` 中即可：
>
> ```java
> label = new JLabel("<html><b>Required</b> entry: </html>");
> ```
>
> 需要说明的是包含 HTML 标签的第一个组件需要延迟一段时间才能显示出来，这是因为需要加载相当复杂的 HTML 显示代码。