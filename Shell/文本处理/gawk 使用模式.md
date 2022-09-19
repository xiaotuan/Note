[toc]

### 1. 正则表达式

在使用正则表达式时，正则表达式必须出现在它要控制的程序脚本的左花括号前。

```shell
$ gawk 'BEGIN { FS="," } /11/{print $1}' data1.txt
data11
```

`gawk` 程序会用正则表达式对记录中所有的数据字段进行匹配，包括字段分隔符。

```shell
$ gawk 'BEGIN { FS="," } /,d/{print $1}' data1.txt
data11
data21
data31
```

### 2. 匹配操作符

**匹配操作符**允许将正则表达式限定在记录中的特定数据字段。匹配操作符是波浪线（`~`）。可以指定匹配操作符、数据字段变量以及要匹配的正则表达式。

```shell
$1 ~ /^data/
```

$1 变量代表记录中的第一个数据字段。这个表达式会过滤出第一个字段以文本 data 开头的所有记录。

```shell
$ gawk 'BEGIN { FS="," } $2 ~ /^data2/{print $0}' data1.txt 
data21,data22,data23,data24,data25
```

`gawk` 程序脚本中经常用它在数据文件中搜索特定的数据元素。

```shell
$ gawk -F: '$1 ~ /xiatuan/{print $1,$NF}' /etc/passwd
xiatuan /bin/bash
```

这个例子会在第一个数据字段中查找文本 xiatuan 。如果在记录中才找到了这个模式，它会打印该记录的第一个和最后一个数据字段值。

你也可以用 `!` 符号来排除正则表达式的匹配。

```shell
$1 !~ /expression
```

如果记录中没有找到匹配正则表达式的文本，程序脚本就会作用到记录数据。

```shell
$ gawk -F: '$1 !~ /rich/{print $1,$NF}' /etc/passwd
root /bin/bash
daemon /usr/sbin/nologin
bin /usr/sbin/nologin
sys /usr/sbin/nologin
sync /bin/sync
......
```

### 3. 数学表达式

除了正则表达式，你也可以在匹配模式中用数学表达式。

```shell
$ gawk -F: '$4 == 0 { print $1 }' /etc/passwd
root
```

这段脚本会查看第四个数据字段含有值 0 的记录。

可以使用任何常见的数据比较表达式：

+ `x == y`： 值 x 等于 y
+ `x <= y`：值 x 小于等于 y
+ `x < y`：值 x 小于 y。
+ `x >= y`：值 x 大于等于 y。
+ `x > y`：值 x 大于 y。

也可以对文本数据使用表达式。但必须小心。跟正则表达式不同，表示式必须完全匹配。数据必须跟模式严格匹配。

```shell
$ gawk -F, '$1 == "data" { print $1 }' data1.txt
$ gawk -F, '$1 == "data11" { print $1 }' data1.txt
data11
```

