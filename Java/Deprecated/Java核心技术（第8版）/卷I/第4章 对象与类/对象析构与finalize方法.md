可以为任何一个类添加 `finalize` 方法。`finalize` 方法将在垃圾回收期清除对象之前调用。

> 注释：有个名为 `System.runFinalizersOnExit(true)` 的方法能够确保 `finallizer` 方法在 `Java` 关闭前被调用。不过，这个方法并不安全，也不鼓励大家使用。有一种替代的方法是使用方法 `Runtime.addShutdownHook` 添加 “关闭钩”（shutdown hook）。

