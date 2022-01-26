由于 Java有自动的垃圾回收器，不需要人工回收内存，所以 Java 不支持析构器。

可以为任何一个类添加 finalize 方法。 finalize 方法将在垃圾回收器清除对象之前调用。在实际应用中，不要依赖于使用 finalize 方法回收任何短缺的资源，这是因为很难知道这个方法什么时候才能够调用。

> 提示
>
> 有个名为 `System.runFinalizersOnExit(true)` 的方法能够确保 finalizer 方法在 Java 关闭前被调用。不过，这个方法并不安全，也不谷粒大家使用。有一种代替的方法是使用方法 `Runtime.addShutdownHook()` 添加 ”关闭钩“。