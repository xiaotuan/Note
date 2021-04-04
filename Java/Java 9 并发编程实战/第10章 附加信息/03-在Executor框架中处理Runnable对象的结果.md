### 10.2　在Executor框架中处理Runnable对象的结果

通过使用 `Callable` 和 `Future` 接口，可以在 `Executor` 框架中得到并发任务的返回结果。虽然传统的Java并发编程是基于 `Runnable` 对象的，但这类对象没有返回值。

本节将使用 `Runnable` 对象来模拟 `Callable` 接口，从而得到并发任务的返回值。

