### 22.3.5 使用诊断命令top

> **分析MongoDB数据库的使用情况**
> 在本节中，您将在MongoDB shell中执行top命令，以查看数据库的使用统计信息。这个示例演示了如何在MongoDB服务器上运行top命令并查看结果。
> 请执行如下步骤，在MongoDB服务器上运行top命令。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．使用下面的命令启动MongoDB shell：
> 4．使用下面的命令切换到数据库admin：
> 5．执行下面的语句，对MongoDB服务器中的所有数据库运行top命令：
> 6．查看针对每个数据库中集合的输出，输出应类似于下面这样：
> ▲

为性能糟糕的数据库排除故障时，一个很有用的MongoDB命令是top。它返回每个数据库的使用统计信息，包含每种操作的执行次数以及花费的时间（单位为毫秒）。这有助于您确定哪些数据库使用的CPU时间最多以及哪些数据库最繁忙（这两类数据库通常不同）。

要执行top命令，可在数据库admin中执行如下命令：

```go
use admin
db.runCommand({top: 1})
```

输出中包含在所有数据库的每个集合中以下操作类型的执行次数以及消耗的时间：

+ total
+ readLock
+ writeLock
+ queries
+ getmore
+ insert
+ update
+ remove
+ commands

▼　Try It Yourself

```go
mongo
```

```go
use admin
```

```go
db.runCommand({top: 1})
```

```go
"words.word_stats" : {
   "total" : {
      "time" : 107502,
      "count" : 32
   },
   "readLock" : {
      "time" : 77193,
      "count" : 24
   },
   "writeLock" : {
      "time" : 30309,
      "count" : 8
   },
   "queries" : {
      "time" : 43574,
      "count" : 24
   },
   "getmore" : {
      "time" : 6455,
      "count" : 2
   },
   "insert" : {
      "time" : 28968,
      "count" : 1
   },
   "update" : {
      "time" : 0,
      "count" : 0
   },
   "remove" : {
      "time" : 147,
      "count" : 1
   },
   "commands" : {
      "time" : 28358,
      "count" : 4
   }
},
```

