[toc]

### 1. 反编译 apk 命令

```shell
$ apktool.bat d apk文件路径 -o 反编译输出目录
```

也可以是：

```shell
$ apktool.bat d apk文件路径
```

例如：

```shell
PS C:\WorkSpaces\ProgramFiles\apktool> .\apktool.bat d .\batterylog.apk
I: Using Apktool 2.5.0 on batterylog.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: C:\Users\Admin\AppData\Local\apktool\framework\1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
Press any key to continue . . .
```

### 2. 重新打包 APK 命令

```shell
$ apktool.bat b --use-aapt2 -o 生成apk的文件路径 反编译输出的目录路径 
```

或者：

```shell
$ apktool.bat b -o 生成apk的文件路径 反编译输出的目录路径 
```

例如：

```shell
PS C:\WorkSpaces\ProgramFiles\apktool> .\apktool.bat b --use-aapt2 -o .\batterylog1.apk .\batterylog\
I: Using Apktool 2.5.0
I: Checking whether sources has changed...
I: Checking whether resources has changed...
I: Building apk file...
I: Copying unknown files/dir...
I: Built apk...
Press any key to continue . . .
```

### 3. 签名 APK 命令

```shell
$ jarsigner.exe -verbose -keystore 签名秘钥文件路径 -signedjar 签名后的APK文件路径 要签名的APK文件路径 签名秘钥别名
```

例如：

