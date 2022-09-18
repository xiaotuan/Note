`sed` 编辑器提供了一种方法，可以基于地址、地址模式或地址区间排除一整块命令。这允许你只对数据流中的特定行执行一组命令。

分支命令 `b` 的格式如下：

```shell
[address]b [label]
```

address 参数决定了哪些行的数据会触发分支命令。`label` 参数定义了要跳转到的位置。如果没有加 `label` 参数，跳转命令会跳转到脚本的结尾。

```shell
$ cat data1.txt
This is the header line.
This is the first data line.
This is the second data line.
This is the last line.
$ sed '{2,3b ; s/This is/Is this/ ; s/line./test?/}' data1.txt
Is this the header test?
This is the first data line.
This is the second data line.
Is this the last test?
```

要是不想直接跳到脚本的结尾，可以为分支命令定义一个要跳转到的标签。标签以冒号开始，最多可以是 7 个字符长度。

```shell
:label2
```

要指定标签，将它加到 `b` 命令后即可。使用标签允许你跳过地址匹配处的命令，但仍然执行脚本中的其他命令。

```shell
$ sed '{/first/b jump1 ; s/This is the/No jump on/; :jump1 ; s/This is the/Jump here on/}' data1.txt
No jump on header line.
Jump here on first data line.
No jump on second data line.
No jump on last line.
```

跳转命令指定如果文本行中出现了 first，程序应该跳到标签为 jump1 的脚本行。如果分支命令的模式没有匹配，`sed` 编辑器会继续执行脚本中的命令，包括分支标签后的命令（因此，所有的替换命令都会在不匹配分支模式的行上执行）。

如果某行匹配了分支模式，`sed` 编辑器就会跳转到带有分支标签的那行。因此，只有最后一个替换命令会执行。

也可以跳转到脚本中靠前面的标签上，这样就达到了循环的效果。

```shell
$ echo "This, is, a, test, to, remove, commad." | sed -n '{:start ; s/,//p ; b start}'
This is, a, test, to, remove, commad.
This is a, test, to, remove, commad.
This is a test, to, remove, commad.
This is a test to, remove, commad.
This is a test to remove, commad.
This is a test to remove commad.
```

脚本的每次迭代都会删除文本中的第一个逗号，并打印字符串。这个脚本有个问题：它永远不会结束。这就形成了一个无穷循环，不停地查找逗号，直到使用 <kbd>Ctrl</kbd> + <kbd>C</kbd> 组合键发送一个信号，手动停止这个脚本。

要防止这个问题，可以为分支命令指定一个地址模式来查找。如果没有模式，跳转就应该结束。

```shell
$ echo "This, is, a, test, to, remove, commad." | sed -n '{:start ; s/,//p ; /,/b start}'
This is, a, test, to, remove, commad.
This is a, test, to, remove, commad.
This is a test, to, remove, commad.
This is a test to, remove, commad.
This is a test to remove, commad.
This is a test to remove commad.
```

