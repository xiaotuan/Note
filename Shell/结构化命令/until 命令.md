`until` 命令要求你指定一个通常返回非零退出状态码的测试命令。只有测试命令的退出状态码不为 0，bash shell 才会执行循环中列出的命令。一旦测试命令返回了退出状态码为0，循环就结束了。`until` 命令的格式如下：

```shell
until test commands
do
	other commands
done
```

例如：

```shell
#!/bin/bash
# using the until command

var1=100

until [ $var1 -eq 0 ]
do 
	echo $var1
	var1=$[ $var1 - 25 ]
done
```

在 `until` 命令中使用多个测试命令时要注意：

```shell
#!/bin/bash
# using the until command

var1=100

until echo $var1
	[ $var1 -eq 0 ]
do
	echo Inside the loop: $var1
	var1=$[ $var1 - 25 ]
done
```

shell 会执行指定的多个测试命令，只有在最后一个命令成立时停止。

