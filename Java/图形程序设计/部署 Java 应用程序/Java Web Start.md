[toc]

Java Web Start 应用程序包含下列主要特性：

+   Java Web Start 应用程序一般通过浏览器发布。只要 Java Web Start 应用程序下载到本地就可以启动它，而不需要浏览器。
+   Java Web Start 应用程序并不在浏览器窗口内。它将显示在浏览器外的一个属于自己的框架中。
+   Java Web Start 应用程序不使用浏览器的 Java 实现。浏览器只是在加载 Java Web Start 应用程序描述符时启动一个外部应用程序。这与启动诸如 Adobe Acrobat 或 RealAudio 这样的辅助应用程序所使用的机制一样。
+   数字签名应用程序可以被赋予访问本地机器的任意权限。未签名的应用程序只能运行在 "沙箱" 中，它可以阻止具有潜在危险的操作。

### 1. 发布 Java Web Start 应用

要想准备一个通过 Java Web Start 发布的应用程序，应该将其打包到一个或多个 JAR 文件中。然后创建一个 Java Network Launch Protocol（JNLP）格式的描述文件。将这些文件放置在 Web 服务器上。

还需要确保 Web 服务器对扩展名为 .jnlp 的文件报告一个 `application/x-java-jnlp-file` 的 MIME 类型。

>   提示：要想体验 Java Web Start，需要从 jakarta.apache.org/tomcat 上安装 Tomcat。Tomcat 是一个 servlet 和 JSP 页面的容器。也提供网页服务。它被预配置为服务于 JNLP 文件所对应的 MIME 类型。

发布 Java Web Start 应用步骤如下：

1）编译程序

```shell
javac -classpath .:jdk/jre/lib/javaws.jar webstart/*.java
```

2）使用下列命令创建一个 JAR 文件：

```shell
jar cvfe Calculator.jar webstart.Calculator webstart/*.class
```

3）使用下列内容准备启动文件 Calculator.jnlp：

```xml
<?xml version="1.0" encoding="utf-8"?>
<jnlp spec="1.0+" codebase="http://localhost:8080/calculator/" href="Calculator.jnlp">
  <information>
    <title>Calculator Demo Application</title>
    <vendor>Cay S. Horstmann</vendor>
    <description>Web Start Calculator</description>
    <icon href="webstart/calc_icon32.png" width="32" height="32" />
    <icon href="webstart/calc_icon64.png" width="64" height="64" />
    <offline-allowed/>
    <shortcut>
      <desktop/>
      <menu submenu="Accessories"/>
    </shortcut>
  </information>  
  <resources>	
    <java version="1.6.0+"/>
    <jar href="Calculator.jar"/>
  </resources>
  <application-desc/>
</jnlp> 
```

要想了解全部的规范，请参看 <www.oracle.com/technetwork/java/javase/javawebstart>。

4）如果使用 Tomcat，则在 Tomcat 安装的根目录上创建一个目录 tomcat/webapps/calculator。创建子目录 tomcat/webapps/calculator/WEB-INF，并且将最小的 web.xml 文件放置在 WEB-INF 子目录下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<web-app version="2.5" xmlns="http://java.sum.com/xml/ns/j2ee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://java.sun.com/xml/ns/j233
                             http://java.sun.com/xml/ns/j2ee/web-app_2_5.xsd">
</web-app>
```

5）将 JAR 文件和启动文件放入 tomcat/webapps/calculator 目录。

6）在 Java 控制面板中将 URL http://localhost:8080 增加到可信站点列表。或者为 JAR 文件签名。

7）在 tomcat/bin 目录执行启动脚本来启动 Tomcat。

8）将浏览器指向 JNLP 文件。例如，如果使用 Tomcat，则访问 <http://localhost:8080/calculator/Calculator.jnlp>。如果已经对浏览器完成了 Java Web Start 的有关配置，应该能看到 Java Web Start 的启动窗口。

如果你的浏览器不知道如何处理 JNLP 文件，可能会提供一个选项将它们与一个应用关联。如果是这样，请选择 `jdk/bin/javaws`。否则，明确如何将 MIME 类型 `application/x-java-jnlp-file` 与 javaws 应用关联。

9）当再次访问 JNLP 文件时，应用程序将从缓存中取出。可以利用 Java 插件控制面板查看缓存内容。

>    提示：如果在测试 JNLP 配置期间不想运行 web 服务器，可以通过执行下列命令临时性地覆盖启动文件中的 URL：
>
>   ```shell
>   javaws -codebase file://projectDirectory JNLPfile
>   ```
>
>   例如：
>
>   ```shell
>   javaws -codebase file://`pwd`Calculator.jnlp
>   ```

可以利用安装器安装桌面和菜单的快捷键。将下列代码添加到 JNLP 文件中：

```xml
<shortcut>
	<desktop />
    <menu submenu="Accessories" />
