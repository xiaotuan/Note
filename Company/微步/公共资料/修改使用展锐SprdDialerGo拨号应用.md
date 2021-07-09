[toc]

### 1. 展讯平台

#### 1.1 Android R

1. 修改 `vendor/partner_gms/overlay/GmsConfigOverlayComms/res/values/config.xml` 文件，将下面代码：

   ```xml
   <string name="config_defaultDialer" translatable="false">com.google.android.dialer</string>
   ```

   注释掉或者去掉：

   ```xml
   <!-- <string name="config_defaultDialer" translatable="false">com.google.android.dialer</string> -->
   ```

2. 修改`vendor/partner_gms/overlay/gms_overlay_comms/packages/services/Telecomm/res/values/config.xml` 文件，将下面的代码：

   ```xml
   <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string>
   ```

   注释掉或者去掉：

   ```xml
   <!-- <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string> -->
   ```

3. 修改 `vendor/partner_gms/overlay/gms_overlay_comms/packages/services/Telephony/res/values/config.xml` 文件，将下面代码：

   ```xml
   <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string>
   ```

   注释掉或者去掉：

   ```xml
   <!-- <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string> -->
   ```

4. 修改 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go_2gb/xml/partner_default_layout.xml` 文件，将下面的代码：

   ```xml
   <favorite container="-101" screen="0" x="0" y="0" packageName="com.google.android.dialer" className="com.google.android.dialer.extensions.GoogleDialtactsActivity"/>
   ```

   替换成：

   ```xml
   <favorite container="-101" screen="0" x="0" y="0"    packageName="com.android.dialer" className="com.android.dialer.main.impl.MainActivity"/>
   ```

5. 修改 `vendor/partner_gms/apps_go/GoogleDialerGo/Android.mk` 文件，将下面代码：

   ```makefile
   LOCAL_OVERRIDES_PACKAGES := Dialer SprdDialerGo
   ```

   替换成：

   ```makefile
   LOCAL_OVERRIDES_PACKAGES := Dialer
   ```

4. 修改 `vendor/partner_gms/products/google_go_comms_suite.mk` 文件，在下面代码：

   ```makefile
   PRODUCT_PACKAGES += \
   	privapp_permissions_google_comms_suite \
   	CarrierServices \
   	GoogleContacts \
   	GoogleDialerGo \
   	GmsConfigOverlayComms \
   	MessagesGo
   ```
   
   中去掉 ` GoogleDialerGo` 应用进去：
   
   ```makefile
   RODUCT_PACKAGES += \
   	privapp_permissions_google_comms_suite \
   	CarrierServices \
   	GoogleContacts \
   	GmsConfigOverlayComms \
   	MessagesGo
   ```
