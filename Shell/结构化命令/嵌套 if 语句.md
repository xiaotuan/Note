有时你需要检查脚本代码中的多种条件。对此，可以使用嵌套的 `if-then` 语句：

```shell
#!/bin/bash
# Testing nested ifs

testuser=NoSuchUser

if grep $testuser /etc/passwd
then
	echo "The user $testuser exists on this system."
else
	echo "The user $testuser does not exist on this system."
	if ls -d /home/$testuser/
	then
		echo "However, $testuser has a directory."
	fi
fi
```

可以继续将多个 `elif` 语句串联起来，形成一个大的 `if-then-elif` 嵌套组合：

```shell
if command1
then
	command set 1
elif command2
then
	command set 2
elif command3
then
	command set 3
elif command4
then
	command set 4
fi
```

