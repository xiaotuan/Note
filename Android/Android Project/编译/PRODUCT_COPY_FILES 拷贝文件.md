使用 PRODUCT_COPY_FILES 拷贝文件的格式如下：

```makefile
PRODUCT_COPY_FILES += 要拷贝的文件路径:拷贝到的文件路径
```

例如要将 device/qcom/media/demo.xml 拷贝到 system/etc/demo.xml 中的代码如下：

```makefile
PRODUCT_COPY_FILES += device/qcom/media/demo.xml:,$(PRODUCT_OUT)/system/etc/demo.xml
```

