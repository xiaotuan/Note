[toc]

### 1. MTK

#### 1.1 Android 12

##### 1.1.1 MT8788

修改 `device/mediatek/mt6771/mtk_platform_codecs_config.xml` 文件如下代码：

```diff
@@ -52,14 +52,17 @@
         <Video name="c2.mtk.h263.encoder"
                type="video/3gpp"
                driverIntf="proprietary"
-               maxConcurrentInstances="16" />
+               maxConcurrentInstances="16"
+                          canSwapWidthHeight="true" />
         <Video name="c2.mtk.mpeg4.encoder"
                type="video/mp4v-es"
                driverIntf="proprietary"
-               maxConcurrentInstances="16" />
+               maxConcurrentInstances="16"
+                          canSwapWidthHeight="true" />
         <Video name="c2.mtk.avc.encoder"
                type="video/avc"
                driverIntf="proprietary"
-               maxConcurrentInstances="16" />
+               maxConcurrentInstances="16"
+                          canSwapWidthHeight="true" />
     </Encoders>
 </MediaCodecs>
```

