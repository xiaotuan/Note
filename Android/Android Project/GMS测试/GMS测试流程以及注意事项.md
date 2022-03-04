[toc]

此文档主要针对GMS所有测试项的介绍以及测试方法(基于android R)。

GMS测试包括CTS测试、GTS测试、CTS-ON-GSI测试、VTS测试、CtsVerifier测试、STS测试、GOATS测试；不同的android版本要求不一样，后面会详细说明具体测试项的一些差异。

### 1. 测试前平板端的测试环境配置要求：
+ 刷SN号

+ 刷Google key

+ WiFi连接外网

+ 设置永不休眠

+ 设置最低亮度

+ 设置无锁屏

+ 打开USB debugging

+ 关闭Verify apps over USB

+ 打开Stay awake

+ 默认语言English（United States）

+ 默认时区GMT-07:00 Pacific Daylight Time

+ 插高性能TF卡

+ 插SIM卡;

### 2. GMS具体测试项介绍：（cts、ctsv、gts、gsi、vts、sts、goats）
#### 2.1 GMS测试流程注意事项
+ 测试命令不同测试项不同；

+ cts和 cts-on-gsi共用一个测试工具（cts测试套件）；

+ cts-on-gsi和 vts 测试前需要刷user版本的软件和谷歌system.img，vts还要刷boot-debug.img；

+ sts和goats测试需要刷userdebug版本；

+ 项目首次测试需要进行GMS full test；

+ 项目后续版本测试可以执行快速测试手段，过滤耗时且不易出错的模块，比如
  
  + cts:run cts --exclude-filter CtsDeqpTestCases --exclude-filter CtsMediaStressTestCases --exclude-filter CtsMediaTestCases
  
  + cts-on-gsi: run cts-on-gsi --exclude-filter CtsDeqpTestCases --exclude-filter CtsMediaStressTestCases --exclude-filter CtsMediaTestCases
  
  + gts: run gts --exclude-filter GtsMediaTestCases --exclude-filter CtsMediaStressTestCases --exclude-filter GtsYouTubeTestCases
  
+ 每个测试项，耗时不一样，GMS full test具体情况如下:

  + cts: 两台设备三天
  + gsi: 两台设备三天 
  + gts: 两台设备一天
  + ctsv: 两台设备一天 
  + vts: 一台设备一天
  + sts: 一台设备一天

  > 建议将耗时的测试项使用多台设备测试，像cts、gsi、gts等测试项；
  > 相对不太耗时的可以使用一台设备测试，像vts、sts等；

+ 充分利用下班、周末时间做耗时测试，掌握缩短测试时间的技巧。

+ 某个模块（如camera）单独修改后，单独测试camera相关的cts/ctsv测试项。

#### 2.2 工具下载地址：
CTS/CTSV下载地址：https://source.android.com/compatibility/cts/
GTS/GMS/VTS/GSI 下载地址（需程少文账号登录）：
https://support.google.com/androidpartners_gms/answer/6173316?
或者通过ftp://219.90.56.51/ 下载；

下载好测试工具，在Linux上面解压，工具脚本在android-cts/tools/cts-tradefed
#### 2.3 各测试项运行命令:
基本命令：
查询已连接设备：l d 
查询测试结果sessionID：l r 
查询所有模块：l m
查询所有subplan： l s
查询run cts的所有参数：run cts --help-all
更新软件，重跑所有fail项，可以将fail做成subplan：
查询help add命令，查看做subplan的方法，
add subplan --session sessionID --name subplan_name --result-type failed
运行subplan的方法：run cts --subplan subplan_name

#### 2.4 cts测试: 

1. ./cts-tradefed 
   用cts测试套件测试（例如：android-cts-11_r3-linux_x86-arm.zip）

2. 单台设备测试: run cts -s serial_number
      多台设备测试：run cts --shard-count 2 -s serial_number1 -s serial_number2
      过滤某个模块：run cts --exclude-filter CtsDeqpTestCase
      单测某个模块：run cts -m CtsCameraTestCase
   单测某个case: run cts -m CtsCameraTestCase -t android.hardware.cts.CameraTest#testJpegExif
   过滤cts-instant模块：run cts --exclude-module-parameters instant_app
   只测cts-instant模块：run cts --module-parameter instant_app
   重跑所有fail：run retry -r sessionID -s serial_number 

3. cts full test可以分成两部分测试，先用两台机把耗时的媒体模块跳过：
   run cts --exclude-filter CtsDeqpTestCases --exclude-filter CtsMediaStressTestCases --exclude-filter CtsMediaTestCases --shard-count 2 
   以上部分测试完成后，再用两台机测试媒体模块：
   run cts --include-filter CtsDeqpTestCases --include-filter CtsMediaStressTestCases --include-filter CtsMediaTestCases --shard-count 2 

在测试时如果网络环境不稳定，也可以加本地资源参数来跑：
--module-arg CtsMediaTestCases:config-url:http://192.168.1.136/media/DynamicConfig.json --module-arg CtsMediaStressTestCases:local-media-path:/tmp/android-cts-media/android-cts-media-1.5

