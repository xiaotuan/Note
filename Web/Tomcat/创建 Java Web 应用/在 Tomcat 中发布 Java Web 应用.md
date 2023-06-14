[toc]

尽管发布的具体细节依赖于 `Tomcat` 本身的实现，但是以下关于发布 `Java Web` 应用的基本思想适用于所有 `Servlet` 容器：

+ 把 `Web` 应用的所有文件复制到 `Servlet` 容器的特定目录下，这是发布 `Web` 应用的最快捷的一种方式。
+ 各种 `Servlet` 容器实现都会从 `Web` 应用的 `web.xml` 配置文件中读取有关 `Web` 组件的配置信息。
+ 为了使用户能更加灵活自如地控制 `Servlet` 容器发布和运行 `Web` 应用的行为，并且为了使 `Servlet` 容器与 `Web` 应用能进行更紧密地协作，许多 `Servlet` 容器还允许用户使用额外的配置文件及配置元素，这些配置文件及配置元素的语法由 `Servlet` 容器的实现决定，与 `Oracle` 公司的 `Servlet` 规范无关。

### 1. Tomcat 的目录结构

<center><b>Tomcat 9.x 的目录结构</b></center>

| 目录     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| /bin     | 存放在 Window 平台以及 Linux 平台上启动和关闭 Tomcat 的脚本文件 |
| /conf    | 存放 Tomcat 服务器的各种配置文件，其中最重要的配置文件是 server.xml |
| /lib     | 存放 Tomcat 服务器以及所有 Web 应用都可以访问的 JAR 文件     |
| /webapps | 在 Tomcat 上发布 Java Web 应用时，默认情况下把 Web 应用文件存放于此目录下 |
| /work    | Tomcat 的工作目录，Tomcat 在运行时把生成的一些工作文件放于此目录下。例如，默认情况下，Tomcat 把编译 JSP 而生成的 Servlet 类文件放于此目录下。 |

假如 `Tomcat` 的类加载器要为一个 `Java Web` 应用加载一个名为 `Sample` 的类，类加载器会按照以下先后顺序到各个目录中去查找 `Sample` 类的 `.class` 文件，直到找到为止，如果所有目录中都不存在 `Sample.class`，则会抛出异常：

（1）在 `Java Web` 应用的 `WEB-INF/classes` 目录下查找 `Sample.class` 文件。

（2）在 `Java Web` 应用的 `WEB-INF/lib` 目录下的 `JAR` 文件中查找 `Sample.class` 文件。

（3）在 `Tomcat` 的 `lib`子目录下直接查找 `Sample.class` 文件。

（4）在 `Tomcat` 的 `lib` 子目录下的 `JAR` 文件中查找 `Sample.class` 文件。

如果想进一步了解 `Tomcat` 的类加载器的工作过程，请参考 `Tomcat` 的有关文档，地址为：`<CATALINA_HOME>/webapps/docs/class-loader-howto.html`。

### 2. 按照默认方式发布 Java Web 应用

在 `Tomcat` 中发布 `Java Web` 应用的最快捷的方式，就是直接把 `Java Web` 应用的所有文件复制到 `Tomcat` 的 `<CATALINA_HOME>/webapps` 目录下。

在 `Web` 应用的开发阶段，为了便于调试，通常采用开放式的目录结构来发布 `Web` 应用，这样可以方便地更新或替换文件。如果开发完毕，进入产品发布阶段，应该将整个 `Web` 应用打包为 `WAR`文件，再进行发布。在 `helloapp` 示例中，按如下步骤发布 `helloapp`：

（1）在 `DOS` 中进入 `helloapp` 应用的根目录 `helloapp`。

（2）把整个 `Web` 应用打包为 `helloapp.war` 文件，命令如下：

```shell
C:\chapter03\helloapp>jar cvf C:\chapter03\helloapp.war *
```

（3）如果在 `Tomcat` 的 `webapps` 目录下已经有 `helloapp` 子目录，先将 `helloapp` 子目录删除。

（4）把 `helloapp.war` 文件复制到 `<CATALINA_HOME>/webapps` 目录下。

（5）启动 `Tomcat` 服务器。

### 3. Web 组件的 URL

无论按照开放式目录结构还是按照打包文件方式发布 `Web` 应用，`Web` 应用的默认 `URL` 入口都是 `Web` 应用的根目录名。例如对于 `helloapp` 应用，它的 `URL` 入口为 `/helloapp`。

