### 18.5.2　登录到IMAP服务器

取得 `IMAPClient` 对象后，调用它的 `login()` 方法，传入用户名（这通常是你的电子邮件地址）和口令字符串。

```javascript
>>> imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
'my_email_address@example.com 
Jane Doe authenticated (Success)'
```



**警告：**
要记住，永远不要直接在代码中写入口令！应该让程序从 `input()` 接收输入的口令。



如果IMAP服务器拒绝用户名/口令的组合，Python会抛出 `imaplib.error` 异常。

