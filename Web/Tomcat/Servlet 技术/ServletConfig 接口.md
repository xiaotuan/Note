`Servlet` 接口的 `init(ServletConfig config)` 方法有一个 `ServletConfig` 类型的参数。当 `Servlet` 容器初始化一个 `Servlet` 对象时，会为这个 `Servlet` 对象创建一个 `ServletConfig` 对象。`ServletConfig` 对象中包含了 `Servlet` 的初始化参数信息，此外，`ServletConfig` 对象还与当前 `Web` 应用的 `ServletContext` 对象关联。

`ServletConfig` 接口中定义了一下方法：

+ `getInitParameter(String name)`：根据给定的初始化参数名，返回匹配的初始化参数值。
+ `getInitParameterNames()`：返回一个 `Enumeration` 对象，里面包含了所有的初始化参数名。
+ `getServletContext()`：返回一个 `ServletContext` 对象。
+ `getServletName()`：返回 `Servlet` 的名字，即 `web.xml` 文件中相应 `<servlet>` 元素的 `<servlet-name>` 子元素的值。如果没有为 `Servlet` 配置 `<servlet-name>` 子元素，则返回 `Servlet` 类的名字。

在 `web.xml` 文件中配置一个 `Servlet` 时，可以通过 `<init-param>` 元素来设置初始化参数。`<init-param>` 元素的 `<param-name>` 子元素设定参数名，`<param-value>` 子元素设定参数值。

```xml
<servlet>
	<servlet-name>Font</servlet-name>
    <servlet-class>mypack.FontServlet</servlet-class>
    <init-param>
    	<param-name>color</param-name>
        <param-value>blue</param-value>
    </init-param>
    <init-param>
    	<param-name>size</param-name>
        <param-value>15</param-value>
    </init-param>
</servlet>

<servlet-mapping>
	<servlet-name>Font</servlet-name>
    <url-pattern>/font</url-pattern>
</servlet-mapping>
```

**示例代码：FontServlet.java**

```java
package mypack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FontServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 获得 word 请求参数
		String word = req.getParameter("word");
		if (word == null) {
			word = "Hello";
		}
		
		// 读取初始化参数
		String color = getInitParameter("color");
		String size = getInitParameter("size");
		System.out.println("servletName: " + getServletName());	// 打印 servletName: Font
		
		// 设置 HTTP 响应的正文的 MIME 类型及字符编码
		resp.setContentType("text/html;charset=GBK");
		
		// 输出 HTML 文档
		PrintWriter out = resp.getWriter();
		out.println("<html><head><title>FontServlet</title></head>");
		out.println("<body>");
		out.println("<font size='" + size + "' color='" + color + "'>" + word + "</font>");
		out.println("</body></html>");
		
		out.close();	// 关闭 PrintWriter
	}
}
```

