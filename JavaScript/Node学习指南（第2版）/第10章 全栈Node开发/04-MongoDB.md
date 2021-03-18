

### 10.2.1　MongoDB

Node程序中最常见的数据库就是MongoDB。MongoDB是一个基于文档的数据库。文档被编码为BSON格式——JSON的一种二进制编码，或许这也是它在JavaScript中流行的原因。MongoDB用BSON文档代替了数据表中的列，用集合代替了数据表。

MongoDB不是唯一一个文档型数据库。同样类型的数据库还有Apache的CouchDB和Amazon的SimpleDB、RavenDB，甚至还有传奇的Lotus Notes。Node对各个现代数据库的支持水平不一，但是MongoDB和CouchDB是支持得最好的。

MongoDB不是一个简单的数据库系统，而且在将它集成到你的程序中之前，你需要花一些时间来学习它的功能。然后，等你准备好了，你会发现Node中的MongoDB原生NodeJS驱动（MongoDB Native NodeJS Driver）对MongoDB的支持简直是天衣无缝，而且你可以通过使用Mongoose来支持面向对象。

我不准备详细介绍如何在Node中使用MongoDB，但是我会提供一个例子，以便你理解它的工作方式。虽然底层的数据结构与关系型数据库不同，但是概念并没有多大变化：你需要创建一个数据库，然后创建一个数据集，向其中添加数据。这样你可以更新、查询或者删除数据。在例10-1的MongoDB例子中，首先连接到一个示例数据库，访问一个叫Widgets的数据集，然后清空数据集，再插入两条数据，最后将这两条数据查询出来并打印。

**例10-1　使用MongoDB数据库**

```python
var MongoClient = require('mongodb').MongoClient;
// Connect to the db
MongoClient.connect("mongodb://localhost:27017/exampleDb",
                                        function(err, db) {
   if(err) { return console.error(err); }
   // access or create widgets collection
   db.collection('widgets', function(err, collection) {
      if (err) return console.error(err);
      // remove all widgets documents
      collection.remove(null,{safe : true}, function(err, result) {
         if (err) return console.error(err);
         console.log('result of remove ' + result.result);
         // create two records
         var widget1 = {title : 'First Great widget',
                         desc : 'greatest widget of all',
                         price : 14.99};
         var widget2 = {title : 'Second Great widget',
                         desc : 'second greatest widget of all',
                         price : 29.99};
         collection.insertOne(widget1, {w:1}, function (err, result) {
            if (err) return console.error(err);
            console.log(result.insertedId);
            collection.insertOne(widget2, {w:1}, function(err, result) {
               if (err) return console.error(err);
               console.log(result.insertedId);
               collection.find({}).toArray(function(err,docs) {
                  console.log('found documents');
                  console.dir(docs);
                  //close database
                  db.close();
               });
            });
         }); 
      });
   }); 
});
```

是的，代码中又出现了Node的回调地狱。你可以使用 `promise` 来规避它。

`MongoClient` 对象就是我们连接数据库时所使用的对象。注意给出的端口号（27017）。这是MongoDB的默认端口号。我们所使用的数据库是exampleDB，写在连接URL中。我们所使用的数据集是widgets，用它来纪念开发者所熟知的 `Widget` 类。

意料之中的是，MongoDB的函数都是异步的。数据被插入之前，我们的程序会先在不使用查询语句的情况下调用 `collection.remove()` ，来删除数据集中的所有记录。如果不这样做，数据库就会存在重复记录，因为MongoDB会对每条新数据都赋予一个系统生成的唯一标识符，而我们也没有指定 `title` 或者其他字段为唯一标识符。

然后，我们调用 `collection.insertOne()` 来创建新数据，将定义对象的JSON作为参数传入。选项 `{w:1}` 表示写入策略（write concern），是MongoDB中写操作的响应级别。

数据被插入以后，我们的程序再次使用 `collection.find()` ，同样不带查询参数，来查询所有数据。这个函数实际上会创建一个指针，然后 `toArray()` 函数会将指针指向的内容生成一个数组返回。我们后面可以用 `console.dir()` 函数将它的内容打印出来。程序执行的结果会类似于下面的内容：

```python
result of remove 1
56c5f535c51f1b8d712b6552
56c5f535c51f1b8d712b6553
found documents
[ { _id: ObjectID { _bsontype: 'ObjectID', id: 'VÅõ5Å\u001f\u001bq+eR' },
   title: 'First Great widget',
   desc: 'greatest widget of all',
   price: 14.99 },
  { _id: ObjectID { _bsontype: 'ObjectID', id: 'VÅõ5Å\u001f\u001bq+eS' },
   title: 'Second Great widget',
   desc: 'second greatest widget of all',
   price: 29.99 } ]
```

每个对象的标识符其实也是一个对象，而且是BSON格式的，所以打印出来的都是乱码。如果想要去掉乱码，你可以分别打印对象中的每个字段，然后使用 `toHexString()` 对BSON格式的内容进行转码：

```python
docs.forEach(function(doc) {
                    console.log('ID : ' + doc._id.toHexString());
                    console.log('desc : ' + doc.desc);
                    console.log('title : ' + doc.title);
                    console.log('price : ' + doc.price);
                 });
```

最后的结果就成了：

```python
result of remove 1
56c5fa40d36a4e7b72bfbef2
56c5fa40d36a4e7b72bfbef3
found documents
ID : 56c5fa40d36a4e7b72bfbef2
desc : greatest widget of all
title : First Great widget
price : 14.99
ID : 56c5fa40d36a4e7b72bfbef3
desc : second greatest widget of all
title : Second Great widget
price : 29.99
```

你可以使用命令行工具来查看MongoDB数据库中的数据。按照下面的顺序调用命令就可以启动工具并查看数据。

（1）输入 **mongo** 启动命令行工具。

（2）输入 **use exampleDb** 切换到exampleDb数据库。

（3）输入 **show collections** 查看所有的数据集。

（4）输入 **db.widgets.find()** 来查看Widget中的所有数据。

如果你想要用一个基于对象的方式来集成MongoDB，那么Mongoose就是你要找的东西。如果要集成到Express，Mongoose也许是一个更好的选择。

不用MongoDB的时候，记得将它关闭。

> <img class="my_markdown" src="../images/102.png" style="zoom:50%;" />
> **Node文档中的MongoDB相关内容**
> Node的MongoDB驱动有在线的文档可以查看，你可以通过GitHub代码库来访问这个文档，也可以在MongoDB的网站上看到这个文档。我更推荐新手使用MongoDB网站上的文档。

