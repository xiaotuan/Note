### 7.3　基于REST的Web服务简介

REST（Representational State Transfer，具象状态传输）是一种设计理念，用于设计那些通过标准的几个动作来操纵资源，并以此来进行相互交流的程序（很多REST使用者都会把操纵资源的动作称为“动词”，也就是verb）。

在大多数编程范型里面，程序员都是通过定义函数然后在主程序中有序地调用这些函数来完成工作的。在面向对象编程（OOP）范型中，程序员要做的事情也是类似的，主要的区别在于，程序员通过创建称为对象（object）的模型来表示事物，然后定义称为方法（method）的函数并将它们附着到模型之上。REST是以上思想的进化版，但它并不是把函数暴露（expose）为可调用的服务，而是以资源（resource）的名义把模型暴露出来，并允许人们通过少数几个称为动词的动作来操纵这些资源。

在使用HTTP协议实现REST服务时，URL将用于表示资源，而HTTP方法则会用作操纵资源的动词，具体如表7-1所示。

<center class="my_markdown"><b class="my_markdown">表7-1　使用HTTP方法与Web服务进行通信</b></center>

| HTTP方法 | 作用 | 使用示例 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| `POST` | 在一项资源尚未存在的情况下创建该资源 | `POST /users` |
| `GET` | 获取一项资源 | `GET /users/1` |
| `PUT` | 重新给定URL上的资源 | `PUT /users/1` |
| `DELETE` | 删除一项资源 | `DELETE /users/1` |

刚开始学习REST的程序员在第一次看到REST使用的HTTP方法与数据库的CRUD操作之间的映射关系时，常常会对此感到非常惊奇。需要注意的是，这种映射并不是一对一映射，而且这种映射也不是唯一的。比如说， `在` 创建一项新的资源时用户既可以使用 `POST` ，也可以使用 `PUT` ，这两种做法都符合REST风格。

`POST` 和 `PUT` 的主要区别在于，在使用 `PUT` 时需要准确地知道哪一项资源将会被替换，而使用 `POST` 只会创建出一项新资源以及一个新URL。换句话说， `POST` 用于创建一项全新的资源，而 `PUT` 则用于替换一项已经存在的资源。

正如第1章所言， `PUT` 方法是幂等的，无论同一个调用重复执行多少次，服务器的状态都不会发生任何变化。无论是使用 `PUT` 创建一项资源，还是使用 `PUT` 修改一项已经存在的资源，给定的URL上面都只会有一项资源被创建出来。相反地，因为 `POST` 并不是幂等的，所以每调用 `POST` 一次，它就会创建一项新资源以及一个新URL。

对刚开始学习REST的程序员来说，另一个需要注意的地方是，REST并不是只能通过表7-1提到的4个HTTP方法实现，比如，不太常见的 `PATCH` 方法就可以用于对一项资源进行部分更新。

下面是一个REST请求示例：

```go
GET /comment/123 HTTP/1.1
```

注意，这个 `GET` 请求并没有与之相关联的主体，而与这个 `GET` 请求相对应的SOAP请求则正好相反：

```go
POST /GetComment HTTP/1.1
Host: www.chitchat.com
Content-Type: application/soap+xml; charset=utf-8
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
<soap:Body xmlns:m="http://www.chitchat.com/forum">
　<m:GetCommentRequest>
　　<m:CommentId>123</m:CommentId>
　</m:GetCommentRequest >
</soap:Body>
</soap:Envelope>
```

这是因为在发送第一个请求的时候，我们使用了HTTP的 `GET` 方法作为动词来获取资源（在这个例子中，资源就是一条博客评论）。对于这个 `GET` 请求，即使Web服务返回一个SOAP响应，它也会被认为是一个REST风格的响应：这是因为REST跟SOAP不同，前者关注的是API的设计，而后者关注的则是被发送报文的格式。不过，因为SOAP报文构建起来非常麻烦，所以人们在使用REST API的时候通常都是返回JSON，或者返回一些比SOAP报文要简单得多的XML，而很少会返回SOAP报文。

正如WSDL跟SOAP的关系一样，基于REST的Web服务也拥有相应的WADL（Web Application Description Language，Web应用描述语言），这种语言可以对基于REST的Web服务进行描述，甚至能够生成访问这些服务的客户端。但是跟WSDL不同的是，WADL没有得到广泛的使用，也没有进行标准化。此外，WADL也拥有Swagger、RAML（Restful API Modeling Language，REST风格API建模语言）和JSON-home这样的同类竞争产品。

在刚开始接触REST的时候，你可能会意识到这种设计理念非常适用于那些只执行简单的CRUD操作的应用，但REST是否适用于更为复杂的服务呢？除此之外，它又是如何对过程或者动作进行建模的呢？

举个例子，在使用REST设计的情况下，一个应用要如何才能激活一个用户的账号呢？因为REST只允许用户使用指定的几个HTTP方法操纵资源，而不允许用户对资源执行任意的动作，所以应用是无法发送像下面这样的请求的：

```go
ACTIVATE /user/456 HTTP/1.1
```

有一些办法可以绕过这个问题，下面是最常用的两种方法：

（1）把过程具体化<a class="my_markdown" href="['#anchor72']"><sup class="my_markdown">[2]</sup></a>，或者把动作转换成名词，然后将其用作资源；

（2）将动作用作资源的属性。

