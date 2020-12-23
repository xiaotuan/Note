logcat命令相关
===
tag:[[debug]]

### SRC
- mstar_Android系统技能(基础篇).pdf
- [Log中'main', 'system', 'radio', 'events'以及android log分析](https://www.cnblogs.com/zhengtu2015/p/5134012.html)

### ANDROID的log
Android中不同的log是写到不同的设备中，共有四中类型：
- /dev/log/system
- /dev/log/main
- /dev/log/radion
- /dev/log/events

其中默认Log.v等写入/dev/log/main中。Slog写入/dev/log/system中。

我们在使用logcat 抓去日至的时候, 可以指定buffer，来请求不同的环形缓冲区 ('main', 'system', 'radio', 'events',默认为"-b main -b system")，因为Android日志系统为日志消息保持了多个循环缓冲区，而且不是所有的消息都被发送到默认缓冲区，要想查看这些附加的缓冲区，可以使用-b 选项，以下是可以指定的缓冲区：

```
main     — 记录应用程序l类型日志 (默认缓冲区)
system   — 记录系统类型日志 (默认缓冲区)
radio     — 记录包含在无线/电话相关的缓冲区消息　　　
events    — 记录事件相关的消息，二进制格式
以上环形缓冲区的大小均为256k
```
实时类的打印logcat如上边介绍，而关于一些系统其他状态信息的打印主要有：
- tcpdump
    - 对于 TCP/IP 协议相关的都可以使用这个来抓
    - adb shell tcpdump -s 10000 -w /sdcard/capture.pcap
- cat /proc/kmsg
    - 打印内核的信息，重复执行不保留上次显示过的信息
- dmesg
    - 打印内核启动过程的所有信息，开机信息亦保存在/var/log目录中，名称为dmesg的文件里
- dumpstate
    - 是系统状态信息，里面比较全，包括手机当前的内存信息、cpu 信息、logcat缓存， kernel缓存等等
    - 如果不能用请开启该service
- dumpsys
    - 关于系统service的内容都在这个里面
- bugreport
    - 里面包含有dmesg,dumpstate和dumpsys
- 工程模式等

### Logcat日志格式
1. 文本类型

```
Priority | tag | msg
优先级（Verbose, Debug, Info, Warn, Error, Fatal） | 标签 | 信息
```

2. 二进制类型

```
tag number | tag name | value(name, type, unit)
```


### Logcat命令参数适用
```
logcat -help
logcat -s <tag> // 屏蔽所有信息，只留下tag的打印
logcat -c // 清除缓冲区log
logcat -g // 获取缓冲区大小
logcat -t <count> //输出最新的count挑log信息
logcat -b // 可以指定输出哪个缓冲区（mian/system/radio/events,默认main/system）
logcat -B // 二进制方式输出
logcat -v // 设置Log输出格式
    logcat -v time
    logcat -v thread
    logcat -v threadtime
    logcat -v log // 全部信息都包含

// 过滤log
logcat *:S tag1 tag2:E // 只留tag1和tag2的E&F信息
// 优先级：
V < D < I < W < I < F
logat tag1:S tag2:E // 屏蔽tag1，显示tag2的E&F
logcat *: E // 显示所有的E&F
```
### 开机自动抓log
init.xx.xx添加：
```
// 直接输出到终端
    service logcat /system/bin/logcat -f /dev/kmsg
    class main
    Oneshot

// 保存到本地
    service logcat /system/bin/logcat -f /data/log.log
    class main
    console // 同时在终端输出
    Oneshot

// 保存多个文件（-n），并由大小限制（-r）
    service logcat /system/bin/logcat -b system -b events -b main -k -r 1000 -n 10 -v threadtime -f /data/log/log.log
    class main
    user log
    group log
```

### 分析内容
1. **错误字眼**
    - error/fail/"E/"这些的错误信息
2. **Build fingerprint**, 为动态库死机
3. **java类**抛异常
    - NullPointException之类
4. **ANR**(Application Not Responding)，直接搜这个关键字查看trace分析Java包问题
    - /data/anr/trace.txt
    - 里边的每一段都是一个线程，先搜tid为1的主线程
    - 搜"DALVIK THREAD"快速定位虚拟机信息日志
    - 这里可以查看mstarxxx基础篇.pdf p313例子
5. **lowmemorykill**
    - 当kernel发现free memory比minfree小（在/drivers/staging/android/lowmemorykiller.c中写死），会自动启动后台内存回收线程
    - 根据apk进程的不同等级进行排序回收（oom_adj），而等级可以在activityManager里边的updateOomAdjLocked里面写死，或者AnroidManifest.xml里面设置android:persistent=true
6. **watchdog killing system process**
    - watchdog 杀死服务进程
7. **看activityManager的CPU等信息**
    - 92%TOTAL: 8.4% user + 9% kernel + ==88% iowait== + 2.1% softirq
8. 


