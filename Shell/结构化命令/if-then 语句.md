`if-then` 语句有如下格式：

```shell
if command
then
	commands
fi
```

bash shell 的 `if` 语句会运行 `if` 后面的那个命令。如果该命令的退出状态码是 0（该命令成功运行），位于 `then` 部分的命令就会被执行。如果该命令的退出状态码是其他值，`then` 部分的命令就不会被执行，bash shell 会继续执行脚本中的下一个命令。`fi` 语句用来表示 `if-then` 语句到此结束。

```shell
#!/bin/bash
# testing the if statement
if pwd
then
	echo "It worked"
fi
```

> 提示：你可能在有些脚本中看到过 `if-then` 语句的另一种形式：
>
> ```shell
> if command; then
> 	commands
> fi
> ```

在 `then` 部分，你可以使用不止一条命令。可以像脚本中的其他地方一样在这里列出多条命令。bash shell 会将这些命令当成一个块，如果 `if` 语句行的命令的退出状态值为 0，所有的命令都会被执行；如果 `if` 语句行的命令的退出状态不为 0，所有的命令都会被跳过。

```shell
#!/bin/bash
# testing multiple commands in the then section

testuser=Christine

if grep $testuser /etc/passwd
then
	echo "This is my first command"
	echo "This is my second command"
	echo "I can even put in other commands besides echo:"
	ls -a /home/$testuser/.b*
fi
```

