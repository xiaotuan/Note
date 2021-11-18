[toc]

### 1. Kotlin 版本

```kotlin
import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.util.EntityUtils

val url = "https://picasaweb.google.com/data/feed/api/user/$userId"
val httpClient = DefaultHttpClient();
val get = HttpGet(url)
// 添加请求头
get.addHeader("Authorization", "Bearer " + accessToken)
val resp = httpClient.execute(get)
if (resp.statusLine.statusCode == 200) {
    val line = EntityUtils.toString(resp.entity)
    // Do your XML Parsing here
}
```

### 2. Java 版本

```java
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

String url = "https://picasaweb.google.com/data/feed/api/user/" + userId;
DefaultHttpClient httpClient = new DefaultHttpClient();
HttpGet get = new HttpGet(url);
// 设置请求头
get.addHeader("Authorization", "Bearer " + accessToken);
HttpResponse resp = httpClient.execute(get);
if (resp.getStatusLine().getStatusCode() == 200) {
    HttpEntity httpEntity = resp.getEntity();
    String line = EntityUtils.toString(httpEntity);
    // Do your XML Parsing here
}
```

