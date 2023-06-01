[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

修改 `sys/vendor/mediatek/proprietary/packages/apps/FMRadio/src/com/android/fmradio/FmMainActivity.java` 文件中 `onPrepareOptionsMenu()` 方法中如下代码：

```diff
@@ -906,6 +906,10 @@ public class FmMainActivity extends Activity implements FmFavoriteEditDialog.Edi
                 : R.drawable.btn_fm_headset_selector);
         mMenuItemHeadset.setTitle(isSpeakerUsed ? R.string.optmenu_speaker
                 : R.string.optmenu_earphone);
+        // Hide Stereo and Mono menu by qty {{&&
+        mMenuItemRdStereo.setVisible(false);
+        mMenuItemRdMono.setVisible(false);
+        // &&}}
         return true;
     }

```

