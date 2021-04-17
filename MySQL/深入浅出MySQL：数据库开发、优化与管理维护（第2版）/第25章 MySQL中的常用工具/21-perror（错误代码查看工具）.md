

在MySQL的使用过程中，可能会出现各种各样的error，这些error有些是由于操作系统引起的，比如文件或者目录不存在；有些则是由于存储引擎使用不当引起的。这些 error 一般都有一个代码，类似于“error：#”或者“Errcode：#”，“#”代表具体的错误号。perror的作用就是解释这些错误代码的详细含义。

perror的用法很简单，如下所示：

perror [OPTIONS] [ERRORCODE [ERRORCODE. .]]

在下面的例子中，可以看一下错误号30和60分别是指什么错误：

[zzx@localhost mysql]$ perror 30 60

OS error code 30: Read-only file system

OS error code 60: Device not a stream



