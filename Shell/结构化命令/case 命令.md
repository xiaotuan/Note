`case` 命令会采用列表格式来检查单个变量的多个值：

```shell
case variable in
pattern1 | pattern2) commands;;
pattern3) commands2;;
*) default commands;;
esac
```

`case` 命令会将指定的变量与不同模式进行比较。如果变量和模式是匹配的，那么 shell 会执行为该模式指定的命令。可以通过竖线操作符在一行中分隔出多个模式。星号会捕获所有与已知模式不匹配的值。

```shell
#!/bin/bash
# using the case command

case $USER in
rich | barbara)
	echo "Welcome, $USER"
	echo "Please enjoy your visit";;
testing)
	echo "Special testing account";;
jessica)
	echo "Do not forget to log off when you're done";;
*)
	echo "Sorry, you are not allowed here";;
esac
```

