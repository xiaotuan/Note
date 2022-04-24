[toc]

### 1. 前提条件

平台：MTK

芯片：MTK8766

Android 版本：Android 12

### 2. 问题现象

一次性拷贝上千个文件至 MTP 目录，电脑拷贝一段时间后，拷贝进度没有变化。打开 MTP 目录后，电脑文件管理器无响应，过了一段时间后设备断开连接，拷贝停止。

### 3. 解决办法

修改 `frameworks/av/media/mtp/MtpFfsHandle.cpp` 文件的如下代码：

```diff
@@ -44,7 +44,7 @@
 namespace {
 
 constexpr unsigned AIO_BUFS_MAX = 128;
-unsigned AIO_BUF_LEN;
+unsigned AIO_BUF_LEN = 16384;
 
 constexpr unsigned FFS_NUM_EVENTS = 5;
 
@@ -96,7 +96,8 @@ int MtpFfsHandle::getPacketSize(int ffs_fd) {
 MtpFfsHandle::MtpFfsHandle(int controlFd) {
     mControl.reset(controlFd);
     mBatchCancel = android::base::GetBoolProperty("sys.usb.mtp.batchcancel", false);
-    AIO_BUF_LEN = getTotalMemory() > (1 * 1024 * 1024 * 1024) ? 64512 : 16384;
+    // AIO_BUF_LEN = getTotalMemory() > (1 * 1024 * 1024 * 1024) ? 64512 : 16384;
+    AIO_BUF_LEN = 16384;
     MAX_FILE_CHUNK_SIZE = AIO_BUFS_MAX * AIO_BUF_LEN;
 }
```

