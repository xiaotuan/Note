[toc]

可以使用如下命令可以查看 `am start` 帮助文档：

```shell
adb shell am
```

### 1. 使用包名类名启动 Activity

```shell
adb shell am start -n 包名/类名
```

例如：

```shell
$ adb shell am start -n com.mediatek.batterywarning/com.mediatek.batterywarning.BatteryWarningActivity
```

### 2. 使用 Action 启动 Activity

```shell
adb shell am start -a Action
```

例如：

```shell
$adb shell am start -a mediatek.intent.action.BATTERY_WARNING
```

### 3. 使用包名启动应用

```shell
adb shell am start 包名
```

例如：

```shell
$ adb shell am start com.android.settings
```

### 4. 带参数启动 Activity

下面以包名类型方式带参数启动 Activity 为例：

```shell
adb shell am start -n 包名/类名 --es key value
```

例如：

```shell
$ adb shell am start -n com.mediatek.batterywarning/com.mediatek.batterywarning.BatteryWarningActivity --es type hight
```

相关参数解释如下：

+ `--es key stringValue`：传递字符串参数
+ `--ez key booleanValue`：传递 Boolean 参数
+ `--ei key intValue`：传递 int 参数
+ `--el key longValue`：传递 long 参数
+ `--ef key floatValue`：传递 float 参数