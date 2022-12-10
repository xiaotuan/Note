Google 应用中 `More` -> `Settings` -> `Voice` -> `Offline speech recognition` 或者 `账号图标` ->  `Settings` -> `Voice` -> `Offline speech recognition` 可以看到 Google 应用已下载的语音包和可下载的语音包。

如果需要将所有语言包在刷机后即可用，可以安装如下方法操作：

1. 编译一个 `userdebug` 软件（为了提取语音包文件）

2. 拷贝 `/data/data/com.google.android.googlequicksearchbox/app_g3_models` 或者 `/data_mirror/data_ce/null/0/com.google.android.googlequicksearchbox/app_g3_models` 目录下的所有文件夹及文件到本地。

3. 在源码中适当的位置存放拷贝出来的文件及文件夹，例如 `vendor/weibu_sz/etc/tts/`。

4. 在适当的 mk 文件中添加如下代码，将语言包文件夹及其文件拷贝到 `/system/usr/srec/` 目录下， 例如在 `vendor/weibu_sz/products/products.mk` 文件中添加如下代码：

   ```makefile
   PRODUCT_COPY_FILES += $(call find-copy-subdir-files,*,vendor/weibu_sz/etc/tts/,$(PRODUCT_OUT)/system/usr/srec/)
   ```

   