> 提示：
>
> 浏览器无法直接访问 `Web` 应用的 `WEB-INF` 目录下的文件。因此，如果出于安全的原因，不希望浏览器直接访问某个 `JSP` 文件，可以把它放到 `WEB-INF` 目录或其子目录下。在这种情况下，只有服务器端的组件才能访问该 `JSP` 文件，例如 `Servlet` 可以把请求转发给 `JSP` 文件。

对于 `Servlet`，对其映射 `URL` 有两种方式：

+ 在 `web.xml` 文件中映射 `URL`。
+ 用 `@WebServlet` 注解来映射 `URL`。

在本范例中，`web.xml` 文件对 `mypack.DispatcherServlet` 类做了如下配置：

```xml
<servlet>
    <servlet-name>dispatcher</servlet-name>
    <servlet-class>mypack.DispatcherServlet</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>dispatcher</servlet-name>
    <url-pattern>/dispatcher</url-pattern>
</servlet-mapping>
```

当浏览器端首次通过该 `URL` 请求访问 `DispatcherServlet` 时，`Tomcat` 需要先找到文件系统中的 `DispatcherServlet.class` 文件，从而能加载 `DispatcherServlet` 类。`Tomcat` 查找 `DispatcherServlet.class` 文件的步骤如下：

（1）参考 `helloapp` 应用的 `web.xml` 文件，找到 `<url-pattern>` 子元素的值为 `/dispatcher` 的 `<servlet-mapping>` 元素。

（2）读取 `<servlet-mapping>` 元素的 `<servlet-name>` 子元素的值，由此确定 `Servlet` 的名字为 `dispatcher`。

（3）找到 `<servlet-name>` 子元素的值为 `dispatcher` 的 `<servlet>` 元素。

（4）读取 `<servlet>` 元素的 `<servlet-class>` 子元素的值，由此确定 `Servlet` 的类名为 `mypack.DispatcherServlet`。

（5）到 `<CATALINA_HOME>/webapps/helloapp/WEB-INF/classes/mypack` 目录下查找 `DispatcherServlet.class` 文件。

初学者发布了 `Servlet` 后，再通过浏览器访问该 `Servlet` 时，服务器可能会返回 ”该文件不存在“ 的错误。这可能是由以下原因导致的：

（1）提供的 URL 不正确。

（2）`web.xml` 作为 `XML` 格式的文件，需要区分大小写。如果不注意大小写，可能会导致对 `Servlet` 的配置不正确。

（3）`Servlet` 的 `.class` 文件的存放路径不正确。

`Servlet` 规范之所以要对 `Servlet` 进行 `URL` 映射，主要由两个原因：

（1）为一个 `Servlet` 对应多个 `URL` 提供了方便的设置途径。假如有个 `Web` 应用规定所有以 `.DO` 结尾的 `URL` 都由 `ActionServlet` 来处理，那么只需在 `web.xml` 文件中对 `ActionServlet` 进行如下配置：

```xml
<servlet>
	<servlet-name>action</servlet-name>
    <servlet-class>mypack1.mypack2.ActionServlet</servlet-class>
</servlet>
<servlet-mapping>
	<servlet-name>action</servlet-name>
    <url-pattern>*.DO</url-pattern>
</servlet-mapping>
```

这样，所有以 `.DO` 结尾的 `URL` 都对应 `ActionServlet`，例如以下 `URL` 都映射到 `ActionServlet`：

```
http://localhost:8080/mywebapp/login.DO
http://localhost:8080/mywebapp/logout.DO
http://localhost:8080/mywebapp/checkout.DO
```

再例如一个 `<servlet>` 还可以对应多个 `<servlet-mapping>` 元素：

```xml
<servlet>
	<servlet-name>Manager</servlet-name>
    <servlet-class>org.apache.catalina.manager.ManagerServlet</servlet-class>
    <init-param>
    	<param-name>debug</param-name>
        <param-value>2</param-value>
    </init-param>
</servlet>
<servlet-mapping>
	<servlet-name>Manager</servlet-name>
    <url-pattern>/list</url-pattern>
</servlet-mapping>
<servlet-mapping>
	<servlet-name>Manager</servlet-name>
    <url-pattern>/expire</url-pattern>
</servlet-mapping>
<servlet-mapping>
	<servlet-name>Manager</servlet-name>
    <url-pattern>/sessions</url-pattern>
</servlet-mapping>
<servlet-mapping>
	<servlet-name>Manager</servlet-name>
    <url-pattern>/start</url-pattern>
</servlet-mapping>
```

