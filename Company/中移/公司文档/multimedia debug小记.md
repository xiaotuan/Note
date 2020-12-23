mm debug小记
===
tag:[[debug]]

## 工具集
- mediainfo查看文件格式
- elecard查看n多信息


## 问题集
### 播放视频黑屏
- 是否osd阻挡（video layer在osd layer之下）
    - 根据平台不同设置屏蔽osd的命令
- 是否视频显示在video layer上
    - 输入cat /sys/class/vfm/map，查看相关信息（具体见aml的指南）
- 按照播放流程查询：来源-demux-decode-display
    - 比如查看各阶段的buffer是否正常

### 花屏 & 抖动
- for aml，查看现场分析指南.pdf 的相应命令debug

### 音视频卡顿
1. 确定片源，web还是本地文件
    - 本地文件请确认文件大小，码率，是否超出了io的能力（比如放到了U盘）
    - 网络下载请确定是否网速问题导致卡顿
2. 确认是audio还是video还是avsync问题
    - 方法1：只播放v活a来确定
    - 方法2：执行freerun命令查看
    - 以上方法各自chip平台均有自有player的属性命令，请查看相应手册
    - 方法3：对比，dump文件下来，放到对比机器或者电脑软解码播放
3. 是否性能问题
    - 查看系统性能的那篇debug小记（CPU/MEM/IO）

### av不同步
- 查看PTS是否差太多（运行chip相应的命令log查看，或者dump本地运用工具查看）
- 开启freerun看看
- dump本地看看
- 确定系统性能
- 不同播放器有其他sync方式可以走，运行相应命令

### seek/切台av不对
- 确定是否package丢到位
- 是否执行了慢同步func
- 因此也是一样方法，只播放a或者v来看看是否正常

## dump相关：
1. 用tcpdump抓原始包
2. 本地：

aml：
```
mkdir /data/tmp
chmod 777 /data/tmp
setprop media.libplayer.dumpmode x
【1】ts,ps,rm 几种流的raw data 从文件或网络读到的数据dump
【2】ts,ps,rm 几种流的raw data 写入解码buffer 的数据dump
【4】es 码流video 数据，读数据dump
【8】es 码流video 数据，写数据dump
【16】es 码流audio 数据，读数据dump
【32】es 码流audio 数据，写数据dump
dump 到的数据存放在/data/temp/pidn_dump_xx.dat 以pidn 开头，可以区分是哪个线程dump 出来的数据
```
###

