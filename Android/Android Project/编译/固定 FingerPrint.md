[toc]

### 1. 展讯平台

#### 1.1 SC9863A Android R

修改 `build/make/core/version_defaults.mk` 文件，将如下代码：

```makefile
BUILD_NUMBER := $(shell date +%s)
```

修改成固定值即可，例如：

```makefile
BUILD_NUMBER := 1632390036
```



