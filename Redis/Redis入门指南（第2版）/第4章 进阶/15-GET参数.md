### 4.3.4　 `GET` 参数

现在小白的博客已经可以按照文章的发布顺序获得一个标签下的文章 ID 列表了，接下来要做的事就是对每个ID都使用 `HGET` 命令获取文章的标题以显示在博客列表页中。有没有觉得很麻烦？不论你的答案如何，都有一种更简单的方式来完成这个操作，那就是借助 `SORT` 命令的 `GET` 参数。

`GET` 参数不影响排序，它的作用是使 `SORT` 命令的返回结果不再是元素自身的值，而是 `GET` 参数中指定的键值。 `GET` 参数的规则和 `BY` 参数一样， `GET` 参数也支持字符串类型和散列类型的键，并使用“ `*` ”作为占位符。要实现在排序后直接返回ID对应的文章标题，可以这样写：

```shell
redis> SORT tag:ruby:posts BY post:*->time DESC GET post:*->title 1) "Windows 8 app designs"
2) "RethinkDB - An open-source distributed database built with love"
3) "Uses for cURL"
4) "The Nature of Ruby"

```

在一个 `SORT` 命令中可以有多个 `GET` 参数（而 `BY` 参数只能有一个），所以还可以这样用：

```shell
redis> SORT tag:ruby:posts BY post:*->time DESC GET post:*->title GET post:*->time 1) "Windows 8 app designs"
2) "1352620100"
3) "RethinkDB - An open-source distributed database built with love"
4) "1352620000"
5) "Uses for cURL"
6) "1352619600"
7) "The Nature of Ruby"
8) "1352619200"

```

可见有*N*个 `GET` 参数，每个元素返回的结果就有*N*行。这时有个问题：如果还需要返回文章ID该怎么办？答案是使用 `GET #` 。就像这样：

```shell
redis> SORT tag:ruby:posts BY post:*->time DESC GET post:*->title GET post:*->time GET #  1) "Windows 8 app designs"
 2) "1352620100"
 3) "12"
 4) "RethinkDB - An open-source distributed database built with love"
 5) "1352620000"
 6) "26"
 7) "Uses for cURL"
 8) "1352619600"
 9) "6"
10) "The Nature of Ruby"
11) "1352619200"
12) "2"

```

也就是说， `GET #` 会返回元素本身的值。

