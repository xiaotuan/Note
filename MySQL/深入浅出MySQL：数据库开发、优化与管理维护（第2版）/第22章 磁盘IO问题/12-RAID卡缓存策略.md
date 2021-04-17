

可以通过MegaCli64 -LDInfo -Lall -aALL命令来查看当前RAID卡设置的缓存策略：

shell> MegaCli64 -LDInfo -Lall -aALL

…

Adapter 0 -- Virtual Drive Information:

Virtual Drive: 0 (Target Id: 0)

Name :

RAID Level : Primary-1, Secondary-0, RAID Level Qualifier-0

Size: 1.089 TB

Mirror Data : 1.089 TB

State : Optimal

Strip Size : 64 KB

Number Of Drives per span:2

Span Depth: 2

Default Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU

Current Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU

Default Access Policy: Read/Write

Current Access Policy: Read/Write

Disk Cache Policy : Disk's Default

Encryption Type : None

…

Default Cache Policy：默认的缓存策略；

Current Cache Policy：当前生效的缓存策略。

下面对缓存策略进行详细的说明。

**1．缓存策略第一段**

写缓存策略，包括WriteBack和WriteThrough。

WriteBack：进行写入操作的时候，将数据写入RAID卡缓存后直接返回，RAID卡控制器将在系统负载低或者RAID缓存满的情况下把数据写入磁盘，减少了磁盘操作的频次，大大提升了RAID卡写入性能，在大多数情况下能够有效降低系统I/O负载。写入RAID卡缓存的数据的可靠性由RAID卡的BBU（Battery Backup Unit）保证。

WriteThrough：进行写入操作的时候，不使用RAID卡缓存，数据直接写入磁盘才返回。也就是RAID卡写缓存被穿透，每次写入都直接写入磁盘。大多数情况下，WriteThrough的策略设置会造成系统I/O负载上升。和WriteBack策略相比，WriteThrough策略则不需要BBU电池来保证数据的完整性，但写性能会大幅下降。

**2．缓存策略第二段**

是否开启预读，包括ReadAheadNone、ReadAhead和ReadAdaptive。

ReadAheadNone：不开启预读。

ReadAhead：开启预读，在读操作的时候，预先把后面顺序的数据加载入缓存，在顺序读取的时候，能提供性能，但是在随机读的时候，开启预读做了不必要的操作，会降低随机读的性能。

ReadAdaptive：自适应预读，在缓存和I/O空闲的时候，选择顺序预读，需要消耗一些计算能力，是默认的策略。

**3．缓存策略第三段**

读操作是否缓存到RAID卡缓存中，包括Direct和Cached。

Direct：读操作不缓存到RAID卡缓存中。

Cached：读操作缓存到RAID卡缓存中。

**4．缓存策略第四段**

如果BBU出问题，是否启用Write Cache，包括Write Cache OK if Bad BBU和No Write Cache if Bad BBU。

No Write Cache if Bad BBU：如果BBU出问题，则不再使用Write Cache，从WriteBack策略自动切换到WriteThrough模式。这是默认配置，确保在没有BBU电池支持的情况，直接写入磁盘而不是RAID卡缓存，以确保数据安全。

Write Cache OK if Bad BBU：如果BBU出问题，仍然启用Write Cache，不推荐的配置，如果BBU出问题，无法保证意外断电后数据能够完整写回磁盘。除非有UPS后备电源或者其他类似方案做电源方面额外的保证。

RAID卡缓存策略可以通过**MegaCli64 -LDSetProp**命令进行修改，常用的策略主要有下面 4种：WriteBack、WriteThrough、Write Cache OK if Bad BBU、No Write Cache if Bad BBU。

shell> MegaCli64 -LDSetProp -WB -Lall -aALL

shell> MegaCli64 -LDSetProp -WT -Lall -aALL

shell> MegaCli64 -LDSetProp -CachedBadBBU -Lall -aALL

shell> MegaCli64 -LDSetProp -NoCachedBadBBU -Lall –aALL

在RAID卡电池校准期间（RAID卡电池电量在降低到特定阀值之后）或者电池故障期间，默认的RAID卡写缓存策略会自动发生变动，从WriteBack变为WriteThrough，造成系统写入性能下降，此时如果正好是业务高峰时间，会引起系统负载大幅度上升、响应时间变长。

此时可以通过临时修改RAID卡缓存策略为Write Cache OK if Bad BBU来解决，修改后立即生效，无需重启系统等额外的配置：

shell> MegaCli64 -LDSetProp CachedBadBBU -Lall -aALL

Set Write Cache OK if bad BBU on Adapter 0, VD 0 (target id: 0) success

Exit Code: 0x00

# MegaCli64 -LDInfo -Lall -aALL

…

Default Cache Policy: WriteBack, ReadAdaptive, Direct, Write Cache OK if Bad BBU

Current Cache Policy: WriteBack, ReadAdaptive, Direct, Write Cache OK if Bad BBU

…

Current Access Policy: Read/Write

注意，临时修改 RAID 卡缓存策略度过业务高峰期之后，仍然应该及时恢复缓存策略为No Write Cache if Bad BBU，避免断电可能导致的数据损失：

shell> MegaCli64 -LDSetProp NoCachedBadBBU -Lall -aALL

Set No Write Cache if bad BBU on Adapter 0, VD 0 (target id: 0) success

Exit Code: 0x00

shell> MegaCli64 -LDInfo -Lall -aALL

…

Default Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU

Current Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU

…

对于RAID卡缓存策略的自动变动带来的I/O性能波动，一般解决方案有两种。



