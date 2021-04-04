### 10.3　在ForkJoinPool类中处理未控制的异常

fork/join框架可以为 `ForkJoinPool` 类中的工作线程抛出的异常设置处理器。在使用 `ForkJoinPool` 之前，应该先弄明白任务和工作线程之间的区别。

要想使用fork/join框架，首先要实现一个继承了 `ForkJoinTask` 的任务，抑或是继承了 `RecursiveAction` 或 `RecursiveTask` 类。该任务需要实现在框架中并发执行的动作，工作线程会在 `ForkJoinPool` 中执行该动作。工作线程可以执行各种各样的任务。 `ForkJoinPool` 实现了工作窃取算法，这使得工作线程在任务完成或需要等待另一个任务完成时，去寻找新的任务。

本节将学习如何处理工作线程抛出的异常。在此之前，需要先实现如下两个元素。

+ 第一个元素是 `ForkJoinWorkerThread` 类的子类。该类实现了 `ForkJoinPool` 的工作线程。我们将实现一个用于抛出异常的基础子类。
+ 第二个元素是用来创建自定义工作线程的工厂类。 `ForkJoinPool` 使用工厂来创建它的工作线程。我们需要创建一个实现 `ForkJoinWorkerThreadFactory` 接口的类，并使用该类的实例对象作为 `ForkJoinPool` 的构造参数。新建的 `ForkJoinPool` 对象会使用这个工厂对象来创建工作线程。

