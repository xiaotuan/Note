[toc]

### 1. 测试命令

```shell
$ run cts -t CtsWindowManagerDeviceTestCases -m android.server.wm.PinnedStackTests#testPinnedStackInBoundsAfterRotation
```

### 2. 报错信息

```
java.lang.AssertionError
	at org.junit.Assert.fail(Assert.java:86)
	at org.junit.Assert.assertTrue(Assert.java:41)
	at org.junit.Assert.assertTrue(Assert.java:52)
	at android.server.wm.PinnedStackTests.assertPinnedStackActivityIsInDisplayBounds(PinnedStackTests.java:1275)
	at android.server.wm.PinnedStackTests.testPinnedStackInBoundsAfterRotation(PinnedStackTests.java:236)
	at java.lang.reflect.Method.invoke(Native Method)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:52)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
	at org.junit.internal.runners.statements.FailOnTimeout$CallableStatement.call(FailOnTimeout.java:148)
	at org.junit.internal.runners.statements.FailOnTimeout$CallableStatement.call(FailOnTimeout.java:142)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.lang.Thread.run(Thread.java:923)
```

### 3. 解决方法

> 提示：
>
> 参考 [Mediatek eService ALPS05580921](https://eservice.mediatek.com/eservice-portal/issue_manager/update/96024955)

该问题产生于设备竖屏横用导致的。

合入 https://android-review.googlesource.com/c/platform/frameworks/base/+/1659166 修改即可，Patch 内容如下所示：

```diff
diff --git a/packages/SystemUI/src/com/android/systemui/pip/PipBoundsHandler.java b/packages/SystemUI/src/com/android/systemui/pip/PipBoundsHandler.java
index 583953c..5043724 100644
--- a/packages/SystemUI/src/com/android/systemui/pip/PipBoundsHandler.java
+++ b/packages/SystemUI/src/com/android/systemui/pip/PipBoundsHandler.java
@@ -80,6 +80,7 @@
     private int mImeHeight;
     private boolean mIsShelfShowing;
     private int mShelfHeight;
+    private boolean mDefaultLandscape;
 
     private final DisplayController.OnDisplaysChangedListener mDisplaysChangedListener =
             new DisplayController.OnDisplaysChangedListener() {
@@ -87,6 +88,7 @@
         public void onDisplayAdded(int displayId) {
             if (displayId == mContext.getDisplayId()) {
                 mDisplayLayout.set(mDisplayController.getDisplayLayout(displayId));
+                mDefaultLandscape = (mDisplayInfo.logicalWidth > mDisplayInfo.logicalHeight);
             }
         }
     };
@@ -362,9 +364,17 @@
     private void updateDisplayInfoIfNeeded() {
         final boolean updateNeeded;
         if ((mDisplayInfo.rotation == ROTATION_0) || (mDisplayInfo.rotation == ROTATION_180)) {
-            updateNeeded = (mDisplayInfo.logicalWidth > mDisplayInfo.logicalHeight);
+            if (!mDefaultLandscape) {
+                updateNeeded = (mDisplayInfo.logicalWidth > mDisplayInfo.logicalHeight);
+            } else {
+                updateNeeded = (mDisplayInfo.logicalWidth < mDisplayInfo.logicalHeight);
+            }
         } else {
-            updateNeeded = (mDisplayInfo.logicalWidth < mDisplayInfo.logicalHeight);
+            if (!mDefaultLandscape) {
+                updateNeeded = (mDisplayInfo.logicalWidth < mDisplayInfo.logicalHeight);
+            } else {
+                updateNeeded = (mDisplayInfo.logicalWidth > mDisplayInfo.logicalHeight);
+            }
         }
         if (updateNeeded) {
             final int newLogicalHeight = mDisplayInfo.logicalWidth;
```

> 注意：
>
> 合入 Patch 后，cts 测试 pass，但是刷 gsi 测试此项和 daily build gsi (aosp_arm64-img-7261607) fail，这是因为 GSI image 镜像 还没有合入该 Patch 造成的，此项可以豁免的。豁免 ID 为 https://android-review.googlesource.com/c/platform/frameworks/base/+/1659166。