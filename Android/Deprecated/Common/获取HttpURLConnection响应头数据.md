可以通过 HttpURLConnection 对象的 getHeaderField() 方法获取响应头信息，比如我们需要获取重定向地址可以使用如下方法：

```java
String location = HttpURLConnection.getHeaderField("Location");
```

