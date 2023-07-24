1. 进入下载页面 <http://dev.mysql.com/downloads/mysql/>，下载 `RPM` 包。

2. 从 `RPM` 列表中选择要下载安装的包，单击 【Download】 按钮，开始下载安装文件。

3. 下载完成后，解压下载的 `tar` 包。

   ```shell
   # tar -xvf MySQL-8.0.13-1.rhel5.i386.tar
   ```

   解压出来的文件有 6 个：

   （1）`MySQL-client-8.0.13-1.rhel5.i386.rpm` 是客户端的安装包。

   （2）`MySQL-server-8.0.13-1.rhel5.i386.rpm` 是服务端的安装包。

   （3）`MySQL-devel-8.0.13-1.rhel5.i386.rpm` 是包含开发用的库头文件安装包。

   （4）`MySQL-shared-8.0.13-1.rhel5.i386.rpm` 是包含 `MySQL` 的一些共享库文件的安装包。

   （5）`MySQL-test-8.0.13-1.rhel5.i386.rpm` 是一些测试的安装包。

   （6）`MySQL-embedded-8.0.13-1.rhel5.i386.rpm` 是嵌入式 `MySQL` 的安装包。

   一般情况下，只需要安装 `client` 和 `server` 两个包，如果需要进行 `C/C++ MySQL` 相关开发，请安装 `MySQL-devel-8.0.13-1.rhel5.i386.rpm`。

4. 切换到 `root` 用户

   ```shell
   $ su - root
   ```

   或

   ```shell
   $ su -
   ```

5. 安装 `MySQL Server 8.0`

   ```shell
   # rpm -ivh MySQL-server-8.0.13-1.rhel5.i386.rpm
   ```

    > 注意：安装之前要查看机器上是否已经装有旧版的 `MySQL`。如果有，最好先把旧版 `MySQL` 卸载，否则可能会产生冲突。查看旧版 `MySQL` 的命令是：
    >
    > ```shell
    > # rpm -qa | grep -i mysql
    > mysql-5.0.77-4.el5_4.2
    > ```
    >
    > 然后，卸载 `mysql-5.0.77-4.el5_4.2` 命令如下：
    >
    > ```shell
    > # rpm -ev mysql-5.0.77-4.el5_4.2			
    > ```

6. 启动服务，输入命令如下：

   ```shell
   # service mysql restart
   ```

   > 注意：从 `MySQL 5.0` 开始，`MySQL` 的服务名改为 `mysql`，而不是 4.* 的 `mysqld`。

   `MySQL` 服务的操作命令是：

   ```
   service mysql start | stop | restart | status
   ```

   
