`POST` 请求示例代码如下：

```java
import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class JavaTest {

    public static void main(String[] arg){
        PrintWriter out = null;
        BufferedReader in = null;
        try {
            URL url = new URL("http://127.0.0.1:8124");
            // 打开和 URL 之间的连接
            URLConnection conn = url.openConnection();
            // 发送 POST 请求必须设置如下两行
            conn.setDoOutput(true);
            conn.setDoInput(true);
            conn.addRequestProperty("Content-Type", "application/json");
            // 获取 URLConnection 对象对应的输出流（设置请求编码为 UTF-8)
            out = new PrintWriter(new OutputStreamWriter(conn.getOutputStream(), "UTF-8"));
            // 发送请求参数
            out.print("{ \"name\": \"qty\", \"age\":28}");
            // flush 输出流的缓冲
            out.flush();
            // 获取请求返回数据（设置返回数据编码为 UTF-8）
            in = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
            StringBuffer sb = new StringBuffer();
            String line;
            while ((line = in.readLine()) != null) {
                if (sb.length() > 0) {
                    sb.append("\n");
                }
                sb.append(line);
            }
            System.out.println("result: " + sb.toString());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
```