#### 2.5 ctsv测试:

手动测试项，安装CtsVerifier.apk，根据测试指引操作，也可以观看MTKonline上面的视频，具体测试项有教程。着重测试的是camera、Sensor、Hardware等测试项； 

#### 2.6 gts测试:

1. ./gts-tradefed
   用gts测试套件测试（例如：android-gts-8-R3(11)-7133222.zip）

2. 单台设备测试: run gts -s serial_number
      多台设备测试：run gts --shard-count 2 -s serial1 -s serial2
      过滤某个模块：run gts --exclude-filter GtsMediaTestCases
      单测某个模块：run gts -m GtsMediaTestCases
   单测某个case: run gts -m GtsMediaTestCases -t 
   重跑所有fail：run retry -r sessionID -s serial_number

3. gts full test可以分成两部分测试，先把耗时的媒体模块跳过：
   run gts --exclude-filter GtsMediaTestCases --exclude-filter GtsExoPlayerTestCases --exclude-filter GtsYouTubeTestCases
   以上部分测试完成后，再测试媒体模块：
   run gts --include-filter GtsMediaTestCases --include-filter GtsExoPlayerTestCases --include-filter GtsYouTubeTestCases

在测试时如果网络环境不稳定，也可以加本地资源参数来跑：
--module-arg GtsExoPlayerTestCases:config-url:http://192.168.1.136/media/gts/exoplayer/dynamic-config-1.0.json --module-arg "GtsMediaTestCases:instrumentation-arg:media-path:=http://192.168.1.136/media/wvmedia"

#### 2.7 测试cts-on-gsi、vts需要刷谷歌的system.img,下面介绍刷机方式：
#### 2.7.1 MTK平台刷gsi方法：

1、刷user版本软件进系统，打开开发者选项->OEM unlocking；
2、adb reboot bootloader或者在关机状态下同时按power键和音量+，进入BootLoader模式，选择fastboot，按音量减进入fastboot模式；连接电脑，打开cmd执行下面的命令：
3、fastboot flashing unlock按音量加键确认解锁
4、fastboot reboot fastboot
5、fastboot flash system_a  Google_system_image.img
6、fastboot reboot

##### 2.7.2 unisoc平台刷gsi方法：

1、刷user版本软件进系统，打开开发者选项->OEM unlocking；
2、adb reboot bootloader
3、fastboot oem get_identifier_token获取设备序列号
4、在linux系统下执行./signidentifier_unlockbootloader.sh  设备序列号 rsa4096_vbmeta.pem signature.bin  生成解锁用的signature.bin文件
5、fastboot flashing unlock_bootloader signature.bin  按音量减键确认解锁
6、fastboot reboot fastboot
7、fastboot flash system_a  Google_system_image.img
8、fastboot reboot

##### 2.7.3 cts-on-gsi测试:

1)	./cts-tradefed
用cts测试套件测试（例如：android-cts-11_r3-linux_x86-arm.zip）

2、单台设备测试: run cts-on-gsi -s serial_number
   多台设备测试：run cts-on-gsi --shard-count 2 -s serial_1 -s serial2
   过滤某个模块：run cts-on-gsi --exclude-filter CtsDeqpTestCase
   单测某个模块：run cts-on-gsi -m CtsCameraTestCase
单测某个case: run cts-on-gsi -m CtsCameraTestCase -t android.hardware.cts.CameraTest#testJpegExif
重跑所有fail：run retry -r sessionID -s serial_number
3、cts-on-gsi full test具体测试方法可参考前面介绍的cts测试方法进行测试；

##### 2.7.4 vts测试:

测试vts的机器需要刷boot-debug.img，刷入方法：
拿一台刷好gsi的机器，输入adb reboot bootloader
进入fastboot模式后执行fastboot flash boot_a boot-debug.img,再
fastboot reboot即可；

1)	./vts-tradefed
用vts测试套件测试（例如：android-vts-7137996-arm64.zip）

2、单台设备测试: run vts -s serial_number
   多台设备测试：run vts --shards 2 -s serial1 -s serial2
   过滤某个模块：run vts --exclude-filter VtsHalGnssV1_0TargetTest
   单测某个模块：run vts -m VtsHalGnssV1_0TargetTest
单测某个case: run vts -m VtsHalGnssV1_0TargetTest -t 
重跑所有fail：run retry -r sessionID -s serial_number

##### 2.7.6 sts测试

测试STS需要刷userdebug版本；

1)	./sts-tradefed
用sts测试套件测试（例如：android-sts-11.0_202103-linux-arm64.zip）
需要注意的是要根据测试机的security_patch日期选用对应的sts测试工具；

2、单台设备测试: run sts-engbuild -s serial_number
   单测某个模块：run sts -m CtsSecurityTestCases
单测某个case: run sts -m CtsSecurityTestCases -t 
重跑所有fail：run retry -r sessionID -s serial_number

##### 2.7.7 GOATS测试

