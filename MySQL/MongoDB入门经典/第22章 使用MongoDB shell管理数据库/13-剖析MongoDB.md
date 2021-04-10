### 22.3.3 剖析MongoDB

> **剖析MongoDB数据库**
> 在本节中，您将对示例数据库进行剖析。这个示例演示了如何启用剖析、查看数据库操作的剖析文档以及禁用剖析。请执行下面的步骤来实现剖析。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．使用下面的命令启动MongoDB shell：
> 4．使用下面的命令切换到数据库words：
> 5．使用下面的命令对耗时超过500毫秒的操作启用剖析：
> 6．执行下面的命令，它执行一个查询操作，以便在集合profile中填充操作剖析数据：
> 7．执行下面的命令来查看集合system.profile的内容：
> 8．查看输出，其中应包含一个类似于下面的文档，该文档为查询请求{word:"test"}的剖析文档：
> 9．执行下面的命令禁用剖析：
> ▲

如果数据库响应缓慢，可对其进行剖析（profile）。通过剖析，可捕获有关数据库性能的数据；随后您可查看这些数据，找出哪些查询的性能非常糟糕。

数据库剖析是一个很有用的工具，但也会影响性能，应仅在需要排除性能故障时启用它。

MongoDB提供了不同的剖析等级，这些等级用数字表示。下面描述了这些等级。

+ 0：不剖析。
+ 1：只剖析速度较慢的操作。
+ 2：剖析所有操作。

要启用剖析，可使用数据库命令profile，并指定剖析等级以及缓慢操作的判断标准（耗时超过了多少毫秒）。

例如，下面的命令启用1级剖析，并将耗时超过500毫秒视为判断缓慢操作的标准：

```go
mongo
```

```go
db.runCommand({profile:1, slowms: 500})
```

剖析提供的信息存储在当前数据库的集合system.profile中，因此要访问剖析信息，可使用下面的方法：

```go
use words
```

```go
db.system.profile.find()
```

system.profile.find()返回的文档中包含请求的性能信息，表22.3描述了剖析文档的一些属性。

```go
db.runCommand({profile:2, slowms: 500})
```

<center class="my_markdown"><b class="my_markdown">表22.3 MongoDB数据库操作剖析文档的属性</b></center>

| 属性 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| op | 数据库操作类型，如插入、更新或查询 |
| ns | 操作针对的命名空间，格式为database.collection |
| query | 使用的查询文档 |
| ntoreturn | 使用limit()返回的文档数 |
| ntoskip | 使用skip()跳过的文档数 |
| nscanned | 为执行操作扫描的文档数 |
| lockStats | 一个文档信息，包含有关数据库锁的信息，如等了多长时间才获得锁 |
| nreturned | 操作返回的文档数 |
| responseLength | 响应的大小，单位为字节 |
| millis | 执行完操作花了多少毫秒 |
| ts | 一个ISO时间戳，指出了发出请求的时间 |
| client | 发出请求的客户端的IP地址 |
| user | 发出请求的用户——如果请求是通过经身份验证的连接发出的 |

```go
db.word_stats.find({word: "test"})
```

另外，由于剖析数据存储在一个集合中，您可使用查询来指定要返回的字段。例如，下面的代码查看这样的操作的剖析数据，即耗时超过10秒且执行时间在指定的ISO时间之后：

```go
db.system.profile.find(
{$and: [
{ts: {$gt: ISODate("2014-02-06T15:15:12.507Z")}},
{millis:{$lt:1}}]})
```

```go
db.system.profile.find()
```

▼　Try It Yourself

```go
{ "op" : "query", "ns" : "words.word_stats", "query" : { "word" : "test" },
  <<toreturn" :0, "ntoskip" : 0, "nscanned" : 1, "keyUpdates" : 0,
  <<umYield" : 0, "lockStats" :
    { "timeLockedMicros" : { "r" : NumberLong(510), "w" : NumberLong(0) },
      <<imeAcquiringMicros": { "r" : NumberLong(9), "w" : NumberLong(4) } },
  <<returned" : 1, "responseLength" :305, "millis" : 0,
  <<s" : ISODate("2014-02-06T00:09:38.530Z"), "client" : "127.0.0.1",
  <<llUsers" : [ ], "user" : "" }
```

```go
db.runCommand({profile:0, slowms: 500})
```

