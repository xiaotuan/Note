

**1．解决方案一**

根据RAID卡电池（BBU电池）下次充放电的时间，定期在业务量较低的时候，提前进行充放电，避免在业务高峰时发生RAID卡写入策略从Write Back到Write Through的更改。在手工触发电池充放电之后，下一次充放电的时间会往后顺延。例如，DELL服务器电池Relearn周期一般为90天，在手工触发DELL服务器BBU电池校准之后，下一次电池Relearn的时间会往后顺延90天；而IBM服务器电池Relearn的周期一般为30天，手工触发IBM服务器BBU电池校准之后，下一次电池Relearn的时间就会往后顺延30天。具体时间周期可以在系统中查看到。

可以从BBU电池的日志中获取到下次电池Relearn时间：

shell> MegaCli64 -fwtermlog -dsply -a0 -nolog

…

11/02/12 21:18:33: Next Learn will start on 01 31 2013

11/02/12 21:18:33: *** BATTERY FEATURE PROPERTIES ***

11/02/12 21:18:33: _________________________________________________

11/02/12 21:18:33: Auto Learn Period : 90 days

11/02/12 21:18:33: Next Learn Time : 412982313

11/02/12 21:18:33: Delayed Learn Interval: 0 hours from scheduled time

11/02/12 21:18:33: Next Learn scheduled on: 01 31 2013 21:18:33

11/02/12 21:18:33: _________________________________________________

…

或者通过命令直接得到下一次电池Relearn的时间：

shell> MegaCli -AdpBbuCmd -GetBbuProperties -aall

…

BBU Properties for Adapter: 0

Auto Learn Period: 90 Days

Next Learn time: Thu Jan 31 21:18:33 2013

Learn Delay Interval:0 Hours

Auto-Learn Mode: Transparent

Exit Code: 0x00

手工触发电池Relearn（电池校准）的操作：

shell> MegaCli64 -AdpBbuCmd -BbuLearn –aALL

**2．解决方案二**

设置Forced WriteBack写策略，也就是说即使在电池电量低于警戒值甚至电池放电完毕的情况下，强制使用WriteBack写缓存策略，避免写入性能波动，此时一定要有UPS之类的后备电源，否则当电池放电完毕时服务器恰好断电，就会导致写入RAID卡缓存中的数据丢失。



