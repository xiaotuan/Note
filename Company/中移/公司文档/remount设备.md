[toc]

### 1. 海思芯片 remoute 方法

#### 1.1  方法一

```shell
$ adb root
$ adb shell mount -o remount rw /system
```

### 1.2 方法二

```shell
$ adb root
$ adb remount
```

### 2. Amlogic 芯片 remoute 方法

```shell
$ adb root
$ adb shell echo 1 > /sys/class/remount/need_remount
$ adb shell mount -o remount /system
```