（2）简化 `Servlet` 的 `URL`，并且可以向客户端隐藏 `Web` 应用的实现细节。如果在 `URL` 中暴露 `Servlet` 的完整类名，会让不懂 `Java Web` 开发的普通客户觉得 `URL` 很复杂，不容易理解和记忆。

### 4. 配置 Tomcat 的 \<Context> 元素

`<Context>` 元素是 `Tomcat` 中使用最频繁的元素，它代表了运行在虚拟机 `<Host>` 上的单个 `Web` 应用。一个 `<Engine>` 中可以有多个 `<Host>`，一个 `<Host>` 中可以有多个 `<Context>`。`<Context>` 元素的主要属性说明如下：

| 属性       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| path       | 指定访问该 Web 应用的 URL 入口                               |
| docBase    | 指定 `Web` 应用的文件路径，可以给定绝对路径，也可以给定相对于 `<Host>` 的 `appBase` 属性的相对路径。如果 Web 应用采用开发目录结构，则指定 `Web` 应用的根目录；如果 `Web` 应用是个 `WAR` 文件，则指定 `WAR` 文件的路径。 |
| className  | 指定实现 `Context` 组件的 `Java` 类的名字，这个 `Java` 类必须实现 `org.apache.catalina.Context` 接口。该属性的默认值为 `org.apache.catalina.core.StandardContext` |
| reloadable | 如果这个属性设为 true，Tomcat 服务器在运行状态下会监视在 `WEB-INF/classes` 和 `WEB-INF/lib` 目录下 `.class` 类文件或 `.jar` 类库文件的改动，如果监测到有类文件或类库文件被更新，服务器会自动重新加载 Web 应用，该属性的默认值为 false。在 Web 应用的开发和调试阶段，把 `reloadable` 设为 `true`，可以方便对 `Web` 应用的调试。在 `Web` 应用正式发布阶段，把 `reloadable` 设为 `false`，可以降低 `Tomcat` 的运行负荷，提高 `Tomcat` 的运行性能。 |

一般情况下，`<Context>` 元素都会使用默认的标准 `Context` 组件，即 `className` 属性采用默认值 `org.apache.catalina.core.StandardContext`。标准 `Context` 组件除了具有上表列出的属性，还具有下表的专有属性：

| 属性        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| unloadDelay | 设定 `Tomcat` 等待 `Servlet` 卸载的毫秒数。该属性的默认值为 2000 毫秒。 |
| workDir     | 指定 `Web` 应用的工作目录。`Tomcat` 运行时会把与这个 `Web` 应用相关的临时文件放在此目录下 |
| uppackWar   | 如果此项设为 true，表示将把 `Web` 应用的 `WAR` 文件先展开为开发目录结构后再运行。如果设为 `false`，则直接运行 `WAR` 文件。该属性默认值为 `true`。 |

在 `Tomcat` 低版本中，允许直接在 `<CATALINA_HOME>/conf/server.xml` 文件中配置 `<Context>` 元素。这种配置方式有一个弊端：如果在 `Tomcat` 运行时修改 `server.xml` 文件，那么所做的修改不会立即生效，而必须重新启动 `Tomcat`，才能使所做的修改生效。

当 `Tomcat` 加载一个 `Web` 应用时，会按照以下顺序查找 `Web` 应用的 `<Context>` 元素：

（1）到 `<CATALINA_HOME>/conf/context.xml` 文件中查找 `<Context>` 元素。这个文件中的 `<Context>` 元素。这个文件中的 `<Context>` 元素的信息适用于所有 `Web` 应用。

（2）到 `<CATALINA_HOME>/conf/[enginename]/[hostname]/context.xml.default` 文件中查找 `<Context>` 元素。`[enginename]` 表示 `<Engine>` 的 `name` 属性，`[hostname]` 表示 `<Host>` 的 `name` 属性。在 `context.xml.default` 文件中的 `<Context>` 元素的信息适用于当前虚拟主机中的所有 `Web` 应用：

```
<CATALINA_HOME>/conf/Catalina/localhost/context.xml.default
```

（3）到 `<CATALINA_HOME>/conf/[enginename]/[hostname]/[contextpath].xml` 文件中查找 `<Context>` 元素。`[contextpath]` 表示单个 `Web` 应用的 `URL` 入口。在 `[contextpath].xml` 文件中的 `<Context>` 元素的信息只适用于单个 `Web` 应用。例如以下文件中的 `<Context>` 元素适用于名为 `Catalina` 的 `Engine` 下的 `localhost` 主机中的 `helloapp` 应用：

