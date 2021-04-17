

MySQL服务器端并不存在共享池的概念，所以在MySQL上使用绑定变量（Bind Variable）最大的好处主要是为了避免SQL注入，增加安全性，以Java语言为例子，同样是根据username来访问user表：

…

Class.forName("com.mysql.jdbc.Driver").newInstance();

String connectionUrl = "jdbc:mysql://localhost:3331/test";

String connectionUser = "test_user";

String connectionPassword = "test_passwd";

conn = DriverManager.getConnection(connectionUrl, connectionUser, conne-ctionPassword);

String sqlStmt = " select * from user where username = ? and password = ?";

System.out.println("Source SQL Statement:" + sqlStmt);

prepStmt = conn.prepareStatement(sqlStmt);

System.out.println("Before Bind Value:" + prepStmt.toString());

prepStmt.setString(1, "angel' or 1=1'");

prepStmt.setString(2, "test");

System.out.println("After Bind Value:" + prepStmt.toString());

rs = prepStmt.executeQuery();

while (rs.next()) {

String ename = rs.getString("username");

String job = rs.getString("password");

System.out.println("username: " + username + ", password: " + password);

}

…

输出日志如下：

Source SQL Statement: select * from user where username = ? and password = ?

Before Bind Value:com.mysql.jdbc.JDBC4PreparedStatement@6910fe28: select * from user where username = ** NOT SPECIFIED ** and password = ** NOT SPECIFIED **

After Bind Value:com.mysql.jdbc.JDBC4PreparedStatement@6910fe28: select * from user where username = 'angel\' or 1=1\'' and password = 'test'

可以注意到，虽然传入的变量中带了“angel' or 1=1'”的条件，企图蒙混过关，但是由于使用了绑定变量（Java驱动中采用PreparedStatement语句来实现），输入的参数中的单引号被正常转义，导致后续的“or 1=1”作为 username条件的内容出现，而不会被作为 SQL的一个单独条件被解析，避免了SQL注入的风险。

同样的，在使用绑定变量的情况下，企图通过注释“/*”或“#”让后续条件失效也是会失败的：

prepStmt.setString(1, "angel '/*");

After Bind Value:com.mysql.jdbc.JDBC4PreparedStatement@6910fe28: select * from user where username = 'angel \'/*' and password = 'test'

prepStmt.setString(1, "angel '#");

After Bind Value:com.mysql.jdbc.JDBC4PreparedStatement@5a9e29fb: select * from user where username = 'angel \'#' and password = 'test'

需要注意，PreparedStatement语句是由JDBC驱动来支持的，在使用PreparedStatement语句的时候，仅仅做了简单的替换和转义，并不是MySQL提供了PreparedStatement的特性。

对Java、JSP开发的应用，可以使用PrepareStatement+Bind-variable来防止SQL注入，另外从PHP 5开始，也在扩展的MySQLI中支持PrepareStatement，所以在使用这类语言作数据库开发时，强烈建议使用PrepareStatement+Bind-variable来实现，下面是PHP的例子：

…

$stmt = $dbh->prepare("SELECT * FROM users WHERE USERNAME = ? AND PASSWORD = ?");

$stmt->execute(array($username, $password));

…



