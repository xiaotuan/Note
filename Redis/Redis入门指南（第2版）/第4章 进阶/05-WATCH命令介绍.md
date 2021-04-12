### 4.1.3　WATCH命令介绍

我们已经知道在一个事务中只有当所有命令都依次执行完后才能得到每个结果的返回值，可是有些情况下需要先获得一条命令的返回值，然后再根据这个值执行下一条命令。例如介绍 `INCR` 命令时曾经说过使用 `GET` 和 `SET` 命令自己实现 `incr` 函数会出现竞态条件，伪代码如下：

```shell
def incr($key)
　　$value = GET $key
　　if not $value
　　　　   $value = 0
　　$value = $value + 1
　　SET $key, $value
　　return $value

```

肯定会有很多读者想到可以用事务来实现 `incr` 函数以防止竞态条件，可是因为事务中的每个命令的执行结果都是最后一起返回的，所以无法将前一条命令的结果作为下一条命令的参数，即在执行 `SET` 命令时无法获得 `GET` 命令的返回值，也就无法做到增1的功能了。

为了解决这个问题，我们需要换一种思路。即在 `GET` 获得键值后保证该键值不被其他客户端修改，直到函数执行完成后才允许其他客户端修改该键键值，这样也可以防止竞态条件。要实现这一思路需要请出事务家族的另一位成员： `WATCH。WATCH` 命令可以监控一个或多个键，一旦其中有一个键被修改（或删除），之后的事务就不会执行。监控一直持续到 `EXEC` 命令（事务中的命令是在 `EXEC` 之后才执行的，所以在 `MULTI` 命令后可以修改 `WATCH` 监控的键值），如：

```shell
redis> SET key 1
OK
redis> WATCH key
OK
redis> SET key 2
OK
redis> MULTI
OK
redis> SET key 3
QUEUED
redis> EXEC
(nil)
redis> GET key
"2"

```

上例中在执行 `WATCH` 命令后、事务执行前修改了key的值（即 `SET key 2` ），所以最后事务中的命令 `SET key 3` 没有执行， `EXEC` 命令返回空结果。

学会了 `WATCH` 命令就可以通过事务自己实现 `incr` 函数了，伪代码如下：

```shell
def incr($key)
　　WATCH $key
　　$value = GET $key
　　 if not $value
　　　　$value = 0
　　 $value = $value + 1
　　MULTI 　　SET $key, $value
　　　　result = EXEC
　　return result[0]

```

因为 `EXEC` 命令返回值是多行字符串类型，所以代码中使用 `result[0]` 来获得其中第一个结果。

提示

> 由于 `WATCH` 命令的作用只是当被监控的键值被修改后阻止之后一个事务的执行，而不能保证其他客户端不修改这一键值，所以我们需要在 `EXEC` 执行失败后重新执行整个函数。

执行 `EXEC` 命令后会取消对所有键的监控，如果不想执行事务中的命令也可以使用 `UNWATCH` 命令来取消监控。比如，我们要实现 `hsetxx` 函数，作用与 `HSETNX` 命令类似，只不过是仅当字段存在时才赋值。为了避免竞态条件我们使用事务来完成这一功能：

```shell
def hsetxx($key, $field, $value)
　　WATCH $key
　　$isFieldExists = HEXISTS $key, $field
　　if $isFieldExists is 1
　　　　  MULTI 　　　　  HSET $key, $field, $value
　　　　  EXEC 　　else
　　　　  UNWATCH 　　return $isFieldExists

```

在代码中会判断要赋值的字段是否存在，如果字段不存在的话就不执行事务中的命令，但需要使用 `UNWATCH` 命令来保证下一个事务的执行不会受到影响。

