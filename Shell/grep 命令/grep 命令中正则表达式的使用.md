[toc]

### 1. 常用正则表达式字符

grep 命令支持的正则表达式：

| 字符 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| ^    | 指向一行的开头                                               |
| $    | 指向一行的结尾                                               |
| .    | 任意单个字符                                                 |
| []   | 方括号内包含一个字符范围，其中任何一个字符都可以被匹配，例如字符范围 `a~e`，或在字符范围前面加上 `^` 符号表示使用反向字符范围，即不匹配指定范围内的字符 |

如果想将上述字符用作普通字符，就需要在它们前面加上 `\` 字符。例如，如果想使用 $ 字符，你需要将它写为 `\$`。

### 2. 特殊匹配模式

| 匹配模式   | 含义                     |
| ---------- | ------------------------ |
| [:alnum:]  | 字母与数字字符           |
| [:alpha:]  | 字母                     |
| [:ascii:]  | ASCII 字符               |
| [:blank:]  | 空格或制表符             |
| [:cntrl:]  | ASCII 控制字符           |
| [:digit:]  | 数字                     |
| [:graph:]  | 非控制、非空格字符       |
| [:lower:]  | 小写字母                 |
| [:print:]  | 可打印字符               |
| [:punct:]  | 标点符号字符             |
| [:space:]  | 空白字符，包括垂直制表符 |
| [:upper:]  | 大写字母                 |
| [:xdigit:] | 十六进制数字             |

### 3. 扩展匹配

如果指定了用于扩展匹配的 `-E` 选项，那些用于控制匹配完成的其他字符可能会遵循正则表达式规则。对于 grep 命令来说，我们还需要在这些字符串之前加上 `\` 字符。

| 选项   | 含义                                |
| ------ | ----------------------------------- |
| ?      | 匹配是可选的，但最多匹配一次        |
| *      | 必须匹配 0 次或多次                 |
| +      | 必须匹配 1 次或多次                 |
| {n}    | 必须匹配 n 次                       |
| {n,}   | 必须匹配 n 次或 n 次以上            |
| {n, m} | 匹配次数在 n 到 m 之间，包括 n 和 m |

### 4. 示例

#### 4.1 查找以字母 e 结尾的行

```shell
$ grep e$ words2.txt
Art thou not, fatal vision, sensible
I see thee yet, in form as palpable
Nature seems dead, and wicked dreams abuse
$
```

#### 4.2 查找以字母 a 结尾的单词

```shell
$ grep a[[:blank:]] words2.txt
Is this a dagger which I see before me,
A dagger of the mind, a false creation,
Moves like a ghost. Thou sure and firm-set earth,
$
```

#### 4.3 查找以 Th 开头的由 3 个字母组成的单词

```shell
$ grep Th.[[:space:]] words2.txt
The handle toward my hand? Come, let me clutch thee.
The curtain'd sleep; witchcraft celebrates
Thy very stones prate of my whereabout,
$
```

#### 4.4  使用扩展 grep 模式来搜索只有 10 个字符长的全部由小写字母组成的单词

```shell
$ grep -E [a-z]\{10\} words2.txt
Proceeding from the heat-oppressed brain?
And such an instrument I was to use.
The curtain'd sleep; witchcraft celebrates
Thy very stones prate of my whereabout,
$
```