</shortcut>
```

还应该为菜单快捷键和启动屏幕提供一个图标。Oracle 建议提供 32 x 32 和 64 x 64 的图标。把这些图标文件与 JNLP 和 JAR 文件一起放在 Web 服务器上。将下列代码添加到 JNLP 文件的 information 节中：

```xml
<icon href="calc_icon32.png" width="32" height="32" />
<icon href="calc_icon64.png" width="64" height="64" />
```

>   注意：这些图标与应用程序图标无关。如果想让应用程序也有图标，需要将一个独立的图标图像添加到 JAR 文件中，并在框架类中调用 `setIconImage` 方法。

### 2. JNLP API

JNLP API 提供了下面的服务：

+   加载和保存文件
+   访问剪贴板
+   打印
+   下载文件
+   在默认的浏览器中显示一个文档
+   保存和获取持久性配置信息
+   确信只运行一个应用程序的实例

要访问服务，需要使用 `ServiceManager`，如下所示：

```java
FileSaveService service = (FileService) ServiceManager.lookup("javax.jnlp.FileSaveService");
```

>   注意：如果想要编译使用了 JNLP API 的程序，那就必须在类路径中包含 `javaws.jar` 文件。这个文件在 JDK 的 jre/lib 子目录下。

要保存文件，需要为文件对话框提供文件的初始路径名和文件扩展类型、要保存的数据和建议的文件名。例如：

```java
service.saveFileDialog(".", new String[] { "txt" }, data, "calc.txt");
```

数据必须由 `InputStream` 传递。这可能有些困难。程序使用下面的策略：

1）创建 `ByteArrayOutputStream` 用于存放需要保存的字节。

2）创建 `PrintStream` 用于将数据传递给 `ByteArrayOutputStream`。

3）将要保存的数据打印到 `PrintStream`。

4）建立 `ByteArrayInputStream` 用于读取保存的字节。

5）将上面的六传递给 `saveFileDialog` 方法。

要想从文件中读取数据，需要使用 `FileOpenService`。它的 `openFileDialog` 对话框接收应用程序提供的初始路径名和文件扩展名，并返回一个 `FileContents` 对象。然后调用 `getInputStream` 和 `getOutputStream` 方法来读写文件数据。如果用户没有选择文件，`openFileDialog` 方法将返回 null：

```java
FileOpenService service = (FileOpenService) ServiceManager.lookup("javax.jnlp.FileOpenService");
FileContents contents = service.openFileDialog(".", new String[] { "txt" });
if (contents != null) {
    InputStream in = contents.getInputStream();
    ...
}
```

>   注意：应用程序不知道文件名或文件所放置的位置。相反地，如果想要打开一个特定的文件，需要使用 `ExtendedService`：
>
>   ```java
>   FileOpenService service = (ExtendedService) ServiceManager.lookup("javax.jnlp.FileOpenService");
>   FileContents contents = service.openFile(new File("c:\\autoexec.bat"));
>   if (contents != null) {
>       InputStream in = contents.getInputStream();
>       ...
>   }
>   ```

要想在默认浏览器中显示一个文档，就需要使用 `BasicService` 接口。注意，有些系统可能没有默认的浏览器。

```java
BasicService service = (BasicService) ServiceManager.lookup("javax.jnlp.BasicService");
if (service.isWebBrowserSupported()) {
    service.showDocument(url);
} else {
    ...
}
```

因为应用程序是彼此分离的，一个特定的应用程序只能使用从 codebase 开始的 URL 键值。例如，如果一个应用程序是从 <http://myserver.com/apps> 下载的，那么它只能使用 <http://myserver.com/apps/subkey1/subkey2/..> 形式的键。访问其他键值的企图终将会失败。

应用程序可以调用 `BasicService` 类的 `getCodeBase` 方法查看它的 codebase。

可以调用 `PersistenceService` 中的 `create` 方法建立一个新的键：

```java
URL url new URL(codeBase, "mykey");
service.create(url, maxSize);
```

要想访问与某个特定键关联的信息，需要调用`get` 方法。这个方法将返回一个 `FileContents` 对象，通过这个对象可以对键数据进行读写。例如：

```java
FileContents contents = service.get(url);
InputStream in = contents.getInputStream();
OutputStream out = contents.getOutputStream(true);	// true = overwrite
```

### 3. 示例代码

```java
package webstart;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.MalformedURLException;
import java.net.URL;

