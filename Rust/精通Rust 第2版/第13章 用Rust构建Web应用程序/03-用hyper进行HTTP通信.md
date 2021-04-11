### 13.2　用hyper进行HTTP通信

hyper软件包可以解析HTTP消息，并且具有优雅的设计、侧重于强类型的API。它被设计为原始HTTP请求类型安全的抽象，而不是像常见的HTTP程序库那样：将所有内容描述为字符串。Hyper中的HTTP状态代码被定义为枚举，例如StatusCode类型。几乎所有可以强类型化的内容都是如此，例如HTTP方法、MIME类型及HTTP首部等。

hyper将客户端和服务器端功能拆分为单独的模块。客户端允许你使用可配置的请求主体、首部及其他底层配置来构建和发送HTTP请求。服务器端允许你打开侦听套接字，并将请求处理程序附加给它。但是，它不包括任何请求路由处理程序实现——这些留给 Web框架处理。它旨在构建更高级Web框架的基础软件包。它在底层使用相同的tokio和futures异步抽象，因此非常高效。

hyper的核心是Service特征概念：

```rust
pub trait Service {
    type ReqBody: Payload;
    type ResBody: Payload;
    type Error: Into<Box<dyn StdError + Send + Sync>>;
    type Future: Future<Item = Response<Self::ResBody>, Error =
Self::Error>;
    fn call(&mut self, req: Request<Self::ReqBody>) -> Self::Future;
}
```

Service特征表示一种类型，它处理从任何客户端发送的HTTP请求，并返回Response响应，这是一个future。该类型需要实现该特征核心API的是call方法，它接受一个泛型Body上参数化的Request，并结合解析为Response的future，该Response通过关联类型ResBody进行参数化。我们不需要手动实现此特征，因为hyper包含一系列可以为用户实现Service特征的工厂方法。你只需提供一个接收HTTP请求并返回响应的函数即可。

在13.2.1小节中，我们将探讨 hyper 软件包中的客户端和服务器端API。让我们先从构建一个短网址服务器来探索服务器端API。

