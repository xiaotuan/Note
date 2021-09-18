[toc]

当 SDK Version 大于 27 时，请求 http 网址会报如下错误：

```
java.io.IOException: Cleartext HTTP traffic to www.amazingrace.cn not permitted
        at com.android.okhttp.HttpHandler$CleartextURLFilter.checkURLPermitted(HttpHandler.java:115)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:458)
        at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:127)
        at net.zenconsult.android.examples.Login.execute(Login.java:37)
        at net.zenconsult.android.examples.LoginDemoClient1Activity.lambda$onCreate$1$LoginDemoClient1Activity(LoginDemoClient1Activity.java:36)
        at net.zenconsult.android.examples.-$$Lambda$LoginDemoClient1Activity$RCcZm8N01nAQvuYFEkEsX9H2ui0.run(Unknown Source:4)
        at java.lang.Thread.run(Thread.java:764)L
```

### 方法一：

在 `AndroidManifest.xml` 文件的 `application` 节点添加如下属性：

```xml
android:usesCleartextTraffic="true"
```

### 方法二：

在 `res` 目录下创建 `xml` 目录，并在 `xml` 目录下创建一个名为 `network_security_config.xml` 的文件，文件内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
	<base-config cleartextTrafficPermitted="true" />
</network-security-config>
```

在 `AndroidManifest.xml` 文件的 `application` 节点添加如下属性：

```xml
android:networkSecurityConfig="@xml/network_security_config"
```