GOATS测试用于验证Android Go版本设备的性能，Android10以上的GO设备才需要进行GOATS测试(Android 8.1、Android 9的Go设备继续使用performance脚本测试设备性能)。
1、./goats-tradefed
2、单台设备测试: run goats -s serial_number
重跑所有fail：run retry -r sessionID -s serial_number

#### 2.8 总结

总结一下测试过程中常见的测试环境引起的fail
⦁	没有ipv6网络引起的fail
CtsLibcoreTestCases           
libcore.java.net.SocketTest#testSocketTestAllAddresses
CtsNetTestCases                                    
android.net.cts.DnsTest#testDnsWorks
⦁	未插境外SIM卡引起的fail
CtsNetTestCases
android.net.cts.ConnectivityManagerTest#testOpenConnection
⦁	未写Google key引起的fail
CtsKeystoreTestCases 模块测试fail
GtsGmscoreHostTestCases 
com.google.android.gts.security.AttestationRootHostTest#testEcAttestationChain
com.google.android.gts.security.AttestationRootHostTest#testRsaAttestationChain

VtsHalKeymasterV4_0TargetTest
PerInstance/AttestationTest#RsaAttestation/0_default
PerInstance/AttestationTest#EcAttestation/0_default
PerInstance/AttestationTest#AttestationApplicationIDLengthProperlyEncoded/0_default
⦁	未插高性能TF卡引起的fail
CtsAppSecurityHostTestCases 
android.appsecurity.cts.AdoptableHostTest#testApps
android.appsecurity.cts.AdoptableHostTest#testEjected  
⦁	未插SIM卡测试引起的fail
CtsTelephonyTestCases模块测试fail
CtsUsageStatsTestCases（插入sim卡打开数据流量）
android.app.usage.cts.NetworkUsageStatsTest#testAppDetails     
android.app.usage.cts.NetworkUsageStatsTest#testAppSummary……
CtsPermission2TestCases（插入已写入号码的sim卡）
android.permission2.cts.NoReceiveSmsPermissionTest#testAppSpecificSmsToken 
android.permission2.cts.NoReceiveSmsPermissionTest#testReceiveTextMessage
GtsTelephonyNumberVerificationHostCases
com.google.android.gts.telephony.numberverification.NumberVerificationHostTest#testNumberVerification
⦁	未插入白卡测试引起的fail
CtsCarrierApiTestCases模块测试fail
GtsNmgiarcTestCases
com.google.android.comms.MessagesTests#testMessagesInstalledCorrectly
GtsSimAppDialogTestCases
com.google.android.simappdialog.gts.InstallCarrierAppActivityTest#testActivityAndNotificationShown_downloadPressed
com.google.android.simappdialog.gts.InstallCarrierAppActivityTest#testNotificationOnlyDuringSetupWizard
com.google.android.simappdialog.gts.InstallCarrierAppActivityTest#testActivityAndNotificationShown_notNowPressed

⦁	测试环境光线不足引起的camera fail
CtsCameraTestCases模块测试fail
⦁	gts测试在开机向导未连接wifi引起的fail
GtsSetupWizardHostTestCases
com.google.android.gts.setupwizard.SetupWizardZeroTouchTest#testZeroTouch_zeroTouchWrapperLaunched
9、未设置默认语言为英语-美国可能引起的fail
CtsAppSecurityHostTestCases
android.appsecurity.cts.ExternalStorageHostTest#testMediaEscalation28
android.appsecurity.cts.ExternalStorageHostTest#testMediaEscalation29
android.appsecurity.cts.ExternalStorageHostTest#testMediaEscalation
android.appsecurity.cts.StorageHostTest#testFullDisk
CtsContentTestCases   
android.content.pm.cts.PermissionInfoTest#testPermissionInfo 
CtsThemeHostTestCases 
android.theme.cts.ThemeHostTest#testThemes
CtsWebkitTestCases    
android.webkit.cts.WebSettingsTest#testAccessAllowFileAccess

10、GPS信号不好引起的fail:
CtsLocationGnssTestCases
android.location.cts.gnss.GnssTtffTests#testTtffWithNetwork
建议将测试机放在GPS信号好的地方插入sim卡测试

11、联网跑出的fail
CtsLibcoreTestCases以下项关闭wifi可以测过
libcore.java.net.InetAddressTest#test_getByName_invalid[1]
libcore.java.net.InetAddressTest#test_getByName_invalid[2]
libcore.java.net.InetAddressTest#test_getByName_invalid[3]
libcore.java.net.InetAddressTest#test_getByName_invalid[4]
libcore.java.net.InetAddressTest#test_getByName_invalid[5]……

12、cts-on-gsi用刷了boot_debug.img的测vts的机器来测gsi导致的fail:
CtsOsTestCases
android.os.cts.SecurityFeaturesTest#testPrctlDumpable
CtsSignedConfigHostTestCases
com.android.cts.signedconfig.SignedConfigHostTest#testDebugKeyNotValidOnUserBuild
13、其他fail可以通过恢复出厂设置再retry测试