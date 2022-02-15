[toc]

### 1. 测试命令

```shell
$ run cts -t CtsPermission3TestCases -m android.permission3.cts.PermissionTest23#testGrantPreviouslyRevokedWithPrejudiceShowsPrompt
```

### 2. 报错信息

```
com.android.compatibility.common.util.UiDumpUtils$UiDumpWrapperException: View not found after waiting for 10000ms: BySelector [RES='\Qcom.android.permissioncontroller:id/permission_allow_foreground_only_button\E']
```

### 3. 解决方法

该项豁免。