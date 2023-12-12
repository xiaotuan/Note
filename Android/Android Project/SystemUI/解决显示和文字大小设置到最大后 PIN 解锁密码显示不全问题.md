[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

问题描述：

1. 执行 `设置` -> `安全` -> `屏幕锁定` -> `PIN 码`，设置锁屏方式
2. 执行 `设置` -> `显示` -> `显示大小和文字` ，将字体大小和显示大小设置到最大。
3. 灭屏，再亮屏，滑动锁屏界面解锁屏幕，在 PIN 码输入界面输入密码时观察键盘上面的密码输入框，密码输入框显示不全。

解决办法：

1. 修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res-keyguard/values-land/donottranslate.xml` 文件中的如下代码，调整键盘按键高度：

   ```diff
   @@ -15,5 +15,5 @@
    -->
    
    <resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">
   -    <string name="num_pad_key_ratio">1.51</string>
   +    <string name="num_pad_key_ratio">1.65</string>
    </resources>
   ```

2. 修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res-keyguard/values-sw360dp-land/dimens.xml` 文件中的如下代码，修改密码输入框高度和文字大小：

   ```diff
   @@ -21,9 +21,9 @@
        <dimen name="num_pad_row_margin_bottom">4dp</dimen>
        <dimen name="keyguard_eca_top_margin">4dp</dimen>
        <dimen name="keyguard_eca_bottom_margin">4dp</dimen>
   -    <dimen name="keyguard_password_height">50dp</dimen>
   +    <dimen name="keyguard_password_height">36dp</dimen>
        <dimen name="num_pad_entry_row_margin_bottom">4dp</dimen>
    
        <!-- The size of PIN text in the PIN unlock method. -->
   -    <integer name="scaled_password_text_size">40</integer>
   +    <integer name="scaled_password_text_size">30</integer>
    </resources>
   ```

3. 在 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/res-keyguard/values-sw360dp-land/` 目录下新建 `styles.xml` 文件，修改键盘文字大小，其内容如下：

   ```diff
   @@ -0,0 +1,32 @@
   +<?xml version="1.0" encoding="utf-8"?>
   +<!--
   +**
   +** Copyright 2012, The Android Open Source Project
   +**
   +** Licensed under the Apache License, Version 2.0 (the "License")
   +** you may not use this file except in compliance with the License.
   +** You may obtain a copy of the License at
   +**
   +**     http://www.apache.org/licenses/LICENSE-2.0
   +**
   +** Unless required by applicable law or agreed to in writing, software
   +** distributed under the License is distributed on an "AS IS" BASIS,
   +** WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   +** See the License for the specific language governing permissions and
   +** limitations under the License.
   +*/
   +-->
   +
   +<resources xmlns:android="http://schemas.android.com/apk/res/android"
   +    xmlns:androidprv="http://schemas.android.com/apk/prv/res/android">
   +    <style name="Widget.TextView.NumPadKey.Digit"
   +           parent="@android:style/Widget.DeviceDefault.TextView">
   +        <item name="android:singleLine">true</item>
   +        <item name="android:gravity">center_horizontal|center_vertical</item>
   +        <item name="android:background">@null</item>
   +        <item name="android:textSize">24sp</item>
   +        <item name="android:textColor">?android:attr/textColorPrimary</item>
   +        <item name="android:fontFamily">@*android:string/config_headlineFontFamily</item>
   +        <item name="android:paddingBottom">-14dp</item>
   +    </style>
   +</resources>
   ```
   
   `<item name="android:textSize">24sp</item>` 修改文字大小，`<item name="android:paddingBottom">-14dp</item>` 修改文字距离底部的内边距。
   
4. 注意，如果在这种情况下锁屏界面还可以旋转的话，可能会导致修改无效，因为 PIN 输入界面没有适配屏幕旋转，导致界面没有使用横屏参数，可以通过设置下面属性解决：

   ```
   lockscreen.rot_override=false
   ```

   