### 18.3.1　连接到SMTP服务器

如果你曾设置过Thunderbird、Outlook或其他程序连接到你的电子邮件账户，你可能熟悉配置SMTP服务器和端口。这些设置因电子邮件提供商的不同而不同，但在网上搜索“<你的提供商> SMTP设置”，应该能找到相应的服务器和端口。

SMTP服务器的域名通常是电子邮件提供商的域名前面加上SMTP。例如，Gmail的 SMTP 服务器是smtp.gmail.com。表 18-1 列出了一些常见的电子邮件提供商及其SMTP服务器（端口是一个整数值，几乎总是587，该端口由命令加密标准TLS使用）。

<center class="my_markdown"><b class="my_markdown">表18-1　电子邮件提供商及其SMTP服务器</b></center>

| 提供商 | SMTP服务器域名 |
| :-----  | :-----  | :-----  | :-----  |
| Gmail* | smtp.gmail.com |
| Outlook/Hotmail | smtp-mail.outlook.com |
| Yahoo Mail* | smtp.mail.yahoo.com |
| AT&T | smpt.mail.att.net（端口465） |
| Comcast | smtp.comcast.net |
| Verizon | smtp.verizon.net（端口465） |

*附加的安全措施让Python无法使用 `smtplib` 模块登录这些服务器。 `ezgmail` 模块可以为Gmail账户绕过这个困难。

得到电子邮件提供商的域名和端口信息后，调用 `smtplib.SMTP()` 创建一个 `SMTP` 对象，并传入域名作为字符串参数，传入端口作为整数参数。 `SMTP` 对象表示与 `SMTP` 邮件服务器的连接，它有一些发送电子邮件的方法。例如，下面的调用创建了一个 `SMTP` 对象，并连接到一个想象的电子邮件服务器：

```javascript
>>> smtpObj = smtplib.SMTP('smtp. ', 587)
>>> type(smtpObj)
<class 'smtplib.SMTP'>
```

输入 `type(smtpObj)` 表明， `smtpObj` 中保存了一个 `SMTP` 对象。你需要这个 `SMTP` 对象，以便调用它的方法登录并发送电子邮件。如果 `smtplib.SMTP()` 调用不成功，你的 `SMTP` 服务器可能不支持 `TLS` 端口587。在这种情况下，你需要利用 `smtplib.SMTP_SSL()` 和465端口来创建 `SMTP` 对象。

```javascript
>>> smtpObj = smtplib.SMTP_SSL('smtp. ', 465)
```



**注意：**
如果没有连接到因特网，Python将抛出 `socket.gaierror: [Errno 11004] getaddrinfo failed` 或类似的异常。



对于你的程序，TLS和SSL之间的区别并不重要。只需要知道你的SMTP服务器使用哪种加密标准，这样就知道如何连接它。在接下来的所有交互式环境示例中， `smtpObj` 变量将包含 `smtplib.SMTP()` 或 `smtplib.SMTP_SSL()` 函数返回的 `SMTP` 对象。

