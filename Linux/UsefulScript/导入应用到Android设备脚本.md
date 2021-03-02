```shell
#!/bin/bash

# 使用方法：
#    ./pushApp.sh 设备IP地址 应用名称 应用包名


# 断开所有设备连接
adb disconnect
# 连接指定IP设备
adb connect $1
# 获取 root 权限
adb root
# 修改系统分区为可读分区
adb remount
# 导入应用 apk 文件
adb push ./$2/$2.apk system/app/$2/
# 导入应用 odex 文件
adb push ./$2/oat/arm/$2.odex system/app/$2/oat/arm/
# 导入应用 vdex 文件
adb push ./$2/oat/arm/$2.vdex system/app/$2/oat/arm/
# 获取应用的进程信息
value=`adb shell ps -A | grep $3`
echo $value
if [[ -n $value ]];then
    # 获取应用进程ID
    pid=`echo $value | awk '{ print $2 }'`
    echo $pid
    # 杀死进程
    adb shell kill $pid
fi
```

### 1. 导入开机向导应用命令

```shell
./pushSysApp.sh 192.168.31.55 SWGuide_sd net.sunniwell.guide
```

