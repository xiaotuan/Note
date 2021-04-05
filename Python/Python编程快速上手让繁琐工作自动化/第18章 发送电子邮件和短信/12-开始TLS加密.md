### 18.3.3　开始TLS加密

如果要连接到SMTP服务器的587端口（即使用TLS加密），那么接下来需要调用 `starttls()` 方法。这是为连接实现加密必需的步骤。如果要连接到465端口（使用SSL），加密已经设置好了，你应该跳过这一步。

下面是 `starttls()` 方法调用的例子：

```javascript
>>> smtpObj.starttls()
(220, b'2.0.0 Ready to start TLS')
```

`starttls()` 让SMTP连接处于TLS模式。返回值220告诉你，该服务器已准备就绪。

