[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

这是谷歌设计的，会预留一部分存储空间，为防止内部存储被拷贝满而影响手机正常使用。具体预留空间设置代码在 `frameworks/base/core/java/android/os/storage/StorageManager.java` 文件的 `getStorageLowBytes()`：

```java
public long getStorageLowBytes(File path) {
    final long lowPercent = Settings.Global.getInt(mResolver,
                                                   Settings.Global.SYS_STORAGE_THRESHOLD_PERCENTAGE, DEFAULT_THRESHOLD_PERCENTAGE);
    final long lowBytes = (path.getTotalSpace() * lowPercent) / 100;

    final long maxLowBytes = Settings.Global.getLong(mResolver,
                                                     Settings.Global.SYS_STORAGE_THRESHOLD_MAX_BYTES, DEFAULT_THRESHOLD_MAX_BYTES);

    return Math.min(lowBytes, maxLowBytes);
}
```

可以通过修改 DEFAULT_THRESHOLD_PERCENTAGE 的值来调整预留空间的大小：

```java
private static final int DEFAULT_THRESHOLD_PERCENTAGE = 5;
```

