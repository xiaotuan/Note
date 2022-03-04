[toc]

### 1. 测试命令

```shell
$ run gts -m GtsGmscoreHostTestCases -t com.google.android.gts.devicepolicy.managedprovisioning.DeviceOwnerProvisioningHostsideTest#testRequiredAppsInManagedDevice	
```

### 2. 报错信息

```
junit.framework.AssertionFailedError
	at junit.framework.Assert.fail(Assert.java:55)
	at junit.framework.Assert.assertTrue(Assert.java:22)
	at junit.framework.Assert.assertTrue(Assert.java:31)
	at junit.framework.TestCase.assertTrue(TestCase.java:200)
	at com.google.android.gts.devicepolicy.managedprovisioning.DeviceOwnerProvisioningHostsideTest.testRequiredAppsInManagedDevice(DeviceOwnerProvisioningHostsideTest.java:69)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at junit.framework.TestCase.runTest(TestCase.java:177)
	at junit.framework.TestCase.runBare(TestCase.java:142)
	at com.android.tradefed.testtype.DeviceTestResult$1.protect(DeviceTestResult.java:90)
	at com.android.tradefed.testtype.DeviceTestResult.runProtected(DeviceTestResult.java:65)
	at com.android.tradefed.testtype.DeviceTestResult.run(DeviceTestResult.java:94)
	at junit.framework.TestCase.run(TestCase.java:130)
	at com.android.tradefed.testtype.DeviceTestCase.run(DeviceTestCase.java:181)
	at com.android.tradefed.testtype.JUnitRunUtil.runTest(JUnitRunUtil.java:54)
	at com.android.tradefed.testtype.JUnitRunUtil.runTest(JUnitRunUtil.java:38)
	at com.android.tradefed.testtype.DeviceTestCase.run(DeviceTestCase.java:146)
	at com.android.tradefed.testtype.HostTest.runRemoteTest(HostTest.java:664)
	at com.android.tradefed.testtype.HostTest.runTestClasses(HostTest.java:577)
	at com.android.tradefed.testtype.HostTest.run(HostTest.java:560)
	at com.android.compatibility.common.tradefed.testtype.JarHostTest.run(JarHostTest.java:56)
	at com.android.tradefed.testtype.suite.GranularRetriableTestWrapper.intraModuleRun(GranularRetriableTestWrapper.java:344)
	at com.android.tradefed.testtype.suite.GranularRetriableTestWrapper.run(GranularRetriableTestWrapper.java:264)
	at com.android.tradefed.testtype.suite.ModuleDefinition.run(ModuleDefinition.java:499)
	at com.android.tradefed.testtype.suite.ITestSuite.runSingleModule(ITestSuite.java:862)
	at com.android.tradefed.testtype.suite.ITestSuite.run(ITestSuite.java:744)
	at com.android.tradefed.invoker.InvocationExecution.runTest(InvocationExecution.java:889)
	at com.android.tradefed.invoker.InvocationExecution.runTests(InvocationExecution.java:714)
	at com.android.tradefed.invoker.TestInvocation.prepareAndRun(TestInvocation.java:507)
	at com.android.tradefed.invoker.TestInvocation.performInvocation(TestInvocation.java:257)
	at com.android.tradefed.invoker.TestInvocation.invoke(TestInvocation.java:1149)
	at com.android.tradefed.command.CommandScheduler$InvocationThread.run(CommandScheduler.java:631)
```

### 3. 解决方法

报错项目是不带通话的。可以通过去掉 `frameworks/native/data/etc/handheld_core_hardware.xml` 文件中的如下 Feature 来解决该问题:

```xml
<feature name="android.software.connectionservice" />
```

