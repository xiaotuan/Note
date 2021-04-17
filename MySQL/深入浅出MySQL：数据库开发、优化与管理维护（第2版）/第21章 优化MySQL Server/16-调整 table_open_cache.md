

每一个SQL执行线程至少都要打开1个表缓存，参数table_open_cache控制所有SQL执行线程可打开表缓存的数量。这个参数的值应根据最大连接数 max_connections 以及每个连接执行关联查询中所涉及表的最大个数（用N表示）来设定：



![figure_0383_0182.jpg](../images/figure_0383_0182.jpg)
在未执行 flush tables命令的情况下，如果MySQL状态变量 opened_tables的值较大，就说明table_open_cache设置得太小，应适当增大。增大table_open_cache的值，会增加MySQL对文件描述符的使用量，因此，也要注意评估open-files-limit的设置是否够用。



