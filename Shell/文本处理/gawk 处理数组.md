[toc]

`gawk` 编程语言使用**关联数组**提供数组功能。

### 1. 定义数组变量

可用用标准赋值语句来定义数组变量。数组变量赋值的格式如下：

```shell
var[index] = element
```

其中 var 是变量名，index 是关联数组的索引值，element 是数据元素值。

```shell
capital["Illinois"] = "Springfield"
capital["Indiana"] = "Indianapolis"
capital["Ohio"] = "Columbus"
```

在引用数组变量时，必须包含索引值来提取相应的数据元素值。

```shell
$ gawk 'BEGIN { capital["Illinois"] = "Springfield" ; print capital["Illinois"] }'
Springfield
```

在引用数组变量时，会得到数据元素的值。数据元素值时数字值时也一样。

```shell
$ gawk 'BEGIN { var[1] = 34 ; var[2] = 3 ; total = var[1] + var[2] ; print total }'
37
```

### 2. 遍历数组变量

如果要在 `gawk` 中遍历一个关联数组，可以用 `for` 语句的一种特殊形式：

```shell
for (var in array)
{
	statements
}
```

这个 `for` 语句会在每次循环时将关联数组 array 的下一个索引值赋给变量 var，然后执行一遍 statements。重要的是记住这个变量中存储的是索引值而不是数组元素值。

```shell
$ gawk 'BEGIN {
> var["a"] = 1
> var["g"] = 2
> var["m"] = 3
> var["u"] = 4
> for (test in var)
> {                      
> print "Index: ", test," - value:", var[test]
> }
> }'
Index:  u  - value: 4
Index:  m  - value: 3
Index:  a  - value: 1
Index:  g  - value: 2
```

### 3. 删除数组变量

从关联数组中删除数组索引要用一个特殊的命令。

```shell
delete array[index]
```

删除命令会从数组中删除关联索引值和相关的数据元素值。

```shell
$ gawk 'BEGIN {
> var["a"] = 1
> var["g"] = 2
> for (test in var)
> {
> print "Index:", test, " - Value:", var[test]
> }
> delete var["g"]
> print "---"
> for (test in var)
>    print "Index:", test, " - Value:", var[test]
> }'
Index: a  - Value: 1
Index: g  - Value: 2
---
Index: a  - Value: 1
```

