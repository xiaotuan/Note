

### 7.2.3　Crypto模块

Node提供了用于加密的模块Crypto，它提供了可以使用OpenSSL功能的接口，包括对OpenSSL的散列算法、HMAC、加密、解密、签名和验证功能的封装。这个Node组件使用起来相当简单，但是有一个非常重要的前提，即开发人员需要知道并了解OpenSSL及其所有功能。

> <img class="my_markdown" src="../images/83.png" style="zoom:50%;" />
> **熟悉OpenSSL**
> 我强烈建议你在使用Node的Crypto模块之前先花时间熟悉一下OpenSSL。你可以浏览OpenSSL的文档，还可以获取一本免费的关于OpenSSL的图书，就是Ivan Ristić所著的OpenSSL Cookbook。

我将使用OpenSSL的hash功能来创建一个密码散列，借此来直观地讲解Crypto模块的用法。同样的功能也可以用来创建校验和，以确保存储或传输中的数据不被损坏。

> <img class="my_markdown" src="../images/84.png" style="zoom:50%;" />
> **MySQL**
> 本节的示例使用了MySQL。有关本节使用的node-mysql模块的更多信息，请参阅该模块的GitHub代码库。如果你无法访问MySQL，则可以将用户名、密码和盐值（salt）存储在本地文件中，并相应地修改代码。

你可以使用Crypto模块的 `createHash` 方法来创建用于存储在数据库中的密码散列。如下例所示，它使用 `sha1` 算法创建散列，使用散列来对密码进行编码，然后将编码结果提取为数据摘要存储在数据库中：

```python
var hashpassword = crypto.createHash('sha1')
                                 .update(password)
                                 .digest('hex');
```

数据摘要会被转化为十六进制编码。默认情况下编码是二进制的，也可以转化为base64编码。

> <img class="my_markdown" src="../images/85.png" style="zoom:50%;" />
> **加密密码或存储散列**
> 存储密码的密文比存储明文要好一些，但是如果有人或者机构掌握了加密的密钥，那么密码还是会被破解的。所以将密码的散列存储起来是一种更安全的方式，虽然这个过程是不可逆的。如果用户忘记了密码，系统会允许他们重置密码，而不是恢复密码。

许多应用程序都使用散列来达到此目的。但是，在数据库中存储密码的散列明文也存在问题，引发问题的正是名字听起来完全无害的彩虹表。

简单来说，彩虹表是一个很简单的表，表中存储着所有可能出现的字符组合的散列值。所以即使你有一个自我感觉绝对不会被破解的密码——说实话，我们一般没有这种自信——那么很可能你的密码在彩虹表中有所对应，而这会使得它更容易被破解。

避免被彩虹表破解的方式是使用盐值（不，不是食用盐）。盐值指的是在加密之前在密码上追加的一个值。可以对所有密码使用同一个盐值，并将其安全地存储在服务器上。然而，为每个用户密码生成唯一的盐值，然后将其与密码一起存储，则是一种更好的实践。诚然，密码的密文被盗的同时，盐值也会被盗，但是破解密码的人必须为这个盐值生成新的彩虹表，这会显著地给破解增加难度。

例7-8是一个简单的程序，它将用户名和密码作为命令行参数传递，生成密码散列，然后将它们作为新用户存储在MySQL数据库表中。我没有选择其他数据库，而使用了MySQL，是因为它的普及程度很高，而且大多数人都很熟悉。

要运行这个示例代码，首先要通过下面的命令安装 `node-mysql` 这个模块：

```python
npm install node-mysql
```

然后使用下面的命令创建表：

```python
CREATE TABLE user (userid INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(userid),
username VARCHAR(400) NOT NULL, passwordhash VARCHAR(400) NOT NULL,
salt DOUBLE NOT NULL );
```

盐值是由日期值乘以一个随机数，然后四舍五入得到的。先将密码和它拼接，然后对密码进行散列运算。最后，所有的用户数据都被插入MySQL用户表中。

**例7-8　使用Crypto的createHash方法和盐值来对密码加密**

```python
var mysql = require('mysql'),
    crypto = require('crypto');
var connection = mysql.createConnection({
   host: 'localhost',
   user: 'username',
   password: 'userpass'
  });
connection.connect();
connection.query('USE nodedatabase');
var username = process.argv[2];
var password = process.argv[3];
var salt = Math.round((Date.now() * Math.random())) + '';
var hashpassword = crypto.createHash('sha512')
                   .update(salt + password, 'utf8')
                   .digest('hex');
// create user record
connection.query('INSERT INTO user ' +
   'SET username = ?, passwordhash = ?, salt = ?
   [username, hashpassword, salt], function(err, result) {
      if (err) console.error(err);
      connection.end();
});
```

我们来看看这段代码，首先与数据库建立连接，然后选择包含新创建的表的数据库。从命令行获取用户名和密码后，就可以开始神奇的加密过程了。

我们生成了盐值并将其传递到函数中，以便使用 `sha512` 算法创建散列。创建散列函数之后，使用盐值更新密码散列的函数并设置散列编码的函数为连续调用，就可以创建散列了。最后将加密的密码散列与用户名一起插入到新创建的表中。

例7-9是一个测试用户名和密码的应用程序，它根据用户名来查询数据库中的密码散列和盐值。它使用盐值再次生成散列。重新创建密码散列后，将其与存储在数据库中的密码进行比较。如果两者不相等，则验证不通过。如果相等，那么用户就登录成功了。

**例7-9　验证用户名和密码**

```python
var mysql = require('mysql'),
    crypto = require('crypto');
var connection = mysql.createConnection({
   user: 'username',
   password: 'userpass'
   });
connection.query('USE nodedatabase');
var username = process.argv[2];
var password = process.argv[3];
connection.query('SELECT password, salt FROM user WHERE username = ?',
   [username], function(err, result, fields) {
   if (err) return console.error(err);
   var newhash = crypto.createHash('sha512')
                 .update(result[0].salt + password, 'utf8')
                 .digest('hex');
   if (result[0].password === newhash) {
      console.log("OK, you're cool");
   } else {
      console.log("Your password is wrong. Try again.");
   } 
   connection.end();
});
```

让我们来测试一下程序，首先输入用户名 `Michael` 、密码 `apple*frk13*` 来创建用户：

```python
node password.js Michael apple*frk13*
```

然后，我们用同样的用户名和密码来检测用户是否存在：

```python
node check.js Michael apple*frk13*
```

这时我们会得到用户存在的结果：

```python
OK, you're cool
```

如果我们使用了错误的密码：

```python
node check.js Michael badstuff
```

我们就会得到密码错误的提示：

```python
Your password is wrong. Try again
```

加密散列也可以用在流中。以校验和为例，这是一个用于确定数据是否已成功发送的算法。你可以为文件创建散列，并在发送文件时将其与文件一起发送。下载文件的人可以使用散列来验证传输的准确性。以下代码使用 `pipe()` 函数和 `Crypto` 函数的双工性来创建这样的散列。

```python
var crypto = require('crypto');
var fs = require('fs');
var hash = crypto.createHash('sha256');
hash.setEncoding('hex');
var input = fs.createReadStream('main.txt');
var output = fs.createWriteStream('mainhash.txt');
input.pipe(hash).pipe(output);
```

你也可以用 `md5` 算法来产生一个MD5校验和。这种方法因其速度快而被广泛应用，虽然它可能不太安全。

```python
var hash = crypto.createHash('md5');
```



