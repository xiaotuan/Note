### 18.1　使用Gmail API发送和接收电子邮件

由于额外的安全和反垃圾邮件措施，因此通过 `ezgmail` 模块控制Gmail账户比本章后面讨论的 `smtplib` 和 `imapclient` 更容易。 `ezgmail` 是我写的一个模块，它基于官方Gmail API，并提供了一些功能，使人们可以轻松地从Python中使用Gmail。你可以在GitHub找到关于 `ezgmail` 的完整细节。 `ezgmail` 不是由Google制作的，也不附属于Google。

要安装 `ezgmail` ，在Windows操作系统上运行 `pip install--user--upgrade ezgmail` （或在macOS和Linux操作系统上使用pip3）。 `--upgrade` 选项将确保你安装最新版本的软件包，与Gmail API这样一个不断变化的在线服务交互，这是非常有必要的。

