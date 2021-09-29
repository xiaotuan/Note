[toc]

### 1. 创建访问 MySQL 数据库的 URL

访问 MySQL 数据库的 URL 的格式如下所示：

```
jbdc:mysql://主机名:端口号/数据库名称?user=用户名&password=用户密码
```

例如：

```java
// 连接数据库的 URL，格式为："jdbc:mysql://数据库IP:数据库端口号/数据库名称?user=MySQL登录账号&password=MySQL登录密码"
String url = "jdbc:mysql://" + host + ":" + port + "/" + db + "?user="
				+ user + "&password=" + pass;
```

### 2. 获取 MySQL 驱动

```java
// 获取 MySQL 驱动
Class.forName("com.mysql.cj.jdbc.Driver");
```

### 3. 连接数据库

```java
// 连接数据库
conn = DriverManager.getConnection(url);
```

### 4. 构建执行语句

```java
// 数据查询语句
String sql = "SELECT * FROM actor";
// 构建查询语句对象
PreparedStatement stmt = conn.prepareStatement(sql);
```

### 5. 执行语句

```java
// 执行查询语句
ResultSet rs = stmt.executeQuery();
```

### 6. 获取执行结果

```java
while (rs.next()) {
    System.out.printf("| %-14s| %-14s| %-20s |\n", rs.getString("first_name"), rs.getString("last_name"), rs.getString("last_update"));
}
```

### 7. 关闭连接

```java
// 关闭数据库连接
conn.close();
```

### 8. 完整的示例代码

```java
package com.qty.test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Enumeration;
import java.util.Hashtable;

public class DevApiSample {
	
	public static void main(String[] args) {		
		Connection conn = null;
		// 数据库 IP 地址
		String host = "127.0.0.1";
		// 数据库端口
		int port = 3306;
		// 要访问的数据库
		String db = "sakila";

		// MySQL 数据库登录账号
		String user = "root";
		// MySQL 数据库登录密码
		String pass = "root";

		// 连接数据库的 URL，格式为："jdbc:mysql://数据库IP:数据库端口号/数据库名称?user=MySQL登录账号&password=MySQL登录密码"
		String url = "jdbc:mysql://" + host + ":" + port + "/" + db + "?user="
				+ user + "&password=" + pass;
		// 数据查询语句
		String sql = "SELECT * FROM actor";

		try {
			// 获取 MySQL 驱动
			Class.forName("com.mysql.cj.jdbc.Driver");
			// 连接数据库
			conn = DriverManager.getConnection(url);

			// 构建查询语句对象
			PreparedStatement stmt = conn.prepareStatement(sql);
			// 执行查询语句
			ResultSet rs = stmt.executeQuery();
			Hashtable<String, String> details = new Hashtable<String, String>();
			System.out.println("+---------------+---------------+----------------------+");
			System.out.printf("| FirstName     | LastName      | LastUpdate           |\n");
			while (rs.next()) {
				details.put(rs.getString("first_name"), rs.getString("last_name"));
				System.out.println("+---------------+---------------+----------------------+");
				System.out.printf("| %-14s| %-14s| %-20s |\n", rs.getString("first_name"), rs.getString("last_name"), rs.getString("last_update"));
			}
			System.out.println("+---------------+---------------+----------------------+");
			String[] names = new String[details.keySet().size()];
			int x = 0;
			for (Enumeration<String> e = details.keys(); e.hasMoreElements();) {
				names[x] = e.nextElement();
				x++;
			}
			// 关闭数据库连接
			conn.close();
		} catch (ClassNotFoundException e) {
			System.out.println("Class not found!");
		} catch (SQLException e) {
			System.out.println("SQL Exception " + e.getMessage());
		}
    }

}
```

> 注意：要在 Eclipse 上执行上面的程序，需要在该工程下的 module-info.java 文件中添加如下代码：
>
> ```java
> module MySQLTest {
> 	requires mysql.connector.java;
> 	requires java.sql;
> }
> ```

