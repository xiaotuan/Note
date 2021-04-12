### 6.4.1  `KEYS` 与 `ARGV` 

前面提到过向脚本传递的参数分为 `KEYS` 和 `ARGV` 两类，前者表示要操作的键名，后者表示非键名参数。但事实上这一要求并不是强制的，比如 `EVAL "return redis.call('get', KEYS[1])" 1 user:Bob`  可以获得  `user:Bob`  的键值，同样还可以使用  `EVAL "return redis.call('get', 'user:' .. ARGV[1])" 0 Bob` 完成同样的功能，此时我们虽然并未按照Redis的规则使用 `KEYS` 参数传递键名，但还是获得了正确的结果。

虽然规则不是强制的，但不遵守规则依然有一定的代价。Redis将要发布的3.0版本会带有集群（cluster）功能，集群的作用是将数据库中的键分散到不同的节点上。这意味着在脚本执行前就需要知道脚本会操作哪些键以便找到对应的节点，所以如果脚本中的键名没有使用 `KEYS` 参数传递则无法兼容集群。

有时候键名是根据脚本某部分的执行结果生成的，这时就无法在执行前将键名明确标出。比如一个集合类型键存储了用户ID列表，每个用户使用散列键存储，其中有一个字段是年龄。下面的脚本可以计算某个集合中用户的平均年龄：

```shell
local sum = 0
local users = redis.call('SMEMBERS', KEYS[1])
for _, user_id in ipairs(users) do
　　 local user_age = redis.call('HGET', 'user:' .. user_id, 'age')
　　 sum = sum + user_age
end
return sum / #users

```

这个脚本同样无法兼容集群功能（因为第 4 行中访问了  `KEYS`  变量中没有的键），但却十分实用，避免了数据往返客户端和服务端的开销。为了兼容集群，可以在客户端获取集合中的用户ID列表，然后将用户ID组装成键名列表传给脚本并计算平均年龄。两种方案都是可行的，至于实际采用哪种就需要开发者自行权衡了。

