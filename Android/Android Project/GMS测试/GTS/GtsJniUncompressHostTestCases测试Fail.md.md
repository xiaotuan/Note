[toc]

### 1. 测试类型

`GTS`

### 2. 测试模块

`GtsJniUncompressHostTestCases`

### 3. 测试项

`com.google.android.gts.jniuncompress.GtsJniUncompressHostTest#testJniLibsUncompressed`

### 4. 测试命令

```shell
gts-tf > run gts -m GtsJniUncompressHostTestCases -t com.google.android.gts.jniuncompress.GtsJniUncompressHostTest#testJniLibsUncompressed -s 设备序列号
```

### 5. 测试失败日志

```log
	java.lang.RuntimeException: [GMS-13.3.5-001] For PRODUCTs that launch with or upgrade to Android11 or higher, if a preloaded APK file targets API level 30 or higher, it MUST be signed and verifiable with the APK Signature scheme v2 or higher. Any native libraries embedded in it MUST be uncompressed and page aligned before signing. [com.google.android.apps.meetings] V2+ verification failure [/system/app/Meet/Meet.apk]. targetSdkVer: 30 [vn.vnnic.ispeed] V2+ verification failure [/system/app/i-SPEED/i-SPEED.apk]. targetSdkVer: 30 [us.zoom.videomeetings] V2+ verification failure [/system/app/Zoom/Zoom.apk]. targetSdkVer: 30 at org.junit.Assert.fail(Assert.java:89) at com.google.android.gts.jniuncompress.GtsJniUncompressHostTest.assertEmptyViolation(GtsJniUncompressHostTest.java:111) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.base/java.lang.reflect.Method.invoke(Method.java:566) at com.android.compatibility.common.util.BusinessLogicExecutor$ResolvedMethod.invoke(BusinessLogicExecutor.java:228) at com.android.compatibility.common.util.BusinessLogicExecutor.invokeMethod(BusinessLogicExecutor.java:153) at com.android.compatibility.common.util.BusinessLogicExecutor.executeAction(BusinessLogicExecutor.java:74) at com.android.compatibility.common.util.BusinessLogic$BusinessLogicRuleAction.invoke(BusinessLogic.java:336) at com.android.compatibility.common.util.BusinessLogic$BusinessLogicRule.invokeActions(BusinessLogic.java:282) at com.android.compatibility.common.util.BusinessLogic$BusinessLogicRulesList.invokeRules(BusinessLogic.java:242) at com.android.compatibility.common.util.BusinessLogic.applyLogicFor(BusinessLogic.java:87) at com.android.compatibility.common.tradefed.testtype.BusinessLogicHostTestBase.executeBusinessLogic(BusinessLogicHostTestBase.java:70) at com.android.compatibility.common.tradefed.testtype.BusinessLogicHostTestBase.handleBusinessLogic(BusinessLogicHostTestBase.java:53) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.base/java.lang.reflect.Method.invoke(Method.java:566) at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:59) at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12) at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:61) at org.junit.internal.runners.statements.RunBefores.invokeMethod(RunBefores.java:33) at org.junit.internal.runners.statements.RunBefores.evaluate(RunBefores.java:24) at org.junit.internal.runners.statements.RunAfters.evaluate(RunAfters.java:27) at org.junit.rules.TestWatcher$1.evaluate(TestWatcher.java:61) at org.junit.runners.ParentRunner$3.evaluate(ParentRunner.java:306) at org.junit.runners.BlockJUnit4ClassRunner$1.evaluate(BlockJUnit4ClassRunner.java:100) at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:366) at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:103) at com.android.tradefed.testtype.DeviceJUnit4ClassRunner.runChild(DeviceJUnit4ClassRunner.java:108) at com.android.tradefed.testtype.DeviceJUnit4ClassRunner.runChild(DeviceJUnit4ClassRunner.java:60) at org.junit.runners.ParentRunner$4.run(ParentRunner.java:331) at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:79) at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:329) at org.junit.runners.ParentRunner.access$100(ParentRunner.java:66) at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:293) at org.junit.runners.ParentRunner$3.evaluate(ParentRunner.java:306) at org.junit.runners.ParentRunner.run(ParentRunner.java:413) at com.android.tradefed.testtype.DeviceJUnit4ClassRunner.run(DeviceJUnit4ClassRunner.java:144) at org.junit.runner.JUnitCore.run(JUnitCore.java:137) at com.android.tradefed.testtype.HostTest.runJUnit4Tests(HostTest.java:723) at com.android.tradefed.testtype.HostTest.runTestClasses(HostTest.java:612) at com.android.tradefed.testtype.HostTest.run(HostTest.java:560) at com.android.compatibility.common.tradefed.testtype.JarHostTest.run(JarHostTest.java:56) at com.android.tradefed.testtype.suite.GranularRetriableTestWrapper.intraModuleRun(GranularRetriableTestWrapper.java:344) at com.android.tradefed.testtype.suite.GranularRetriableTestWrapper.run(GranularRetriableTestWrapper.java:264) at com.android.tradefed.testtype.suite.ModuleDefinition.run(ModuleDefinition.java:495) at com.android.tradefed.testtype.suite.ITestSuite.runSingleModule(ITestSuite.java:854) at com.android.tradefed.testtype.suite.ITestSuite.run(ITestSuite.java:736) at com.android.tradefed.invoker.InvocationExecution.runTest(InvocationExecution.java:880) at com.android.tradefed.invoker.InvocationExecution.runTests(InvocationExecution.java:705) at com.android.tradefed.invoker.TestInvocation.prepareAndRun(TestInvocation.java:483) at com.android.tradefed.invoker.TestInvocation.performInvocation(TestInvocation.java:252) at com.android.tradefed.invoker.TestInvocation.invoke(TestInvocation.java:1107) at com.android.tradefed.command.CommandScheduler$InvocationThread.run(CommandScheduler.java:631)
```

