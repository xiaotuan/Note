使用 PRODUCT_COPY_FILES 拷贝文件夹的格式如下：

```makefile
PRODUCT_COPY_FILES += $(call find-copy-subdir-files,*,要拷贝的文件夹路径,拷贝到的文件夹路径)
```

例如要将 `device/fsl/imx8q/userdata/app` 拷贝到 `system/app` 中的代码如下：

```makefile
PRODUCT_COPY_FILES += $(call find-copy-subdir-files,*,device/fsl/imx8q/userdata/app,,$(PRODUCT_OUT)/system/app)
```

