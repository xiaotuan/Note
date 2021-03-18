### 12.3.1　launch函数

launch函数是协程的一个启动函数，它以非阻塞（non-blocking）的方式来启动当前协程，同时返回一个Job类型的对象作为当前协程的引用。下面是launch函数的一段代码。

```python
public fun launch(
    context: CoroutineContext = DefaultDispatcher,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope.() -> Unit
): Job {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy)
        LazyStandaloneCoroutine(newContext, block) else
        StandaloneCoroutine(newContext, active = true)
    coroutine.initParentJob(context[Job])
    start(block, coroutine, coroutine)
    return coroutine
}
```

launch函数主要有3个入参：context、start、block。这些参数的说明如表12-1所示。

<center class="my_markdown"><b class="my_markdown">表12-1　launch函数入参</b></center>

| 参数 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| context | 协程上下文 |
| start | 协程启动选项 |
| block | 由suspend修饰，是协程真正要执行的代码块 |

launch函数返回一个Job类型，Job接口实际上继承自CoroutineContext类型。Job是协程创建的一个后台任务概念，它持有该协程的引用，主要有表12-2所示的3种状态。

<center class="my_markdown"><b class="my_markdown">表12-2　launch函数的Job类型状态</b></center>

| 状态 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| New | 新建（可选的初始状态） |
| Active | 活动中（默认初始状态） |
| Completed | 结束（最终状态） |

