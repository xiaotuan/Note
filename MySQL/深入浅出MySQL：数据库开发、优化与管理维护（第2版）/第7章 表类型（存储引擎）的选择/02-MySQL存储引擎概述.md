Transactions: NO



插件式存储引擎是MySQL数据库最重要的特性之一，用户可以根据应用的需要选择如何存储和索引数据、是否使用事务等。MySQL默认支持多种存储引擎，以适用于不同领域的数据库应用需要，用户可以通过选择使用不同的存储引擎提高应用的效率，提供灵活的存储，用户甚至可以按照自己的需要定制和使用自己的存储引擎，以实现最大程度的可定制性。

MySQL 5.0支持的存储引擎包括MyISAM、InnoDB、BDB、MEMORY、MERGE、EXAMPLE、NDB Cluster、ARCHIVE、CSV、BLACKHOLE、FEDERATED等，其中 InnoDB和BDB提供事务安全表，其他存储引擎都是非事务安全表。

创建新表时如果不指定存储引擎，那么系统就会使用默认存储引擎，MySQL 5.5之前的默认存储引擎是MyISAM，5.5之后改为了InnoDB。如果要修改默认的存储引擎，可以在参数文件中设置default-table-type。查看当前的默认存储引擎，可以使用以下命令：

mysql> show variables like 'table_type';

+---------------+--------+

| Variable_name | Value |

+---------------+--------+

| table_type | MyISAM |

+---------------+--------+

1 row in set (0.00 sec)

可以通过下面两种方法查询当前数据库支持的存储引擎，第一种方法为：

mysql> SHOW ENGINES \G

*************************** 1. row ***************************

Engine: MyISAM

Support: DEFAULT

Comment: Default engine as of MySQL 3.23 with great performance

Transactions: NO

XA: NO

Savepoints: NO

*************************** 2. row ***************************

Engine: MEMORY

Support: YES

Comment: Hash based, stored in memory, useful for temporary tables

XA: NO

Savepoints: NO

*************************** 3. row ***************************

Engine: MRG_MYISAM

Support: YES

Comment: Collection of identical MyISAM tables

Transactions: NO

XA: NO

Savepoints: NO

*************************** 4. row ***************************

Engine: InnoDB

Support: YES

Comment: Supports transactions, row-level locking, and foreign keys

Transactions: YES

XA: YES

Savepoints: YES

*************************** 5. row ***************************

Engine: CSV

Support: YES

Comment: CSV storage engine

Transactions: NO

XA: NO

Savepoints: NO

5 rows in set (0.00 sec)

第二种方法为：

mysql> SHOW VARIABLES LIKE 'have%';

+----------------------------+-------+

| Variable_name | Value |

+----------------------------+-------+

| have_archive | NO |

| have_bdb | NO |

| have_blackhole_engine | NO |

| have_compress | YES |

| have_crypt | YES |

| have_csv | YES |

| have_dlopen | YES |

| have_example_engine | NO |

| have_federated_engine | NO |

| have_geometry | YES |

| have_innodb | YES |

| have_ndbcluster | NO |

| have_openssl| NO|

| have_partitioning| YES |

| have_query_cache| YES |

| have_row_based_replication | YES |

| have_rtree_keys| YES |

| have_symlink| YES |

+----------------------------+-------+

18 rows in set (0.00 sec)

以上两种方法都可以查看当前支持哪些存储引擎，其中Value显示为“DISABLED”的记录表示支持该存储引擎，但是数据库启动的时候被禁用。

在创建新表的时候，可以通过增加ENGINE关键字设置新建表的存储引擎，例如，在下面的例子中，表ai的存储引擎是MyISAM，而country表的存储引擎是InnoDB：

CREATE TABLE ai (

i bigint(20) NOT NULL AUTO_INCREMENT,

PRIMARY KEY (i)

) ENGINE=MyISAM DEFAULT CHARSET=gbk;

CREATE TABLE country (

country_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,

country VARCHAR(50) NOT NULL,

last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

PRIMARY KEY (country_id)

)ENGINE=InnoDB DEFAULT CHARSET=gbk;

也可以使用ALTER TABLE语句，将一个已经存在的表修改成其他的存储引擎。下面的例子介绍了如何将表ai从MyISAM存储引擎修改到InnoDB存储引擎：

mysql> alter table ai engine = innodb;

Query OK, 0 rows affected (0.13 sec)

Records: 0 Duplicates: 0 Warnings: 0

mysql> show create table ai \G

*************************** 1. row ***************************

Table: ai

Create Table: CREATE TABLE 'ai' (

'i' bigint(20) NOT NULL AUTO_INCREMENT,

PRIMARY KEY ('i')

) ENGINE=InnoDB DEFAULT CHARSET=gbk

1 row in set (0.00 sec)

这样修改后，表ai的存储引擎是InnoDB，可以使用InnoDB存储引擎的相关特性。



