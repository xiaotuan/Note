### 9.2.1　理解方法aggregate()

Collection对象提供了对数据执行聚合操作的方法aggregate()，这个方法的语法如下：

```go
aggregate(operator, [operator], [...])
```

参数operator是一系列聚合运算符（如表9.1所示），让您能够指定要在流水线的各个阶段对数据执行哪种聚合操作。执行第一个运算符后，结果将传递给下一个运算符，后者对数据进行处理并将结果传递给下一个运算符，这个过程不断重复，直到到达流水线末尾。

在MongoDB 2.4和更早的版本中，方法aggregate()返回一个对象，该对象有一个名为result的属性，是一个包含聚合结果的迭代器。这意味着使用2.4版的MongoDB shell时，需要使用类似于下面的代码来访问聚合结果：

```go
results = myCollection.aggregate( ...);
results.result.forEach( function(item){
...
});
```

在更高的MongoDB版本中，方法aggregate()直接返回一个包含聚合结果的迭代器。这意味着使用2.6和更高版本的MongoDB shell时，需要使用类似于下面的代码来访问聚合结果：

```go
results = myCollection.aggregate( ...);
results.forEach( function(item){
...
});
```

程序清单9.3所示的示例针对的是MongoDB 2.4。

