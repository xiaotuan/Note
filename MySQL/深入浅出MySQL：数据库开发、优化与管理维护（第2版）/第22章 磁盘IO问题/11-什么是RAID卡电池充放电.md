

RAID卡都有写缓存（Battery Backed Write Cache），写缓存对 I/O性能的提升非常明显，为了避免掉电丢失写缓存中的数据，所以RAID卡都有电池（Battery Backup Unit，简称BBU）来提供掉电后将写缓存中的数据写入磁盘。

为了记录RAID卡电池的放电曲线，便于RAID卡控制器了解电池的状态，同时为了延长电池的使用寿命，默认会定期启动自动校准模式（AutoLearn Mode），在Learn Cycle期间，RAID卡控制器不会启用BBU直到完成校准。通俗的说，RAID卡电池会定期充放电，定期充放电的操作叫做电池Relearn或者电池校准。

查看RAID卡BBU的状态：

shell> MegaCli64 -AdpBbuCmd -GetBbuStatus -aALL

BBU status for Adapter: 0

BatteryType: BBU

Voltage: 3945 mV

Current: 0 mA

Temperature: 47 C

Battery State: Optimal

BBU Firmware Status:

Charging Status : None

Voltage : OK

Temperature : OK

Learn Cycle Requested : No

Learn Cycle Active : No

Learn Cycle Status : OK

Learn Cycle Timeout : No

I2c Errors Detected : No

Battery Pack Missing : No

Battery Replacement required : No

Remaining Capacity Low : No

Periodic Learn Required : No

Transparent Learn : No

No space to cache offload : No

Pack is about to fail & should be replaced : No

Cache Offload premium feature required : No

Module microcode update required : No

BBU GasGauge Status: 0x0228

Relative State of Charge: 100 %

Charger Status: Complete

Remaining Capacity: 442 mAh

Full Charge Capacity: 446 mAh

isSOHGood: Yes

Exit Code: 0x00

Charging Status：None、Charging、Discharging分别代表BBU处于不充放电状态、充电状态、放电状态。

Learn Cycle Requested：Yes代表当前有Learn Cycle请求，正在处于校准中。

Learn Cycle Active：Yes代表处于Learn Cycle校准阶段，控制器开始校准。

Battery Replacement Required：Yes代表电池需要更换。

Remaining Capacity Low：Yes代表电池容量过低，需要更换电池。

电池校准一般会经历3个阶段：首先RAID卡控制器会将BBU充满到最大程度，然后开始放电，放电完毕后重新将BBU充满到最大程度，一次BBU校准完成。整个过程一般为3个小时或者更多，期间RAID卡会自动禁用WriteBack策略，以保证数据完整性，而系统I/O性能会出现较大的波动。

默认DELL服务器90天执行一次校准，而IBM服务器是30天。DELL和IBM都不推荐关闭BBU电池的Auto Learn模式，不做校准的RAID卡电池寿命会从正常的 2年降低到正常寿命的1/3，也就是8个月。



