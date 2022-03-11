[toc]

### 1. 测试命令

```shell
$ run cts -m CtsAssistTestCases -t android.assist.cts.ScreenshotTest#testGreenScreenshot
```

### 2. 错误列表

#### 2.1 横屏设备在横屏下测试失败

1. 报错信息

   ```
   expected to be true
   	at android.assist.cts.ScreenshotTest.lambda$validateDeviceAndRunTestForColor$0$ScreenshotTest(ScreenshotTest.java:75)
   	at android.assist.cts.-$$Lambda$ScreenshotTest$YjTpy2HV6GZPU194jKP6cslLROk.run(Unknown Source:4)
   	at android.assist.cts.AssistTestBase.lambda$eventuallyWithSessionClose$6$AssistTestBase(AssistTestBase.java:680)
   	at android.assist.cts.-$$Lambda$AssistTestBase$iM8663-rZRABpIkmWhnhtq0y24o.call(Unknown Source:6)
   	at com.android.compatibility.common.util.Timeout.run(Timeout.java:171)
   	at android.assist.cts.AssistTestBase.eventuallyWithSessionClose(AssistTestBase.java:678)
   	at android.assist.cts.ScreenshotTest.validateDeviceAndRunTestForColor(ScreenshotTest.java:72)
   	at android.assist.cts.ScreenshotTest.testGreenScreenshot(ScreenshotTest.java:47)
   ```

2. 问题分析

   设备是横屏设备，在测试该项时是横屏放置的，当开启自动旋转，并竖屏放置设备，这时测试可以通过

3. 解决方法

   测试前，开启自动旋转功能，并竖着放置设备（保持屏幕竖屏显示）。

