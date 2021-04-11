### 13.2.1　hyper服务器端API——构建一个短网址服务

在本小节中，我们将构建一个短网址服务器，并公开一个/shorten 端点，此端点接收POST请求，其主体包含要缩短的URL网址。让我们通过运行cargo new hyperurl命令创建一个新项目，其中的Cargo.toml文件包含以下依赖项：

```rust
# hyperurl/Cargo.toml
[dependencies]
hyper = "0.12.17"
serde_json = "1.0.33"
futures = "0.1.25"
lazy_static = "1.2.0"
rust-crypto = "0.2.36"
log = "0.4"
pretty_env_logger = "0.3"
```

我们将该URL短网址服务器命名为hyperurl。URL短网址服务是一种为给定URL创建较短的URL的服务。当你有一个较长的URL时，与某人分享它会变得很烦琐。目前存在很多URL短网址服务，例如bit.ly。Twitter经常在推文中使用短网址，以便节省空间。

这是我们在main.rs中的初始实现：

```rust
// hyperurl/src/main.rs
use log::{info, error};
use std::env;
use hyper::Server;
use hyper::service::service_fn;
use hyper::rt::{self, Future};
mod shortener;
mod service;
use crate::service::url_service;
fn main() {
    env::set_var("RUST_LOG","hyperurl=info");
    pretty_env_logger::init();
    let addr = "127.0.0.1:3002".parse().unwrap();
    let server = Server::bind(&addr)
        .server(|| service_fn(url_service))
        .map_err(|e| error!("server error: {}", e));
    info!("URL shortener listening on http://{}", addr);
    rt::run(server);
}
```

在main函数中，我们创建了一个Server实例，并将其绑定到回送地址和端口的字符串"127.0.0.1:3002"。这将返回一个构造器实例，在该实例上调用server，然后传入实现Service特征的函数url_service。函数url_service将Request映射到Response的future。service_fn是具有以下签名的工厂函数：

```rust
pub fn service_fn<F, R, S>(f: F) -> ServiceFn<F, R> where
    F: Fn(Request<R>) -> S,
    S: IntoFuture,
```

如你所见，F必须是一个Fn闭包。

我们的函数url_service实现了Service特征。接下来，让我们看看service.rs中的代码：

```rust
// hyperurl/src/service.rs
use std::sync::RwLock;
use std::collections::HashMap;
use std::sync::{Arc};
use std::str;
use hyper::Request;
use hyper::{Body, Response};
use hyper::rt::{Future, Stream};
use lazy_static::lazy_static;
use crate::shortener::shorten_url;
type UrlDb = Arc<RwLock<HashMap<String, String>>>;
type BoxFut = Box<Future<Item = Response<Body>, Error = hyper::Error> +
Send>;
lazy_static! {
    static ref SHORT_URLS: UrlDb = Arc::new(RwLock::new(HashMap::new()));
}
pub(crate) fn url_service(req: Request<Body>) -> BoxFut {
    let reply = req.into_body().concat2().map(move |chunk| {
        let c = chunk.iter().cloned().collect::<Vec<u8>>();
        let url_to_shorten = str::from_utf8(&c).unwrap();
        let shortened_url = shorten_url(url_to_shorten);
        SHORT_URLS.write().unwrap().insert(shortened_url,
url_to_shorten.to_string());
        let a = &*SHORT_URLS.read().unwrap();
        Response::new(Body::from(format!("{:#?}", a)))
    });
    Box::new(reply)
}
```

该模块公开了一个函数url_service，它实现了Service特征。

我们的url_service方法通过获取Request<Body>类型的请求来实现call方法，并返回Box类型的future。

接下来是我们的shortener模块：

```rust
// hyperurl/src/shortener.rs
use crypto::digest::Digest;
use crypto::sha2::Sha256;
pub(crate) fn shorten_url(url: &str) -> String {
    let mut sha = Sha256::new();
    sha.input_str(url);
    let mut s = sha.result_str();
    s.truncate(5);
    format!("https://u.rl/{}", s)
}
```

我们的shorten_url函数将URL缩短为&str。然后它计算URL的Sha-256的哈希值并将其截断为长度为5的字符串。这显然不是真正的URL缩短功能的处理过程，也不是可扩展的解决方案，但是它方便我们演示代码。

让我们来看看它的细节：

![160.png](../images/160.png)
我们的服务器正在运行，此时可以通过curl向其发送POST请求。另一种方法是通过构建命令行客户端将URL发送给此短网址服务器。

虽然Hyper被推荐用于复杂的HTTP应用程序，但每次创建处理程序服务，注册并在运行时运行它都非常麻烦。通常，为了构建一些小型的工具应用，有时需要发送几个GET请求的命令行应用程序，这样做就有点小题大作了。幸运的是，我们还有一个名为reqwest的软件包，它是一个支持自定义的hyper包装器。顾名思义，它的设计灵感来自Python的Requests库。我们将使用它来构建发送URL缩短请求的hyperurl客户端。

