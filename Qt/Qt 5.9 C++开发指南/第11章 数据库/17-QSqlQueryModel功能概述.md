### 11.3.1　QSqlQueryModel功能概述

从图11-2的SQL数据模型类的继承关系看，QSqlQueryModel是QSqlTableModel的父类。QSqlQueryModel封装了执行SELECT语句从数据库查询数据的功能，但是QSqlQueryModel只能作为只读数据源使用，不可以编辑数据。

QSqlQueryModel类的主要接口函数见表11-10（省略了函数中的const关键字和缺省参数）。

<center class="my_markdown"><b class="my_markdown">表11-10　QSqlQueryModel类的主要函数</b></center>

| 接口函数 | 功能描述 |
| :-----  | :-----  | :-----  | :-----  |
| void　clear() | 清除数据模型，释放所有获得的数据 |
| QSqlError　lastError() | 返回上次的错误，可获取错误的类型和文本信息 |
| QSqlQuery　query() | 返回当前关联的QSqlQuery对象 |
| void　setQuery(QSqlQuery &query) | 设置一个QSqlQuery对象，获取数据 |
| void　setQuery(QString &query) | 设置一个SELECT语句创建查询，获取数据 |
| QSqlRecord　record() | 返回一个空记录，包含当前查询的字段信息 |
| QSqlRecord　record(int row) | 返回行号为row的记录 |
| int　rowCount() | 返回查询到的记录条数 |
| int　columnCount() | 返回查询的字段个数 |
| void　setHeaderData(int section, Qt::Orientation orientation, QVariant &value) | 设置表头数据，一般用于设置字段的表头标题 |

使用QSqlQueryModel作为数据模型从数据库里查询数据，只需使用setQuery()函数设置一个SELECT查询语句即可。QSqlQueryModel可以作为QTableView等视图组件的数据源，也可以使用QDataWidgetMapper创建字段与界面组件的映射，只是查询出来的数据是不可编辑的。