import javax.jnlp.BasicService;
import javax.jnlp.FileContents;
import javax.jnlp.FileOpenService;
import javax.jnlp.FileSaveService;
import javax.jnlp.PersistenceService;
import javax.jnlp.ServiceManager;
import javax.jnlp.UnavailableServiceException;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;

/**
 * A frame with a calculator panel and a menu to load and save the calculator
 * history.
 */
public class CalculatorFrame extends JFrame {
   private CalculatorPanel panel;

   public CalculatorFrame() {
      setTitle();
      panel = new CalculatorPanel();
      add(panel);

      JMenu fileMenu = new JMenu("File");
      JMenuBar menuBar = new JMenuBar();
      menuBar.add(fileMenu);
      setJMenuBar(menuBar);

      JMenuItem openItem = fileMenu.add("Open");
      openItem.addActionListener(event -> open());
      JMenuItem saveItem = fileMenu.add("Save");
      saveItem.addActionListener(event -> save());

      pack();
   }

   /**
    * Gets the title from the persistent store or asks the user for the title if
    * there is no prior
    * entry.
    */
   public void setTitle() {
      try {
         String title = null;

         BasicService basic = (BasicService) ServiceManager.lookup("javax.jnlp.BasicService");
         URL codeBase = basic.getCodeBase();

         PersistenceService service = (PersistenceService) ServiceManager
               .lookup("javax.jnlp.PersistenceService");
         URL key = new URL(codeBase, "title");

         try {
            FileContents contents = service.get(key);
            InputStream in = contents.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            title = reader.readLine();
         } catch (FileNotFoundException e) {
            title = JOptionPane.showInputDialog("Please supply a frame title:");
            if (title == null)
               return;

            service.create(key, 100);
            FileContents contents = service.get(key);
            OutputStream out = contents.getOutputStream(true);
            PrintStream printOut = new PrintStream(out);
            printOut.print(title);
         }
         setTitle(title);
      } catch (UnavailableServiceException | IOException e) {
         JOptionPane.showMessageDialog(this, e);
      }
   }

   /**
    * Opens a history file and updates the display.
    */
   public void open() {
      try {
         FileOpenService service = (FileOpenService) ServiceManager
               .lookup("javax.jnlp.FileOpenService");
         FileContents contents = service.openFileDialog(".", new String[] { "txt" });

         JOptionPane.showMessageDialog(this, contents.getName());
         if (contents != null) {
            InputStream in = contents.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
               panel.append(line);
               panel.append("\n");
            }
         }
      } catch (UnavailableServiceException e) {
         JOptionPane.showMessageDialog(this, e);
      } catch (IOException e) {
         JOptionPane.showMessageDialog(this, e);
      }
   }

   /**
    * Saves the calculator history to a file.
    */
   public void save() {
      try {
         ByteArrayOutputStream out = new ByteArrayOutputStream();
         PrintStream printOut = new PrintStream(out);
         printOut.print(panel.getText());
         InputStream data = new ByteArrayInputStream(out.toByteArray());
         FileSaveService service = (FileSaveService) ServiceManager
               .lookup("javax.jnlp.FileSaveService");
         service.saveFileDialog(".", new String[] { "txt" }, data, "calc.txt");
      } catch (UnavailableServiceException e) {
         JOptionPane.showMessageDialog(this, e);
      } catch (IOException e) {
         JOptionPane.showMessageDialog(this, e);
      }
   }
}
```

