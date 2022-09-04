[toc]

bash shell 提供了两项可在 `if-then` 语句中使用的高级特性：

+ 用于数学表达式的双括号
+ 用于高级字符串处理功能的双方括号

### 1. 使用双括号

**双括号**命令允许你在比较过程中使用高级数学表达式。`test` 命令只能在比较中使用简单的算术操作。双括号命令的格式如下：

```shell
(( expression ))
```

expression 可以是任意的数学赋值或比较表达式。除了 `test` 命令使用的标准数学运算符，双括号命令中会用到其他运算符：

| 符号  | 描述     |
| ----- | -------- |
| val++ | 后增     |
| val-- | 后减     |
| ++val | 先增     |
| --val | 先减     |
| !     | 逻辑求反 |
| ~     | 位求反   |
| **    | 幂运算   |
| <<    | 左位移   |
| >>    | 右位移   |
| &     | 位布尔和 |
| \|    | 位布尔或 |
| &&    | 逻辑和   |
| \|\|  | 逻辑或   |

可以在 `if` 语句中用双括号命令，也可以在脚本中的普通命令里使用来赋值：

```shell
#!/bin/bash
# using double parenthesis

val1=10	

if (( $val1 ** 2 > 90 ))
then
	(( val2 = $val1 ** 2 ))
	echo "The square of $val1 is $val2"
fi
```

> 注意：不需要将双括号中表达式里的大于号转义。这是双括号命令提供的另一个高级特性。

### 2. 使用双方括号

**双方括号**命令提供了针对字符串比较的高级特性。双方括号命令的格式如下：

```shell
[[ expression ]]
```

双方括号里的 expression 使用了 test 命令中采用的标准字符串比较。但它提供了 `test` 命令未提供的另一个特性——**模式匹配**。

> 注意：双方括号在 bash shell 中工作良好。不过要小心，不是所用的 shell 都支持双方括号。

```shell
#!/bin/bash
# using pattern matching

if [[ $USER == r* ]]
then	
	echo "Hello $USER"
else
	echo "Sorry, I do not know you"
fi
```

