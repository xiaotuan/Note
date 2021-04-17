

在MySQL 5.0版本之前，MyISAM存储引擎默认的表大小只支持到 4GB，可以用以下命令来查看：

[zzx@bj34 ams]$ myisamchk -dv t1

MyISAM file: t1

Record format: Packed

Character set: gbk_chinese_ci (28)

File-version: 1

Creation time: 2007-07-10 16:50:47

Recover time: 2007-07-10 16:51:15

Status: open,changed

Data records: 224299 Deleted blocks: 0

Datafile parts: 224299 Deleted data: 0

Datafile pointer (bytes): 4 Keyfile pointer (bytes): 4

Datafile length: 63059248 Keyfile length: 9486336

Max datafile length: 4294967294 Max keyfile length: 4398046510079

Recordlength: 10284

粗体字的第一行显示了当前数据文件的大小（Datafile Length）和索引文件的大小（Keyfile Length），第二行显示了最大数据文件的大小（Max Datafile Length）和最大索引文件的大小（Max Keyfile Length）。可以看出，表的最大数据文件 size是 4294967294字节，也就是 4GB。

可以用下面的命令对数据文件的最大size进行扩充：

alter table tbl_name MAX_ROWS=1000000000 AVG_ROW_LENGTH=15000;

此命令可以修改表的最大记录数和平均记录长度，因此可以修改数据文件的最大size。对上面的测试表修改后，再次进行查看：

mysql> alter table t1 MAX_ROWS=10000000000 AVG_ROW_LENGTH=15000;

Query OK, 0 rows affected (0.01 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> exit

Bye

[zzx@bj34 test]$ myisamchk -dv t1

MyISAM file:t1

Record format:Packed

Character set: gbk_chinese_ci (28)

File-version: 1

Creation time: 2007-07-10 16:50:47

Recover time: 2007-07-10 16:51:15

Status: open,changed

Data records: 224299 Deleted blocks: 0

Datafile parts: 224299 Deleted data:0

Datafile pointer (bytes): 4 Keyfile pointer (bytes): 4

Datafile length: 63059248 Keyfile length:9486336

Max datafile length: 281474976710654 Max keyfile length: 17179868159

Recordlength:10284

果然，数据文件的最大size已经变得相当大了（281474976710654字节，约280TB）。



