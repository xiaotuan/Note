### 3.3　在MongoDB shell脚本中输出数据

在MongoDB shell脚本中输出数据时，本书使用了三个方法：

```go
print(data, ...);
printjson(object);
print(JSON.stringify(object));
```

方法print()打印传递给它的参数data，例如下述语句的输出为Hello From Mongo：

```go
print("Hello From Mongo");
```

如果传入了多个数据项，将一起打印它们。例如，下述语句的输出也是Hello From Mongo：

```go
print("Hello", "From", "Mongo");
```

方法printjson()以美观的方式打印JavaScript对象。方法print(JSON.stringify(object))也将JavaScript对象打印为紧凑的字符串。