```
<CATALINA_HOME>/conf/Catalina/localhost/helloapp.xml
```

（4）到 `Web` 应用的 `META-INF/context.xml` 文件中查找 `<Context>` 元素。这个文件中的 `<Context>` 元素的信息适用于当前 `Web` 应用。

（5）到 `<CATALINA_HOME>/conf/server.xml` 文件中的 `<Host>` 元素中查找 `<Context>` 子元素。该 `<Context>` 元素的信息只适用于单个 `Web` 应用。

如果仅仅为单个 `Web` 应用配置 `<Context>` 元素，可以优先选择第三种或第四种方式。第三种方式要求在 `Tomcat` 的相关目录下增加一个包含 `<Context>` 元素的配置文件，而第四种方式则要求在 `Web` 应用的相关目录下增加一个包含 `<Context>` 元素的配置文件。对于这两种方式，`Tomcat` 在运行时会监测包含 `<Context>` 元素的配置文件是否被更新，如果被更新，`Tomcat` 会自动重新加载并启动 `Web` 应用，使对 `<Context>` 元素所作的修改生效。

下面先采用第四种方式配置 `<Context>` 元素。在 `helloapp` 目录下新建一个 `META-INF` 子目录，然后在其中创建一个 `context.xml` 文件，它的内容如下：

```xml
<Context path="/helloapp" docBase="helloapp" reloadable="true" />
```

以上 `<Context>` 元素的 `docBase` 属性表明，`helloapp` 应用的文件路径为 `<CATALINA_HOME>/webapps/helloapp`；`path` 属性表明访问 `helloapp` 应用的 `URL` 入口为 `/helloapp`。

下面再采用第三种方式配置 `<Context>` 元素。假定 `helloapp` 应用的文件路径为 `C:\chapter03\helloapp`，并且在 `<CATALINA_HOME>/webapps` 目录下没有发布 `helloapp` 应用。在 `<CATALINA_HOME>/conf` 目录下先创建 `Catalina` 目录，接着在 `Catalina` 目录下再创建 `localhost` 目录，然后在 `<CATALINA_HOME>/conf/Catalina/localhost/` 目录下创建 `helloapp.xml` 文件，它的内容如下：

```xml
<Context path="/helloapp"
         docBase="C:\chapter03\helloapp"
         reloadable="true" />
```

由于 `helloapp.xml` 文件位于 `Catalina/localhost/` 子目录下，因此 `helloapp` 应用将运行在名为 `Catalina` 的 `Engine` 组件的 `localhost` 虚拟主机中。访问 `helloapp` 应用中的 `login.html` 和 `hello.jsp` 的 `URL` 分别为：

```
http://localhost:8080/helloapp/login.html
http://localhost:8080/helloapp/hello.jsp
```

在 `server.xml` 文件中已经有一个名为 `localhost` 的 `<Host>` 元素，如果采用第五种方式配置 `<Context>` 元素，最常见的做法是在该 `<Host>` 元素中插入 `<Context>` 子元素，例如：

```xml
<Host name="localhost" appBase="webapps"
      unpackWARs="true" autoDeploy="true"
      xmlValidation="false" xmlNamespaceAware="false">
	......
    <Context path="/helloapp" docBase="helloapp" reloadable="true" />
</Host>
```

### 5. 配置 Tomcat 的虚拟主机

在 `Tomcat` 的配置文件 `server.xml` 中，`<Host>` 元素代表虚拟主机，在同一个 `<Engine>` 元素下可以配置多个虚拟主机。例如，有两个公司的 `Web` 应用都发布在同一个 `Tomcat` 服务器上，可以为每家公司分别创建一个虚拟主机，它们的虚拟主机名分别为：

```
www.javathinkorok.com
www.javathinkerext.com
```

尽管以上两个虚拟主机实际上对应同一个主机，但是当客户端通过以上两个不同的虚拟主机名访问 `Web` 应用时，客户端会感觉这两个应用分别拥有独立的主机。

此外，还可以为虚拟主机建立别名。下面介绍如何配置 `www.javathinkerok.com` 虚拟主机。

（1）打开 `<CATALINA_HOME>/conf/server.xml` 文件，会发现在 `<Engine>` 元素中已经有一个名为 `localhost` 的 `<Host>` 元素，可以在它的后面（即 `</Host>` 标记后面）加入如下 `<Host>` 元素：

