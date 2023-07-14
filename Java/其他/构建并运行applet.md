构建并运行 `applet` 命令如下：

```shell
# 编译 java 文件
javac 文件名.java
# 打包 编译后的 class
jar cvfm 文件名.jar 文件名.mf *.class
# 运行 html
appletviewer 文件名.html
```

**mf** 文件内容如下：

```
Manifest-Version: 1.0
Permissions: sandbox
```

