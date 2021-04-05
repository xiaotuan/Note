### 18.3.6　从SMTP服务器断开

确保在完成发送电子邮件时，调用 `quit()` 方法，这让程序从SMTP服务器断开：

```javascript
>>> smtpObj.quit()
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
```

返回值221表示会话结束。

要复习连接和登录服务器、发送电子邮件和断开的所有步骤，请参阅18.3节“发送电子邮件”。

