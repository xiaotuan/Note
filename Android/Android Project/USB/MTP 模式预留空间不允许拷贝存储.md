[toc]

### 1. MTK

#### 1.1 MTK8768

##### 1.1.1 Android S

修改 `frameworks/av/media/mtp/MtpStorage.cpp` 文件的如下代码：

```diff
@@ -72,7 +72,7 @@ uint64_t MtpStorage::getFreeSpace() {
     struct statfs   stat;
     if (statfs(getPath(), &stat))
         return -1;
-    return (uint64_t)stat.f_bavail * (uint64_t)stat.f_bsize;
+    return (uint64_t)stat.f_bavail * (uint64_t)stat.f_bsize - (200 * 1000 * 1000);
 }
 
 const char* MtpStorage::getDescription() const {
```

> 注意：上面的修改针对所有存储设备，如果需要只针对内部存储需要对其进行过滤。