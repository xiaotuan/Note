[toc]

### 1. 执行 SQL 语句

在执行 `SQL` 语句之前，首先需要创建一个 `Statement` 对象。要创建 `Statement` 对象，需要使用调用 `DriverManager.getConnection` 方法所获得的 `Connection` 对象。

```java
Statement stat = conn.createStatement();
```

接着，把要执行的 `SQL` 语句放入字符串中，例如：

```java
String command = "UPDATE Books"
    + " SET Price = Price - 5.00"
    + " WHERE Title NOT LIKE '%Introduction%'";
```

然后，调用 `Statement` 接口中的 `executeUpdate` 方法：

```java
stat.executeUpdate(command);
```

 `executeUpdate` 方法将返回受 `SQL` 语句影响的行数，或者对不返回行数的语句返回 0。

`executeUpdate` 方法既可以执行诸如 `INSERT`、`UPDATE`、`DELETE` 之类的操作，也可以执行诸如 `CREATE TABLE` 和 `DROP TABLE` 之类的数据定义语句。但是，执行 `SELECT` 查询时必须使用 `executeQuery` 方法。另外还有一个 `execute` 语句可以执行任意的 `SQL` 语句，此方法通常只用于由用户提供的交互式查询。

`executeQuery` 方法会返回一个 `ResultSet` 类型的对象，可以通过它来每次一行地迭代遍历所有查询结果。

```java
ResultSet rs = stat.executeQuery("SELECT * FROM Books");
```

分析结果集时通常可以使用类似如下的循环语句代码：

```java
while (rs.next()) {
    look at a row of the result set
}
```

结果集中行的顺序是任意排列的。除非使用 `ORDER BY` 子句指定行的顺序，否则不能为行序强加任何意义。

查看每一行时，可能希望知道其中每一列的内容，有许多访问器方法可以用于获取这些信息：

```java
String isbn = rs.getString(1);
double price = rs.getDouble("Price");
```

不同的数据类型有不同的访问器，比如 `getString` 和 `getDouble`。每个访问器都有两种形式，一种接受数字型参数，另一种接受字符串参数。当使用数字型参数时，我们指的是该数字所对应的列。例如，`rs.getString(1)` 返回的是当前行中第一列的值。

> 注意：与数组的索引不同，数据库的列序号是从 1 开始计算的。

当使用字符串参数时，指的是结果集中以该字符串为列名的列。例如，`rs.getDouble("Price")` 返回列名为 `Price` 的列所对应的值。

当 `get` 方法的类型和列的数据类型不一致时，每个 `get` 方法都会进行合理的类型转换。
