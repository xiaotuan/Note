下面是一个最简形式的 applet 标记示例：

```html
<applet class="applet/NotHelloWorld.class" archive="NotHelloWorld.jar" width="300" height="300">
</applet>
```

可以在 applet 标记中使用以下属性：

+ width，height

  这些属性是必要的，指定了 applet 的宽度和高度（单位为像素）。

+ align

  这个属性指定了 applet 的对齐方式。属性值与 HTML img 标记的 align 属性值相同。

+ vspace，hspace

  这些属性是可选的，指定了 applet 上下的像素数以及左右两边的像素数。

+ code

  这个属性指定了 applet 的类文件名。

  路径名必须与 applet 类的包一致。。例如，如果 applet 类在包 com.mycompany 中，那么这个属性就是 `code="com/mycompany/MyApplet.class"`，也可以是 `code="com.mycompany.MyApplet.class"。

+ archive

  这个属性会列出包含 applet 的类以及其他资源的 JAR 文件（可能有多个 JAR 文件）。这些文件会在加载 applet 之前从Web 服务器获取。JAR 文件用逗号分隔。例如：

  ```html
  <applet code="MyApplet.class"
          archive="MyClasses.jar,corejava/CoreJavaClasses.jar"
          width="100" height="150">
      
  </applet>
  ```

+ codebase

  这个属性是加载 JAR 文件（早期还可以加载类文件）的 URL。

+ object

  这个属性已经过时，可以指定包含串行化 applet 对象的文件的文件名，这个文件用于持久存储 applet 状态。

+ alt

  Java 禁用时，可以使用 alt 属性来显示一个消息。

  如果一个浏览器根本无法处理 applet，它会忽略未知的 applet 和 param 标记。浏览器会显示 `<applet>` 和 `</applet>` 标记之间的所有文本。例如：

  ```html
  <applet ... alt="If you activated Java, you would see my applet here">
      If your browser could show Java, you would see my applet here.
  </applet>
  ```

+ name

  编写脚本的人可以为 applet 指定一个 name 属性，用来指示所编写的 applet。

  要从 JavaScript 访问一个 applet，首先要指定一个名字：

  ```html
  <applet ... name="mine"></applet>
  ```

  然后可以用 `document.applets.appletname` 表示这个对象。例如：

  ```js
  var myApplet = document.applets.mine;
  ```

  接下来就可以调用 applet 方法了：

  ```js
  myApplet.init();
  ```

  希望同一个页面上的两个 applet 相互直接通信时 name 属性也很重要。为每个当前 applet 实例指定一个名字，将这个字符串传递到 AppletContext 接口的 `getApplet` 方法。