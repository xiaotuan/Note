测试命令（`t`）也可以用来改变 `sed` 编辑器脚本的执行流程。测试命令会根据替换命令的结果跳转到某个标签，而不是根据地址进行跳转。测试命令使用与分支命令相同的格式：

```shell
[address]t [label]
```

跟分支命令一样，在没有指定标签的情况下，如果测试成功，`sed` 会跳转到脚本的结尾。测试命令提供了对数据流中的文本执行基本的 `if-then` 语句的一个低成本办法。举个例子，如果已经做了一个替换，不需要再做另一个替换，那么测试命令能帮上忙：

```shell
$ cat data1.txt
This is the header line.
This is the first data line.
This is the second data line.
This is the last line.
$ sed '{s/first/matched/; t ; s/This is the/No match on/}' data1.txt
No match on header line.
This is the matched data line.
No match on second data line.
No match on last line.
```

第一个替换命令会查找模式文本 first。如果匹配了行中的模式，它就会替换文本，而且测试命令会跳过后面的替换命令。如果第一个替换命令未能匹配模式，第二个替换命令就会被执行。

有了测试命令，你就能结束之前用分支命令形成的无限循环。

```shell
$ echo "This, is, a, test, to, remove, commas." | sed -n '{:start ; s/,//1p; t start}'
This is, a, test, to, remove, commas.
This is a, test, to, remove, commas.
This is a test, to, remove, commas.
This is a test to, remove, commas.
This is a test to remove, commas.
This is a test to remove commas.
```

