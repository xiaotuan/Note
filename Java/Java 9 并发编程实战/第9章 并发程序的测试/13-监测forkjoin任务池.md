### 9.5　监测fork/join任务池

使用Executor框架可以把开发者从创建和管理线程的烦冗工作中释放出来。为了提升其他任务（如直接使用 `Thread` 对象或者Executor框架）的性能，Java 9提供了Executor框架的扩展，也就是fork/join框架。

利用框架中的 `fork()` 和 `join()` 方法，可以把任务切分成更小的任务模块。 `ForkJoinPool` 类可实现上述的任务框架。

本节将介绍在 `ForkJoinPool` 中会有哪些信息并且如何获得这些信息。

