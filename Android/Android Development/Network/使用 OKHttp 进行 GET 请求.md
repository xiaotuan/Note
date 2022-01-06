[toc]

> 提示
>
> 在 AndroidStudio 中使用 OkHttp 库的方法请参阅 《[在 AndroidStudio 中使用 OkHttp 库](./在 AndroidStudio 中使用 OkHttp 库.md)》。

### 1. 一个简单的 GET 请求

#### 1.1 Kotlin

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

#### 1.2 Java

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

### 2. 设置请求头

可以通过 `HttpGet` 的 `addheader()` 方法向 `GET` 请求中添加请求头：

#### 2.1 Kotlin

```kotlin
val url = "https://picasaweb.google.com/data/feed/api/user/$userId"
val httpClient = DefaultHttpClient();
val get = HttpGet(url)
// 添加请求头
get.addHeader("Authorization", "Bearer " + accessToken)
```

#### 2.2 Java

```java
String url = "https://picasaweb.google.com/data/feed/api/user/" + userId;
DefaultHttpClient httpClient = new DefaultHttpClient();
HttpGet get = new HttpGet(url);
// 设置请求头
get.addHeader("Authorization", "Bearer " + accessToken);
```

### 3. 获取返回结果

#### 3.1 方法一

##### 3.1.1 Kotlin

```kotlin
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

##### 3.1.2 Java

```java
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

#### 3.2 方法二

##### 3.2.1 Kotlin

```kotlin
val url = "https://picasaweb.google.com/data/feed/api/user/$userId"
val httpClient = DefaultHttpClient();
val get = HttpGet(url)
// 添加请求头
get.addHeader("Authorization", "Bearer " + accessToken)
val resp = httpClient.execute(get)
if (resp.statusLine.statusCode == 200) {
    val br = BufferedReader(InputStreamReader(resp.entity.content))
}
```

#### 3.2.2 Java

```java
String url = "https://picasaweb.google.com/data/feed/api/user/" + userId;
DefaultHttpClient httpClient = new DefaultHttpClient();
HttpGet get = new HttpGet(url);
// 设置请求头
get.addHeader("Authorization", "Bearer " + accessToken);
HttpResponse resp = httpClient.execute(get);
if (resp.getStatusLine().getStatusCode() == 200) {
    BufferedReader br = new BufferedReader(new InputStreamReader(resp.getEntity().getContent()));
}
```



