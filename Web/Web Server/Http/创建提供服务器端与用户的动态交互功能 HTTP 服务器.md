[toc]

### 1. HTTPServer1.java

```java
package server;

import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class HTTPServer1 {
	private static Map<String, Servlet> servletCache = new HashMap<String, Servlet>();

	public static void main(String args[]) {
		int port;
		ServerSocket serverSocket;

		try {
			port = Integer.parseInt(args[0]);
		} catch (Exception e) {
			System.out.println("port = 8080 (默认)");
			port = 8080; // 默认端口为8080
		}

		try {
			serverSocket = new ServerSocket(port);
			System.out.println("服务器正在监听端口：" + serverSocket.getLocalPort());

			while (true) { // 服务器在一个无限循环中不断接收来自客户的TCP连接请求
				try {
					// 等待客户的TCP连接请求
					final Socket socket = serverSocket.accept();
					System.out.println("建立了与客户的一个新的TCP连接，该客户的地址为：" + socket.getInetAddress() + ":" + socket.getPort());

					service(socket); // 响应客户请求
				} catch (Exception e) {
					System.out.println("客户端请求的资源不存在");
				}
			} // #while
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/** 响应客户的HTTP请求 */
	public static void service(Socket socket) throws Exception {

		/* 读取HTTP请求信息 */
		InputStream socketIn = socket.getInputStream(); // 获得输入流
		Thread.sleep(500); // 睡眠500毫秒，等待HTTP请求
		int size = socketIn.available();
		byte[] requestBuffer = new byte[size];
		socketIn.read(requestBuffer);
		String request = new String(requestBuffer);
		System.out.println(request); // 打印HTTP请求数据

		/* 解析HTTP请求 */
		// 获得HTTP请求的第一行
		int endIndex = request.indexOf("\r\n");
		if (endIndex == -1) {
			endIndex = request.length();
        }
		String firstLineOfRequest = request.substring(0, endIndex);

		// 解析HTTP请求的第一行
		String[] parts = firstLineOfRequest.split(" ");
		String uri = "";
		if (parts.length >= 2)
			uri = parts[1]; // 获得HTTP请求中的uri

		/* 如果请求访问Servlet，则动态调用Servlet对象的service()方法 */
		if (uri.indexOf("servlet") != -1) {
			// 获得Servlet的名字
			String servletName = null;
			if (uri.indexOf("?") != -1)
				servletName = uri.substring(uri.indexOf("servlet/") + 8, uri.indexOf("?"));
			else
				servletName = uri.substring(uri.indexOf("servlet/") + 8, uri.length());
			// 尝试从Servlet缓存中获取Servlet对象
			Servlet servlet = servletCache.get(servletName);
			// 如果Servlet缓存中不存在Servlet对象，就创建它，并把它存放在Servlet缓存中
			if (servlet == null) {
				servlet = (Servlet) Class.forName("server." + servletName).getDeclaredConstructor().newInstance();
				servlet.init();// 先调用Servlet对象的init()方法
				servletCache.put(servletName, servlet);
			}

			// 调用Servlet的service()方法
			servlet.service(requestBuffer, socket.getOutputStream());

			Thread.sleep(1000); // 睡眠1秒，等待客户接收HTTP响应结果
			socket.close(); // 关闭TCP连接
			return;
		}

		/* 决定HTTP响应正文的类型 */
		String contentType;
		if (uri.indexOf("html") != -1 || uri.indexOf("htm") != -1) {
			contentType = "text/html";
		} else if (uri.indexOf("jpg") != -1 || uri.indexOf("jpeg") != -1) {
			contentType = "image/jpeg";
		} else if (uri.indexOf("gif") != -1) {
			contentType = "image/gif";
		} else {
			contentType = "application/octet-stream";
		}

		/* 创建HTTP响应结果 */
		// HTTP响应的第一行
		String responseFirstLine = "HTTP/1.1 200 OK\r\n";
		// HTTP响应头
		String responseHeader = "Content-Type:" + contentType + "\r\n\r\n";
		// 获得读取响应正文数据的输入流
		InputStream in = HTTPServer1.class.getResourceAsStream("root/" + uri);

		/* 发送HTTP响应结果 */
		OutputStream socketOut = socket.getOutputStream(); // 获得输出流
		// 发送HTTP响应的第一行
		socketOut.write(responseFirstLine.toString().getBytes());
		// 发送HTTP响应的头
		socketOut.write(responseHeader.toString().getBytes());
		// 发送HTTP响应的正文
		int len = 0;
		byte[] buffer = new byte[128];
		while ((len = in.read(buffer)) != -1) {
			socketOut.write(buffer, 0, len);
		}

		Thread.sleep(1000); // 睡眠1秒，等待客户接收HTTP响应结果
		socket.close(); // 关闭TCP连接

	}
}
```

### 2. Servlet.java

```java
package server;
import java.io.*;

public interface Servlet{
	public void init()throws Exception;
	public void service(byte[] requestBuffer, OutputStream out)throws Exception;
}
```

### 3. HelloServlet.java

