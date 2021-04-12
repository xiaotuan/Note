### 4.3.5　 `STORE` 参数

默认情况下 `SORT` 会直接返回排序结果，如果希望保存排序结果，可以使用 `STORE` 参数。如希望把结果保存到 `sort.result` 键中：

```shell
redis> SORT tag:ruby:posts BY post:*->time DESC GET post:*->title GET post:*->time 　　 GET # STORE sort.result (integer) 12
redis> LRANGE sort.result 0 -1  1) "Windows 8 app designs"
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

保存后的键的类型为列表类型，如果键已经存在则会覆盖它。加上 `STORE` 参数后 `SORT` 命令的返回值为结果的个数。

`STORE` 参数常用来结合 `EXPIRE` 命令缓存排序结果，如下面的伪代码：

```shell
# 判断是否存在之前排序结果的缓存
$isCacheExists = EXISTS cache.sort
if $isCacheExists is 1
　　# 如果存在则直接返回
　　return LRANGE cache.sort, 0, -1
else
　　# 如果不存在，则使用SORT命令排序并将结果存入cache.sort键中作为缓存
　　$sortResult = SORT some.list STORE cache.sort
　　# 设置缓存的过期时间为10分钟
　　EXPIRE cache.sort, 600
　　# 返回排序结果
　　return $sortResult

```

