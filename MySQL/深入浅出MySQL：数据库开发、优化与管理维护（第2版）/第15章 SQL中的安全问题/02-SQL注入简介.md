

结构化查询语言（SQL）是一种用来和数据库交互的文本语言。SQL注入（SQL Injection）就是利用某些数据库的外部接口将用户数据插入到实际的数据库操作语言（SQL）当中，从而达到入侵数据库乃至操作系统的目的。它的产生主要是由于程序对用户输入的数据没有进行严格的过滤，导致非法数据库查询语句的执行。

SQL注入攻击具有很大的危害，攻击者可以利用它读取、修改或者删除数据库内的数据，获取数据库中的用户名和密码等敏感信息，甚至可以获得数据库管理员的权限，而且，SQL注入也很难防范。网站管理员无法通过安装系统补丁或者进行简单的安全配置进行自我保护，一般的防火墙也无法拦截SQL注入攻击。

下面的用户登录验证程序就是SQL注入的一个例子（以PHP程序举例）。

（1）创建用户表user：

CREATE TABLE user (

userid int(11) NOT NULL auto_increment,

username varchar(20) NOT NULL default '',

password varchar(20) NOT NULL default '',

PRIMARY KEY (userid)

) TYPE=MyISAM AUTO_INCREMENT=3 ;

（2）给用户表user添加一条用户记录：

INSERT INTO `user` VALUES (1, 'angel', 'mypass');

（3）验证用户root登录localhost服务器：

<?php

$servername = "localhost";

$dbusername = "root";

$dbpassword = "";

$dbname = "injection";

mysql_connect($servername,$dbusername,$dbpassword) or die ("数据库连接失败");

$sql = "SELECT * FROM user WHERE username='$username' AND password= '$password'";

$result = mysql_db_query($dbname, $sql);

$userinfo = mysql_fetch_array($result);

if (empty($userinfo))

{

echo "登录失败";

} else {

echo "登录成功";

}

echo "<p>SQL Query:$sql<p>";

?>

（4）然后提交如下URL：

http://127.0.0.1/injection/user.php?username=angel' or '1=1

结果发现，这个 URL 可以成功登录系统，但是很显然这并不是我们预期的结果。同样也可以利用SQL的注释语句实现SQL注入，如下面的例子：

http://127.0.0.1/injection/user.php?username=angel'/*

http://127.0.0.1/injection/user.php?username=angel'#

因为在SQL语句中，“/*”或者“#”都可以将后面的语句注释掉。这样上述语句就可以通过这两个注释符中任意一个将后面的语句给注释掉了，结果导致只根据用户名而没有密码的URL都成功进行了登录。利用“or”和注释符的不同之处在于，前者是利用逻辑运算，而后者则是根据MySQL的特性，这个比逻辑运算简单得多了。虽然这两种情况实现的原理不同，但是达到了同样的SQL注入效果，都是我们应该关注的。



