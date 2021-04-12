### 2.4.1 使用命令行选项--eval执行JavaScript表达式

一种以脚本方式执行MongoDB shell命令的方法是，使用命令行选项--eval。参数--eval接受一个JavaScript字符串或JavaScript文件，启动MongoDB shell，并立即执行这些JavaScript代码。除--eval外，您还可使用其他命令行参数指定配置文件、数据库、端口、身份验证信息等。

例如，下面的命令启动MongoDB shell，连接到数据库test，对该数据库执行db.getCollections()，并以JSON字符串的方式输出结果：

```go
mongo test --eval "printjson(db.getCollectionNames())"
```

上述命令的输出类似于下面这样：

```go
C:\Users\Brad>mongo words --eval "printjson(db.getCollectionNames())"
MongoDB shell version: 2.4.8
connecting to: words
[
          "system.indexes",
          "word_stats",
          "word_stats2",
          "word_stats_new",
          "words"
]
```

