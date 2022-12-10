按传统，我们首先编写一个 NotHelloWorld 程序，这里把它写为一个 applet。applet 就是一个扩展了 `java.applet.Applet` 类的 Java 类。

> 提示：如果你的 applet 包含 Swing 组件，必须扩展 JApplet 类。普通 Applet 中的 Swing 组件不能正确绘制。

**示例代码：**

```java
package applet;

import java.awt.*;
import javax.swing.*;

public class NotHelloWorld extends JApplet {
    public void init() {
        EventQueue.invokeLater(() -> {
            JLabel label = new JLabel("Not a Hello, World applet", SwingConstants.CENTER);
            add(label);
        });
    }
}
```

要执行 applet，需要完成以下 3 个步骤：

1）将 Java 源文件编译为类文件。

2）将类打包到一个 JAR 文件中。

3）创建一个 HTML 文件，告诉浏览器首先加载哪个类文件，以及如何设定 applet 的大小。

下面给出这个文件的内容：

```html
<applet class="applet/NotHelloWorld.class" archive="NotHelloWorld.jar" width="300" height="300">
</applet>
```

在浏览器中查看 applet 之前，最好先在 JDK 自带的 applet viewer（applet 查看器）程序中进行测试。要使用 applet 查看器测试我们的示例 applet，可以在命令行输入：

```shell
appletview NotHelloWorldApplet.html
```

要正确地查看 applet，只需要把 HTML 文件加载到浏览器。如果 applet 没有出现，则需要安装 Java Plug-in，并允许它加载无签名的本地 applet。

> 提示：如果修改了 applet 并重新编译，就需要重新启动浏览器，这样才会加载新的类文件。只是刷新 HTML 页面并不会加载新代码。

很容易把一个图形化 Java 应用转换为可以嵌入在 Web 页面中的 applet。基本上来说，所有用户界面代码都可以保持不变。下面给出具体的步骤：

1）建立一个 HTML 页面，其中包含加载 applet 代码的适当标记。

2）提供 JApplet 类的一个子类。将这个类标记为 public。否则 applet 将无法加载。

3）删去应用中的 `main` 方法。不要为应用构造框架窗口。你的应用将在浏览器中显示。

4）把所有初始化代码从框架窗口移至 applet 的 init 方法。不需要明确构造 applet 对象，浏览器会实例化 applet 对象并调用 init 方法。

5）删除 `setSize` 调用；对 applet 来说，用 HTML 文件中的 width 和 height 参数就可以指定大小。

6）删除 `setDefaultCloseOperation` 调用。applet 不能关闭；浏览器退出时 applet 就会终止运行。

7）如果应用调用 `setTitle` ，则删除这个方法调用。`applet` 没有标题栏。（当然，可以用 HTML title 标记为 Web 页面本身指定标题）

8）不要调用 `setVisible(true)`。applet 会自动显示。