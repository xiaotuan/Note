[toc]

作为Androd开发工作者的我们，经常会在实际的开发工作中遇到各种Android卡死黑屏系统稳定性等问题，遇到如上问题除了考验Android基本功是否扎实以外，最重要的是就是能否抓取到足够的日志和是否有足够的调试手段进行分析了，下面奉上我在实际工作中总结的抓取Log日志用到的各种必杀技。

### 应用冻结/奔溃

   应用冻结/奔溃对于Android应用开发的工程师来说是比较常见的，该种问题通常大概率是ANR或者是Jni层Native crash了，可以通过如下手段获取奔溃日志：

```
1.捕获通用日志
logcat log (main, system, event, radio)

2.抓取内核日志(Dmesg/kernel logs)
adb shell  " cat  /proc/kmsg "  或者 adb shell dmesg

3.获取系统ANRT日志（Trace file /data/anr） 
adb pull /data/anr/  .\anr

4.获取系统墓碑日志(tombstones )
adb pull /data/tombstones  .\tombstones

5.过滤运行时异常和DEBUG异常
adb logcat  -s AndroidRuntime,DEBUG > crash.txt
```

如上相关日志的获取必须在发生异常的时候立马获取，这个原因自不必多说。

### Reboot Android系统

   Reboot Android系统这种系统稳定性问题，一般出现在system_server出现了死锁问题，然后Android的WatchDog看门狗检测到了，然后重启Android相关进程导致，可以通过如下手段捕获奔溃日志：

```
1.捕获通用日志
logcat log (main, system, event, radio)

2.抓取内核日志(Dmesg/kernel logs)
adb shell  " cat  /proc/kmsg "  或者 adb shell dmesg

3.抓取bugreport信息(该信息是Android为了方便开发人员分析整个系统平台和某个app在运行一段时间之内的所有信息，专门开发了bugreport工具)
adb shell bugreport  > bugreport.txt

4.抓取dumpstate信息(dumpstate类似于dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpstate > dumpstate.txt

5.抓取dumpsate(dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpsys > dumpsys.txt

6.抓取Binder传输日志
adb pull /d/binder/ .\binder

7.获取系统ANRT日志（Trace file /data/anr） 
adb pull /data/anr/  .\anr

8.获取系统墓碑日志(tombstones )
adb pull /data/tombstones  .\tombstones
```

### 终端黑屏(Black screen)
   终端黑屏(Black screen)这种系统稳定性问题，一般出现问题时，此时power按键一般能用，可以通过adb shell getevent查看到input事件信息。可以通过如下手段捕获奔溃日志：

```
1.捕获通用日志
logcat log (main, system, event, radio)

2.抓取内核日志(Dmesg/kernel logs)
adb shell  " cat  /proc/kmsg "  或者 adb shell dmesg

3.抓取bugreport信息(该信息是Android为了方便开发人员分析整个系统平台和某个app在运行一段时间之内的所有信息，专门开发了bugreport工具)
adb shell bugreport  > bugreport.txt

4.抓取dumpstate信息(dumpstate类似于dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpstate > dumpstate.txt

5.抓取dumpsate(dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpsys > dumpsys.txt

6.抓取Binder传输日志
adb pull /d/binder/ .\binder

7.获取系统ANRT日志（Trace file /data/anr） 
adb pull /data/anr/  .\anr

8.获取系统墓碑日志(tombstones )
adb pull /data/tombstones  .\tombstones

9.获取meminfo日志(Meminfo log) 
adb shell cat proc/meminfo >meminfo.txt 

10.获取Procrank信息 (Procrank log) 
adb shell procrank >procrank.txt 

11 获取top信息日志(Top log) 
adb shell top -m 10  >top.txt 

12.Add below information: 
•Adb workable or not, ANR or not 
•CTP workable or not
 -> touch screen and observe the output of
 "adb shell getevent". 
•Display driver workable or not
 -> Use the screencast to see
 if the screen can be displayed 
•Power key/volume key work or not? 
Menu/back/home key work or not? 

13 .查看kernel的线程函数栈
adb shell "echo t > /proc/sysrq-trigger"
adb shell "cat /proc/kmsg" > ./kmsg_trigger.txt
```

### 系统卡死/屏幕卡死(System Freeze/ Touch panel freeze)

   出现这个问题，恭喜你，这个是Android系统稳定性里面最严重的，此时一般Power按键，菜单键等都统统失效了，此时通过可以通过adb shell getevent查看到input事件信息也看不到任何信息了，那么我们此时可以通过如下手段捕获日志：

```
1.捕获通用日志
logcat log (main, system, event, radio)

2.抓取内核日志(Dmesg/kernel logs)
adb shell  " cat  /proc/kmsg "  或者 adb shell dmesg

3.抓取bugreport信息(该信息是Android为了方便开发人员分析整个系统平台和某个app在运行一段时间之内的所有信息，专门开发了bugreport工具)
adb shell bugreport  > bugreport.txt

4.抓取dumpstate信息(dumpstate类似于dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpstate > dumpstate.txt

5.抓取dumpsate(dumpsys都是android提供给开发者的帮助了解系统运行状态的利器)
adb shell dumpsys > dumpsys.txt

6.抓取Binder传输日志
adb pull /d/binder/ .\binder

7.获取系统ANRT日志（Trace file /data/anr） 
adb pull /data/anr/  .\anr

8.获取系统墓碑日志(tombstones )
adb pull /data/tombstones  .\tombstones

9.获取meminfo日志(Meminfo log) 
adb shell cat proc/meminfo >meminfo.txt 

10.获取Procrank信息 (Procrank log) 
adb shell procrank >procrank.txt 

11 获取top信息日志(Top log) 
adb shell top -m 10  >top.txt 

12.Add below information: 
•Adb workable or not, ANR or not 
•CTP workable or not
 -> touch screen and observe the output of
 "adb shell getevent". 
•Display driver workable or not
 -> Use the screencast to see
 if the screen can be displayed 
•Power key/volume key work or not? 
Menu/back/home key work or not? 

13 .查看kernel的线程函数栈
adb shell "echo t > /proc/sysrq-trigger"
adb shell "cat /proc/kmsg" > ./kmsg_trigger.txt

14.抓取窗口信息 (Dumpsys window log)
adb shell dumpsys window > dump_window.txt

15.抓取可以 event信息(Key events log) 
adb shell getevent -rtl /dev/input/event0 按键事件
```

### 结语
   如上是分别针对不同的Android系统稳定性稳定，提供的日志抓取方法。有了相关的日志信息了，接下来的步骤就是进行相关的具体日志分析了，分析日志就要考验开发者的硬实力了。不过这个也有一定的套路可以遵循，在这里打一个广告，可以参见如下的bug进行分析和借鉴。
[记一次Android概率性定屏问题分析解决路程](https://blog.csdn.net/tkwxty/article/details/102756703)
[ChkBugReport的使用](https://blog.csdn.net/tkwxty/article/details/97959066)
[Android ANR日志实战分析指南](https://blog.csdn.net/tkwxty/article/details/102753227)
————————————————
版权声明：本文为CSDN博主「IT先森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/tkwxty/article/details/103121718