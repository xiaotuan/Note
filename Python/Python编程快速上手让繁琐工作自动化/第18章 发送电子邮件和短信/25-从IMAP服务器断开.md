### 18.5.8　从IMAP服务器断开

如果程序已经完成了获取和删除电子邮件任务，就调用 `IMAPClient` 的 `logout()` 方法从IMAP服务器断开连接：

```javascript
>>> imapObj.logout()
```

如果程序运行了几分钟或更长时间，IMAP服务器可能会超时或自动断开。在这种情况下，接下来程序对 `IMAPClient` 对象的方法调用会抛出异常，像下面这样：

```javascript
imaplib.abort: socket error: [WinError 10054] An  existing connection was
forcibly closed by the remote host
```

在这种情况下，程序必须调用 `imapclient.IMAPClient()` ，来再次连接服务器。

你现在有办法让Python程序登录到一个电子邮件账户，并获取电子邮件。需要回忆所有步骤时，你可以随时参考18.5节“用IMAP获取和删除电子邮件”。

