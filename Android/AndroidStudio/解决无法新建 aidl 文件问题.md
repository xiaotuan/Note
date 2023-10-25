执行 `File` -> `New` -> `AIDL` -> `AIDL File` ，`AIDL File` 置灰无法点击，且菜单显示为：

```
AIDL File (Requires setting the buildFeatures.aidl to true in the build file)
```

解决版本如下：

在 `app` 目录下的 `build.gradle` 文件中的 `android` 节点末尾添加如下代码：

```
buildFeatures {
	aidl true
}
```

最终代码如下：

```
android {
	......
	
	buildFeatures {
        aidl true
    }
}
```

