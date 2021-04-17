

使用MySQL的CHECK TABLE和REPAIR TABLE命令一起进行修复，CHECK TABLE用来检查表是否有损坏；REPAIR TABLE用来对坏表进行修复。这两个命令的语法如下：

CHECK TABLE tbl_name [, tbl_name] . . [option] . .

option = {QUICK | FAST | MEDIUM | EXTENDED | CHANGED}

REPAIR [LOCAL | NO_WRITE_TO_BINLOG] TABLE

tbl_name [, tbl_name]… [QUICK] [EXTENDED] [USE_FRM]

关于以上选项的详细说明，有兴趣的读者可以参考MySQL的帮助文档。



