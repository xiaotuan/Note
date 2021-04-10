### 23.2.4　部署MongoDB分片集群

> **创建MongoDB分片集群**
> 在本节中，您将在自己的开发系统上实现一个MongoDB分片集群。开发型分片集群的实现与生产型分片集群类似，主要差别在于，所有MongoDB服务器都运行在同一台机器上，且数据库的规模被设置得较小。
> 请执行如下步骤来实现一个MongoDB分片集群，它包含一个配置服务器、一个mongos服务器（查询路由器）和两个分片服务器。
> 1．确保关闭了前面使用的所有MongoDB服务器。
> 2．在文件夹code中创建如下文件夹，这些文件夹用于存储集群中配置服务器和分片服务器的数据文件：
> 3．在文件夹code/hour23中创建文件configdb.conf（这是配置服务器的配置），并添加程序清单23.6所示的内容。设置smallfiles和oplogSize将数据库限制为很小的规模，这适用于开发目的。端口27019是配置服务器的默认端口。您需要将<code>替换为相应的路径。
> **程序清单23.6　configdb.conf：分片集群中配置服务器的配置**
> 4．在文件夹code/hour23中创建文件shard1.conf（这是第一个分片服务器的配置），并添加程序清单23.7所示的内容。
> **程序清单23.7　shard1.conf：第一个分片服务器的配置**
> 5．在文件夹code/hour23中创建文件shard2.conf（这是第二个分片服务器的配置），并添加程序清单23.8所示的内容。
> **程序清单23.8　shard2.conf：第二个分片服务器的配置**
> 6．打开4个控制台窗口并执行如下命令（每个窗口中一个）；这将首先启动配置服务器，再启动查询路由器（mongos服务器），最后启动分片服务器（您需要将<code>替换为相应的路径）。
> 7．再打开一个控制台窗口，并使用下面的命令启动MongoDB shell并连接到运行在默认端口上的mongos服务器。
> 8．使用下面的命令将MongoDB分片服务器加入到集群中。
> 9．在依然连接到mongos服务器的MongoDB shell中，执行下面的命令对数据库words启用分片。
> 10．执行下面的命令对集合word_stats启用分片，并将字段first的散列值用作片键。
> 11．再打开一个控制台窗口，切换到目录code/hour05，并执行下面的命令在分片集群中生成数据库words。代码执行的时间很长，大约1分钟才完成，这是因为需要生成基于字段first的散列索引，还需要在配置服务器、mongos服务器和分片服务器之间通信。
> 12．在连接到mongos服务器的MongoDB shell中执行下面的命令，以核实创建了数据库words并在其中填充了单词。
> 13．执行下面的命令显示分片集群的状态，以核实所有服务器都报告了状态且根据first字段创建了散列片键索引。输出应类似于程序清单23.9。
> **程序清单23.9　MongoDB分片集群的状态**
> 14．在前面打开的MongoDB shell中，执行下面的命令连接到每个服务器并关闭它们——首先是分片服务器，最后是配置服务器：
> 您创建了一个MongoDB分片集群。
> ▲

要部署MongoDB分片集群，需要执行多个步骤来建立不同类型的服务器并配置数据库和集合。部署MongoDB集群的步骤如下。

1．创建配置服务器。

2．启动查询路由器。

3．在集群中添加分片服务器。

4．对数据库启用分片。

5．对集合启用分片。

```go
code/hour23/data/configdb
code/hour23/data/shard1
code/hour23/data/shard2
```

接下来的几小节更详细地介绍这些步骤。

警告：

```go
code/hour23/configdb.conf
```

> 分片集群的每个成员都必须能够连接到其他所有成员，包括所有的分片服务器和配置服务器。请确保网络和安全系统（包括所有的接口和防火墙）都允许进行这些连接。

#### 创建配置服务器

```go
port = 27019
dbpath=<code>\hour23\data\configdb
smallfiles = true
oplogSize = 128
```

