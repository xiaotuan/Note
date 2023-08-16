`Servlet` 通过 `ServletResponse` 对象来生成响应结果。当 `Servlet` 容器接收到客户端要求访问特定 `Servlet` 的请求时，容器会创建一个 `ServletResponse` 对象，并把它作为参数传递给 `Servlet` 的 `service()` 方法。

`ServletResponses` 接口中定义了一系列与生成响应结果相关的方法：

+ `setCharacterEncoding(String charset)`：设置响应正文的字符编码。响应正文的默认字符编码为 `ISO-8859-1`。
+ `setContentLength(int len)`：设置响应正文的长度。
+ `setContentType(String type)`：设置响应正文的 `MIME` 类型。
+ `getCharacterEncoding()` ：返回响应正文的字符编码。
+ `getContentType()`：返回响应正文的 MIME 类型。
+ `setBufferSize(int size)`：设置用于存放响应正文数据的缓冲区的大小。
+ `getBufferSize()`：获得用于存放响应正文数据的缓冲区的大小。
+ `reset()`：清空缓冲区内的正文数据，并且清空响应状态代码以及响应头。
+ `resetBuffer()`：仅仅清空缓冲区内的正文数据，不清空响应状态代码以及响应头。
+ `flushBuffer()`：强制性地把缓冲区内的响应正文数据发送到客户端。
+ `isCommitted()`：返回一个 `boolean` 类型的值。如果为 `true`，表示缓冲区内的数据已经提交给客户，即数据已经发送到客户端。
+ `getOutputStream()`：返回一个 `ServletOutputStream` 对象，`Servlet` 用它来输出二进制的正文数据。
+ `getWriter()`：返回一个 `PrintWriter` 对象，`Servlet` 用它来输出字符串形式的正文数据。

> 提示：
>
> `ServletResponse` 中响应正文的默认 MIME 类型为 `text/plain`，即纯文本类型。而 `HttpServletResponse` 中响应正文的默认 MIME 类型为 `text/html`，即 HTML 文档类型。

`Servlet` 通过 `ServletResponse` 对象主要产生 HTTP 响应结果的正文部分。`ServletResponse` 的 `getOutputStream()`  方法返回一个 `ServletOutputStream` 对象，`Servlet` 可以利用 `SerlvletOutputStream` 来输出二进制的正文数据。`ServletResponse` 的 `getWriter()` 方法返回一个 `PrintWriter` 对象，`Servlet` 可以利用 `PrintWriter` 来输出字符串形式的正文数据。

为了提高输出数据的效率，`ServletOutputStream` 和 `PrintWriter` 先把数据写到缓冲区内。当缓冲区内的数据被提交给客户后，`ServletResponse` 的 `isCommitted()` 方法返回 `true`。在以下几种情况下，缓冲区内的数据会被提交给客户，即数据被发送到客户端：

+ 缓冲区内数据一满时，`ServletOutputStream` 或 `PrintWriter` 会自动把缓冲区内的数据发送给客户端，并且清空缓冲区。
+ `Servlet` 调用 `ServletResponse` 对象的 `flushBuffer()` 方法。
+ `Servlet` 调用 `ServletOutputStream` 或 `PrintWriter` 对象的 `flush()` 方法或 `close()` 方法。

> 提示：
>
> 在 `Tomcat` 的实现中，如果 `Servlet` 的 `service()` 方法没有调用 `ServletOutputStream` 或 `PrintWriter` 的 `close()`  方法，那么 `Tomcat` 在调用完 `Servlet` 的 `service()` 方法后，会关闭 `ServletOutputStream` 或 `PrintWriter`，从而确保 `Servlet` 输出的所有数据被提交给客户。

值得注意的是，如果要设置响应正文的 MIME 类型和字符编码，必须先调用 `ServletResponse` 对象的 `setContentType()` 和 `setCharacterEncoding()` 方法，然后再调用 `ServletResponse` 的 `getOutputStream()` 或 `getWriter()` 方法，以及提交缓冲区内的正文。