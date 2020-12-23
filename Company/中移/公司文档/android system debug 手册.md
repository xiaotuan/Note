android system debug 手册
===
tag:[[debug]]

### SRC
- Amlogic MBOX现场分析指南


### shell debug命令
./logcat命令相关.md

./常用shell debug命令.md

### 内存泄漏
./JAVA内存泄漏DEBUG.md

./性能debug相关/Android CPU&MEM debug小记.md

./性能debug相关/Linux下清理内存和Cache方法




### 系统内部相关信息
#### /proc 目录内容
FROM:[src](http://blog.chinaunix.net/uid-22666248-id-3040364.html)
- 查看内核启动的命令行
```
cat /proc/cmdline
```

- 查看某程序在进程中执行的命令行
```
cat /proc/1234/cmdline   //1234为进程pid，但是cat会省略如/0符号，需要注意
```

### 其他
- 查询tombstone     
    - /data/tombstones（比较严重的系统错误）
- core dump（core为内存意思）
    - 原因主要有：
        - 内存越界/非法指针/堆栈溢出
---
测试复现问题注意点
1. logcat抓的时间点、内容
2. 性能方面log也要抓
3. 卡死问题记得抓tombstone
3. apk问题记得有anr要提取trace.txt

---

## 问题集
### 开机无法启动
- check是否system有mount
- 是否概率性
- data之类分区是否读写权限正确
- log搜下backtrace

### 系统慢
- logcat分析
- 分析系统CPU占用，top/meminfo
- 关闭所有的log，包括logcat,kmsg等

### 开机速度慢
- 开机日志(logcat -v time/ logcat -b events -v time)

### ANR
- 分析系统性能
    - CPU / MEM / IO/ log中的activityManager打印性能
- 分析trace
    - 是否死锁（waiting to lock）
