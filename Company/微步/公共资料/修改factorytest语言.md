[toc]

### 1. 展讯平台

#### 1.1 Android R

修改 `vendor/sprd/proprietories-source/factorytest/Android.mk`文件，将文件中如下代码：

```makefile
LOCAL_CFLAGS += -DLANGUAGE_CN
```

注释或者去掉即可。