### 14.4.2　Gradle构建方式

如果通过Gradle方式来添加kotlinx.html依赖，则可以在项目的build.gradle脚本文件中添加如下配置信息。

```python
repositories {
    jcenter()
}
dependencies {
    def kotlinx_html_version = "0.6.9"  // kotlinx.html版本
    compile "org.jetbrains.kotlinx:kotlinx-html-jvm:${kotlinx_html_version}"
    compile "org.jetbrains.kotlinx:kotlinx-html-js:${kotlinx_html_version}"
    }
```

除此之外，还可以使用npm和Bintray仓库来添加kotlinx.html环境配置。如果通过npm方式安装，安装的命令如下。

```python
npm install kotlinx-html
```

kotlinx.html的最新版本发布在JCenter仓库上，可以通过下面的地址来添加JCenter仓库的配置。

```python
repositories {
        maven { url 'https://jitpack.io' } mavenCentral()
        jcenter()       
        //…
        }
```

