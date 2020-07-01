> 提示： `Mongoose` 官网：<http://mongoosejs.com/>。

安装 `Mongoose`：

```console
npm install mongoose
```

定义 Mongoose model 对象：

```js
var mongoose = require('mongoose')

var Widget = new mongoose.Schema({
  sn: {type: String, require: true, trim: true, unique: true},
  name: {type: String, required: true, trim: true},
  desc: String,
  price: Number
})

var widget = mongoose.model('Widget', Widget)
```