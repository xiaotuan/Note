`URL` 和 `URLConnection` 类封装了大量复杂的实现细节，这些细节涉及如何从远程站点获取信息。例如，可以自一个字符串构建一个 `URL` 对象：

```java
URL url = new URL(urlString);
```

如果只是想获得该资源的内容，可以使用 `URL` 类中的 `openStream` 方法。该方法将产生一个 `InputStream` 对象，然后就可以安装一般的用法来使用这个对象了，比如用它构建一个 `Scanner` 对象：

```java
InputStream inStream = url.openStream();
Scanner in = new Scanner(inStream, "utf-8");
```

`URI` 是个纯粹的语法结构，包含用来指定 `Web` 资源的字符串的各种组成部分。`URL` 是 `URI` 的一个特例，它包含了用于定位 `Web` 资源的足够信息。

`URI` 规范给出了标记这些标识符的规则。一个 `URI` 具有以下句法：

```
[scheme:]schemeSpecificPart[#fragment]
```

上式中，`[...]` 表示可选部分，并且 `:` 和 `#` 可以被包含在标识符内。

包含 `scheme:` 部分的 `URI` 称为绝对 `URI`。否则，称为相对 `URI`。

如果绝对 `URI` 的 `schemeSpecificPart` 不是以 `/` 开头的，我们就称它是不透明的。例如：

```
mailto:cay@horstmann.com
```

一个分层 `URI` 的 `schemeSpecificPart` 具有以下结构：

```
[//authority][path][?query]
```

`URI` 类的作用之一是解析标识符并将它分解成各种不同的组成部分。你可以用以下方法读取他们：

```
getScheme
getSchemeSpecificPart
getAuthority
getUserInfo
getHost
getPort
getPath
getQuery
getFragment
```

`URI` 类的另一个作用是处理绝对标识符和相对标识符。如果存在一个如下的绝对 `URI`：

```
http://doc.mycompany.com/api/java/net/ServerSocket.html
```

和一个如下的相对 `URI`：

```
../../java/net/Socket.html#Socket()
```

那么可以用它们组合出一个绝对 `URI`：

```
http://doc.mycompany.com/api/java/net/Socket.html#Socket()
```

与此相反的过程称为相对化。例如，假设有一个基本 `URI`：

```
http://docs.mycompany.com/api
```

和另一个 `URI`：

```
http://docs.mycompany.com/api/java/lang/String.html
```

那么相对化之后的 `URI` 就是：

```
java/lang/String.html
```

`URI` 类同时支持以下两个操作：

```java
relative = base.relativize(combined);
combined = base.resolve(relative);
```



