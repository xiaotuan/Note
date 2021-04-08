### 2.6.1　在Linux或FreeBSD系统上安装

www.postgresql.org/download为各种不同版本的Linux和FreeBSD都提供了预编译的二进制安装包，用户只需要下载其中一个安装包，然后根据指示进行安装就可以了。比如说，通过执行以下命令，我们可以在Ubuntu发行版上安装Postgres：

```go
sudo apt-get install postgresql postgresql-contrib
```

这条命令除了会安装 `postgres` 包之外，还会安装附加的工具包，并在安装完毕之后启动PostgreSQL数据库系统。

在默认情况下，Postgres会创建一个名为 `postgres` 的用户，并将其用于连接服务器。为了操作方便，你也可以使用自己的名字创建一个Postgres账号。要做到这一点，首先需要登入Postgres账号：

```go
sudo su postgres
```

接着使用 `createuser` 命令创建一个PostgreSQL账号：

```go
createuser –interactive
```

最后，还需要使用 `createdb` 命令创建以你的账号名字命名的数据库：

```go
createdb <YOUR ACCOUNT NAME>
```

