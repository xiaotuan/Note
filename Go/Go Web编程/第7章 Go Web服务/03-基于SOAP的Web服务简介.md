### 7.2　基于SOAP的Web服务简介

SOAP是一种协议，用于交换定义在XML里面的结构化数据，它能够跨越不同的网络协议并在不同的编程模型中使用。SOAP原本是Simple Object Access Protocol（简单对象访问协议）的首字母缩写，但这实际上是一个名不符实的名字，因为这种协议处理的并不是对象，并且时至今日它也已经不再是一种简单的协议了。在最新版的SOAP 1.2规范中，这种协议的官方名称仍然为SOAP，但它已经不再代表Simple Object Access Protocol了。

因为SOAP不仅高度结构化，而且还需要严格地进行定义，所以用于传输数据的XML可能会变得非常复杂。WSDL是客户端与服务器之间的契约，它定义了服务提供的功能以及提供这些功能的方式，服务的每个操作以及输入/输出都需要由WSDL明确地定义。

虽然本章主要关注的是基于REST的Web服务，但出于对比需要，我们也会了解一下基于SOAP的Web服务的运作机制。

SOAP会将它的报文内容放入到信封（envelope）里面，信封相当于一个运输容器，并且它还能够独立于实际的数据传输方式存在。因为本书只会对SOAP Web服务进行考察，所以我们将通过HTTP协议来说明被传输的SOAP报文。

下面是一个经过简化的SOAP请求报文示例：

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

因为前面已经介绍过HTTP报文的首部，所以这里给出的HTTP首部对你来说应该不会感到陌生。需要注意的是， `Content-Type` 的值被设置成了 `application/soap+xml` ，而HTTP请求的主体就是SOAP报文本身，至于SOAP报文的主体则包含了请求报文。在这个例子中，报文请求的是ID为 `123` 的评论：

```go
<m:GetCommentRequest>
　<m:CommentId>123</m:CommentId>
</m:GetCommentRequest >
```

这条SOAP报文示例经过了简化，实际的SOAP请求通常会复杂得多。下面展示的则是一条简化后的SOAP响应报文示例：

```go
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
<soap:Body xmlns:m="http://www.example.org/stock">
　<m:GetCommentResponse>
　　<m:Text>Hello World!</m:Text>
　</m:GetCommentResponse>
</soap:Body>
</soap:Envelope>
```

跟请求报文一样，响应报文也被包含在了SOAP报文的主体里面，它的内容为文本“Hello World!”：

```go
<m:GetCommentResponse>
　<m:Text>Hello World!</m:Text>
</m:GetCommentResponse>
```

正如上面的例子所示，与报文有关的所有数据都会被包含在信封里面。对基于SOAP的Web服务来说，这意味着它传输的所有信息都会被包裹在SOAP信封里面，然后再发送。顺带一提，虽然SOAP 1.2允许通过HTTP的 `GET` 方法发送SOAP报文，但大多数基于SOAP的Web服务都是通过HTTP的 `POST` 方法发送SOAP报文的。

下面展示的是一个WSDL报文示例，这种报文不仅详细，而且还很冗长，即使对简单的服务来说也是如此。基于SOAP的Web服务之所以没有基于REST的Web服务那么流行，其中一部分原因就与此有关——一个基于SOAP的Web服务越复杂，它对应的WSDL报文就越冗长。

```go
<?xml version="1.0" encoding="UTF-8"?>
<definitions　name ="ChitChat"
　targetNamespace="http://www.chitchat.com/forum.wsdl"
　xmlns:tns="http://www.chitchat.com/forum.wsdl"
　xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
　xmlns:xsd="http://www.w3.org/2001/XMLSchema"
　xmlns="http://schemas.xmlsoap.org/wsdl/">
　<message name="GetCommentRequest">
　　<part name="CommentId" type="xsd:string"/>
　</message>
　<message name="GetCommentResponse">
　　<part name="Text" type="xsd:string"/>
　</message>
　<portType name="GetCommentPortType">
　　<operation name="GetComment">
　　　<input message="tns:GetCommentRequest"/>
　　　<output message="tns:GetCommentResponse"/>
　　</operation>
　</portType>
　<binding name="GetCommentBinding" type="tns:GetCommentPortType">
　　<soap:binding style="rpc"
　　　transport="http://schemas.xmlsoap.org/soap/http"/>
　　<operation name="GetComment">
　　　<soap:operation soapAction="getComment"/>
　　　<input>
　　　　<soap:body use="literal"/>
　　　</input>
　　　<output>
　　　　<soap:body use="literal"/>
　　　</output>
　　</operation>
　</binding>
　<service name="GetCommentService" >
　　<documentation>
　　　Returns a comment
　　</documentation>
　　<port name="GetCommentPortType" binding="tns:GetCommentBinding">
　　　<soap:address location="http://localhost:8080/GetComment"/>
　　</port>
　</service>
</definitions>
```

位于报文开头的是报文对自身的定义，该定义给出了报文各个部分的名字，以及这些部分的类型：

```go
<message name="GetCommentRequest">
　<part name="CommentId" type="xsd:string"/>
</message>
<message name="GetCommentResponse">
　<part name="Text" type="xsd:string"/>
</message>
```

在此之后，报文通过 `GetComment` 操作定义了 `GetCommentPortType` 端口，该操作的输入报文为 `GetCommentRequest` ，而输出报文则为 `GetCommentResponse` ：

```go
<portType name="GetCommentPortType">
　<operation name="GetComment">
　　<input message="tns:GetCommentRequest"/>
　　<output message="tns:GetCommentResponse"/>
　</operation>
</portType>
```

最后，报文在位置http://localhost:8080/GetComment定义了一个 `GetCommentService` 服务，并将它与 `GetCommentPortType` 端口以及 `GetCommentsBinding` 地址进行绑定：

```go
<service name="GetCommentService" >
　<documentation>
　　Returns a comment
　</documentation>
　<port name="GetCommentPortType" binding="tns:GetCommentBinding">
　　<soap:address location="http://localhost:8080/GetComment"/>
　</port>
</service>
```

在实际中，SOAP请求报文通常会由WSDL生成的SOAP客户端负责生成；同样地，SOAP响应报文通常也是由WSDL生成的SOAP服务器负责生成。具体语言的客户端（如一个Go SOAP客户端）通常也会由WSDL负责生成，而其他代码则会通过使用这个客户端与服务器进行交互。这样做的结果是，只要WSDL是明确定义的，那么它生成的SOAP客户端通常也会是健壮的；与此同时，这种做法的缺陷是，开发人员每次修改服务器，即使是修改返回值的类型这样微小的修改，客户端都需要重新生成。重复生成客户端的过程通常都是冗长而乏味的，这也解释了为什么SOAP Web服务通常很少会出现大量的修改——因为对大型的SOAP Web服务来说，频繁的修改将是一场噩梦。

本章接下来不会再对基于SOAP的Web服务做进一步的介绍，但我们会学习如何使用Go语言创建以及分析XML。

