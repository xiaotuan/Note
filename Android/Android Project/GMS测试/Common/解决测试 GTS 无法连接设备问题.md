[toc]

### 1. 报错信息

```
02-22 11:16:25 W/CommandScheduler: Device LT878811003 is unresponsive. Reason: Attempted adb content multiple times on device LT878811003 without communication success. Aborting.
02-22 11:17:26 W/BusinessLogicPreparer: Option config-filename isn't set. Using empty string instead.
02-22 11:17:26 W/BusinessLogicPreparer: Option version isn't set. Using 'null' instead.
02-22 11:20:00 W/NativeDevice: TimeoutException () when attempting adb content on device LT878811003
02-22 11:22:06 W/NativeDevice: TimeoutException () when attempting adb content on device LT878811003
02-22 11:24:12 W/NativeDevice: TimeoutException () when attempting adb content on device LT878811003
02-22 11:24:18 W/TestInvocation: Invocation did not complete due to device LT878811003 becoming not available. Reason: com.android.tradefed.device.DeviceUnresponsiveException[DEVICE_UNRESPONSIVE|520751|LOST_SYSTEM_UNDER_TEST]: Attempted adb content multiple times on device LT878811003 without communication success. Aborting.
02-22 11:26:15 E/RunCommandTargetPreparer: Skipping command teardown since exception was DeviceNotAvailable
02-22 11:26:15 E/ReportLogCollector: Invocation finished with DeviceNotAvailable, skipping collecting logs.
02-22 11:26:15 E/RunCommandTargetPreparer: Skipping command teardown since exception was DeviceNotAvailable
02-22 11:26:15 E/NativeDevice: Skip Tradefed Content Provider teardown due to DeviceNotAvailableException.
02-22 11:26:15 E/TestDevice: Skip WifiHelper teardown due to DeviceNotAvailableException.
02-22 11:26:15 E/TestInvocation: 'adb devices' output:
List of devices attached 
LT878811003	device

02-22 11:26:15 W/NativeDevice: Attempting to stop logcat when not capturing for LT878811003
02-22 11:26:16 I/SuiteResultReporter: 
============================================
================= Results ==================
=============== Consumed Time ==============
Total aggregated tests run time: 0 ms
=============== Summary ===============
Total Run time: 9m 50s
0/0 modules completed
Total Tests       : 0
PASSED            : 0
FAILED            : 0
============== End of Results ==============
============================================
```

### 2. 解决方法

因为 adb 版本过低造成的，通过如下命令安装最新 adb：

```shell
$ sudo apt install adb
```

