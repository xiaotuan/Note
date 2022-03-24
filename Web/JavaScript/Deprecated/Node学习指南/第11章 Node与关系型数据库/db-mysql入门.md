这一章中，我会通过两种不同的方法来将关系型数据库 `MySQL` 整合到我们的 `Node` 应用程序中。一种方法是使用 `mysql (node-mysql)`，它是一个较为流行的 JavaScript MySQL 客户端；另一种方法是使用 `db-mysql`，它是 node-db （Node 尝试构建的一个通用数据库引擎）的一部分。

这两个模块目前都不支持事务操作（不知最新版是否支持）。但是，通过使用 mysql-series 模块，我们可以为 node-mysql 添加类似的功能。另外，我们还会对 Sequelize 做个简单介绍，它是一个基于 MySQL 数据库的 ORM（对象——关系映射）库。

在使用 db-mysql 之前，我要先安装 `MySQLclient` 库。你可以在 <http://nodejsdb.org/db-mysql/> 找到安装包和安装说明。

