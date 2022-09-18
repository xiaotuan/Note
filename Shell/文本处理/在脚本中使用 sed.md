[toc]

### 1. 使用包装脚本

实现 `sed` 编辑器脚本的过程很烦琐，尤其是脚本很长的话。可以将 `sed` 编辑器命令放到 shell **包装脚本** 中，不用每次使用时都重新键入整个脚本。

在 shell 脚本中，可以将普通的 shell 变量及参数和 `sed` 编辑器脚本一起使用。

```shell
#!/bin/bash
# Shell wrapper for sed editor script.
#			to reverse text file lines.
#
sed -n '{ 1!G ; h ; $p }' $1
#
```

运行结果如下：

```shell
$ ./test.sh data1.txt
This is the last line.
This is the second data line.
This is the first data line.
This is the header line.
```

### 2. 重定向 sed 的输出

默认情况下，`sed` 编辑器会将脚本的结果输出到 STDOUT 上。你可以在 shell 脚本中使用各种标准方法对 `sed` 编辑器的输出进行重定向。可以在脚本中用 `$()` 将 `sed` 编辑器命令的输出重定向到一个变量中，以备后用。

```shell
#!/bin/bash
# Add commas to number in factorial answer
#
factorial=1
counter=1
number=$1
#
while [ $counter -le $number ]
do 
	factorial=$[ $factorial * $counter ]
	counter=$[ $counter + 1 ]
done
#
result=$(echo $factorial | sed '{:start ; s/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/ ; t start}')
#
echo "The result is $result"
#
```

运行结果如下：

```shell
$ ./test.sh 20
The result is 2,432,902,008,176,640,000
```

