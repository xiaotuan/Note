[toc]

`gawk` 编程语言支持两种不同类型的变量：

+ 内建变量
+ 自定义变量

### 1. 内建变量

数据字段变量允许你使用美元符号（`$`）和字段在该记录中的位置值来引用记录对应的字段。因此，要引用记录中的第一个数据字段，就用变量 `$1`；要引用第二个字段，就用 `$2`，依次类推。

数据字段是由字段分隔符来划定的。默认情况下，字段分隔符时一个空白字符，也就是空格符或者制表符。

<center><b>gawk 数据字段和记录变量</b></center>

| 变量        | 描述                                             |
| ----------- | ------------------------------------------------ |
| FIELDWIDTHS | 由空格分隔的一列数字，定义了每个数据字段确切宽度 |
| FS          | 输入字段分隔符                                   |
| RS          | 输入记录分隔符                                   |
| OFS         | 输出字段分隔符                                   |
| ORS         | 输出记录分隔符                                   |

变量 `FS` 和 `OFS` 定义了 `gawk` 如何处理数据流中的数据字段。变量 `OFS` 具备与 `FS` 相同的功能，只不过是用在 `print` 命令的输出上。

默认情况下，`gawk` 将 `OFS` 设成了一个空格，所以如果你用命令：

```shell
print $1,$2,$3
```

会看到如下输出：

```shell
field1 field2 field3
```

通过设置 `OFS` 变量，可以在输出中使用任意字符串来分隔字段：

```shell
$ cat data1.txt
data11,data12,data13,data14,data15
data21,data22,data23,data24,data25
data31,data32,data33,data34,data35
$ gawk 'BEGIN {FS="," ; OFS="-"} {print $1,$2,$3}' data1.txt
data11-data12-data13
data21-data22-data23
data31-data32-data33
```

`FIELDWIDTHS` 变量允许你不依靠字段分隔符来读取记录。在一些应用程序中，数据并没有使用字段分隔符，而是被放置在了记录中的特定列。在这种情况下，必须设定 `FIELDWIDTHS` 变量来匹配数据在记录中的位置。

一旦设置了 `FIELDWIDTHS` 变量，`gawk` 就会忽略 `FS` 变量，并根据提供的字段宽度来计算字段。

```shell
$ cat data1.txt
1005.3247596.37
115-2.349194.00
05810.1298100.1
$ gawk 'BEGIN { FIELDWIDTHS="3 5 2 5" } { print $1,$2,$3,$4}' data1.txt
100 5.324 75 96.37
115 -2.34 91 94.00
058 10.12 98 100.1
```

`FIELDWIDTHS` 变量定义了四个字段，`gawk` 依次来解析数据记录。每个记录中的数字串会根据已定义号的字段长度来分割。

> 注意：一定要记住，一旦设定了 `FIELDWIDTHS` 变量的值，就不能再改变了。这种方法并不适用于变长的字段。

如果你用默认的 `FS` 和 `RS` 变量来读取这组数据，`gawk` 就会把每行作为一条单独的记录来读取，并将记录中的空格当作字段分隔符。

要解决这个问题，只需把 `FS` 变量设置成换行符。这就表明数据流中的每行都是一个单独的字段，每行上的所有数据都属于同一个字段。但现在令你头疼的是无从判断一个新的数据行从何开始。

对于这一问题，可以把 `RS` 变量设置成空字符串，然后在数据记录间留一个空白行。`gawk` 会把每个空白行当作一个记录分隔符。

```shell
$ cat data1.txt
Riley Mullen
123 Main Street
Chicago, IL 60601
(312)555-1234

Frank Williams
456 Oak Street
Indianapolis, IN 46201
(317)555-9876

Haley Snell
4231 Elm Street
Detroit, MI 48201
(313)555-4938
$ gawk 'BEGIN { FS="\n"; RS="" } { print $1,$4}' data1.txt
Riley Mullen (312)555-1234
Frank Williams (317)555-9876
Haley Snell (313)555-4938
```

现在 `gawk` 把文件中的每行都当成一个字段，把空白行当作记录分隔符。

### 2. 数据变量

