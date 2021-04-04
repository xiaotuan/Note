### 8.8　自定义运行于fork/join框架中的任务

`Executor` 框架分离任务的创建及其执行。有了它，只需要实现 `Runnable` 对象并使用一个 `Executor` 对象即可。只需将 `Runnable` 任务发送给执行程序，并创建、管理和确定执行这些任务所需的线程。

Java 9在fork/join框架中提供了一种特殊的执行器（它在Java 7中引入）。这个框架旨在解决用分治（divide and conquer）技术将任务分解成更小任务的问题。在任务内部，必须检查想要解决问题的大小，如果问题的大小大于既定大小，则将其分为两个或多个任务，并使用该框架执行它们；如果问题的大小小于既定大小，则直接在任务中解决问题。当然，它也可以返回一个结果。fork/join框架实现了工作窃取算法，可以改善这些问题的整体性能。

fork/join框架的 `Main` 类是 `ForkJoinPool` 类。具体来说，它有以下两个要素。

+ 正在等待执行的任务队列。
+ 执行任务的线程池。

默认情况下，由 `ForkJoinPool` 类执行的任务是 `ForkJoinTask` 类的对象。也可以将 `Runnable` 和 `Callable` 对象发送到 `ForkJoinPool` 类中，但它们无法利用fork/join框架的所有优点。通常来说，会发送 `ForkJoinTask` 类的两个子类中的一个到 `ForkJoinPool` 对象。

+ `RecursiveAction` ：如果任务没有返回结果。
+ `RecursiveTask` ：如果任务有返回结果。

本节将介绍如何通过扩展 `ForkJoinTask` 类的任务来实现自己的fork/join框架的任务。要实现的任务会测量并将执行时间打印到控制台，以便可以控制其演变。也可以实现自己的fork/join任务来打印日志信息，获取任务中使用的资源或者后置处理任务的结果。

