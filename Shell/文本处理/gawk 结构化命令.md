[toc]

### 1. if 语句

`gawk` 编程语言支持标准的 `if-then-else` 格式的 `if` 语句。你必须为 `if` 语句定义一个求值的条件，并将其圆括号括起来。如果条件求值为 TRUE，紧跟在 `if` 语句后的语句会执行。如果条件求值为 FALSE，这条语句就会被跳过。可以用这种格式：

```shell
if (condition)
	statement1
```

也可以将它放在一行上，像这样：

```shell
if (condition) statement1
```

例如：

```shell
$ gawk '{ if ($1 > 20) print $1}' data1.txt 
50
34
```

如果需要在 `if` 语句中执行多条语句，就必须用花括号将它们括起来。

```shell
$ gawk '{ if ($1 > 20) { x = $1 * 2; print x; }}' data1.txt 
100
68
```

`gawk` 的 `if` 语句也支持 `else` 子句，允许在 `if` 语句条件不成立的情况下执行一条或多条语句。

```shell
$ gawk '{ if ($1 > 20) { x = $1 * 2; print x } else { x = $1 / 2; print x}}'  data1.txt 
5
2.5
6.5
100
68
```

可以在单行上使用 `else` 子句，但必须在 if 语句部分之后使用分号。

```shell
if (condition) statement1; else statement2
```

例如：

```shell
$ gawk '{ if ($1 > 20) print $1 * 2; else print $1 / 2}' data1.txt 
5
2.5
6.5
100
68
```

### 2. while 语句

`while` 语句为 `gawk` 程序提供了一个基本的循环功能。下面是 `while` 语句的格式：

```shell
while (condition)
{
	statements
}
```

例如：

```shell
$ gawk '{ total = 0; i = 1; while (i < 4) { total += $i; i++; }; avg = total / 3; print "Averate: ", avg; }' data1.txt 
Averate:  128.333
Averate:  137.667
Averate:  176.667
```

`gawk` 编程语言支持在 `while` 循环中使用 `break` 语句和 `continue` 语句，允许你从循环中跳出。

```shell
$ gawk '{ total = 0; i = 1; while (i < 4) { total += $i; if (i == 2) break;  i++; }; avg = total / 2; print "The average of the first two data elements is: ", avg; }' data1.txt 
The average of the first two data elements is:  125
The average of the first two data elements is:  136.5
The average of the first two data elements is:  157.5
```

### 3. do-while 语句

`do-while` 语句类似于 `while` 语句，但会在检查条件语句之前执行命令。下面是 `do-while` 语句的格式。

```shell
do {
	statements
} while (condition)
```

这种格式保证了语句会在条件被求值之前至少执行一次。

```shell
$ gawk '{ total = 0; i = 1; do { total += $i; i++; } while (total < 150); print total }' data1.txt 
250
160
315
```

### 4. for 语句

`gawk` 编程语言支持 C 风格的 `for` 循环。

```shell
for ( variable assignment; condition; iteration process)
```

例如：

```shell
$ gawk '{ total = 0; for (i = 1; i < 4; i++) { total += $i; }; avg = total / 3; print "Average: ", avg }' data1.txt 
Average:  128.333
Average:  137.667
Average:  176.667
```

