[toc]

`while` 命令允许定义一个要测试的命令，然后循环执行一组命令，只要定义的测试命令返回的是退出状态码 0.它会在每次迭代的一开始测试 `test` 命令。在 `test` 命令返回非零退出状态码时，`while` 命令会停止执行那组命令。

### 1. while 的基本格式

`while` 命令的格式是：

```shell
while test command
do
	other commands
done
```

例如：

```shell
#!/bin/bash
# while command test

var1=10
while [ $var1 -gt 0 ]
do 
	echo $var1
	var1=$[ $var1 - 1 ]
done
```

### 2. 使用多个测试命令

`while` 命令允许你在 `while` 语句行定义多个测试命令。只有最后一个测试命令的退出状态码会被用来决定什么时候结束循环：

```shell
#!/bin/bash
# testing a multicommand while loop

var1=10

while echo $var1
	[ $var1 -ge 0 ]
do 
	echo "This is inside the loop"
	var1=$[ $var1 - 1 ]
done
```

运行结果如下：

```shell
$ ./test.sh 
10
This is inside the loop
9
This is inside the loop
8
This is inside the loop
7
This is inside the loop
6
This is inside the loop
5
This is inside the loop
4
This is inside the loop
3
This is inside the loop
2
This is inside the loop
1
This is inside the loop
0
This is inside the loop
-1
```

在含有多个命令的 `while` 语句中，在每次迭代中所有的测试命令都会被执行，包括测试命令失败的最后一次迭代。要留心这种用法。另一处要留意的是该如何指定多个测试命令。注意，每个测试命令都出现在单独的一行上。