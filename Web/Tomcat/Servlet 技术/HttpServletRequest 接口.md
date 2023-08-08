`HttpServletRequest` 接口是 `ServletRequest` 接口的子接口。`HttpServletRequest` 接口提供了用于读取 HTTP 请求相关信息的方法：

+ `getContextPath()`：返回客户端所请求访问的 Web 应用的 URL 入口。例如，如果客户端访问的 URL 为 <http://localhost:8080/helloapp/info>，那么该方法返回 `/helloapp`。
+ `getCookies()`：返回 HTTP 请求中的所有 Cookie。
+ `getHeader(String name)`：返回 HTTP 请求头部的特定项。
+ `getHeaderNames()`：返回一个 `Enumeration` 对象，它包含了 HTTP 请求头部的所有项目名。
+ `getMethod()`：返回 HTTP 请求方式。
+ `getRequestURI()`：返回 HTTP 请求的头部的第 1 行中的 URI。
+ `getQueryString()`：返回 HTTP 请求中的查询字符串，即 URL 中 `?` 后面的内容。例如，如果客户端访问的 URL 为 <http://localhost:8080/helloapp/info?username=Tom>，那么该方法返回 `username=Tom`。

**示例代码：RequestInfoServlet.java**

```java
package mypack;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class RequestInfoServlet extends HttpServlet {

	/**
	 * 响应客户请求
	 */
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// 设置 HTTP 响应的正文的数据类型
		resp.setContentType("text/html;charset=GBK");
		
		// 输出 HTML 文档
		PrintWriter out = resp.getWriter();
		out.println("<html><head><title>RequestInfo</title></head>");
		out.println("<body>");
		// 打印服务器端的 IP 地址
		out.println("<br>LocalAddr: " + req.getLocalAddr());
		// 打印服务器端的主机名
		out.println("<br>LocalName: " + req.getLocalName());
		// 打印服务器端的 FTP 端口号
		out.println("<br>LocalPort: " + req.getLocalPort());
		// 打印客户端与服务器通信所用的协议的名称以及版本号
		out.println("<br>Protocol: " + req.getProtocol());
		// 打印客户端的 IP 地址
		out.println("<br>RemoteAdd: " + req.getRemoteAddr());
		// 打印客户端的主机名
		out.println("<br>RemoteHost: " + req.getRemoteHost());
		// 打印客户端的 FTP 端口
		out.println("<br>RemotePort: " + req.getRemotePort());
		// 打印 HTTP 请求方式
		out.println("<br>Method: " + req.getMethod());
		// 打印 HTTP 请求中的 URL
		out.println("<br>URI: " + req.getRequestURI());
		// 打印客户端所请求访问的 Web 应用的 URL 入口
		out.println("<br>ContextPath: " + req.getContextPath());
		// 打印 HTTP 请求中的查询字符串
		out.println("<br>QueryString: " + req.getQueryString());
		// 打印 HTTP 请求头
		out.println("<br>****打印 HTTP 请求头****");
		Enumeration eu = req.getHeaderNames();
		while (eu.hasMoreElements()) {
			String headerName = (String) eu.nextElement();
			out.println("<br>" + headerName + ": " + req.getHeader(headerName));
		}
		out.println("<br>****打印 HTTP 请求头结束****<br>");
		// 打印请求参数 username
		out.println("<br>username: " + req.getParameter("username"));
		out.println("</body></html>");
		
		// 关闭输出流
		out.close();
	}
}
```

