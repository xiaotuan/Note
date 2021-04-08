### 4.2　Go与HTML表单

在学习如何从 `POST` 请求中获取表单数据之前，让我们先来了解一下HTML表单。在绝大多数情况下， `POST` 请求都是通过HTML表单发送的，这些表单看上去通常会是下面这个样子：

```go
<form action="/process" method="post">
　<input type="text" name="first_name"/>
　<input type="text" name="last_name"/>
　<input type="submit"/>
</form>
```

`<form>` 标签可以包围文本行、文本框、单选按钮、复选框以及文件上传等多种HTML表单元素，而用户则可以把想要传递给服务器的数据输入到这些元素里面。当用户按下发送按钮、又或者通过某种方式触发了表单的发送操作之后，用户在表单中输入的数据就会被发送至服务器。

用户在表单中输入的数据会以键值对的形式记录在请求的主体中，然后以HTTP  `POST` 请求的形式发送至服务器。因为服务器在接收到浏览器发送的表单数据之后，还需要对这些数据进行语法分析，从而提取出数据中记录的键值对，因此我们还需要知道这些键值对在请求主体中是如何格式化的。

HTML表单的内容类型（content type）决定了 `POST` 请求在发送键值对时将使用何种格式，其中，HTML表单的内容类型是由表单的 `enctype` 属性指定的：

```go
<form action="/process" method="post" enctype="application/x-www-form-urlencoded">
　<input type="text" name="first_name"/>
　<input type="text" name="last_name"/>
　<input type="submit"/>
</form>
```

`enctype` 属性的默认值为 `application/x-www-form-urlencoded` 。浏览器至少需要支持 `application/x-www-form-urlencoded` 和 `multipart/form-data` 这两种编码方式。除以上两种编码方式之外，HTML5还支持 `text/plain` 编码方式。

如果我们把 `enctype` 属性的值设置为 `application/x-www-form-urlencoded` ，那么浏览器将把HTML表单中的数据编码为一个连续的“长查询字符串”（long query string）：在这个字符串中，不同的键值对将使用 `&` 符号分隔，而键值对中的键和值则使用等号 `=` 分隔。这种编码方式跟我们在第1章看到过的URL编码是一样的， `application/x-www-form-` urlencoded编码名字中的 `urlencoded` 一词也由此而来。换句话说，一个 `application/x-` www-  `form-urlencoded` 编码的HTTP请求主体看上去将会是下面这个样子的：

```go
first_name=sau%20sheong&last_name=chang
```

但是，如果我们把 `enctype` 属性的值设置为 `multipart/form-data` ，那么表单中的数据将被转换成一条MIME报文：表单中的每个键值对都构成了这条报文的一部分，并且每个键值对都带有它们各自的内容类型以及内容配置（disposition）。以下是一个使用 `multipart/form-data` 编码对表单数据进行格式化的例子：

```go
------WebKitFormBoundaryMPNjKpeO9cLiocMw
 Content-Disposition: form-data; name="first_name"
sau sheong
 ------WebKitFormBoundaryMPNjKpeO9cLiocMw
 Content-Disposition: form-data; name="last_name"
 chang
 ------WebKitFormBoundaryMPNjKpeO9cLiocMw--
```

既然表单同时支持 `application/x-www-form-urlencoded` 编码和 `multipart/form-data` 编码，那么我们该选择使用哪种编码呢？答案是，如果表单传送的是简单的文本数据，那么使用URL编码格式更好，因为这种编码更为简单、高效，并且它所需的计算量要比另一种编码少。但是，如果表单需要传送大量数据（如上传文件）那么使用 `multipart` /form- data编码格式会更好一些。在需要的情况下，用户还可以通过Base64编码，以文本方式传送二进制数据。

到目前为止，我们只讨论了如何通过 `POST` 请求发送表单，但实际上通过 `GET` 请求也是可以发送表单的——因为HTML表单的 `method` 属性的值既可以是 `POST` 也可以是 `GET` ，所以下面这个HTML表单也是合法的：

```go
<form action="/process" method="get">
　<input type="text" name="first_name"/>
　<input type="text" name="last_name"/>
　<input type="submit"/>
</form>
```

因为 `GET` 请求并不包含请求主体，所以在使用 `GET` 方法传递表单时，表单数据将以键值对的形式包含在请求的URL里面，而不是通过主体传递。

在了解了HTML表单向服务器传递数据的方法之后，让我们回到服务器一端，学习一下如何使用 `net/http` 库来处理这些表单数据。

