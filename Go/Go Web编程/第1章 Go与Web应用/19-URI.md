### 1.7　URI

Tim Berners-Lee在创建万维网的同时，也引入了使用位置字符串表示互联网资源的概念。他在1994年发表的RFC 1630中对统一资源标识符（Uniform Resource Identifier，URI）进行了定义。在这篇RFC中，他描述了一种使用字符串表示资源名字的方法，以及一种使用字符串表示资源所在位置的方法，其中前一种方法被称为统一资源名称（Uniform Resource Name，URN），而后一种方法则被称为统一资源定位符（Uniform Resource Location，URL）。URI是一个涵盖性术语，它包含了URN和URL，并且这两者也拥有相似的语法和格式。因为本书只会对URL进行讨论，所以本书中提及的URI指代的都是URL。

URI的一般格式为：

```go
<方案名称>:<分层部分>[ ? <查询参数> ] [ # <片段> ]
```

URI中的方案名称（scheme name）记录了URI正在使用的方案，它定义了URI其余部分的结构。因为URI是一种非常常用的资源标识方式，所以它拥有大量的方案可供使用，不过本书在大多数情况下只会使用HTTP方案。

URI的分层部分（hierarchical part）包含了资源的识别信息，这些信息会以分层的方式进行组织。如果分层部分以双斜线（ `//` ）开头，那么说明它包含了可选的用户信息，这些信息将以 `@` 符号结尾，后跟分层路径。不带用户信息的分层部分就是一个单纯的路径，每个路径都由一连串的分段（segment）组成，各个分段之间使用单斜线（ `/` ）分隔。

在URI的各个部分当中，只有“方案名称”和“分层部分”是必需的。以问号（ `?` ）为前缀的查询参数（query）是可选的，这些参数用于包含无法使用分层方式表示的其他信息。多个查询参数会被组织成一连串的键值对，各个键值对之间使用 `&` 符号分隔。

URI的另一个可选部分为片段（fragment），片段使用井号（ `#` ）作为前缀，它可以对URI定义的资源中的次级资源（secondary resource）进行标识。当URI包含查询参数时，URI的片段将被放到查询参数之后。因为URI的片段是由客户端负责处理的，所以Web浏览器在将URI发送给服务器之前，一般都会先把URI中的片段移除掉。如果程序员想要取得URI片段，那么可以通过JavaScript或者某个HTTP客户端库，将URI片段包含在一个 `GET` 请求里面。

让我们来看一个使用HTTP方案的URI示例：http://sausheong:password@www.example.com/docs/file?name=sausheong&location=singapore#summary 。

这个URI使用的是 `http` 方案，跟在方案名之后的是一个冒号。位于 `@` 符号之前的分段sausheong:password记录的是用户名和密码，而跟在用户信息之后的www.example.com/docs/file就是分层部分的其余部分。位于分层部分最高层的是服务器的域名www.example.com，之后跟着的两个层分别为doc和file，每个分层之间都使用单斜线分隔。跟在分层部分之后的是以问号（ `?` ）为前缀的查询参数，这个部分包含了name=sausheong和location=singapore这两个键值对，键值对之间使用一个 `&` 符号连接。最后，这个URI的末尾还带有一个以井号（ `#` ）为前缀的片段。

因为每个URL都是一个单独的字符串，所以URL里面是不能够包含空格的。此外，因为问号（ `?` ）和井号（ `#` ）等符号在URL中具有特殊的含义，所以这些符号是不能够用于其他用途的。为了避开这些限制，我们需要使用URL编码来对这些特殊符号进行转换（URL编码又称百分号编码）。

RFC 3986定义了URL中的保留字符以及非保留字符，所有保留字符都需要进行URL编码：URL编码会把保留字符转换成该字符在ASCII编码中对应的字节值（byte value），接着把这个字节值表示为一个两位长的十六进制数字，最后再在这个十六进制数字的前面加上一个百分号（ `%` ）。

比如说，空格在ASCII编码中的字节值为32，也就是十六进制中的20。因此，经过URL编码处理的空格就成了 `%20` ，URL中的所有空格都会被替换成这个值。比如在接下来展示的这个URL里面，用户名sau和sheong之间的空格就被替换成了 `%20` ：<a class="my_markdown" href="['http://www.example.com/docs/file?name=sau%20sheong&location=singapore']">http://www.example.com/docs/file? name=sau%20sheong&location=singapore</a>。

