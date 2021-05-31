下面的代码是为新项目创建的默认 `build.gradel` 文件。第一个区块告诉 gradle 使用哪个仓库下载构建所用的插件以及依赖（这个依赖不同于后面即将介绍的项目依赖）。接下来的部分告诉 gradle 应用哪种插件，本例中使用的是 Android 插件，基于此即可开展后面的 Android 开发。再下面是项目的依赖，本例只使用了位于 libs 目录里的支持包。最后的区块以 android 开头，定义了项目的配置项。

```
buildscript {
    repositories {
        maven { url 'http://repo1.maven.org/maven2' }
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:0.5+'
    }
}
apply plugin: 'android'

dependencies {
    compile files{'libs/android-support-v4.jar'}
}

android {
    compileSdkVersion 18
    buildToolsVersion "18.0.0"
    
    defaultConfig {
        minSdkVersion 18
        targetSdkVersion 18
    }
}
```

> 可在 http://tools.android.com/tech-docs/new-build-system/user-guide 查看新的 Gradle 构建系统用户手册。

虽然可以直接在 Android Studio IDE 中构建运行项目，也可以通过命令行与构建系统交互。Gradle 定义了一系列任务。在项目根目录下输入如下命令即可列出所有可用的任务。

```shell
$ ./gradlew tasks
```

比如，如果从头开始构建应用程序，只需运行下面的命令。

```shell
$ ./gradlew clean build
```

**从现有项目迁移到 Gradle**

由于大部分现有 Android 项目并没有使用 Gradle 构建系统，所以需要一个迁移向导。最简单的迁移方法是使用 Android Studio 创建新的 Android 项目，然后把原项目复制到新项目的子文件夹内。

接下来把 Android Studio 创建的 build.gradle 文件复制到已迁移项目的根目录下。

```
android {
    sourceSets {
        main {
            manifest.srcFile 'AndroidManifest.xml'
            java.srcDirs = ['src']
            resources.srcDirs = ['src']
            aidl.srcDirs = ['src']
            renderscript.srcDirs = ['src']
            res.srcDirs = ['res']
            assets.srcDirs = ['assets']
        }
    }
}
```

