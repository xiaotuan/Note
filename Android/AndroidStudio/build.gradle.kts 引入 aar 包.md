创建工程时，在 Build configuration language 中选择 Kotlin DSL (build.gradle.kts) [Recommended] 。如果需要在 build.gradle.kts 文件向工程引入 aar 可以按照下面步骤操作：

1. 将 aar 文件拷贝到 app/libs 目录下

2. 在 app/build.gradle.kts 文件中 dependencies 项中添加如下代码：

   ```
   implementation(fileTree(baseDir = "libs"))
   ```

   或者

   ```
   implementation(files("libs/achartengine-1.2.0.aar"))
   ```

   