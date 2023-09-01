[toc]

`Java Web` 应用的生命周期是由 `Servlet` 容器来控制的。归纳起来，`Java Web` 应用的生命周期包括三个阶段：

+ 启动阶段：加载 `Web` 应用的有关数据，创建 `ServletContext` 对象，对 `Filter`（过滤器）和一些 `Servlet` 进行初始化。
+ 运行时阶段：为客户端提供服务。
+ 终止阶段：释放 `Web` 应用所占用的各种资源。

### 1. 启动阶段

`Servlet` 容器在启动 `Java Web` 应用时，会完成以下操作：

（1）把 `web.xml` 文件中的数据加载到内存中。

（2）为 `Java Web` 应用创建一个 `ServletContext` 对象。

（3）对所有的 `Filter` 进行初始化。

（4）对那些需要在 `Web` 应用启动时就初始化的 `Servlet` 进行初始化。

### 2. 运行时阶段

这是 `Java Web` 应用最主要的生命阶段。在这个阶段，它的所有 `Servlet` 都处于待命状态，随时可以响应客户端的特定请求，提供相应的服务。假如客户端请求的 `Servlet` 还不存在，`Servlet` 容器会先加载并初始化 `Servlet`，然后再调用它的 `service()` 服务方法。

### 3. 终止阶段

`Servlet` 容器在终止 `Java Web` 应用时，会完成以下操作：

（1）销毁 `Java Web` 应用中所有处于运行时状态的 `Servlet`。

（2）销毁 `Java Web` 应用中所有处于运行时状态的 `Filter`。

（3）销毁所有与 `Java Web` 应用相关的对象，如 `ServletContext` 对象等，并且释放 `Web` 应用所占用的相关资源。

