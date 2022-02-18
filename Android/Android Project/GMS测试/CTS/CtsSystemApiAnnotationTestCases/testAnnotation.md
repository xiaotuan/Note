[toc]

### 1. 测试命令

```shell
$ run cts -m CtsSystemApiAnnotationTestCases -t android.signature.cts.api.AnnotationTest#testAnnotation
```

### 2. 报错信息

```
	
java.lang.NoClassDefFoundError: Class not found using the boot class loader; no stack trace available
```

### 3. 解决方法

该项豁免。