配置服务器的进程是mongod实例，存储的是集群的元数据而不是集合。每个配置服务器都存储着集群元数据的完整拷贝。在生产环境中，必须部署三个配置服务器实例，且每个都运行在不同的服务器上，以确保高可用性和数据完整性。

要实现配置服务器，请在每台服务器上执行如下步骤。

```go
code/hour23/shard1.conf
```

1．创建用于存储配置数据库的数据目录。

2．启动配置服务器实例，传入第1步创创建的数据目录的路径，并使用选项--configsvr option指出这是配置服务器，如下所示：

```go
port = 27021
dbpath=<code>\hour23\data\shard1
smallfiles = true
oplogSize = 128
```

```go
mongod --configsvr --dbpath <path> --port <port>
```

3．mongod实例启动后，配置服务器就准备就绪了。

```go
code/hour23/shard2.conf
```

提示：

> 配置服务器的默认端口为27019。

```go
port = 27022
dbpath=<code>\hour23\data\shard2
smallfiles = true
oplogSize = 128
```

#### 启动查询路由器（mongos）

查询路由器（mongos）不需要数据库目录，因为配置存储在配置服务器上，而数据存储在分片服务器上。查询路由器是轻量级的，完全可以将其与应用程序服务器放在同一个系统上。

```go
mongod --configsvr --config <code>/hour23/configdb.conf
mongos --configdb localhost:27019 --port 27017
mongod --config <code>/hour23/shard1.conf
mongod --config <code>/hour23/shard2.conf
```

可创建多个查询路由器来将请求路由到分片集群，但为确保高可用性，不能将它们放在同一个系统上。

要启动查询路由器，可执行命令mongos并传入参数--configdb以及分片集群中各个配置服务器的DNS/主机名，如下所示：

```go
mongo
```

```go
mongos --configdb c1.test.net:27019,c2.test.net:27019,c3.test.net:27019
```

默认情况下，mongos示例运行在端口27017上，但可使用命令行选项--port <port>指定其他端口。

```go
sh.addShard("localhost:27021")
sh.addShard("localhost:27022")
```

提示：

> 为避免中断服务，给配置服务器指定逻辑DNS 名（与物理或虚拟主机名无关）。如果没有逻辑DNS名，要移动或重命名配置服务器，必须关闭分片集群中的所有mongod和mongos实例。

```go
sh.enableSharding("words")
```

#### 在集群中添加分片

集群中的分片是标准的MongoDB服务器，它们可以是独立的服务器，也可以是副本集。要将MongoDB服务器作为分片加入到集群中，只需从MongoDB shell访问mongos服务器，并执行命令sh.addShard()。

```go
sh.shardCollection( "words.word_stats", { first: "hashed" } )
```

命令sh.addShard()的语法如下：

```go
sh.addSharrd(<replica_set_or_server_address>)
```

```go
mongo generate_words.js
```

例如，要将服务器mgo1.test.net上的副本集rs1添加到集群中，可在连接到mongos服务器的MongoDB shell中执行下面的命令：

```go
sh.addShard( "rs1/mgo1.test.net:27017" )
```

```go
use words
db.words.find().count()
```

要将服务器mgo1.test.net作为分片加入到集群中，可在连接到mongos服务器的MongoDB shell中执行下面的命令：

```go
sh.addShard( "mgo1.test.net:27017" )
```

```go
sh.status()
```

将所有分片都加入集群后，集群将开始通信并对数据进行分片。对于预定义的数据，需要花点时间才能将块分配好。

#### 对数据库启用分片

