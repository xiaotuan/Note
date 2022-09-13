`-t` 选项会强制 `mktemp` 命令来在系统的临时目录来创建该文件。在用这个特性时，`mktemp` 命令会返回用来创建临时文件的全路径，而不是只有文件名。

```shell
$ mktemp -t test.XXXXXX
/tmp/test.g1ewAb
$ ls -al /tmp/test.*
-rw------- 1 xiatuan xiatuan 0 Sep 13 11:30 /tmp/test.g1ewAb
```

例如：

```shell
#!/bin/bash
# cteating a temp file in /tmp

tempfile=$(mktemp -t tmp.XXXXXX)

echo "This is a test file." > $tempfile 
echo "This is the second line of the test." >> $tempfile

echo "The temp file is located at: $tempfile"
cat $tempfile
rm -f $tempfile 
```

运行结果如下：

```shell
$ ./test.sh 
The temp file is located at: /tmp/tmp.AeGSz5
This is a test file.
This is the second line of the test.
```

