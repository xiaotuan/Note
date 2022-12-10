与应用可以使用命令行信息一样，applet 可以使用内嵌的 HTML 文件中的参数。这是利用 HTML param 标记以及所定义的属性来完成的。例如，假设想让 Web 页面确定 applet 中使用的字体样式。可以使用以下 HTML 标记：

```html
<applet code="FontParamApplet.class" ...>
    <param name="font" value="Helvetica" />
</applet>
```

然后使用 Applet 类的 `getParameter` 方法得到参数的值：

```java
public class FontParamApplet extends JApplet {
    public void init() {
        String fontName = getParameter("font");
        ...
    }
}
```

> 注意：只能在 applet 的 `init` 方法中调用 `getParameter` 方法，而不能在构造器中调用。执行 applet 构造器时，参数还没有准备好。由于大多数重要 applet 的布局都由参数确定，所以建议不要为 applet 提供构造器，要把所有初始化代码放在 `init` 方法中。

参数总是作为字符串返回。如果需要数值类型，则需要将字符串转换为数值。

> 注意：param 标记中的 name 属性值与 `getParameter` 方法的参数匹配时，会使用不区分大小写的比较。

除了要确保代码中的参数匹配之外，还要检查是否缺少 size 参数。可以简单地测试是否为 null 来达到目的。例如：

```java
int fontsize;
String sizeString = getParemeter("size");
if (sizeString == null) fontSize = 12;
else fontSize = Integer.parseInt(sizeString);
```

**示例代码：**

**HTML**

```html
<applet code="Chart.class" width="400" height="300">
    <param name="title" value="Diameters of the Planets" />
    <param name="values" value="9" />
    <param name="name.1" value="Mercury" />
    <param name="name.2" value="Venus" />
    <param name="name.3" value="Earth" />
    <param name="name.4" value="Mars" />
    <param name="name.5" value="Jupiter" />
    <param name="name.6" value="Saturn" />
    <param name="name.7" value="Uranus" />
    <param name="name.8" value="Neptune" />
    <param name="name.9" value="Pluto" />
    <param name="value.1" value="3100" />
    <param name="value.2" value="7500" />
    <param name="value.3" value="8000" />
    <param name="value.4" value="4200" />
    <param name="value.5" value="88000" />
    <param name="value.6" value="71000" />
    <param name="value.7" value="32000" />
    <param name="value.8" value="30600" />
    <param name="value.9" value="1430" />
</applet>
```

**JAVA**

```java
```

