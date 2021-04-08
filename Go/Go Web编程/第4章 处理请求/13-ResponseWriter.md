### 4.3　ResponseWriter

首先创建一个 `Response` 结构，接着将数据存储到这个结构里面，最后将这个结构返回给客户端——如果你认为服务器是通过这种方式向客户端返回响应的，那么你就错了：服务器在向客户端返回响应的时候，真正需要用到的是 `ResponseWriter` 接口。

`ResponseWriter` 是一个接口，处理器可以通过这个接口创建HTTP响应。 `ResponseWriter` 在创建响应时会用到 `http.response` 结构，因为该结构是一个非导出（nonexported）的结构，所以用户只能通过 `ResponseWriter` 来使用这个结构，而不能直接使用它。

为什么要以传值的方式将ResponseWriter传递给ServeHTTP

> 在阅读了本章前面的内容之后，有的读者可能会感到疑惑—— `ServeHTTP` 为什么要接受 `ResponseWriter` 接口和一个指向 `Request` 结构的指针作为参数呢？接受 `Request` 结构指针的原因很简单：为了让服务器能够察觉到处理器对 `Request` 结构的修改，我们必须以传引用（pass by reference）而不是传值（pass by value）的方式传递 `Request` 结构。但是另一方面，为什么 `ServeHTTP` 却是以传值的方式接受 `ResponseWriter` 呢？难道服务器不需要知道处理器对 `ResponseWriter` 所做的修改吗？
> 对于这个问题，如果我们深入探究 `net/http` 库的源码，就会发现 `ResponseWriter` 实际上就是 `response` 这个非导出结构的接口，而 `ResponseWriter` 在使用 `response` 结构时，传递的也是指向 `response` 结构的指针，这也就是说， `ResponseWriter` 是以传引用而不是传值的方式在使用 `response` 结构。
> 换句话说，实际上 `ServeHTTP` 函数的两个参数传递的都是引用而不是值——虽然 `ResponseWriter` 看上去像是一个值，但它实际上却是一个带有结构指针的接口。

`ResponseWriter` 接口拥有以下3个方法：

+ `Write` ;
+ `WriteHeader` ;
+ `Header` 。

