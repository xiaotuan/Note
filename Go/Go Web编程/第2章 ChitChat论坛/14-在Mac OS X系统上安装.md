### 2.6.2　在Mac OS X系统上安装

要在Mac OS X上安装PostgreSQL，最简单的方法是使用PostgresApp.com提供的Postgres应用：你只需要把网站上提供的zip压缩包下载下来，解压它，然后把 `Postgres.app` 文件拖曳到自己的 `Applications` 文件夹里面就可以了。启动 `Postgres.app` 的方法跟启动其他Mac OS X应用的方法完全一样。 `Postgres.app` 在初次启动的时候会初始化一个新的数据库集群，并为自己创建一个数据库。因为命令行工具 `psql` 也包含在了 `Postgres.app` 里面，所以在设置好正确的路径之后，你就可以使用 `psql` 访问数据库了。设置路径的工作可以通过在你的 `~/.profile` 文件或者 `~/.bashrc` 文件中添加以下代码行来完成<a class="my_markdown" href="['#anchor21']"><sup class="my_markdown">[1]</sup></a>：

```go
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin
```