```java
package server;

import java.io.*;

public class HelloServlet implements Servlet {
	public void init() throws Exception {
		System.out.println("HelloServlet is inited");
	}

	public void service(byte[] requestBuffer, OutputStream out) throws Exception {
		String request = new String(requestBuffer);

		// 获得HTTP请求的第一行
		String firstLineOfRequest = request.substring(0, request.indexOf("\r\n"));
		// 解析HTTP请求的第一行
		String[] parts = firstLineOfRequest.split(" ");
		String method = parts[0]; // 获得HTTP请求中的请求方式
		String uri = parts[1]; // 获得HTTP请求中的uri

		/* 获得请求参数username */
		String username = null;
		// 如果请求方式为“GET”，则请求参数紧跟HTTP请求的第一行的uri的后面
		if (method.equalsIgnoreCase("get") && uri.indexOf("username=") != -1) {

			/* 假定uri="servlet/HelloServlet?username=Tom&password=1234" */
			// parameters="username=Tom&password=1234"
			String parameters = uri.substring(uri.indexOf("?"), uri.length());

			// parts={"username=Tom","password=1234"};
			parts = parameters.split("&");
			// parts={"username","Tom"};
			parts = parts[0].split("=");
			username = parts[1];
		}
		// 如果请求方式为“POST”，则请求参数位于HTTP请求的请求正文中。
		if (method.equalsIgnoreCase("post")) {
			int locate = request.indexOf("\r\n\r\n");
			// 获得响应正文
			String content = request.substring(locate + 4, request.length());
			if (content.indexOf("username=") != -1) {
				/* 假定content="username=Tom&password=1234" */
				// parts={"username=Tom","password=1234"};
				parts = content.split("&");
				// parts={"username","Tom"};
				parts = parts[0].split("=");
				username = parts[1];
			}
		}

		/* 创建并发送HTTP响应 */
		// 发送HTTP响应第一行
		out.write("HTTP/1.1 200 OK\r\n".getBytes());
		// 发送HTTP响应头
		out.write("Content-Type:text/html\r\n\r\n".getBytes());
		// 发送HTTP响应正文
		String content = "<html><head><title>HelloWorld" + "</title></head><body>";
		content += "<h1>Hello:" + username + "</h1></body><head>";
		out.write(content.getBytes());

	}
}
```

### 4. UploadServlet.java

```java
package server;

import java.io.*;

public class UploadServlet implements Servlet {
	public void init() throws Exception {
		System.out.println("UploadServlet is inited");
	}

	public void service(byte[] requestBuffer, OutputStream out) throws Exception {
		String request = new String(requestBuffer);

		// 获得HTTP请求的头
		String headerOfRequest = request.substring(request.indexOf("\r\n") + 2, request.indexOf("\r\n\r\n"));

		BufferedReader br = new BufferedReader(new StringReader(headerOfRequest));
		String data = null;
		// 获取boundary
		String boundary = null;
		while ((data = br.readLine()) != null) {
			if (data.indexOf("Content-Type") != -1) {
				boundary = data.substring(data.indexOf("boundary=") + 9, data.length()) + "\r\n";
				break;
			}
		}

		if (boundary == null) {
			out.write("HTTP/1.1 200 OK\r\n".getBytes());
			// 发送HTTP响应头

			out.write("Content-Type:text/html\r\n\r\n".getBytes());
			// 发送HTTP响应正文
			out.write("Uploading is failed".getBytes());
			return;
		}

		// 第一个boundary出现的位置
		int index1OfBoundary = request.indexOf(boundary);
		// 第二个boundary出现的位置
		int index2OfBoundary = request.indexOf(boundary, index1OfBoundary + boundary.length());
		// 第三个boundary出现的位置
		int index3OfBoundary = request.indexOf(boundary, index2OfBoundary + boundary.length());
		// 文件部分的正文部分的开始前的位置
		int beforeOfFilePart = request.indexOf("\r\n\r\n", index2OfBoundary) + 3;
		// 文件部分的正文部分的结束后的位置
		int afterOfFilePart = index3OfBoundary - 4;
		// 文件部分的头的第一行结束后的位置
		int afterOfFilePartLine1 = request.indexOf("\r\n", index2OfBoundary + boundary.length());
		// 文件部分的头的第二行
		String header2OfFilePart = request.substring(index2OfBoundary + boundary.length(), afterOfFilePartLine1);
		// 上传文件的名字
		String fileName = header2OfFilePart.substring(header2OfFilePart.lastIndexOf("=") + 2,
				header2OfFilePart.length() - 1);
		// 文件部分的正文部分之前的字符串的字节长度
		int len1 = request.substring(0, beforeOfFilePart + 1).getBytes().length;
		// 文件部分的正文部分之后的字符串的字节长度
		int len2 = request.substring(afterOfFilePart, request.length()).getBytes().length;
		// 文件部分的正文部分的字节长度
		int fileLen = requestBuffer.length - len1 - len2;

		/* 把文件部分的正文部分保存到本地文件系统中 */
		FileOutputStream f = new FileOutputStream("server\\root\\" + fileName);
		f.write(requestBuffer, len1, fileLen);
		f.close();

		/* 创建并发送HTTP响应 */
		// 发送HTTP响应第一行
		out.write("HTTP/1.1 200 OK\r\n".getBytes());
		// 发送HTTP响应头
		out.write("Content-Type:text/html\r\n\r\n".getBytes());
		// 发送HTTP响应正文
		String content = "<html><head><title>HelloWorld</title></head><body>";
		content += "<h1>Uploading is finished.<br></h1>";
		content += "<h1>FileName:" + fileName + "<br></h1>";
		content += "<h1>FileSize:" + fileLen + "<br></h1></body><head>";
		out.write(content.getBytes());
	}
}
```

