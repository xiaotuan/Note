<center>
  <font size="5">
  	<b>定义gradle变量</b>
  </font>
</center>

[toc]

#### 1. 定义变量

可以通过两种方式定义gradle变量。

1. 在app目录下build.gradle文件中定义，定义方式如下：

```
ext {
	变量名 = 变量值
}
```

或者 

```json
dependencies {
    def nav_version = '2.2.1'
}
```



例如

```
ext {
    exoplayer_version = "2.7.0"
    supportlib_version = "27.1.0"
    anko_version = "0.10.4"
}
```

2. 在项目根目录下的gradle.properties文件中定义，定义方式如下：

```
变量名 = 变量值
```

例如：

```
EXOPLAYER_VERSION = r2.11.3
```

3. 在根目录下的 `build.gradle` 文件中使用如下方法定义：

```json
buildscript {
    ext.java_version = JavaVersion.VERSION_1_8
}
```



#### 2. 使用gradle变量

直接就可以使用该变量，例如：

```
defaultConfig {
  applicationId "com.example.android.videoplayersample"
  minSdkVersion MINSDK_VERSION
  targetSdkVersion 29
  versionCode 1
  versionName "1.0"
}

android {
    kotlinOptions {
    	jvmTarget = "$rootProject.ext.java_version"
    }
}
```

如果在字符串中使用，字符串需要使用双引号（ " ）括起来，不能使用单引号（ ' ），在变量名前面添加（ $ ）符号，可以使用大括号（ {} ）将变量名括起来，也可以不用：

```
dependencies {
		......
    implementation "com.google.android.exoplayer:exoplayer:$EXOPLAYER_VERSION"   
}
```

或者

```
dependencies {
		......
    implementation "com.google.android.exoplayer:exoplayer:${EXOPLAYER_VERSION}"   
}
```

