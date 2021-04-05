### 18.4　IMAP

正如SMTP是用于发送电子邮件的协议，因特网消息访问协议（IMAP）规定了如何与电子邮件服务提供商的服务器通信，取回发送到你的电子邮件地址的电子邮件。Python带有一个 `imaplib` 模块，但实际上第三方的 `imapclient` 模块更好用。本章介绍了如何使用 `imapclient` 。

`imapclient` 模块从IMAP服务器下载电子邮件，格式相当复杂。你很可能希望将它们从这种格式转换成简单的字符串。 `pyzmail` 模块可以替你完成解析这些邮件的辛苦工作。

在Windows操作系统上用 `pip install --user -U imapclient==2.1.0` 和 `pip install --user -U pyzmail36==1.0.4` （或在macOS和Linux操作系统上用 `pip3` ），从命令行窗口安装 `imapclient` 和 `pyzmail` 。附录A包含了安装第三方模块的步骤。

