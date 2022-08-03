[toc]

### 1. 基本使用方法

`grep` 命令的命令行格式如下：

```shell
grep [options] pattern [file]
```

`grep` 命令会在输入或指定的文件中查找包含匹配指定模式的字符的行。`grep` 的输出就是包含了匹配模式的行。

```shell
$ grep three file1
three
$ grep t file1
two
three
$
```

### 2. 反向搜索

如果要进行反向搜索（输出不匹配该模式的行），可加 `-v` 参数：

```shell
$ grep -v t file1
one
four
five
$
```

### 3. 显示行号

如果要显示匹配模式的行所在的行号，可加 `-n` 参数：

```shell
$ grep -n t file1
2: two
3: three
$
```

### 4. 统计匹配总数

如果只要知道有多少行含有匹配的模式，可用 `-c` 参数。

```shell
$ grep -c t file1
2
$
```

### 5. 指定多个匹配模式

如果要指定多个匹配模式，可用 `-e` 参数来指定每个模式。

```shell
$ grep -e t -e file1
two
three
four
five
$
```

### 6. 使用正则表达式来匹配

默认情况下，`grep` 命令用基本的 Unix 风格正则表达式来匹配模式。

```shell
$ grep [tf] file1
two
three
four
five
$
```

### 7. egrep 命令

`egrep` 命令是 `grep` 的一个衍生，支持 POSIX 扩展正则表达式。POSIX 扩展正则表达式含有更多的可以用来指定匹配模式的字符。

### 8. fgrep 命令

`fgrep` 则是 `grep` 另外一个版本，支持将匹配模式指定为用换行符分隔的一列固定长度的字符串。这样就可以把这列字符串放到一个文件中，然后在 `fgrep` 命令中用其在一个大型文件中搜索字符串。
