### 6.3.1 在脚本中调用Redis命令

在脚本中可以使用 `redis.call` 函数调用Redis命令。就像这样：

```shell
redis.call('set', 'foo', 'bar')
local value = redis.call('get', 'foo')　　  -- value的值为bar

```

`redis.call` 函数的返回值就是Redis命令的执行结果。第2章介绍过Redis命令的返回值有5种类型， `redis.call` 函数会将这5种类型的回复转换成对应的Lua的数据类型，具体的对应规则如表6-7所示（空结果比较特殊，其对应Lua的 `false` ）。

<center class="my_markdown"><b class="my_markdown">表6-7 Redis返回值类型和Lua数据类型转换规则</b></center>

| Redis返回值类型 | Lua数据类型 |
| :-----  | :-----  | :-----  | :-----  |
| 整数回复 | 数字类型 |
| 字符串回复 | 字符串类型 |
| 多行字符串回复 | 表类型（数组形式） |
| 状态回复 | 表类型（只有一个ok字段存储状态信息） |
| 错误回复 | 表类型（只有一个err字段存储错误信息） |

Redis还提供了 `redis.pcall` 函数，功能与 `redis.call` 相同，唯一的区别是当命令执行出错时 `redis.pcall` 会记录错误并继续执行，而 `redis.call` 会直接返回错误，不会继续执行。

