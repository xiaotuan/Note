默认情况下，`sort` 命令按照会话指定的默认语言的排序规则对文本文件中的数据行排序。

```shell
$ cat result.txt
one
two
three
four
five
six
seven
eight
night
ten
$ sort result.txt 
eight
five
four
night
one
seven
six
ten
three
two
```

当使用 `sort` 命令对包含数字的数据进行排序时可能出现问题，例如：

```shell
$ cat result.txt 
1
2
100
45
3
10
145
75
xiaotuan@xiaotuan-VirtualBox:~/桌面$ sort result.txt
1
10
100
145
2
3
45
75
```

默认情况下，`sort` 命令会把数字当做字符来执行标准的字符排序，产生的输出可能根本就不是你要的。解决这个问题可用 `-n` 参数，它会告诉 `sort` 命令把数字识别成数字而不是字符串，并且按值排序。

```shell
$ sort -n result.txt
1
2
3
10
45
75
100
145
```

另一个常用的参数是 `-M`，按月排序。Linux 的日志文件经常会在每行的起始位置有一个时间戳，用来表明事件是什么时候发生的。

<center><b>sort 命令参数</b></center>

| 单破折线 | 双破折线                    | 描述                                                         |
| -------- | --------------------------- | ------------------------------------------------------------ |
| `-b`     | `--ignore-leading-blanks`   | 排序时忽略起始的空白                                         |
| `-C`     | `--check=quiet`             | 不排序，如果数据无序也不要报告                               |
| `-c`     | `--check`                   | 不排序，但检查输入数据是不是已排序；未排序的话，报告         |
| `-d`     | `--dictionary-order`        | 仅考虑空白和字母，不考虑特殊字符                             |
| `-f`     | `--ignore-case`             | 默认情况下，会将大写字母排在前面；这个参数会忽略大小写       |
| `-g`     | `--general-number-sort`     | 按通用数值来排序（跟 `-n` 不同，把值当浮点数来排序，支持科学计数法表示的值） |
| `-i`     | `--ignore-nonprinting`      | 在排序时忽略不可打印字符                                     |
| `-k`     | `--key=POS1[,POS2]`         | 排序从 POS1 位置开始；如果指定了 POS2 的话，到 POS2 位置结束 |
| `-M`     | `--month-sort`              | 用三个字符月份名按月份排序                                   |
| `-m`     | `--merge`                   | 将两个已排序数据文件合并                                     |
| `-n`     | `--numeric-sort`            | 按字符串数值来排序（并不转换为浮点数）                       |
| `-o`     | `--output=file`             | 将排序结果写出到指定的文件中                                 |
| `-R`     | `--random-sort`             | 按随机生成的散列表的键值排序                                 |
|          | `--random-source=FILE`      | 指定 `-R` 参数用到随机字节的源文件                           |
| `-r`     | `--reverse`                 | 反序排序（升序变成降序）                                     |
| `-S`     | `--buffer-size=SIZE`        | 指定使用的内存大小                                           |
| `-s`     | `--stable`                  | 禁用最后重排序比较                                           |
| `-T`     | `--temporary-directory=DIR` | 指定一个位置存储临时工作文件                                 |
| `-t`     | `--field-separator=SEP`     | 指定一个用来区分键位置的字符                                 |
| `-z`     | `--zero-terminated`         | 用 NULL 字符作为行尾，而不是用换行符                         |



