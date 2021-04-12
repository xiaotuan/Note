### 4.3.2　 `SORT` 命令

除了使用有序集合外，我们还可以借助Redis提供的 `SORT` 命令来解决小白的问题。 `SORT` 命令可以对列表类型、集合类型和有序集合类型键进行排序，并且可以完成与关系数据库中的连接查询相类似的任务。

小白的博客中标有“ruby”标签的文章的ID分别是“2”、“6”、“12”和“26”。由于在集合类型中所有元素是无序的，所以使用 `SMEMBERS` 命令并不能获得有序的结果3。为了能够让博客的标签页面下的文章也能按照发布的时间顺序排列（如果不考虑发布后再修改文章发布时间，就是按照文章ID的顺序排列），可以借助 `SORT` 命令实现，方法如下所示：

3集合类型经常被用于存储对象的ID，很多情况下都是整数。所以Redis对这种情况进行了特殊的优化，元素的排列是有序的。4.6节会详细介绍具体的原理。

```shell
redis> SORT tag:ruby:posts 1) "2"
2) "6"
3) "12"
4) "26"

```

是不是十分简单？除了集合类型， `SORT`  命令还可以对列表类型和有序集合类型进行排序：

```shell
redis> LPUSH mylist 4 2 6 1 3 7 (integer) 6
redis> SORT mylist 1) "1"
2) "2"
3) "3"
4) "4"
5) "6"
6) "7"

```

在对有序集合类型排序时会忽略元素的分数，只针对元素自身的值进行排序。比如：

```shell
redis> ZADD myzset 50 2 40 3 20 1 60 5 (integer) 4
redis> SORT myzset 1) "1"
2) "2"
3) "3"
4) "5"

```

除了可以排列数字外， `SORT` 命令还可以通过 `ALPHA` 参数实现按照字典顺序排列非数字元素，就像这样：

```shell
redis> LPUSH mylistalpha a c e d B C A (integer) 7
redis> SORT mylistalpha (error) ERR One or more scores can't be converted into double
redis> SORT mylistalpha ALPHA 1) "A"
2) "B"
3) "C"
4) "a"
5) "c"
6) "d"
7) "e"

```

从这段示例中可以看到如果没有加 `ALPHA` 参数的话， `SORT` 命令会尝试将所有元素转换成双精度浮点数来比较，如果无法转换则会提示错误。

回到小白的问题， `SORT` 命令默认是按照从小到大的顺序排列，而一般博客中显示文章的顺序都是按照时间倒序的，即最新的文章显示在最前面。 `SORT` 命令的 `DESC` 参数可以实现将元素按照从大到小的顺序排列：

```shell
redis> SORT tag:ruby:posts DESC 1) "26"
2) "12"
3) "6"
4) "2"

```

那么如果文章数量过多需要分页显示呢？ `SORT` 命令还支持 `LIMIT` 参数来返回指定范围的结果。用法和SQL语句一样， `LIMIT offset count` ，表示跳过前 `offset` 个元素并获取之后的 `count` 个元素。

`SORT` 命令的参数可以组合使用，像这样：

```shell
redis> SORT tag:ruby:posts DESC LIMIT 1 2 1) "12"
2) "6"

```

