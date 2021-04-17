

当面对一个有 SQL 性能问题的数据库时，我们应该从何处入手来进行系统的分析，使得能够尽快定位问题SQL并尽快解决问题，本节将向读者介绍这个过程。

本章所有涉及的案例表都包括在MySQL的案例库sakila上，sakila是一个MySQL官方提供的模拟电影出租厅信息管理系统的数据库，类似Oracle提供的scott库，sakila库的下载地址为***http://downloads.mysql.com/docs/sakila-db.zip。***

压缩包包括3个文件：sakila-schema.sql、sakila-data.sql和sakila.mwb，分别是sakila库的表结构创建、数据灌入、sakila的MySQL Workbench数据模型（可以在MySQL工作台打开查看数据库模型）。



