### 11.4.1　QSqlQuery基本用法

QSqlQuery是能执行任意SQL语句的类，如SELECT、INSERT、UPDATE、DELETE等，QSqlQuery类的一些常用函数见表11-11（省略函数中的const关键字，省略缺省参数，不同参数的同名函数一般只给出一种参数形式）。

<center class="my_markdown"><b class="my_markdown">表11-11　QSqlQuery类的主要函数</b></center>

| 接口函数 | 功能描述 |
| :-----  | :-----  | :-----  | :-----  |
| bool　prepare(QString &query) | 设置准备执行的SQL语句，一般用于带参数的SQL语句 |
| void　bindValue(QString &placeholder, QVariant &val) | 设置SQL语句中参数的值，以占位符表示参数 |
| void　exec() | 执行由prepare()和bindValue()设置的SQL语句 |
| void　exec(QString &query) | 直接执行一个不带参数的SQL语句 |
| bool　isActive() | 如果成功执行了exec()函数，就返回true |
| bool　isSelect() | 如果执行的SQL语句是SELECT语句，就返回true |
| QSqlRecord　record() | 返回当前记录 |
| QVariant　value(QString &name) | 返回当前记录名称为name的字段的值 |
| bool　isNull(QString &name) | 判断一个字段是否为空，当query非活动、未定位在有效记录、无此字段或字段为空时都返回true |
| int　size() | 对于SELECT语句，返回查询到的记录条数，其他语句返回-1 |
| int　numRowsAffected() | 返回SQL语句影响的记录条数，对于SELECT语句无定义 |
| bool　first() | 定位到第一条记录，isActive和isSelect都为true时才有效 |
| bool　previous() | 定位到上一条记录，isActive和isSelect都为true时才有效 |
| bool　next() | 定位到下一条记录，isActive和isSelect都为true时才有效 |
| bool　last() | 定位到最后一条记录，isActive和isSelect都为true时才有效 |
| bool　seek(int index) | 定位到指定序号的记录 |
| int　at() | 返回当前记录的序号 |

使用QSqlQuery执行不带参数的SQL语句时可以用exec(QString)函数，如：

```css
QSqlQuery query;
query.exec("SELECT * FROM employee");
query.exec("UPDATE employee SET Salary=3000 where Gender='女' ");
```

使用带参数的SQL语句时，先用prepare()函数准备SQL语句，然后用bindValue()函数设置参数值，再用exec()执行SQL语句，如：

```css
QSqlQuery query;
query.prepare ("SELECT * FROM employee where EmpNo=:ID");
query.bindValue(":ID", 2003);
query.exec();
```

上面是SQL语句中的参数用“冒号+参数名”表示的形式，还可以直接用占位符来表示参数，如：

```css
QSqlQuery query;
query.prepare ("UPDATE employee SET Name=?, Gender=?, Height=? where EmpNo=?");
query.bindValue(0, "高某某");
query.bindValue(1, "男");
query.bindValue(2, 1.78);
query.bindValue(3,2010);
query.exec();
```

