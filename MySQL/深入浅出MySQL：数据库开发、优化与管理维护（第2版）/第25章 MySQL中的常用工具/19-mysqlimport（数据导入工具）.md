

mysqlimport是客户端数据导入工具，用来导入mysqldump加-T选项后导出的文本文件。它实际上是客户端提供了LOAD DATA INFILEQL语句的一个命令行接口。用法和LOAD DATA INFILE子句非常类似，我们在第 27章（备份与恢复）中对mysqlimport和LOAD DATA INFILE的用法都举例进行了详细的介绍，这里就不再赘述。

mysqlimport的基本用法如下：

shell> mysqlimport [options] db_name textfile1 [textfile2 . .]



