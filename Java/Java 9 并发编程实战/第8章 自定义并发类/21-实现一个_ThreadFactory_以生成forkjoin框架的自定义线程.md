### 8.7　实现一个_ThreadFactory_以生成fork/join框架的自定义线程

Java 9最有趣的特性之一就是fork/join框架。它是 `Executor` 和 `ExecutorService` 接口的实现，允许执行 `Callable` 和 `Runnable` 任务，且无须管理执行它们的线程。

这个执行器的目标是可以执行分成更小部分的任务。其主要组成部分如下所示。

+ 这是一种由 `ForkJoinTask` 类实现的特殊任务。
+ 它提供了将任务分成子任务（fork操作）和等待这些子任务（join操作）完成的两个操作。
+ 这是一种命名为工作窃取的算法（work-stealing algorithm），可以优化线程池的使用。当一个任务等待它的子任务时，执行它的线程可以用来执行另一个线程。

fork/join框架的主要部分是 `ForkJoinPool` 类。具体来说，它有以下两个要素。

+ 正在等待执行的任务队列。
+ 执行任务的线程池。

`ForkJoinWorkerThread` 为 `Thread` 类增加了新的方法，比如创建线程时执行的 `onStart()` 方法和调用线程进行资源清理的 `onTermination()` 方法。 `ForkJoinPool` 类使用 `ForkJoinWorker ThreadFactory` 接口实现来创建它使用的工作线程。

本节将介绍如何实现一个用于 `ForkJoinPool` 类的自定义工作线程，以及如何在扩展 `ForkJoinPool` 类和实现 `ForkJoinWorkerThreadFactory` 接口的工厂对象中使用它。

