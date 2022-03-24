`MongoDB collection` 与关系型数据库中的 table 从根本上来说功能一致，但是与 table 并没有任何形式上的相似之处。

**创建 colletion**

```js
db.collection('mycollection', function (err, collection) {})	// 并没有马上创建实际的 collection，而是在添加第一行数据后再创建
db.createCollection('mycollection', function (err, collection) {})	// 马上创建 collection
```

以上两个方法都可以接收第二个参数作为可选项，`{safe: true}` 该参数用于在 `db.collectio` 中 collection 不存在或者 `db.createCollection` 中 collection 存在的情况下告知 driver 错误信息：

```js
db.collection('mycollection', {safe:true}, function (err, collection) {})
db.createCollection('mycollection', {safe: true}, function (err, collection) {})
```

如果对一个已存在的 collection 使用 `db.createCollection` 方法，你直接访问该 collection —— driver 并不会覆盖这一部分。

如果希望彻底销毁一个 collection，可以使用 `db.dropCollection`：

```js
db.dropCollection('mycollection', function(err, result) {})
```