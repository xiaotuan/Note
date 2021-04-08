### 4.2.5　处理带有JSON主体的POST请求

因为前面的内容一直只使用HTML表单发送POST请求，所以到目前为止，我们考虑的都是如何处理请求主体中的键值对。但实际上，POST请求并不是只能通过HTML表单发送：诸如jQuery这样的客户端库，又或者是Angular、Ember这样的客户端框架，甚至是Adobe Flash、Microsoft Silverlight这样的技术，都能够发送POST请求，并且这种行为正在变得越来越常见。

需要注意的是，使用 `ParseForm` 方法是无法从Angular客户端发送的POST请求中获取JSON数据的，但使用jQuery这样的JavaScript库却不会出现这样的问题。

造成这一区别的原因在于，不同客户端使用了不同的方式编码POST请求：jQuery会像HTML表单一样，使用 `application/x-www-form-urlencoded` 对POST请求进行编码（具体做法是，jQuery会把POST请求的 `Content-Type` 首部的值设置为 `application/x-www-form-urlencoded` ），而Angular在编码POST请求时使用的却是 `application/json` 。因为Go语言的 `ParseForm` 方法只会对表单数据进行语法分析，它并不接受 `application/json` 编码，所以使用这一编码发送POST请求的用户自然也无法通过 `ParseForm` 方法获得任何数据。

这个问题跟库的实现无关，真正的罪魁祸首实际上是没有足够的文档对这种行为进行说明，而程序员又对他们使用的框架做了某种假设，这样一来，问题自然而然地也就出现了。

因为框架可以隐藏复杂性和实现细节，所以程序员应该使用框架。但与此同时，理解框架的工作方式，了解框架如何化繁为简，也是非常重要的。否则，在使用框架与其他程序进行对接的时候，就可能会出现各种各样的问题。

到目前为止，本章已经对“如何处理请求”这一问题做了足够多的介绍，现在，是时候讲讲如何向用户发送响应了。

