### 2.3.2　如何保存和恢复Canvas状态

保存（推送）当前状态到堆栈，调用以下函数。

```javascript
context.save()
```

调出最后存储的堆栈恢复画布，使用以下函数。

```javascript
context.restore()
```

