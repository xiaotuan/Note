你需要获得包含了你所使用的数据库的驱动程序的 `JAR` 文件。

+ **PostgreSQL**：<https://jdbc.postgresql.org/download/>
+ **Derby**：<https://db.apache.org/derby/derby_downloads.html>（数据库安装目录下的 `lib/derbyclient.jar` 文件
+ **MySQL**：<https://central.sonatype.com/artifact/mysql/mysql-connector-java/8.0.32/versions>

在运行访问数据库的程序时，需要将驱动程序的 `JAR` 文件包括到类路径中（编译时并不需要这个 `JAR` 文件）。

在从命令行启动程序时，只需要使用下面的命令：

```shell
java -classpath driverPath:. -jar ProgramName.jar
```

