> Mongoose 官网：<http://mongoosejs.com/>。

安装 `Mongoose`：

```console
npm install mongoose
```

首先使用 Mongoose Schema 定义对象，然后用 Mongoose model 对象同步数据库：

```js
var mongoose = require('mongoose')

var Widget = new mongoose.Schema({
  sn: {type: String, require: true, trim: true, unique: true},
  name: {type: String, required: true, trim: true},
  desc: String,
  price: Number
})

var widget = mongoose.model('Widget',  Widget)
```

任何时候访问该 collection，用同样的方法调用 mongoose.model。

