#### 
  4.3.1 MySQL5.6所支持的存储引擎


MySQL提供了多个不同的存储引擎，包括处理事务安全表的引擎和处理非事务安全表的引擎。在MySQL中，不需要在整个服务器中使用同一种存储引擎，针对具体要求，可以对每一个表使用不同的存储引擎。MySQL 5.6支持的存储引擎有：InnoDB，MyISAM，Memory，Merge，Archive，Federated，CSV，BLACKHOLE等。可以使用SHOW ENGINES语句查看系统所支持的引擎类型，执行结果如下。

&#13;
    mysql> SHOW ENGINES \G&#13;
    *************************** 1.row ***************************&#13;
    Engine: FEDERATED&#13;
    Support: NO&#13;
    Comment: Federated MySQL storage engine&#13;
    Transactions: NULL&#13;
    XA: NULL&#13;
    Savepoints: NULL&#13;
    *************************** 2.row ***************************&#13;
    Engine: MRG_MYISAM&#13;
    Support: YES&#13;
    Comment: Collection of identical MyISAM tables&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 3.row ***************************&#13;
    Engine: MyISAM&#13;
    Support: YES&#13;
    Comment: MyISAM storage engine&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 4.row ***************************&#13;
    Engine: BLACKHOLE&#13;
    Support: YES&#13;
    Comment: /dev/null storage engine (anything you write to it disappears)&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 5.row ***************************&#13;
    Engine: CSV&#13;
    Support: YES&#13;
    Comment: CSV storage engine&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 6.row ***************************&#13;
    Engine: MEMORY&#13;
    Support: YES&#13;
    Comment: Hash based, stored in memory, useful for temporary tables&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 7.row ***************************&#13;
    Engine: ARCHIVE&#13;
    Support: YES&#13;
    Comment: Archive storage engine&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    *************************** 8.row ***************************&#13;
    Engine: InnoDB&#13;
    Support: DEFAULT&#13;
    Comment: Supports transactions, row-level locking, and foreign keys&#13;
    Transactions: YES&#13;
    XA: YES&#13;
    Savepoints: YES&#13;
    *************************** 9.row ***************************&#13;
    Engine: PERFORMANCE_SCHEMA&#13;
    Support: YES&#13;
    Comment: Performance Schema&#13;
    Transactions: NO&#13;
    XA: NO&#13;
    Savepoints: NO&#13;
    9 rows in set (0.01 sec)&#13;

Support列的值表示某种引擎是否能使用：YES表示可以使用，NO表示不能使用，DEFAULT表示该引擎为当前默认存储引擎。

