<center><font size="5"><b>gradle设置编译使用的Java版本</b></font></center>

在项目跟目录下的 `build.gradle` 文件中定义 `Java` 版本的变量：

```text
buildscript {
	ext.java_version = JavaVersion.VERSION_1_8
}
```

按照如下代码修改 `app` 目录下的 `build.gradle` 文件：

```text
android {
	compileOptions {
        sourceCompatibility rootProject.ext.java_version
        targetCompatibility rootProject.ext.java_version
    }
}
```

