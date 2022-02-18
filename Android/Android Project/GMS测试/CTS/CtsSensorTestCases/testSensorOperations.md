[toc]

### 1. 测试命令

```shell
$ run cts -m CtsSensorTestCases -t android.hardware.cts.SensorTest#testSensorOperations
```

### 2. 报错项列表

#### 2.1 不支持传感器获取传感器类型失败

1. 报错信息

   ```
   java.lang.NullPointerException: Attempt to invoke virtual method 'int android.hardware.Sensor.getType()' on a null object reference
   ```

2. 错误分析

   因为设备不支持某些传感器，在使用该传感器 Sensor 对象时，对象为 null 造成的。

3. 解决方法

   先解决 CtsAppTestCases 中的 android.app.cts.SystemFeaturesTest#testSensorFeatures 相关报错再重试就可以了。