| 变量       | 描述                                                     |
| ---------- | -------------------------------------------------------- |
| ARGC       | 当前命令行参数个数                                       |
| ARGIND     | 当前文件在 ARGV 中的位置                                 |
| ARGV       | 包含命令行参数的数组                                     |
| CONVFMT    | 数字的转换格式（参见 printf 语句），默认值为 `%.6g`      |
| ENVIRON    | 当前 shell 环境变量及其值组成的关联数组                  |
| ERRNO      | 当读取或关闭输入文件发生错误时的系统错误号               |
| FILENAME   | 用作 `gawk` 输入数据的数据文件的文件名                   |
| FNR        | 当前数据文件中的数据行数                                 |
| IGNORECASE | 设成非零值时，忽略 `gawk` 命令中出现的字符串的字符大小写 |
| NF         | 数据文件中的字段总数                                     |
| NR         | 已处理的输入记录数                                       |
| OFMT       | 数字的输出格式，默认值为 `%.6g`                          |
| RLENGTH    | 由 match 函数所匹配的子字符串的长度                      |
| RSTART     | 由 match 函数所匹配的子字符串的起始位置                  |

你应该能从上面的列表中认出一些 shell 脚本编程中的变量。ARGC 和 ARGV 变量允许从 shell 中获得命令行参数的总数以及它们的值。但这可能有点麻烦，因为 `gawk` 并不会将脚本当成命令行参数的一部分。

```shell
$ gawk 'BEGIN { print ARGC,ARGV[1]}' data1.txt
2 data1.txt
```

ARGC 变量表明命令行上有两个参数。这包括 `gawk` 命令和 `data1.txt` 参数（记住，程序脚本并不算参数）。ARGV 数组从索引 0 开始，代表的是命令。第一个数组值是 `gawk` 命令后的第一个命令行参数。

> 说明：跟 shell 变量不同，在脚本中引用 `gawk` 变量时，变量名前不加美元符。

ENVIRON 变量看起来可能有点陌生。它使用**关联数组**来提取 shell 环境变量。关联数组用文本作为数组的索引值，而不是数值。

数组索引中的文本是 shell 环境变量名，而数组的值则是 shell 环境变量的值。下面有个例子：

```shell
$ gawk 'BEGIN { print ENVIRON["HOME"]; print ENVIRON["PATH"]; }'
/home/xiaotuan
/home/xiaotuan/jdk-11.0.14_linux-x64_bin/jdk-11.0.14/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

ENVIRON["HOME"] 变量从 shell 中提取了 HOME 环境变量的值。

当要在 `gawk` 程序中跟踪数据字段和记录时，变量 FNR、NF 和 NR 用起来就非常方便。有时你并不知道记录中到底有多少个数据字段。NF 变量可以让你在不知道具体位置的情况下指定记录中的最后一个数据字段：

```shell
$ gawk 'BEGIN { FS=":" ; OFS=":" } { print $1,$NF}' /etc/passwd
root:/bin/bash
daemon:/usr/sbin/nologin
bin:/usr/sbin/nologin
sys:/usr/sbin/nologin
sync:/bin/sync
games:/usr/sbin/nologin
man:/usr/sbin/nologin
......
```

NF 变量含有数据文件中最后一个数据字段的数字值。可以在它前面加个美元符将其用作字段变量。

FNR 和 NR 变量虽然类似，但又略有不同。FNR 变量含有当前数据文件中已处理过的记录数，NR 变量则含有已处理过的记录总数。

```shell
$ gawk 'BEGIN { FS="," } { print $1,"FNR="FNR}' data1.txt data1.txt
data11 FNR=1
data21 FNR=2
data31 FNR=3
data11 FNR=1
data21 FNR=2
data31 FNR=3
```

在这个例子中，`gawk` 程序的命令行定义了两个输入文件（两次指定的是同样的输入文件）。这个脚本会打印第一个数据字段的值和 FNR 变量的当前值。注意，当 `gawk` 程序处理第二个数据文件时，FNR 值被设回了 1。

现在，让我们加上 NR 变量看看会输出什么。

```shell
$ gawk 'BEGIN { FS="," } { print $1,"FNR="FNR,"NR="NR } END { print "There were", NR, "records pricessed" }' data1.txt data1.txt
data11 FNR=1 NR=1
data21 FNR=2 NR=2
data31 FNR=3 NR=3
data11 FNR=1 NR=4
data21 FNR=2 NR=5
data31 FNR=3 NR=6
There were 6 records pricessed
```

FNR 变量的值在 `gawk` 处理第二个数据文件时被重置了，而 NR 变量则在处理第二个数据文件时继续计数。

### 3. 自定义变量