```xml
<Host name="www.javathinkerok.com" appBase="C:\javathinkerok" unpackWARs="true" autoDeploy="true">
	<Alias>javathinkerok.com</Alias>
    <Alias>javathinkerok</Alias>
</Host>
```

`<Host>` 元素还有一个子元素 `<Alias>`，它用于指定虚拟主机的别名。`<Host>` 元素允许包含多个 `<Alias>` 子元素，因此可以指定多个别名。

<center><b>&lt;Host&gt; 元素的属性</b></center>

| 属性            | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| name            | 指定虚拟主机的名字                                           |
| className       | 指定实现虚拟主机的 `Java` 类的名字，这个 `Java` 类必须实现 `org.apache.cataline.Host` 接口。该属性的默认值为 `org.apache.catalina.core.StandardHost` |
| appBase         | 指定虚拟主机的目录，可以指定绝对目录，也可以指定相对于 `<CATALINA_HOME>` 的相对目录。如果此项没有设定，默认值为 `<CATALINA_HOME>/webapps` |
| autoDeploy      | 如果此项设为 `true`，表示当 `Tomcat` 服务器处于运行状态时，能够监测 `appBase` 下的文件，如果有新的 `Web` 应用加入进来，则会自动发布这个 `Web` 应用 |
| deployOnStartup | 如果此项设为 `true`，则表示 `Tomcat` 启动时会自动发布 `appBase` 目录下所有的 `Web` 应用。如果 `Web` 应用没有相应的 `<Context>` 元素，那么 `Tomcat` 会提供一个默认的 `Context` 组件。`deployOnStartup` 的默认值为 `true`。 |

一般情况下，`<Host>` 元素都会使用默认的标准虚拟主机，即 `className` 属性使用默认值 `org.apache.catalina.core.StandardHost`。标准虚拟主机还具有以下属性：

| 属性       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| unpackWARs | 如果此项设为 `true`，表示将把 `appBase` 属性指定的目录下的 `Web` 应用的 `WAR` 文件先展开为开放目录结构后再运行。如果设为 `false`，则直接运行 `WAR` 文件。 |
| workDir    | 指定虚拟主机的工作目录。`Tomcat` 运行时会把与这个虚拟主机的所有 `Web` 应用相关的临时文件放在此目录下。它的默认值为 `<CATALINA_HOME>/work`。如果 `<Host>` 元素下的一个 `<Context>` 元素也设置了 `workDir` 属性，那么 `<Context>` 元素的 `workDir` 属性会覆盖 `<Host>` 元素的 `workDir` 属性 |
| deployXML  | 如果设为 `false`，那么 `Tomcat` 不会解析 `Web` 应用中的用于设置 `Context` 元素的 `META-INF/context.xml` 文件。出于安全原因，如果不希望 `Web` 应用中包含 `Tomcat` 的配置元素，就可以把这个属性设置为 `false`，在这种情况下，应该在 `<CATALINA_HOME>/conf/[enfinename]/[hostname]` 下设置 `Context` 元素。该属性的默认值为 `true`。 |

（2）把 `helloapp` 应用（`helloapp.war` 文件或者是整个 `helloapp` 目录）复制到 `<Host>` 元素的 `appBase` 属性指定的目录 `C:\javathinkerok` 下。

（3）为了使以上配置的虚拟主机生效，必须在 `DNS` 服务器中注册以上虚拟主机名和别名，使它们和 `Tomcat` 服务器所在的主机的 `IP` 地址进行映射。

（4）重启 `Tomcat` 服务器，然后通过浏览器访问：

```
http://www.javathinkerok.com:8080/helloapp/login.html
```

每个虚拟主机都可以有一个默认 `Web` 应用，它的默认根目录为 `ROOT`。例如在 `<CATALINA_HOME>/webapps` 目录下有一个 `ROOT` 目录，它是 `localhost` 虚拟主机的默认 `Web` 应用，访问 <http://localhost:8080/index.jsp>，就会显示这个 `Web` 应用的 `index.jsp` 页面。

对于 <www.javathinkerok.com> 虚拟主机，也可以提供默认的 `Web` 应用。把 `C:\javathinkerok` 下的 `helloapp` 目录改名为 `ROOT` 目录，这个虚拟主机就有了一个默认 `Web` 应用。访问 <http://www.javathinkerok.com:8080/login.html>，就会显示这个 `Web` 应用的 `login.html` 页面。

> 提示：如果要设置虚拟主机的默认 `Web` 应用的 `<Context>` 元素，那么它的 `path` 属性值应该为一个空的字符串（即 `path=""`）。
