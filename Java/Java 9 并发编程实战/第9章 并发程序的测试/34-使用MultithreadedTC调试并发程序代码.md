### 9.11　使用MultithreadedTC调试并发程序代码

由于Java并发应用在执行时具有不确定性，因此引入了可以测试并发应用的库 `MultithreadedTC` 。另外，在实际运行中，由于开发者不能保证应用中线程执行的顺序，因此可以使用 `MultithreadedTC` 中的 **节拍器** 。本案例中的所有测试线程都将以类的方法来实现。

本节将介绍如何使用 `MultithreadedTC` 库来实现对 `LinkedTransferQueue` 的测试。

