**表10-1 Node.js MongoDB driver 与 MongoDB 数据类型的映射关系**

| MongoDB 类型 | JavaScript 类型 | 备注/例子 |
| :-: | :-: | :- |
| JSON 数组 | Array[1, 2, 3] | [1, 2, 3] |
| String | String | Utf8编码 |
| Boolean | Boolean | True, false |
| Integer | Number | MongoDB 支持 32-64bit 的数字，JavaScript number是64bit float。MongoDB driver 首先尝试将数值转换为 32bit，如果失败，转换为 64bit，如果依然失败，则转换为 Long 类型 |
| Interger | Long Class | Long 类型支持 64bit interger |
| Float | Number | |
| Float | Double Class | 用于表示 float 值的特殊类型 |
| Date | Date | |
| Regular expression | RegExp | |
| Null | Null | |
| Object | Object | |
| Object id | ObjectID class | 用于表示 MongoDB id 的特殊类 |
| Binary data | Binary Class、 Code Class、 DbRef Class、 Symbol class | 存储二进制数据类型；存储 JavaScript 函数和方法；存储对另一个文档的引用；描述符号（对于符号语言不仅是 JavaScript） |

`remove` 方法接受三个可选参数：

 + 文档的选择器。如果没有改参数，所有文档会被删除；
 + safe 模式标识，`safe {true | {w:n, wtimeout:n} | {fsync:true}， default: false}`；
 + 回调函数（如果 safe 模式被设置为 true 则必须要有回调函数）。

`insert` 方法也接收三个参数：文档或者带添加的文档，可选参数，回调函数。

+ safe模式：`safe {true | {w:n, wtimeout:n} | {fsync:true}), default:false}`
+ keepGoing：设置为 true 时，当插入文档报错时会继续执行后续代码。
+ serializeFunctions：文档中的序列号方法。

`insert` 方法的调用是异步的。

