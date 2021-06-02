这个需求只有管理员才能解决：

（1）如果 SVN 管理员没有历史备份，只能重新用 `svnadmin dump` 导出整个版本库。

（2）再用 `svndumpfilter` 命令过滤掉不应检入的大文件。

（3）然后用 `svnadmin load` 重建版本库。