### 6. 解决办法

> 参考：<https://blog.csdn.net/qq_25815655/article/details/121635538>

凡是预置的 **API level>= 30** 的任何 APK 必须满足如下要求：
1. 必须使用 `V2+ signatures`

2. apk 中不要存在被压缩的 `JNI libs（.so）` 或 `Dex` 文件,如果压缩需要按照要求配置修改，否则将导致这类apk 无法使用

3. 此项要求从2021年10月1日起, 通过 GTS 9.0 R1（GtsJniUncompressHostTest）开始检查，不满足则存在GTS fail 。

4. 适用对象：
   针对 Android R（11）及以上的所有项目（包括升级项目），以及所有的 Build （IR/LR/MR/SMR）上预置的API level>= 30 的任何 APK

5. 检查方法：

  + 确认apklevel是否为>=30，如>=30则走2

    ````shell
    $ aapt dump badging 拖进apk | grep targetSdkVersion
    ````

  + 确认APK签名，必须为V2+，如果不是V2+签名则 apk必须整改

    ```shell
    $ java -jar apksigner.jar verify -verbose -print-certs  拖进apk
    ```
    
  + 确认apk中的JNI so和dex是否被压缩：
    ```shell
    unzip -v E:\APK\aida64-v178.apk lib/*.so 
    unzip -v E:\APK\aida64-v178.apk *.dex
    ```
    如果存在.so/.dex压缩，则必须使用：LOCAL_REPLACE_PREBUILT_APK_INSTALLED 编译apk，不要使用copy命令！

符合上面条件的需要通过如下方式内置apk：

**Android.mk**

```makefile
LOCAL_PATH := $(call my-dir)

my_archs := arm arm64
my_src_arch := $(call get-prebuilt-src-arch, $(my_archs))

include $(CLEAR_VARS)

LOCAL_MODULE := Meet
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_PATH := $(TARGET_OUT)/app
LOCAL_REPLACE_PREBUILT_APK_INSTALLED := $(LOCAL_PATH)/$(LOCAL_MODULE).apk
LOCAL_DEX_PREOPT := false
LOCAL_MULTILIB := 64

LOCAL_PREBUILT_JNI_LIBS := \
    lib/$(my_src_arch)/libfilterframework_jni.so \
    lib/$(my_src_arch)/libvideochat_jni.so

LOCAL_MODULE_TARGET_ARCH := $(my_src_arch)

include $(BUILD_PREBUILT)
```

文件目录结构如下：

```
Meet
|
|__lib
|  |__arm64
|     |__libfilterframework_jni.so
|     |__libvideochat_jni.so
|__Meet.apk
|__Android.mk
```

> **特别说明：禁止使用cp命令拷贝apk、so库，请使用下面属性预置：**
>
> **预置apk使用属性： LOCAL_REPLACE_PREBUILT_APK_INSTALLED** 
>
> **预置so库使用属性：LOCAL_PREBUILT_JNI_LIBS**

