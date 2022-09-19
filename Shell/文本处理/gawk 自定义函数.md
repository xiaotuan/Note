[toc]

### 1. 定义函数

要定义自己的函数，必须用 `function` 关键字。

```shell
function name([variables])
{
	statements
}
```

函数名必须能够唯一标识函数。可以在调用的 `gawk` 程序中传给这个函数一个或多个变量。

```shell
function printthird()
{
	print $3
}
```

函数还能用 `return` 语句返回值：

```shell
return value
```

值可以是变量，或者是最终能计算出值的算式：

```shell
function myrand(limit)
{
	return int(limit * rand())
}
```

你可以将函数的返回值付给 `gawk` 程序中的一个变量：

```shell
x = myrand(100)
```

### 2. 使用自定义函数

在定义函数时，它必须出现在所有代码块之前（包括 BEGIN 代码块）。

```shell
$ gawk 'function myprint() { printf "%-16s - %s\n", $1, $4 }; BEGIN { FS="\n"; RS="" } { myprint() }' data1.txt 
Riley Mullen     - (312)555-1234
Frank Williams   - (317)555-9876
Haley Snell      - (313)555-4938
```

### 3. 创建函数库

首先，你需要穿件一个存储所有 gawk 函数的文件。

```shell
$ cat funclib
function myprint()
{
    printf "%-16s - %s\n", $1, $4
}

function myrand(limit)
{
    return int(limit * rand())
}

function printthird()
{
    print $3
}
```

funclib 文件含有三个函数定义。需要使用 `-f` 命令行参数来使用它们。很遗憾，不能将 `-f` 命令行参数和内联 `gawk` 脚本放到一起使用，不过可以在同一个命令行中使用多个 `-f` 参数。

```shell
$ cat script
BEGIN { FS="\n"; RS=""}
{
    myprint()
}
$ gawk -f funclib -f script data1.txt 
Riley Mullen     - (312)555-1234
Frank Williams   - (317)555-9876
Haley Snell      - (313)555-4938
```

