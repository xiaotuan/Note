#### 
  4.3.4 MEMORY存储引擎


MEMORY存储引擎将表中的数据存储到内存中，为查询和引用其他表数据提供快速访问。MEMORY主要特性如下。

⑴MEMORY表的每个表可以有多达32个索引，每个索引16列，以及500字节的最大键长度。

⑵MEMORY存储引擎执行HASH和BTREE索引。

⑶在一个MEMORY表中可以有非唯一键。

⑷MEMORY表使用一个固定的记录长度格式。

⑸MEMORY不支持BLOB或TEXT列。

⑹MEMORY支持AUTO_INCREMENT列和对可包含NULL值的列的索引。

⑺MEMORY表在所有客户端之间共享（就像其他任何非TEMPORARY表）。

⑻MEMORY表内容被存在内存中，内存是MEMORY表和服务器在查询处理时的空闲中创建的内部共享。

⑼当不再需要MEMORY表的内容时，要释放被MEMORY表使用的内存，应该执行DELETE FROM或TRUNCATE TABLE，或者删除整个表（使用DROP TABLE）。

