### 15.4.2　其他WebAssembly项目

除了wasm-bindgen软件包和类似的软件包之外，Rust社区还有很多其他新兴的框架和项目值得探究。

#### Rust

wasm-bindgen并不是唯一一个旨在创造良好开发体验的项目。Rust生态系统中的其他部分项目如下所示。

+ **Stdweb** ：该软件包旨在提供一个基于Rust的高级API，用于通过Web访问DOM API。
+ **Yew** ：这是一个完整的前端Web应用程序构建框架，允许用户在Rust中编写可以访问Web API并将其编译为wasm的Web应用程序，以便它们可以在Web上运行。它的灵感来自Elm和ReactJS项目。它还通过Web上的Web worker封装基于actor的消息传递实现并发。Yew内部采用stdweb软件包访问DOM API。
+ **Nebutlet** ：这是一个微内核，它可以在没有系统调用接口的情况下执行WebAssembly程序，这在大多数操作系统上都是很常见的。
+ **Wasmi** ：这是一个用Rust实现的wasm虚拟机，但它与浏览器引擎中的wasm VM无关。该项目由Parity（一家基于以太坊的初创公司）发起，它更适合在多个平台上运行WebAssembly应用程序。

#### 其他语言

其他语言也有针对WebAssembly的技术，如下所示。

+ **Life** ：它是一个WebAssembly虚拟机，是由Golang实现的，可以安全地运行高性能、分布式的应用程序。
+ **AssemblyScript** ：这是一个TypeScript到WebAssembly的编译器。
+ **Wagon** ：它是Golang下的WebAssembly解释器。

