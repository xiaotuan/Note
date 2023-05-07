[toc]

### 1. HTTPServer.java

```java
package server;

import java.io.*;
import java.net.*;

public class HTTPServer {
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
					System.out.println(
							"建立了与客户的一个新的TCP连接，" + "该客户的地址为：" + socket.getInetAddress() + ":" + socket.getPort());

					service(socket); // 响应客户请求
				} catch (Exception e) {
					System.out.println("客户端请求的资源不存在");
					e.printStackTrace();
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
		byte[] buffer = new byte[size];
		socketIn.read(buffer);
		String request = new String(buffer);
		System.out.println(request); // 打印HTTP请求数据

		/* 解析HTTP请求 */
		// 获得HTTP请求的第一行
		int endIndex = request.indexOf("\n");
		if (endIndex == -1) {
			endIndex = request.length();
		}
		String firstLineOfRequest = request.substring(0, endIndex);

		// 解析HTTP请求的第一行
		String[] parts = firstLineOfRequest.split(" ");
		String uri = "";
		if (parts.length >= 2) {
			uri = parts[1].substring(1); // 获得HTTP请求中的uri
		}

		/* 决定HTTP响应正文的类型，此处作了简化处理 */
		String contentType;
		if (uri.indexOf("html") != -1 || uri.indexOf("htm") != -1) {
			contentType = "text/html";
		} else if (uri.indexOf("jpg") != -1 || uri.indexOf("jpeg") != -1) {
			contentType = "image/jpeg";
		} else if (uri.indexOf("gif") != -1) {
			contentType = "image/gif";
		} else {
			contentType = "application/octet-stream"; // 字节流类型
		}

		/* 创建HTTP响应结果 */
		// HTTP响应的第一行
		String responseFirstLine = "HTTP/1.1 200 OK\n";
		// HTTP响应头
		String responseHeader = "Content-Type:" + contentType + "\n\n";
		// 获得读取响应正文数据的输入流
		InputStream in = HTTPServer.class.getResourceAsStream("root/" + uri);

		/* 发送HTTP响应结果 */
		OutputStream socketOut = socket.getOutputStream(); // 获得输出流
		// 发送HTTP响应的第一行
		socketOut.write(responseFirstLine.getBytes());
		// 发送HTTP响应的头
		socketOut.write(responseHeader.getBytes());
		// 发送HTTP响应的正文
		int len = 0;
		buffer = new byte[128];
		while ((len = in.read(buffer)) != -1) {
			socketOut.write(buffer, 0, len);
		}

		Thread.sleep(1000); // 睡眠1秒，等待客户接收HTTP响应结果
		socket.close(); // 关闭TCP连接
	}
}
```

### 2. HTTPClient.java

```java
package client;

import java.net.*;
import java.io.*;
import java.util.*;

public class HTTPClient {
	public static void main(String args[]) {
		// 确定HTTP请求的uri
		String uri = "index.htm";
		if (args.length != 0)
			uri = args[0];

		doGet("localhost", 8080, uri); // 按照GET请求方式访问HTTPServer
	}

	/** 按照GET请求方式访问HTTPServer */
	public static void doGet(String host, int port, String uri) {
		Socket socket = null;

		try {
			socket = new Socket(host, port); // 与HTTPServer建立FTP连接
		} catch (Exception e) {
			e.printStackTrace();
		}

		try {
			/* 创建HTTP请求 */
			StringBuffer sb = new StringBuffer("GET " + uri + " HTTP/1.1\r\n");
			sb.append("Accept: */*\r\n");
			sb.append("Accept-Language: zh-cn\r\n");
			sb.append("Accept-Encoding: gzip, deflate\r\n");
			sb.append("User-Agent: HTTPClient\r\n");
			sb.append("Host: localhost:8080\r\n");
			sb.append("Connection: Keep-Alive\r\n\r\n");

			/* 发送HTTP请求 */
			OutputStream socketOut = socket.getOutputStream(); // 获得输出流
			socketOut.write(sb.toString().getBytes());

			Thread.sleep(2000); // 睡眠2秒，等待响应结果

			/* 接收响应结果 */
			InputStream socketIn = socket.getInputStream(); // 获得输入流
			int size = socketIn.available();
			byte[] buffer = new byte[size];
			socketIn.read(buffer);
			System.out.println(new String(buffer)); // 打印响应结果

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				socket.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	} // #doGet()
}
```

