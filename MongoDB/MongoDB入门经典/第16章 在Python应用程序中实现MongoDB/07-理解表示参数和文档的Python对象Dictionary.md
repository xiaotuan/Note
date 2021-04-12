### 16.1.5　理解表示参数和文档的Python对象Dictionary

正如您在本书前面介绍MongoDB shell的章节中看到的，大多数数据库、集合和游标操作都将对象作为参数。这些对象定义了查询、排序、聚合以及其他运算符。文档也是以对象的方式从数据库返回的。

在MongoDB shell中，这些对象是JavaScript对象，但在Python中，表示文档和请求参数的对象都是Dictionary对象。服务器返回的文档是用Dictionary对象表示的，其中包含与文档字段对应的键。对于用作请求参数的对象，也是用Dictionary对象表示的。

要创建Dictionary对象，可使用标准的Python语法：

```go
myDict = {key : value, ...)
```

