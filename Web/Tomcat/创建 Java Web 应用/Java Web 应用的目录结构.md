<center><b>Java Web 应用的目录结构</b></center>

| 目录                      | 描述                                                         |
| ------------------------- | ------------------------------------------------------------ |
| /helloapp                 | Web 应用的根目录，所有的 JSP 和 HTML 文件都存放于此目录或子目录下 |
| /helloapp/WEB-INF         | 存放 Web 应用的配置文件 web.xml                              |
| /helloapp/WEB-INF/classes | 存放各种 .class 文件，Servlet 类的 .class 文件也存放于此目录下 |
| /helloapp/WEB-INF/lib     | 存放 Web 应用所需的各种 JAR 文件（类库文件）。例如，在这个目录下可以存放 JDBC 驱动程序的 JAR文件。 |

在运行时，`Servlet` 容器的类加载器先加载 `classes` 目录下的类，再加载 `lib` 目录下的 `JAR` 文件中的类。因此，如果两个目录下存在同名的类，`classes` 目录下的类具有优先权。

> 提示：
>
> 在开发阶段，为了便于调试和运行 `helloapp` 应用，可以直接在 `Tomcat` 的 `<CATALINA_HOME>/webapps` 目录下创建该 `Web` 应用的目录结构。

