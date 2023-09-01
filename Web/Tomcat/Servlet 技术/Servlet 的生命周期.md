[toc]

`Servlet` 的生命周期可以分为 3 个阶段：初始化阶段、运行时阶段和销毁阶段。在 `javax.servlet.Servlet` 接口中定义了 3 个方法：`init()`、`service()` 和 `destroy()`，它们将分别在 `Servlet` 的不同阶段被 `Servlet` 容器调用。

### 1. 初始化阶段

`Servlet` 的初始化阶段包括四个步骤：

（1）`Servlet` 容器加载 `Servlet` 类，把它的 `.class` 文件中的数据读入到内存中。

（2）`Servlet` 容器创建 `ServletConfig` 对象。`ServletConfig` 对象包含了特定 `Servlet` 的初始化配置信息，如 `Servlet` 的初始参数。此外，`Servlet` 容器还会使得 `ServletConfig` 对象与当前 `Web` 应用的 `ServletContext` 对象关联。

（3）`Servlet` 容器创建 `Servlet` 对象。

（4）`Servlet` 容器调用 `Servlet` 对象的 `init(ServletConfig config)` 方法。在 `Servlet` 接口的 `GenericServlet` 实现类的 `init(ServletConfig config)` 

