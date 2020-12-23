Android CPU&MEM debug 小记
===
tag:[[debug]][[android]][[system]]

## CPU
1. top -n 1 -d 1
    实时显示系统中各个进程的资源占用状况，类似于 Windows 的任务管理器

## Memory
> 像Linux这种现代操作系统的内存使用是很复杂的，因此很难准确的知道你的应用程序使用了好多内存。
>
> **查看内存使用的方式有很多种，但是各个方式查看到的结果可能会有微略不同。**

查看内存占用方法：
### 无控制台情况
通过Android设备[正在运行的服务]查看
- 入口：设置->开发者选项->正在运行的服务（老版本Android设备：Setting->Applications->Running services）

### 控制台输入命令
[src](https://zhidao.baidu.com/question/510267324.html)
[src2](http://blog.csdn.net/hudashi/article/details/7050897)

1. free -m
    ```
    [root@host ~]# free -m
    total used free shared buffers cached
    Mem: 1024 1005 19 0 9 782
    -/+ buffers/cache: 212 811
    Swap: 996 0 995
    ```
    从上看出这个Linux系统一共有内存1024M，但当前Linux 系统已经占用的内存有多少呢？大多数用户的答案是1005M，其实不然。
    
    当前占用的内存应该是212M，也就是1005下面那个数字：212，代表已经占用的内存。后面的那个811，代表当前Linux系统的可用内存。
    
    =="-/+ buffers/cache:"开头的这行才是实际的占用内存和可用内存==。
    
    所以，看内存使用情况，应该看"-/+ buffers/cache:"开头的这一行，如果这一行最后的数字接近0，那么说明Linux系统的内存快用完了，这时候Linux系统反应就比较慢。如果这个数字还比较大，那么Linux系统还有较多内存可用，系统不应该慢。

2. dumpsys meminfo [xx thread]

    得到com.teleca.robin.test进程使用的内存的信息:
    ```
    [root@host ~]# adb shell dumpsys meminfo com.teleca.robin.test"
    
    Applications Memory Usage (kB):
    Uptime: 12101826 Realtime: 270857936
    
    ** MEMINFO in pid 3407 [com.teleca.robin.test] **
                        native   dalvik    other    total
                size:     3456     3139      N/A     6595
           allocated:     3432     2823      N/A     6255
                free:       23      316      N/A      339
               (Pss):      724     1101     1070     2895
      (shared dirty):     1584     4540     1668     7792
        (priv dirty):      644      608      688     1940
     
     Objects
               Views:        0        ViewRoots:        0
         AppContexts:        0       Activities:        0
              Assets:        3    AssetManagers:        3
       Local Binders:        5    Proxy Binders:       11
    Death Recipients:        0
     OpenSSL Sockets:        0
     
     SQL
                heap:        0       memoryUsed:        0
    pageCacheOverflo:        0  largestMemAlloc:        0
    Asset Allocations
    zip:/data/app/com.teleca.robin.test-1.apk:/resources.arsc: 1K
    ```
     "size" 表示的是总内存大小（kb）, "allocated" 表示的是已使用了的内存大小（kb）, "free"表示的是剩余的内存大小（kb）, 更多的可以参照下文[内存名词解释](#内存名词解释)
     
     PSS意思请参照下文[Android内存之VSS/RSS/PSS/USS](#Android内存之VSS/RSS/PSS/USS)
     
3. procrank

    查看所有进程的内存使用情况:
    ```
    [root@host ~]#  procrank
    
    PID      Vss      Rss      Pss      Uss  cmdline
      188   75832K   51628K   24824K   19028K  system_server
      308   50676K   26476K    9839K    6844K  system_server
     2834   35896K   31892K    9201K    6740K  com.sec.android.app.twlauncher
      265   28536K   28532K    7985K    5824K  com.android.phone
      100   29052K   29048K    7299K    4984K  zygote
      258   27128K   27124K    7067K    5248K  com.swype.android.inputmethod
      270   25820K   25816K    6752K    5420K  com.android.kineto
     1253   27004K   27000K    6489K    4880K  com.google.android.voicesearch
     2898   26620K   26616K    6204K    3408K  com.google.android.apps.maps:FriendService
      297   26180K   26176K    5886K    4548K  com.google.process.gapps
     3157   24140K   24136K    5191K    4272K  android.process.acore
     2854   23304K   23300K    4067K    2788K  com.android.vending
     3604   22844K   22840K    4036K    3060K  com.wssyncmldm
      592   23372K   23368K    3987K    2812K  com.google.android.googlequicksearchbox
     3000   22768K   22764K    3844K    2724K  com.tmobile.selfhelp
      101    8128K    8124K    3649K    2996K  /system/bin/mediaserver
     3473   21792K   21784K    3103K    2164K  com.android.providers.calendar
     3407   22092K   22088K    2982K    1980K  com.teleca.robin.test
     2840   21380K   21376K    2953K    1996K  com.sec.android.app.controlpanel
    ```
     Vss、PSS等意思请参照下文[Android内存之VSS/RSS/PSS/USS](#Android内存之VSS/RSS/PSS/USS)
     
     为procrank命令和meminfo命令使用的内核机制不太一样，结果会有细微差别

4. cat /proc/meminfo

    该方式只能得出系统整个内存的大概使用情况。
    ```
    MemTotal:         395144 kB //总计物理内存的大小
    MemFree:          184936 kB //可用内存有多少
    Buffers:             880 kB //磁盘缓存内存的大小
    Cached:            84104 kB 
    SwapCached:            0 kB
    
    MemTotal ：可供系统和用户使用的总内存大小 (它比实际的物理内存要小，因为还有些内存要用于radio, DMA buffers, 等). 
    MemFree：剩余的可用内存大小。这里该值比较大，实际上一般Android system 的该值通常都很小，因为我们尽量让进程都保持运行，这样会耗掉大量内存。
    Cached: 这个是系统用于文件缓冲等的内存. 通常systems需要20MB 以避免bad paging states;。当内存紧张时，the Android out of memory killer将杀死一些background进程，以避免他们消耗过多的cached RAM ，当然如果下次再用到他们，就需要paging.
    ```

5.  ps -x


    ```
    主要得到的是内存信息是VSIZE 和RSS。
    USER     PID   PPID  VSIZE  RSS     WCHAN    PC         NAME
    .........................省略.................................
    app_70    3407  100   267104 22056 ffffffff afd0eb18 S com.teleca.robin.test (u:55, s:12)
    app_7     3473  100   268780 21784 ffffffff afd0eb18 S com.android.providers.calendar (u:16, s:8)
    radio     3487  100   267980 21140 ffffffff afd0eb18 S com.osp.app.signin (u:11, s:12)
    system    3511  100   273232 22024 ffffffff afd0eb18 S com.android.settings (u:11, s:4)
    app_15    3546  100   267900 20300 ffffffff afd0eb18 S com.sec.android.providers.drm (u:15, s:6)
    app_59    3604  100   272028 22856 ffffffff afd0eb18 S com.wssyncmldm (u:231, s:54)
    root      4528  2     0      0     c0141e4c 00000000 S flush-138:13 (u:0, s:0)
    root      4701  152   676    336   c00a68c8 afd0e7cc S /system/bin/sh (u:0, s:0)
    root      4702  4701  820    340   00000000 afd0d8bc R ps (u:0, s:5)
    VSZIE:意义暂时不明。
    VSS：请参考《Android内存之VSS/RSS/PSS/USS》
    注意1：由于RSS的价值不是很大，所以一般不用。
    注意2：通过该命令提取RSS，已经有了工具，具体参照《Android内存泄露利器（RSS内存统计篇）》及其系列。
    ```


### 编写应用查看
1. ActivityManager的getMemoryInfo(ActivityManager.MemoryInfo outInfo)
    ```
    /* ActivityManager.MemoryInfo只有三个Field:
     * availMem:表示系统剩余内存
     * lowMemory：它是boolean值，表示系统是否处于低内存运行
     * threshold：它表示当系统剩余内存低于好多时就看成低内存运行
     */
    private void displayBriefMemory() {    
        final ActivityManager activityManager = (ActivityManager) getSystemService(ACTIVITY_SERVICE);    
        ActivityManager.MemoryInfo info = new ActivityManager.MemoryInfo();   
        activityManager.getMemoryInfo(info);    
        Log.i(tag,"系统剩余内存:"+(info.availMem >> 10)+"k");   
        Log.i(tag,"系统是否处于低内存运行："+info.lowMemory);
        Log.i(tag,"当系统剩余内存低于"+info.threshold+"时就看成低内存运行");
    }
    ```
    ActivityManager.getMemoryInfo()是用ActivityManager.MemoryInfo返回结果，而不是Debug.MemoryInfo，他们不一样的。

2. Debug的getMemoryInfo(Debug.MemoryInfo memoryInfo)或ActivityManager的MemoryInfo[] getProcessMemoryInfo(int[] pids)

    该方式得到的MemoryInfo所描述的内存使用情况比较详细.数据的单位是kb.
    ```
    MemoryInfo的Field如下：
    dalvikPrivateDirty： The private dirty pages used by dalvik。
    dalvikPss ：The proportional set size for dalvik.
    dalvikSharedDirty ：The shared dirty pages used by dalvik.
    nativePrivateDirty ：The private dirty pages used by the native heap.
    nativePss ：The proportional set size for the native heap.
    nativeSharedDirty ：The shared dirty pages used by the native heap.
    otherPrivateDirty ：The private dirty pages used by everything else.
    otherPss ：The proportional set size for everything else.
    otherSharedDirty ：The shared dirty pages used by everything else.
    ```
    
    Android和Linux一样有大量内存在进程之间进程共享。某个进程准确的使用好多内存实际上是很难统计的。因为有paging out to disk（换页），所以如果你把所有映射到进程的内存相加，它可能大于你的内存的实际物理大小。
    
    这里可以参照下文[内存名词解释](#内存名词解释)
    
    - 注意1：MemoryInfo所描述的内存使用情况都可以通过命令adb shell "dumpsys meminfo %curProcessName%" 得到。
    - 注意2：如果想在代码中同时得到多个进程的内存使用或非本进程的内存使用情况请使用ActivityManager的MemoryInfo[] getProcessMemoryInfo(int[] pids)，否则Debug的getMemoryInfo(Debug.MemoryInfo memoryInfo)就可以了。
    - 注意3：可以通过ActivityManager的List<ActivityManager.RunningAppProcessInfo> getRunningAppProcesses()得到当前所有运行的进程信息。ActivityManager.RunningAppProcessInfo中就有进程的id，名字以及该进程包括的所有apk包名列表等。
    - 注意4：数据的单位是KB.

3. 使用Debug的getNativeHeapSize ()，getNativeHeapAllocatedSize ()，getNativeHeapFreeSize ()方法。

    该方式只能得到Native堆的内存大概情况，数据单位为字节。
    
    ```
    static long getNativeHeapAllocatedSize() 
    Returns the amount of allocated memory in the native heap.
    返回的是当前进程navtive堆中已使用的内存大小
    static long getNativeHeapFreeSize()
    Returns the amount of free memory in the native heap.
    返回的是当前进程navtive堆中已经剩余的内存大小
    static long getNativeHeapSize()
    Returns the size of the native heap.
    返回的是当前进程navtive堆本身总的内存大小
    
    示例代码：
    Log.i(tag,"NativeHeapSizeTotal:"+(Debug.getNativeHeapSize()>>10));
    Log.i(tag,"NativeAllocatedHeapSize:"+(Debug.getNativeHeapAllocatedSize()>>10));
    Log.i(tag,"NativeAllocatedFree:"+(Debug.getNativeHeapFreeSize()>>10));
    ```
    注意：DEBUG中居然没有与上面相对应的关于dalvik的函数。
    
---
## 附：

### 内存名词解释
    
```
dalvik：是指dalvik所使用的内存。
native：是被native堆使用的内存。应该指使用C\C++在堆上分配的内存。
other:是指除dalvik和native使用的内存。但是具体是指什么呢？至少包括在C\C++分配的非堆内存，比如分配在栈上的内存。
private:是指私有的。非共享的。
share:是指共享的内存。
PSS：实际使用的物理内存（比例分配共享库占用的内存）
Pss：它是把共享内存根据一定比例分摊到共享它的各个进程来计算所得到进程使用内存。网上又说是比例分配共享库占用的内存，那么至于这里的共享是否只是库的共享，还是不清楚。
PrivateDirty：它是指非共享的，又不能换页出去（can not be paged to disk ）的内存的大小。比如Linux为了提高分配内存速度而缓冲的小对象，即使你的进程结束，该内存也不会释放掉，它只是又重新回到缓冲中而已。
SharedDirty:参照PrivateDirty我认为它应该是指共享的，又不能换页出去（can not be paged to disk ）的内存的大小。比如Linux为了提高分配内存速度而缓冲的小对象，即使所有共享它的进程结束，该内存也不会释放掉，它只是又重新回到缓冲中而已。
```


### Android内存之VSS/RSS/PSS/USS
[src](http://hubingforever.blog.163.com/blog/static/17104057920114411313717/)
[src2](http://blog.csdn.net/cfy_phonex/article/details/9365983)

```
VSS - Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）
RSS - Resident Set Size 实际使用物理内存（包含共享库占用的内存）
PSS - Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存）
USS - Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）
```
**一般来说内存占用大小有如下规律：VSS >= RSS >= PSS >= USS**

> The aim of this post is to provide information that will assist in interpreting memory reports from various tools so the true memory usage for Linux processes and the system can be determined.
>
> Android has a tool called procrank (/system/xbin/procrank), which lists out the memory usage of Linux processes in order from highest to lowest usage. The sizes reported per process are VSS, RSS, PSS, and USS.
>
> For the sake of simplicity in this description, memory will be expressed in terms of pages, rather than bytes. Linux systems like ours manage memory in 4096 byte pages at the lowest level.
>
> VSS (reported as VSZ from ps) is the total accessible address space of a process. This size also includes memory that may not be resident in RAM like mallocs that have been allocated but not written to. VSS is of very little use for determing real memory usage of a process.
>
> RSS is the total memory actually held in RAM for a process. RSS can be misleading, because it reports the total all of the shared libraries that the process uses, even though a shared library is only loaded into memory once regardless of how many processes use it. RSS is not an accurate representation of the memory usage for a single process.
>
> PSS differs from RSS in that it reports the proportional size of its shared libraries, i.e. if three processes all use a shared library that has 30 pages, that library will only contribute 10 pages to the PSS that is reported for each of the three processes. PSS is a very useful number because when the PSS for all processes in the system are summed together, that is a good representation for the total memory usage in the system. When a process is killed, the shared libraries that contributed to its PSS will be proportionally distributed to the PSS totals for the remaining processes still using that library. In this way PSS can be slightly misleading, because when a process is killed, PSS does not accurately represent the memory returned to the overall system.
>
> USS is the total private memory for a process, i.e. that memory that is completely unique to that process. USS is an extremely useful number because it indicates the true incremental cost of running a particular process. When a process is killed, the USS is the total memory that is actually returned to the system. USS is the best number to watch when initially suspicious of memory leaks in a process.
>
> For systems that have Python available, there is also a nice tool called smem that will report memory statistics including all of these categories.

**为了简化描述，内存占用以页为单位表述，而不是字节。 通常每页为 4096 字节。**

- VSS 
    - ( 等同于 ps 命令列出的 VSZ) 是单个进程全部可访问的地址空间。
    - 其大小包括可能还尚未在内存中驻留的部分。比如地址空间已经被 malloc 分配，但是还没有实际写入。
    - 对于确定单个进程实际内存使用大小， VSS 用处不大。
 
- RSS
    - 是单个进程实际占用的内存大小。
    - RSS易被误导的原因在于， 它包括了该进程所使用的所有共享库的全部内存大小。对于单个共享库， 尽管无论多少个进程使用，实际该共享库只会被装入内存一次。
    - 对于单个进程的内存使用大小， RSS不是一个精确的描述。
 
- PSS 
    - 不同于RSS，它只是按比例包含其所使用的共享库大小。
    - 例如， 三个进程使用同一个占用30内存页的共享库。 对于三个进程中的任何一个，PSS将只包括10个内存页。
    - PSS 是一个非常有用的数字，因为系统中全部进程以整体的方式被统计， 对于系统中的整体内存使用是一个很好的描述。
    - 如果一个进程被终止，其PSS 中所使用的共享库大小将会重新按比例分配给剩下的仍在运行并且仍在使用该共享库的进程。
    - 此种计算方式有轻微的误差，因为当某个进程中止的时候，PSS 没有精确的表示被返还给整个系统的内存大小。
 
- USS 
    - 是单个进程的全部私有内存大小。亦即全部被该进程独占的内存大小。
    - USS是一个非常非常有用的数字， 因为它揭示了运行一个特定进程的真实的内存增量大小。
    - 如果进程被终止，USS就是实际被返还给系统的内存大小。
    - USS是针对某个进程开始有可疑内存泄露的情况，进行检测的最佳数字。
