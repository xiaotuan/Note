[toc]

### 1. 展讯平台

#### 1.1 Android R

1. 修改 `vendor/partner_gms/overlay/GmsConfigOverlayComms/res/values/config.xml` 文件，将下面代码：

   ```xml
   <!-- <string name="config_defaultDialer" translatable="false">com.google.android.dialer</string> -->
   ```

   去掉注释掉或者添加如下代码：

   ```xml
   <string name="config_defaultDialer" translatable="false">com.google.android.dialer</string>
   ```

2. 修改`vendor/partner_gms/overlay/gms_overlay_comms/packages/services/Telecomm/res/values/config.xml` 文件，将下面的代码：

   ```xml
   <!-- <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string> -->
   ```

   去掉注释掉或者添加如下代码：

   ```xml
   <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string>
   ```

3. 修改 `vendor/partner_gms/overlay/gms_overlay_comms/packages/services/Telephony/res/values/config.xml` 文件，将下面代码：

   ```xml
   <!-- <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string> -->
   ```

   去掉注释掉或者添加如下代码：

   ```xml
   <string name="dialer_default_class" translatable="false">com.google.android.dialer.extensions.GoogleDialtactsActivity</string>
   ```


5. 修改 `vendor/partner_gms/apps/GmsSampleIntegration/res_dhs_go_2gb/xml/partner_default_layout.xml` 文件，将下面的代码：

    ```xml
    <favorite container="-101" screen="0" x="0" y="0" packageName="com.android.dialer" className="com.android.dialer.main.impl.MainActivity"/>
    ```

    替换成：

    ```xml
    <favorite container="-101" screen="0" x="0" y="0" packageName="com.google.android.dialer" className="com.google.android.dialer.extensions.GoogleDialtactsActivity"/>
    ```

6. 修改 `vendor/partner_gms/apps_go/GoogleDialerGo/Android.mk` 文件，将下面代码：

   ```makefile
   LOCAL_OVERRIDES_PACKAGES := Dialer
   ```

   替换成：

   ```makefile
   LOCAL_OVERRIDES_PACKAGES := Dialer SprdDialerGo
   ```

4. 修改 `vendor/partner_gms/products/google_go_comms_suite.mk` 文件，在下面代码：

   ```makefile
   PRODUCT_PACKAGES += \
   	privapp_permissions_google_comms_suite \
   	CarrierServices \
   	GoogleContacts \
   	GmsConfigOverlayComms \
   	MessagesGo
   ```

   中添加 ` GoogleDialerGo` 应用进去：

   ```makefile
   PRODUCT_PACKAGES += \
   	privapp_permissions_google_comms_suite \
   	CarrierServices \
   	GoogleContacts \
   	GoogleDialerGo \
   	GmsConfigOverlayComms \
   	MessagesGo
   ```

> 提示：
>
> 修改可以参考如下提交代码：
>
> ```
> commit 27d0f24ec8fb8f14219f3bfee5d4baaf037acba4
> Author: soft-server <soft-server@weibu.com>
> Date:   Mon Jun 28 02:30:55 2021 -0400
> 
>     BD-FW-10.1-U863JR200-002-GO-HD-2.4G-asb-余志鹏-ExpressPlus认证类型需使用GoogleDialerGo
> ```

