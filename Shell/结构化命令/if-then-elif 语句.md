可以使用 `else` 部分的另一种形式：`elif`。`elif` 使用另一个 `if-then` 语句延续 `else` 部分：

```shell
if command1
then
	commands
elif command2
then
	more commands
fi
```

`elif` 语句行提供了另一个要测试的命令，这类似于原始的 `if` 语句行。如果 `elif` 后命令的退出状态码是 0，则 bash 会执行第二个 then 语句部分的命令：

```shell
#!/bin/bash
# Testing nested ifs - use elif

testuser=NoSuchUser

if grep $testuser /etc/passwd
then
	echo "The user $testuser exists on this system."
elif ls -d /home/$testuser
then
	echo "The user $testuser does not exist on this system."
	echo "However, $testuser has a directory."
fi
```

在嵌套 `elif` 中也可以加入一个 `else` 语句：

```shell
#!/bin/bash
# Testing nested ifs - use elif

testuser=NoSuchUser

if grep $testuser /etc/passwd
then
	echo "The user $testuser exists on this system."
elif ls -d /home/$testuser
then
	echo "The user $testuser does not exist on this system."
	echo "However, $testuser has a directory."
else
	echo "The user $testuser does not exist on this system."
	echo "And, $testuser does not have a directory."
fi
```

> 注意：在 `elif` 语句中，紧跟其后的 `else` 语句属于 `elif` 代码块。它们并不属于之前的 `if-then` 代码块。

