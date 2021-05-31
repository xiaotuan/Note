当 HttpURLConnection 请求反回一个重定向页面时会自动请求该重定向地址，也就是说最后我们拿到的 ReponseCode 是 200，如果我们希望拿到的是重定向状态码 302，则需要禁止 HttpURLConnection 自动进行重定向跳转，方法是调用 HttpURLConnection 对象的 setInstanceFollowRedirects() 方法，并设置参数值为 false：

```java
HttpURLConnection.setInstanceFollowRedirects(false);
```

