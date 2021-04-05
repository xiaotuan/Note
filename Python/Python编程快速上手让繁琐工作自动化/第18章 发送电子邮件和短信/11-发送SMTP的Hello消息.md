### 18.3.2　发送SMTP的“Hello”消息

得到 `SMTP` 对象后，调用它的 `ehlo()` 方法以向SMTP电子邮件服务器“打招呼”。这种问候是SMTP中的第一步，对于建立到服务器的连接是很重要的。你不需要知道这些协议的细节，只要确保得到 `SMTP` 对象后，第一件事就是调用 `ehlo()` 方法，否则以后的方法调用会导致错误。下面是一个 `ehlo()` 调用和返回值的例子：

```javascript
>>> smtpObj.ehlo()
(250, b'mx.    at   your   service,   [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
```

如果在返回的元组中，第一项是整数 `250` （SMTP中“成功”的代码），那么问候成功了。

