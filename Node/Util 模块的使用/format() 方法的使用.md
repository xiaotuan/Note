`uitl.format()` 方法用于创建格式化的字符串：

```js
var util = require('util');
var val = 10.5,
    str = 'a string';
var msg = util.format('The value is %d and the string is %s',val,str);
console.log(msg);
```

它提供的格式化选项有：

+ `%s`：字符串；
+ `%d`：数字（整型和浮点型）；
+ `%j`：JSON；
+ `%%`：使用百分号。