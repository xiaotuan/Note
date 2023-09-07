解决中文乱码可以选用以下方式之一：

（1）对读取到的请求参数进行字符编码转换：

```java
String userName = request.getParameter("username");
if (username != null) {	// 把请求参数转换为 GBK 编码
	userName = new String(userName.getBytes("ISO8859-1"), "GBK");
}
```

或者：

```java
String userName = request.getParameter("username");
if (username != null) {	// 把请求参数转换为 UTF-8 编码
    userName = new String(userName.getBytes("ISO8859-1"), "UTF-8");
}
```

（2）对于 `POST` 请求方式，采用如下方式设置请求参数编码：

```java
request.setCharacterEncoding("GBK");
```

以上代码只能设置请求正文中的字符编码，而不能设置请求头中的字符编码。而 `GET` 请求方式中的请求参数位于请求头中，所以无法用上述方法设置 `GET` 请求方式中的请求参数的字符编码。

（3）利用 `ServletContext` 对象的 `getRequestCharacterEncoding()` 和 `setRequestCharacterEncoding()` 方法，来分别读取或设置当前 `Web` 应用中请求正文数据的字符编码。这两个方法是从 `Servlet API 4` 版本才开始引进的。

（4）在 `Tomcat` 的 `server.xml` 配置文件中对 `HTTP` 连接器进行如下配置：

```xml
<Connector port="8080" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" URIEncoding="UTF=8" />
```

这种方式可以一劳永逸地解决读取 `URI` 请求参数时的乱码问题。但是如果发布环境不允许随意修改 `server.xml` 文件，那么只能使用其他方法。

（5）编写一个预处理器，并且在一个自定义的 `HttpServletRequest` 包装类中对请求参数进行编码转换：

```java
package mypack;

import javax.servlet.http.*;
import javax.servlet.*;
import java.io.*;

public class MyRequestWrapper extends HttpServletRequestWrapper {
    
    public MyRequestWrapper(HttpServletRequest request) {
        super(reques);
    }
    
    public String getParameter(String name) {
        String value = super.getParameter(name);
        if (value != null) {
            try {
                value = new String(value.getBytes("ISO-8859-1"), "GB2312");
            } catch (Exception e) {
                
            }
        }
        return value;
    }
}
```

服务器端在对请求参数进行编码转换时，首先需要了解客户端传来的请求参数的字符编码，以下 `EncodeTool` 类提供了一个使用方法 `getEncoding(String str)`，它可以判断出任意一个字符串所使用的字符编码。

```java
package mypack;

public class EncodeTool {

    private static final String[] encodes = { "GBK", "GB2312", "ISO-8859-1", "UTF-8"};
    
    /* 判断 str 参数字符串是否采用特定字符编码 */
    public static boolean isEncoding(String str, String encode) {
        try {
            if (str.equals(new String(str.getBytes(encode), encode))) {
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            return false;
        }
    }
    
    /* 获取 str 参数字符串使用的字符编码 */
    public static String getEncoding(String str) {
        for (int i = 0; i < encodes.length; i++) {
            if (isEncoding(str, encodes[i])) {
                return encodes[i];
            }
        }
        return null;
    }
    
    public static void main(String args[]) throws Exception {
        // 测试程序
        String s1 = new String("你好".getBytes[], "GBK");
        String s2 = new String("你好".getBytes[], "UTF-8");
        String s3 = new String("你好".getBytes[], "ISO-8859-1");
        
        System.out.println("s1 的编码：" + getEncoding(s1));	// 打印 GBK
        System.out.println("s2 的编码：" + getEncoding(s1));	// 打印 UTF-8
        System.out.println("s3 的编码：" + getEncoding(s1));	// 打印 ISO-8859-1
    }
}
```

借助 `EncodeTool` 实用类，可以对采用任意字符编码的请求参数进行字符编码转换：

```java
String userName = request.getParameter("username");
if (userName != null) {	// 把请求参数转换为 GBK 编码
	String encode = EncodeTool.getEncoding(userName);
    userName = new String(userName.getBytes(encode), "GBK");
}
```

