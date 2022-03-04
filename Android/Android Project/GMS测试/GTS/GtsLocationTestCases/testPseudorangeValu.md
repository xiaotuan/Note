[toc]

### 1. 测试命令

```shell
$ run gts -m GtsLocationTestCases -t com.google.android.location.gts.gnss.GnssPseudorangeVerificationTest#testPseudorangeValue	
```

### 2. 报错信息

```
junit.framework.AssertionFailedError: Time elapsed without getting enough location fixes. Possibly, the test has been run deep indoors. Consider retrying test outdoors.
	at junit.framework.Assert.fail(Assert.java:50)
	at junit.framework.Assert.assertTrue(Assert.java:20)
	at com.google.android.location.gts.gnss.SoftAssert.failOrWarning(SoftAssert.java:174)
	at com.google.android.location.gts.gnss.GnssPseudorangeVerificationTest.testPseudorangeValue(GnssPseudorangeVerificationTest.java:143)
```

### 3. 解决办法

与驱动工程师沟通，只要确保 GPS 可以搜到星定到位即可解决该问题。