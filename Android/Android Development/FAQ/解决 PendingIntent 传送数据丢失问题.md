问题代码如下：

```java
private void uninstall(String packageName) {
    Intent broadcastIntent = new Intent(BROADCAST_ACTION);
    broadcastIntent.setFlags(Intent.FLAG_RECEIVER_FOREGROUND);
    broadcastIntent.putExtra(EventResultPersister.EXTRA_ID, mUninstallId);
    broadcastIntent.setPackage(getPackageName());
    PendingIntent pendingIntent = PendingIntent.getBroadcast(mContext, mUninstallId,
									broadcastIntent, 
                                    PendingIntent.FLAG_IMMUTABLE);
    PackageInstaller packageInstaller = mContext.getPackageManager().getPackageInstaller();
    packageInstaller.uninstall(packageName, pendingIntent.getIntentSender());
}
```

在接收到 `PendingIntent` 发送广播后，从广播 `Intent` 中得到的数据为空。

可以通过修改 `PendingIntent.getBroadcast()` 方法中的最后一个参数 `flag` 来解决：

+ `FLAG_CANCEL_CURRENT`：如果该 `PendingIntent` 已经存在，则在生成新的之前取消当前的。
+ `FLAG_NO_CREATE`：如果该 `pendingIntent` 不存在，直接返回 null 而不是创建一个 `PendingIntent`。
+ `FLAG_ONE_SHOT`：该 `PendingIntent` 只能用一次，在 `send()` 方法执行后，自动取消。
+ `FLAG_UPDATE_CURRENT`：如果该 `PendingIntent` 已经存在，则用新传入的 `Intent` 更新当前的数据。我们需要把最后一个参数改为 `PendingIntent.FLAG_UPDATE_CURRENT`，这样在启动的 `Broadcast` 里就可以接收 `Intent` 传送数据的方法正常接收。

最后修改代码如下：

```java
private void uninstall(String packageName) {
    Intent broadcastIntent = new Intent(BROADCAST_ACTION);
    broadcastIntent.setFlags(Intent.FLAG_RECEIVER_FOREGROUND);
    broadcastIntent.putExtra(EventResultPersister.EXTRA_ID, mUninstallId);
    broadcastIntent.setPackage(getPackageName());
    PendingIntent pendingIntent = PendingIntent.getBroadcast(mContext, mUninstallId,
    			broadcastIntent, 
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_MUTABLE);
    PackageInstaller packageInstaller = mContext.getPackageManager().getPackageInstaller();
    packageInstaller.uninstall(packageName, pendingIntent.getIntentSender());
}
```

