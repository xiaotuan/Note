### 
  2.6 MySQL存储引擎


<img class="my_markdown" class="h-pic" src="../images/Figure-0064-69.jpg" style="width:87px;  height: 86px; "/> 本节视频教学录像：2分钟

存储引擎是MySQL中一个重要的组成部分。MySQL提供了多个不同的存储引擎，包括处理事务安全表的引擎和处理非事务安全表的引擎。在MySQL中，不需要在整个服务器中使用同一种引擎，应该针对具体的要求，对每一个表使用不同的存储引擎。

MySQL 5.6支持的存储引擎有InnoDB、MyISAM、Memory、Merge、Archive、Federated、CSV、BLACKHOLE等。其中InnoDB是支持事务型的存储引擎，从MySQL 5.5之后，InnoDB就是MySQL的默认事务引擎。InnoDB支持事务安全表（ACID）,也支持行锁定和外键。InnoDB 为 MySQL 提供了具有事务(transaction)、回滚(rollback)和崩溃修复能力(crash recovery capabilities)、多版本并发控制(multi-versioned concurrency control)的事务安全(transaction-safe (ACID compliant))型表。

关于MySQL存储引擎的详细介绍以及如何选择存储引擎，在第4章会有详细讲解。

