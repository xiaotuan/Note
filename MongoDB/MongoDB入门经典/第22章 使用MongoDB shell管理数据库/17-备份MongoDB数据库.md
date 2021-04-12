### 22.5 备份MongoDB数据库

对MongoDB而言，最佳的备份策略是使用副本集实现高可用性，这可确保数据是最新的且始终可用。然而，如果数据至关重要，无法承受其受损带来的损失，应考虑如下情况。

+ 如果数据中心出现故障，该怎么办？对于这种情况，可定期备份数据并离线存储，或者添加离线的副本集。
+ 如果应用程序数据受损并被复制，该怎么办？这始终是个令人担心的问题。对于这种情况，除了备份别无他法。

确定需要定期备份数据后，应考虑备份对系统的影响并制定相应的策略。

+ **对生产环境的影响：** 备份通常是资源密集型的，必须尽可能降低其对生产环境的影响。
+ **需求：** 如果打算采取类似于块级快照的方式备份数据库，需要确保系统基础设施支持这种方式。
+ **分片：** 如果对数据进行了分片，所有分片都必须一致——不能备份一个分片，而不备份其他分片。另外，为生成实时备份，必须停止将数据写入集群。
+ **相关数据：** 为降低备份对系统的影响，也可只备份对系统来说生死攸关的数据。例如，对于永远不会变的数据库，只需备份一次。如果数据库很容易重新生成但非常大，那么相比于频繁备份，可能值得付出重新生成的代价。

备份MongoDB数据库的主要方法有两种。一是使用命令mongodump进行二进制转储。您可将离线存储这些二进制数据，供以后使用。例如，要将主机mg1.test.net上的副本集和独立系统mg2.test.net的数据库，转储到文件夹/opt/backup/current，可使用下面的命令：

```go
mongodump --host rset1/mg1.test.net:27018,mg2.test.net –out/ opt/backup/current
```

要恢复使用mongodump转储的数据库，可使用命令mongorestore。要使用mongorestore，最简单的方式是，在关闭了MongoDB服务器的情况下使用如下语法：

```go
mongorestore --dbpath <database path> <path to the backup>
```

例如：

```go
mongorestore --dbpath /opt/data/db /opt/backup/current
```

也可在运行着MongoDB服务器的情况下使用下面的语法来恢复：

```go
mongorestore --port <database port> <path to the backup>
```

备份MongoDB数据库的第二种方法是使用文件系统快照。快照很容易拍摄，但也大得多，要求启用日记，并要求系统支持块级备份。如果您想实现快照备份方法，请参阅下述网址的指南：<a class="my_markdown" href="['http://docs.mongodb.org/manual/tutorial/back-up-databases-with-filesystem-snapshots/']">http://docs.mongodb.org/manual/tutorial/back-up-databases-with-filesystem-snapshots/</a>。

