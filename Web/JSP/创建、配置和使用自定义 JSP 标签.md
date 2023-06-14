以下是创建、配置和使用 `hello` 标签的步骤：

（1）编写用于处理 `hello` 标签的类，名为 `HelloTag` 类。

**HelloTag.java**

```java
package mypack;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspTagException;
import javax.servlet.jsp.tagext.TagSupport;

public class HelloTag extends TagSupport {
    
    // 当 JSP 解析器遇到 hello 标签的结束标志时，调用此方法
    public int doEndTag() throws JspException {
        try {
            // 打印字符串 "Hello"
            pageContext.getOut().print("Hello");
        } catch (Exception e) {
            throw new JspTagException(e.getMessage());
        }
        return EVAL_PAGE;
    }
}
```

编译 `HelloTag.java` 时，需要将 `Servlet API` 的类库文件（`servlet-api.jar`） 以及  `JSP API` 的类库文件（`jsp-api.jar`）添加到 `classpath` 中，这两个 `JAR` 文件位于 `<CATALINA_HOME>/lib` 目录下。编译生成的 `HelloTag.class` 存放位置为 `WEB-INF/classes/mypack/HelloTag.class`。

（2）创建一个 `TLD` （`Tag Library Descriptor`，标签库描述符）文件。假定 `hello` 标签位于 `mytaglib` 标签库中，因此创建一个名为 `mytaglib.tld` 的 `TLD` 文件。在这个文件中定义 `mytaglib` 标签库和 `hello` 标签。这个文件的存放位置为 `WEB-INF/mytaglib.tld`。

**mytaglib.tld**

```xml
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE taglib PUBLIC "...//Sun Microsystems, Inc.//DTD JSP Tag Library 1.2//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_2.dtd">
<!-- a tag library descriptor -->

<taglib>
	<tlib-version>1.1</tlib-version>
    <jsp-version>2.4</jsp-version>
    <short-name>mytaglib</short-name>
    <uri>/mytaglib</uri>
    
    <tag>
    	<name>hello</name>
        <tag-class>mypack.HelloTag</tag-class>
        <body-content>empty</body-content>
        <description>Just Says Hello</description>
    </tag>
</taglib>
```

> 提示：`Servlet` 规范规定，`TLD` 文件在 `Web` 应用中必须存放在 `WEB-INF` 目录或者自定义的子目录下，但不能放在 `WEB-INF\classes` 目录和 `WEB-INF\lib` 目录下。`web.xml` 文件中的 `<taglib>` 元素的 `<taglib-location>` 子元素用来设置标签库描述文件的存放路径，应该保证 `<taglib-location>` 子元素的取值与 `TLD` 文件的实际存放位置相符。

（3）在 `web.xml` 文件中配置 `<taglib>` 元素。

**web.xml**

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

	<servlet>
  		<servlet-name>dispatcher</servlet-name>  
      	<servlet-class>mypack.DispatcherServlet</servlet-class>
  	</servlet>
    
    <servlet-mapping>
    	<servlet-name>dispatcher</servlet-name>
        <url-pattern>/dispatcher</url-pattern>
    </servlet-mapping>
    
    <welcome-file-list>
    	<welcome-file>login.html</welcome-file>
    </welcome-file-list>

    <jsp-config>
    	<taglib>
        	<taglib-uri>/mytaglib</taglib-uri>
        	<taglib-location>/WEB-INF/mytaglib.tld</taglib-location>
    	</taglib>
    </jsp-config>
</web-app>
```

`<taglib-uri>` 指定标签库的 `URI`；`<taglib-location>` 指定标签库的 `TLD` 文件的存放位置。

（4）在 `hello.jsp` 文件中使用 `hello` 标签。首先，在 `hello.jsp` 中加入引用 `mytaglib` 标签库的 `taglib` 标签的指令：

```xml
<%@ taglib uri="/mytaglib" prefix="mm" %>
```

`prefix` 属性用来为 `mytaglib` 标签库指定一个前缀 `mm`。接下来，`hello.jsp` 就可以用 `<mm: hello/>` 的形式来使用 `hello` 标签。

**hello.jsp**

```jsp
<% taglib uri="/mytaglib" prefix="mm" %>
<html>
    <head>
        <title>helloapp</title>
    </head>
    <body>
        <b><mm: hello/>: <%= requet.getAttribute("USER") %></b>
    </body>
</html>
```

当客户端请求访问 `hello.jsp` 时，`Servlet` 容器会按照如下步骤处理 `hello.jsp` 中的 `<mm: hello/>` 标签。

（1）由于 `<mm: hello/>` 的前缀为 `mm`，与 `hello.jsp` 中的如下 `taglib` 指令匹配：

```jsp
<% taglib uri="/mytaglib" prefix="mm" %>
```

由此得知 `hello` 标签来自 `URI` 为 `/mytaglib` 的标签库。

（2）在 `web.xml` 文件中对 `URI` 为 `/mytaglib` 的标签库的匹配如下：

```xml
<taglib>
    <taglib-uri>/mytaglib</taglib-uri>
    <taglib-location>/WEB-INF/mytaglib.tld</taglib-location>
</taglib>
```

由此得知 `URI` 为 `/mytaglib` 的标签库的 `TLD` 文件为 `WEB-INF/mytaglib.tld`。

（3）在 `WEB-INF/mytaglib.tld` 文件中对名为 `hello` 的标签的定义如下：

```xml
<tag>
    <name>hello</name>
    <tag-class>mypack.HelloTag</tag-class>
    <body-content>empty</body-content>
    <description>Just Says Hello</description>
</tag>
```

由此得知 `hello` 标签的处理类为 `mypack.HelloTag` 类。因此当 `Servlet` 容器运行 `hello.jsp` 时，如果遇到 `<mm: hello/>` 标签，就会加载 `WEB-INF/classes/mypack` 目录下的 `HelloTag.class` 文件。遇到 `<mm: hello/>` 标签的结束标志时，就会调用 `HelloTag` 类的 `doEndTag()` 方法。
