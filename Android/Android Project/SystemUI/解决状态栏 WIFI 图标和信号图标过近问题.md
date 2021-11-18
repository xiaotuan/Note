[toc]

### 1. MTK 平台

#### 1.1 MTK8766、Android R

1. 修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/res/layout/status_bar_wifi_group.xml` 文件：

   ```diff
   @@ -22,6 +22,7 @@
        android:id="@+id/wifi_combo"
        android:layout_width="wrap_content"
        android:layout_height="match_parent"
   +    android:paddingEnd="3dp"
        android:gravity="center_vertical" >
    
        <com.android.keyguard.AlphaOptimizedLinearLayout
   ```

2. 修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/res/layout/system_icons.xml` 文件：

   ```diff
   @@ -19,6 +19,7 @@
        android:id="@+id/system_icons"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
   +    android:paddingEnd="3dp"
        android:gravity="center_vertical">
    
        <com.android.systemui.statusbar.phone.StatusIconContainer android:id="@+id/statusIcons"
   ```

   

