[toc]

### 1. 语法

只有最新版本的 shell 才提供 printf 命令。X/Open 规范建议我们应该用它来代替 echo 命令，以产生格式化的输出。

它的语法是：

```shell
printf "format string" parameter1 parameter2 ...
```

### 2. 支持的转义序列

| 转义序列 | 说明                         |
| -------- | ---------------------------- |
| `\"`     | 双引号                       |
| `\\`     | 反斜线字符                   |
| `\a`     | 报警（响铃或蜂鸣）           |
| `\b`     | 退格字符                     |
| `\c`     | 取消进一步的输出             |
| `\f`     | 进纸换页字符                 |
| `\n`     | 换行符                       |
| `\r`     | 回车符                       |
| `\t`     | 制表符                       |
| `\v`     | 垂直制表符                   |
| `\ooo`   | 八进制值 ooo 表示的单个字符  |
| `\xHH`   | 十六进制值 HH 表示的单个字符 |

### 3. 转换字符

| 字符转换限定符 | 说明               |
| -------------- | ------------------ |
| d              | 输出一个十进制数字 |
| c              | 输出一个字符       |
| s              | 输出一个字符串     |
| %              | 输出一个% 字符     |

### 4. 示例

```shell
$ printf "%s\n" hello
hello
$ printf "%s %d\t%s" "Hi There" 15 people
Hi There 15 people
```

