当操作一个 `URLConnectiong` 对象时，必须像下面这样非常小心地安排操作步骤：

1）调用 `URL` 类中的 `openConnection` 方法获得 `URLConnection` 对象：

```java
URLConnection connection = url.openConnection();
```

2）使用以下方法来设置任意的请求属性：

```
setDoInput
setDoOutput
setIfModifiedSince
setUseCaches
setAllowUserInteraction
setRequestProperty
setConnectTimeout
setReadTimeout
```

3）调用 `connect` 方法连接远程资源：

```java
connection.connect();
```

4）与服务器建立连接后，你可以查询头信息。`getHeaderFieldKey` 和 `getHeaderField` 这两个方法枚举了消息头的所有字段。`getHeaderFields` 方法返回一个包含了消息头中所有字段的标准 `Map` 对象。为了方便使用，以下方法可以查询各种标准字段：

```
getContentType
getContentLength
getContentEncoding
getDate
getExpiration
getLastModified
```

5）最后，访问资源数据。使用 `getInputStream` 方法获取一个输入流用以读取信息（这个输入流与 `URL` 类中的 `openStream` 方法所返回的流相同）。另一个方法 `getContent` 在实际操作中并不是很有用。由标准内容类型（比如 `text/plain` 和 `image/gif`）所返回的对象需要使用 `com.sun` 层次结构中的类来进行处理。

> 警告：一些程序员在使用 `URLConnection` 类的过程中形成了错误的观念，他们认为 `URLConnection` 类中的 `getInputStream` 和 `getOutputStream` 方法与 `Socket` 类中的这些方法相似，但是这种想法并不十分正确。`URLConnection` 类具有很多表象之下的神奇功能，尤其在处理请求和响应消息头时。正因为如此，严格遵循建立连接的每个步骤显得非常重要。

有几个方法可以在与服务器建立连接之前设置连接属性，其中最重要的是 `setDoInput` 和 `setDoOutput`。在默认情况下，建立的连接只产生服务器读取信息的输入流，并不产生任何执行写操作的输出流。如果想获得输出流（例如，用于向一个 `Web` 服务器提交数据），那么你需要调用：

```java
connection.setDoOutput(true);
```

接下来，也许想设置某些请求头。请求头是与请求命令一起被发送到服务器的。例如：

```
GET www.server.com/index.html HTTP/1.0
Referer: http://www.somewhere.com/links.html
Proxy-Connection: Keep-Alive
User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.4)
Host: www.server.com
Accept: text/html, image/gif, image/jpeg, image/png, */*
Accept-Language: en
Accept-Charset: iso-8859-1,*,utf-8
Cookie: orangemilano=1892218887821987
```

`setIfModifiedSince` 方法用于告诉连接你只对来自某个特定日期以来被修改过的数据感兴趣；`setUseCaches` 和 `setAllowUserInteraction` 这两个方法只作用于 `Applet`；`setUserCaches` 方法用于命令浏览器首先检查它的缓存；`setAllowUserInteraction` 方法则用于在访问有密码保护的资源时弹出对话框，以便查询用户名和口令。

最后介绍一个总览全局的方法：`setRequestProperty`，它可以用来设置对特定协议起作用的任何 `名-值对`。

如果你想访问一个有密码保护的 `Web` 页，那么就必须按如下步骤操作：

1）将用户名、冒号和密码以字符串形式连接在一起。

```java
String input = username + ":" + password;
```

2）计算上一步骤所得字符串的 `Base64` 编码。（`Base64` 编码用于将字节序列编码成可打印的 ASCII 字符序列。

```java
Base64.Encoder encoder = Base64.getEncoder();
String encoding = encoder.encodeToString(input.getBytes(StandardCharsets.UTF-8));
```

3）用 `Authorization` 这个名字和 `Basic` + `encoding` 的值调用 `setRequestProperty` 方法。

```java
connection.setRequestProperty("Authorization", "Basic" + encoding);
```

