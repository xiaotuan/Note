[toc]

`sed` 编辑器会执行下列操作：

（1）一次从输入中读取一行数据。

（2）根据所提供的编辑命令匹配数据。

（3）按照命令修改流中的数据。

（4）将新的数据输出到 STDOU。

`sed` 命令的格式如下：

```shell
sed options script file
```

<center><b>sed 命令选项</b></center>

| 选项      | 描述                                                   |
| --------- | ------------------------------------------------------ |
| -e script | 在处理输入时，将 script 中指定的命令添加到已有的命令中 |
| -f file   | 在处理输入时，将 file 中指定的命令添加到已有的命令中   |
| -n        | 不产生命令输出，使用 `print` 命令来完成输出            |

script 参数指定了应用于流数据上的单个命令。如果需要用多个命令，要么使用 `-e` 选项在命令行中指定，要么使用 `-f` 选项在单独的文件中指定。

### 1. 在命令行定义编辑器命令

默认情况下，`sed` 编辑器会将指定的命令应用到 STDIN 输入流上。这样你可以直接将数据通过管道输入 `sed` 编辑器处理：

```shell
$ echo "This is a test" | sed 's/test/big test/'
This is a big test
```

> 提示：`sed` 编辑器并不会修改文本文件的数据。它只会将修改后的数据发送到 STDOUT。
>
> ```shell
> $ cat data1.txt
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> $ sed 's/dog/cat/' data1.txt
> The quick brown fox jumps over the lazy cat.
> The quick brown fox jumps over the lazy cat.
> The quick brown fox jumps over the lazy cat.
> The quick brown fox jumps over the lazy cat.
> The quick brown fox jumps over the lazy cat.
> $ cat data1.txt
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> The quick brown fox jumps over the lazy dog.
> ```

### 2. 在命令行使用多个编辑器命令

要在 `sed` 命令行上执行多个命令时，只要用 `-e` 选项就可以了：

```shell
$ sed -e 's/brown/green/; s/dog/cat/' data1.txt
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
The quick green fox jumps over the lazy cat.
```

命令之间必须用分号隔开，并且在命令末尾和分号之间不能有空格。如果不想用分号，也可以用 bash shell 中的次提示符来分隔命令。只要输入第一个单引号标示出 `sed` 程序脚本的起始，bash 会继续提示你输入更多命令，直到输入了标示结束的单引号。

```shell
$ sed -e '
> s/brown/green/
> s/fox/elephant/
> s/dog/cat/' data1.txt
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
```

> 注意：必须要在封尾单引号所在行结束命令。

### 3. 从文件中读取编辑器命令

如果有大量要处理的 `sed` 命令，那么将它们放进一个单独的文件中通常会更方便一些。可以在 `sed` 命令中用 `-f` 选项来指定文件：

```shell
$ cat script1.sed
s/brown/green/
s/fox/elephant/
s/dog/cat/
$ sed -f script1.sed data1.txt
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
The quick green elephant jumps over the lazy cat.
```

在这种情况下，不用再每条命令后面放一个分号。`sed` 编辑器知道每行都是一条单独的命令。