```go
--- Sharding Status ---
sharding version: {
  "_id" : 1,
  "version" : 3,
  "minCompatibleVersion" : 3,
  "currentVersion" : 4,
  "clusterId" : ObjectId("52f266705b29f951d4defa85")
}
shards:
  { "_id" : "shard0000", "host" : "localhost:27021" }
  { "_id" : "shard0001", "host" : "localhost:27022" }
databases:
  { "_id" : "admin", "partitioned" : false, "primary" : "config" }
  { "_id" : "test", "partitioned" : false, "primary" : "shard0000" }
  { "_id" : "words", "partitioned" : true, "primary" : "shard0000" }
    words.word_stats
      shard key: { "first" : "hashed" }
      chunks:
              shard0000  2
              shard0001  2
      { "first" : { "$minKey" : 1 } } -->> { "first" :
  NumberLong("-4611686018427387902")}
          on : shard0000 Timestamp(2, 2)
      { "first" : NumberLong("-4611686018427387902") } -->> { "first" :
  NumberLong(0) }
          on : shard0000 Timestamp(2, 3)
        { "first" : NumberLong(0) } -->> { "first" :
  NumberLong("4611686018427387902") }
          on : shard0001 Timestamp(2, 4)
        { "first" : NumberLong("4611686018427387902") } -->> { "first" : {
  "$maxKey" : 1 } }
            on : shard0001 Timestamp(2, 5)
```

要对集合进行分片，需要对其所属的数据库启用分片。启用分片并不会自动重新分配数据，而只是给数据库指定主分片并调整其他配置，使得能够对集合进行分片。

要对数据库启用分片，需要使用MongoDB shell连接到一个mongos实例，再执行命令sh.enableSharding(database)。例如，要对数据库bigWords启用分片，可这样做：

```go
db = connect("localhost:27022/admin")
db.shutdownServer()
db = connect("localhost:27021/admin")
db.shutdownServer()
db = connect("localhost:27017/admin ")
db.shutdownServer()
db = connect("localhost:27019/admin ")
db.shutdownServer()
```

```go
sh.enableSharding("bigWords");
```

#### 对集合启用分片

对数据库启用分片后，便可以在集合级启用分片了。您无需对数据库中的所有集合启用分片，而只对合适的集合这样做。

要对集合启用分片，可采取如下步骤。

1．按本章前面介绍的方式选择要用作片键的字段。

2．使用ensureIndex()创建基于片键的索引。

```go
db.myDB.myCollection.ensureIndex( { _id : "hashed" } )
```

3．使用sh.shardCollection(<database>.<collection>, shard_key)对集合启用分片，其中shard_key与创建索引时指定的参数相同，如下所示：

```go
sh.shardCollection("myDB.myCollection", { "_id": "hashed" } )
```

#### 指定分片标记和片键范围

对集合启用分片后，您可能想添加标记（tag），将片键范围关联到分片。为说明这一点，一个很好的例子是按邮政编码分片的集合。为改善性能，可添加用城市代码（如NYC和SFO）表示的标记，并给标记指定相应城市的邮政编码范围。这样，邮政编码为这些城市的文档将存储到集群的同一个分片中；对于基于同一个城市的多个邮政编码的查询，这将改善其性能。

要指定分片标记，可在连接到mongos实例的MongoDB shell中执行命令sh.addShardTag (shard_server, tag_name)，如下所示：

```go
sh.addShardTag("shard0001", "NYC")
sh.addShardTag("shard0002", "SFO")
```

然后，给标记指定片键范围（这里是给每个城市的标记指定邮政编码范围），为此可在连接到mongos实例的MongoDB shell中执行命令sh.addTagRange(collection_path, startValue, endValue, tag_name)，如下所示：

```go
sh.addTagRange("records.users", { zipcode: "10001" }, { zipcode: "10281" }, "NYC")
sh.addTagRange("records.users", { zipcode: "11201" }, { zipcode: "11240" }, "NYC")
sh.addTagRange("records.users", { zipcode: "94102" }, { zipcode: "94135" }, "SFO")
```

注意到给NYC指定了多个范围。这让您能够将多个片键范围对应的文档分配给同一个分片。

如果以后要删除分片标记，可使用sh.removeShardTag(shard_server, tag_name)，如下所示：

```go
sh.removeShardTag("shard0002", "SFO")
```

▼　Try It Yourself

