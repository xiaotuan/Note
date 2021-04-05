### 18.5.1　连接到IMAP服务器

就像你需要一个 `SMTP` 对象连接到SMTP服务器并发送电子邮件一样，你也需要一个 `IMAPClient` 对象连接到IMAP服务器并接收电子邮件。首先，你需要电子邮件服务提供商的IMAP服务器域名。这和SMTP服务器的域名不同。表18-2列出了几个流行的电子邮件服务提供商的IMAP服务器。

<center class="my_markdown"><b class="my_markdown">表18-2　电子邮件提供商及其IMAP服务器</b></center>

| 提供商 | IMAP服务器域名 |
| :-----  | :-----  | :-----  | :-----  |
| Gmail* | imap.gmail.com |
| Outlook/Hotmail * | imap-mail.outlook.com |
| Yahoo Mail* | imap.mail.yahoo.com |
| AT&T | imap.mail.att.net |
| Comcast | imap.comcast.net |
| Verizon | incoming.verizon.net |

*附加的安全措施让Python无法使用 `imapclient` 模块登录这些服务器。

得到IMAP服务器域名后，调用 `imapclient.IMAPClient()` 函数来创建一个 `IMAPClient` 对象。大多数电子邮件提供商要求SSL加密，传入 `ssl=True` 关键字参数。在交互式环境中输入以下代码（使用你的提供商的域名）：

```javascript
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap. ', ssl=True)
```

在接下来的小节里所有交互式环境的例子中， `imapObj` 变量将包含 `imapclient. IMAPClient()` 函数返回的 `IMAPClient` 对象。在这里，客户端是连接到服务器的对象。

