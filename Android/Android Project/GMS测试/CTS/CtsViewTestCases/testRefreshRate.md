[toc]

### 1. 测试命令

```shell
$ run cts -t CtsViewTestCases -m android.view.cts.DisplayRefreshRateTest#testRefreshRate
```

### 2. 报错信息

```
java.lang.AssertionError
	at org.junit.Assert.fail(Assert.java:86)
	at org.junit.Assert.assertTrue(Assert.java:41)
	at org.junit.Assert.assertTrue(Assert.java:52)
	at android.view.cts.DisplayRefreshRateTest.testRefreshRate(DisplayRefreshRateTest.java:97)
	at java.lang.reflect.Method.invoke(Native Method)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:52)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
	at org.junit.internal.runners.statements.FailOnTimeout$CallableStatement.call(FailOnTimeout.java:148)
	at org.junit.internal.runners.statements.FailOnTimeout$CallableStatement.call(FailOnTimeout.java:142)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.lang.Thread.run(Thread.java:923)
```

### 3. 解决方法

CTS 要求设备屏幕刷新频率为 60 ±2 Hz，让驱动同事修改屏幕刷新频率为 60 Hz 即可。