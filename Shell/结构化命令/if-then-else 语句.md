`if-then-else` 语句格式如下：

```shell
if command
then
	commands
else
	commands
fi
```

当 `if` 语句中的命令返回退出状态码为 0 时，then 部分中的命令会被执行。当 `if` 语句中的命令返回非零退出状态码时，bash shell 会执行 else 部分中的命令。

```shell
#!/bin/bash
# testing the else section

testuser=NoSuchUser

if grep $testuser /etc/passwd
then
	echo "This is my first command"
	echo "This is my second command"
	echo "I can even put in other commands besides echo:"
	ls -a /home/$testuser/.b*
else
	echo "The user $testuser does not exist on this system."
	echo
fi
```