```shell
Admin@DESKTOP-DCE08LH MINGW64 /c/WorkSpaces/ProgramFiles/apktool
$ jarsigner.exe -verbose -keystore yjzd.jks -signedjar batterylog-sign.apk batterylog1.apk yjzd
输入密钥库的密码短语: birdsfly
   正在添加: META-INF/MANIFEST.MF
   正在添加: META-INF/YJZD.SF
   正在添加: META-INF/YJZD.RSA
  正在签名: AndroidManifest.xml
  正在签名: classes.dex
  正在签名: res/drawable-hdpi-v4/bg_fragment_detail.9.png
  正在签名: res/drawable-hdpi-v4/ic_btn_zoom_in.png
  正在签名: res/drawable-hdpi-v4/ic_btn_zoom_out.png
  正在签名: res/drawable-hdpi-v4/ic_btn_zoom_reset.png
  正在签名: res/drawable-hdpi-v4/ic_launcher.png
  正在签名: res/drawable-hdpi-v4/ic_menu_help.png
  正在签名: res/drawable-hdpi-v4/ic_menu_refresh.png
  正在签名: res/drawable-hdpi-v4/ic_menu_save.png
  正在签名: res/drawable-hdpi-v4/ic_menu_settings.png
  正在签名: res/drawable-hdpi-v4/level_000.png
  正在签名: res/drawable-hdpi-v4/level_001.png
  正在签名: res/drawable-hdpi-v4/level_002.png
  正在签名: res/drawable-hdpi-v4/level_003.png
  正在签名: res/drawable-hdpi-v4/level_004.png
  正在签名: res/drawable-hdpi-v4/level_005.png
  正在签名: res/drawable-hdpi-v4/level_006.png
  正在签名: res/drawable-hdpi-v4/level_007.png
  正在签名: res/drawable-hdpi-v4/level_008.png
  正在签名: res/drawable-hdpi-v4/level_009.png
  正在签名: res/drawable-hdpi-v4/level_010.png
  正在签名: res/drawable-hdpi-v4/level_011.png
  正在签名: res/drawable-hdpi-v4/level_012.png
  正在签名: res/drawable-hdpi-v4/level_013.png
  正在签名: res/drawable-hdpi-v4/level_014.png
  正在签名: res/drawable-hdpi-v4/level_015.png
  正在签名: res/drawable-hdpi-v4/level_016.png
  正在签名: res/drawable-hdpi-v4/level_017.png
  正在签名: res/drawable-hdpi-v4/level_018.png
  正在签名: res/drawable-hdpi-v4/level_019.png
  正在签名: res/drawable-hdpi-v4/level_020.png
  正在签名: res/drawable-hdpi-v4/level_021.png
  正在签名: res/drawable-hdpi-v4/level_022.png
  正在签名: res/drawable-hdpi-v4/level_023.png
  正在签名: res/drawable-hdpi-v4/level_024.png
  正在签名: res/drawable-hdpi-v4/level_025.png
  正在签名: res/drawable-hdpi-v4/level_026.png
  正在签名: res/drawable-hdpi-v4/level_027.png
  正在签名: res/drawable-hdpi-v4/level_028.png
  正在签名: res/drawable-hdpi-v4/level_029.png
  正在签名: res/drawable-hdpi-v4/level_030.png
  正在签名: res/drawable-hdpi-v4/level_031.png
  正在签名: res/drawable-hdpi-v4/level_032.png
  正在签名: res/drawable-hdpi-v4/level_033.png
  正在签名: res/drawable-hdpi-v4/level_034.png
  正在签名: res/drawable-hdpi-v4/level_035.png
  正在签名: res/drawable-hdpi-v4/level_036.png
  正在签名: res/drawable-hdpi-v4/level_037.png
  正在签名: res/drawable-hdpi-v4/level_038.png
  正在签名: res/drawable-hdpi-v4/level_039.png
  正在签名: res/drawable-hdpi-v4/level_040.png
  正在签名: res/drawable-hdpi-v4/level_041.png
  正在签名: res/drawable-hdpi-v4/level_042.png
  正在签名: res/drawable-hdpi-v4/level_043.png
  正在签名: res/drawable-hdpi-v4/level_044.png
  正在签名: res/drawable-hdpi-v4/level_045.png
  正在签名: res/drawable-hdpi-v4/level_046.png
  正在签名: res/drawable-hdpi-v4/level_047.png
  正在签名: res/drawable-hdpi-v4/level_048.png
  正在签名: res/drawable-hdpi-v4/level_049.png
  正在签名: res/drawable-hdpi-v4/level_050.png
  正在签名: res/drawable-hdpi-v4/level_051.png
  正在签名: res/drawable-hdpi-v4/level_052.png
  正在签名: res/drawable-hdpi-v4/level_053.png
  正在签名: res/drawable-hdpi-v4/level_054.png
  正在签名: res/drawable-hdpi-v4/level_055.png
  正在签名: res/drawable-hdpi-v4/level_056.png
  正在签名: res/drawable-hdpi-v4/level_057.png
  正在签名: res/drawable-hdpi-v4/level_058.png
  正在签名: res/drawable-hdpi-v4/level_059.png
  正在签名: res/drawable-hdpi-v4/level_060.png
  正在签名: res/drawable-hdpi-v4/level_061.png
  正在签名: res/drawable-hdpi-v4/level_062.png
  正在签名: res/drawable-hdpi-v4/level_063.png
  正在签名: res/drawable-hdpi-v4/level_064.png
  正在签名: res/drawable-hdpi-v4/level_065.png
  正在签名: res/drawable-hdpi-v4/level_066.png
  正在签名: res/drawable-hdpi-v4/level_067.png
  正在签名: res/drawable-hdpi-v4/level_068.png
  正在签名: res/drawable-hdpi-v4/level_069.png
  正在签名: res/drawable-hdpi-v4/level_070.png
  正在签名: res/drawable-hdpi-v4/level_071.png
  正在签名: res/drawable-hdpi-v4/level_072.png
  正在签名: res/drawable-hdpi-v4/level_073.png
  正在签名: res/drawable-hdpi-v4/level_074.png
  正在签名: res/drawable-hdpi-v4/level_075.png
  正在签名: res/drawable-hdpi-v4/level_076.png
  正在签名: res/drawable-hdpi-v4/level_077.png
  正在签名: res/drawable-hdpi-v4/level_078.png
  正在签名: res/drawable-hdpi-v4/level_079.png
  正在签名: res/drawable-hdpi-v4/level_080.png
  正在签名: res/drawable-hdpi-v4/level_081.png
  正在签名: res/drawable-hdpi-v4/level_082.png
  正在签名: res/drawable-hdpi-v4/level_083.png
  正在签名: res/drawable-hdpi-v4/level_084.png
  正在签名: res/drawable-hdpi-v4/level_085.png
  正在签名: res/drawable-hdpi-v4/level_086.png
  正在签名: res/drawable-hdpi-v4/level_087.png
  正在签名: res/drawable-hdpi-v4/level_088.png
  正在签名: res/drawable-hdpi-v4/level_089.png
  正在签名: res/drawable-hdpi-v4/level_090.png
  正在签名: res/drawable-hdpi-v4/level_091.png
  正在签名: res/drawable-hdpi-v4/level_092.png
  正在签名: res/drawable-hdpi-v4/level_093.png
  正在签名: res/drawable-hdpi-v4/level_094.png
  正在签名: res/drawable-hdpi-v4/level_095.png
  正在签名: res/drawable-hdpi-v4/level_096.png
  正在签名: res/drawable-hdpi-v4/level_097.png
  正在签名: res/drawable-hdpi-v4/level_098.png
  正在签名: res/drawable-hdpi-v4/level_099.png
  正在签名: res/drawable-hdpi-v4/level_100.png
  正在签名: res/drawable-xhdpi-v4/ic_launcher.png
  正在签名: res/layout/activity_main.xml
  正在签名: res/layout/activity_main_dual.xml
  正在签名: res/layout/fragment_export.xml
  正在签名: res/layout/fragment_graphview.xml
  正在签名: res/layout/fragment_logview.xml
  正在签名: res/layout/fragment_menu.xml
  正在签名: res/layout/list_empty.xml
  正在签名: res/layout/logview_item.xml
  正在签名: res/layout/logview_item_header.xml
  正在签名: res/layout/menu_list_footer.xml
  正在签名: res/layout/menu_list_item.xml
  正在签名: res/layout/menu_list_item_act.xml
  正在签名: res/menu/export.xml
  正在签名: res/menu/logview.xml
  正在签名: res/menu/main.xml
  正在签名: res/xml/settings.xml
  正在签名: resources.arsc
  正在签名: org/achartengine/image/zoom-1.png
  正在签名: org/achartengine/image/zoom_in.png
  正在签名: org/achartengine/image/zoom_out.png
>>> 签名者
    X.509, C=518000, ST=Guangdong, L=Shenzhen, O=Personal, OU=Personal, CN=Weitao Zhang
    [可信证书]

jar 已签名。

警告:
签名者证书为自签名证书。

```

