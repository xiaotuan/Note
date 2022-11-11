简单的说，用于操作数据库的对象有：

+ `SqlConnection`：用于建立到 `SQL Server` 数据源的连接。
+ `DataSet`：数据在内存中的表示。使用 `DataSet` 有多种方法，如通过 `DataTables`。
+ `DataTable`：存储数据结果集，用于操作和导航。
+ `DataAdapter`：用于填充 `DataReader`。

除 `DataTable` 外，所有 `ADO.NET` 对象都位于命名空间 `System.Data` 中；`DataTable` 位于命名空间 `System.XML` 中。