> 提示：如果想要通过 `FTP` 访问一个有密码保护的文件时，则需要采用一种完全不同的方法，构建如下格式的 `URL`：
>
> ```
> ftp://username:password@ftp.yourserver.com/pub/file.txt
> ```

一旦调用了 `connect` 方法，就可以查询响应头信息了。似乎是为了展示自己的个性，该类的实现者引入了另一种迭代协议。调用如下方法：

```java
String key = connection.getHeaderFieldKey(n);
```

可以获得响应头的第 `n` 个键，其中 `n` 从 1 开始！如果 `n` 为 0 或大于消息头的字段总数，该方法将返回 `null` 值。没有哪种方法可以返回字段的数量，你必须反复调用 `getHeaderFieldKey` 方法直到返回 `null` 为止。同样地，调用以下方法：

```java
String value = connection.getHeaderField(n);
```

`getHeaderFields` 方法可以返回一个封装了响应头字段的 `Map` 对象。

```java
Map<String, List<String>>  headerFields = connection.getHeaderFields();
```

**示例代码：URLConnectionTest.java**

```java
import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * This program connects to an URL and displays the response header data and the first 10 lines of
 * the requested data.
 * Supply the URL and an optional username and password (for HTTP basic authentication) on the
 * command line.
 */
public class URLConnectionTest {

	public static void main(String[] args) {
		try {
			String urlName;
			if (args.length > 0) {
				urlName = args[0];
			} else {
				urlName = "http://horstmann.com";
			}
			
			URL url = new URL(urlName);
			URLConnection connection = url.openConnection();
			
			// set username, password if specified on command line
			
			if (args.length > 2) {
				String username = args[1];
				String password = args[2];
				String input = username + ":" + password;
				Base64.Encoder encoder = Base64.getEncoder();
				String encoding = encoder.encodeToString(input.getBytes(StandardCharsets.UTF_8));
				connection.setRequestProperty("Authorization",  "Basic " + encoding);
			}
			
			connection.connect();
			
			// print header fields
			
			Map<String, List<String>> headers = connection.getHeaderFields();
			for (Map.Entry<String, List<String>> entry : headers.entrySet()) {
				String key = entry.getKey();
				for (String value : entry.getValue()) {
					System.out.println(key + ": " + value);
				}
			}
			
			// print convenience function
			
			System.out.println("---------------------");
			System.out.println("getContentType: " + connection.getContentType());
			System.out.println("getContentLength: " + connection.getContentLength());
			System.out.println("getContentEncoding: " + connection.getContentEncoding());
			System.out.println("getDate: " + connection.getDate());
			System.out.println("getExpiration: " + connection.getExpiration());
			System.out.println("getLastModified: " + connection.getLastModified());
			System.out.println("---------------------");
			
			String encoding = connection.getContentEncoding();
			if (encoding == null) {
				encoding = "utf-8";
			}
			try (Scanner in = new Scanner(connection.getInputStream(), encoding)) {
				// print first ten lines of contents
				for (int n = 1; in.hasNextLine() && n <= 10; n++) {
					System.out.println(in.nextLine());
				}
				if (in.hasNextLine()) {
					System.out.println("...");
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
```

运行结果如下：

```
Keep-Alive: timeout=3, max=500
X-Frame-Options: SAMEORIGIN
null: HTTP/1.1 301 Moved Permanently
Strict-Transport-Security: max-age=63072000; includeSubDomains
Server: Apache
X-Content-Type-Options: nosniff
Connection: Keep-Alive
Content-Length: 230
Date: Tue, 20 Jun 2023 01:15:55 GMT
Content-Type: text/html; charset=iso-8859-1
Location: https://horstmann.com/
---------------------
getContentType: text/html; charset=iso-8859-1
getContentLength: 230
getContentEncoding: null
getDate: 1687223755000
getExpiration: 0
getLastModified: 0
---------------------
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="https://horstmann.com/">here</a>.</p>
</body></html>
```

