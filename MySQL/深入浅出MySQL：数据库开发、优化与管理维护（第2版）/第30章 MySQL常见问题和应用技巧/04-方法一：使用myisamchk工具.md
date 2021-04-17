

使用MySQL自带的myisamchk工具进行修复，此工具前面曾经介绍过，是专门用来修复MyISAM的表的工具。恢复命令如下：

myisamchk -r tablename

其中-r参数的含义是recover，上面的方法几乎能解决所有问题，如果不行，则使用命令：

myisamchk -o tablename

其中-o参数的含义是--safe-recover，可以进行更安全的修复。



