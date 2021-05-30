> 更多关于 `MongoDB` 的信息包括安装帮助参考：<http://www.mongodb.org/> 。
> `Node-mongodb-native` 的 `GitHub` 页面：<https://github.com/mongodb/node-mongoodb-native> ，文档参考：<http://mongodb.github.com/node-mongodb-native> 。

要使用 `MongoDB` 需要安装客户端。安装完成客户端后，再使用下面命令安装 `MongoDB Native Node.js Driiver`：

```js
npm install mongodb
```

**MongoDB入门**

1. 引入 `mongodb` 模块

```js
var mongodb = require('mongodb')
```

2. 建立 `MongoDB` 数据库的连接：

```js
var server = new mongodb.Server('localhost', :27017, {auto_reconnect:true})
```

3. 构建数据库对象：

```js
var db = new mongodb.Db('mydb', server)
```

**定义、创建以及销毁 MongoDB Collection**

`MongoDB collection` 与关系型数据库中的 table 从根本上来说功能一致，但是与 table 并没有任何形式上的相似之处。
