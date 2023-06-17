1. 安装 `MySQL` 服务器

   ```shell
   sudo apt-get install mysql-server
   ```

2. 安装 `MySQL` 客户端

   ```shell
   sudo apt-get install mysql-client
   ```

3. 配置 `MySQL`（非必需）

   运行 `MySQL` 初始化安全脚本：

   ```shell
   sudo mysql_secure_installation
   ```

   `mysql_secure_installation` 脚本设置的东西：更改 `root` 密码、移除`MySQL` 的匿名用户、禁止 `root` 远程登录、删除 `test` 数据库和重新加载权限。除了询问是否要更改 `root` 密码时，看情况是否需要更改，其余的问题都可以按 <kbd>Y</kbd>，然后 <kbd>ENTER</kbd> 接受所有后续问题的默认值。使用上面的这些选项可以提高 `MySQL` 的安全。