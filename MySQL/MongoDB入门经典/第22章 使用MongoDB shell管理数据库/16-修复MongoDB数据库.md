### 22.4 修复MongoDB数据库

想要修复MongoDB数据库的原因有多种。例如，系统可能崩溃、应用程序可能出现数据完整性问题、您可能想收回一些未用的磁盘空间。

要修复MongoDB数据库，可在MongoDB shell中进行，也可在mongod命令行中进行。要从命令行执行修复，可使用语法--repair和--repairpath <repair_path> syntax，其中<repair_path>为临时修复文件的存储位置，如下所示：

```go
mongod --repair --repairpath /tmp/mongdb/data
```

要在MongoDB shell中执行修复，可使用命令db.repairDatabase(options)，如下所示：

```go
db.repareDatabase({ repairDatabase: 1,
   preserveClonedFilesOnFailure: <boolean>,
   backupOriginalFiles: <boolean> })
```

启动修复后，数据库中的所有集合都将被压缩，以减少占用的磁盘空间。另外，所有无效的记录都将被删除。因此，从备份恢复可能胜过运行修复。

运行修复所需的时间取决于数据量。修复会影响系统性能，应在非高峰期间运行。

警告：

> 如果副本集的其他成员有未受损的数据拷贝，就应使用该拷贝进行恢复，而不要试图去修复。repairDatabase()会将受损的数据删除，导致这些数据丢失。

