常用shell debug命令
===
tag:[[debug]][[shell]]










- 查询android service
```
service list
```

- getevent命令获取输入设备或者遥控器ir码
```
getevent
getevent -p // 查看板子的输入设备
$getevent -l /dev/input/event0 // 获得该设备底层发送的事件
EV_KEY       KEY_RIGHT            DOWN                
EV_SYN       SYN_REPORT           00000000            
EV_KEY       KEY_RIGHT            UP                  
EV_SYN       SYN_REPORT           00000000 
```

- input命令输入模拟按键
```
input keyevent HOME
input tap 168 252 // 模拟鼠标输入
input swipe 100 250 200 280
```
具体参阅：./命令行GUI相关操作/adb shell input来模拟滑动、按键、点击事件.md
```
// 可以java中用一下命令模拟：
execShellCmd("getevent -p");  
execShellCmd("sendevent /dev/input/event0 1 158 1");  
execShellCmd("sendevent /dev/input/event0 1 158 0");  
execShellCmd("input keyevent 3");//home  
execShellCmd("input text  'helloworld!' ");  
execShellCmd("input tap 168 252");  
execShellCmd("input swipe 100 250 200 280");
```

- am命令启动相关
```
am start -n com.jrm.localmm/.ui.main.FileBrowserActivity // am启动应用
am broadcast -a android.intent.action.MASTER_CLEAR // 发一个恢复出厂设置的广播
am broadcast -a com.android.launcher4.launcherReceiver --es path "/mnt/sdcard/xx.apk" --ei action 1 --ei versionCode 21 // am发送广播
```

- pm命令相关
```
pm list packages // 列出所有的包名
pm list packages com.android.setting // 列出setting的包的绝对路径
pm clear  [pkgname] // 清空指定包名应用数据
```

- dumpsys命令相关
```
dumpsys package 列出所有的安装应用的信息
dumpsys package com.android.XXX：查看某个包的具体信息
dumpsys meminfo [pname/pid]
dumpsys cpuinfo/power/display/SurfaceFlinger/activity...
```

- 截屏和录屏
```
screencap -p /sdcard/tmp.png
screenrecord /sdcard/tmp.mp4 录屏操作
```

- wm命令相关
```
wm density
wm size
```

- other（未验证）
```
// 查看apk中的信息以及编辑apk程序包
//首先需要注意：配置aapt工作环境（build-tools/版本号）
aapt dump xmltree demo.apk AndroidManifest.xml > xml.txt 
// 查看这个apk文件的程序名、包名、所用的sdk，程序版本以及权限信息等等 
aapt dump badging *.apk

//查看一个dex文件的详细信
dexdump[dex文件路径]
```
