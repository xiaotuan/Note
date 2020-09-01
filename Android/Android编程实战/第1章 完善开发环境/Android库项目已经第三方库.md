[toc]

### 1. 使用 JAR 库

如果使用 ProGuard 对应用的代码进行混幸福，会同时处理所有被引入的 JAR 文件。这在需要引入比较大的第三方库而只使用其中部分类时特别有用。要在项目中引入一个本地 JAR 依赖，只需像下面这样把它加入 `build.gradle` 的依赖部分：

```
dependencies {
    compile files('libs/android-support-v4.jar')
}
```

另一种方式是使用远程依赖仓库，比如中央 Maven 仓库。要想从远程仓库引入一个第三方库，只需按如下方式更新 `build.gradle` 文件：

```
repositories {
    mavenCentral()
}

dependencies {
    compile 'com.google.code.gson:gson:2.2.4'
}
```

> 可在 [http://search.maven.org/] 搜索第三方库。找到正确的库后只需点击版本号并把标识字符串复制到 gradle 的相应部分。需要注意的是，并非所有在中央 Maven 仓库找到的库都能得到 Android 的支持。首先还要参考文档。

### 2. 创建库项目

可在 Android Studio IDE 中建立库项目。只需创建一个 Android 库类型的模块，新的库项目会生成如下所示的 `gradle.build` 文件。

```
buildscript {
    repositories {
        maven { url 'http://repo1.maven.org/maven2' }
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:0.4'
    }
}
apply plugin: 'android-library'

dependencies {
    compile files('libs/android-support-v4.jar')
}

android {
    compileSdkVersion 17
    buildToolsVersion "17.0.0"
    
    defaultConfig {
        minSdkVersion 7
        targetSdkVersion 16
    }
}
```

要在应用程序的构建配置中引入库项目，只需像下面这样把它当做一个依赖引入。

```
dependencies {
    compile project(':libraries:MyLibrary')
}
```