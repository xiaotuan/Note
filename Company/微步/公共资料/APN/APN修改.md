[toc]

### 1. 展讯平台

#### 1. Android R

根据 `verdor/sprd/telephony-res/apply_telephony_res.mk` 文件判断最终使用那个 APN 配置文件。

```makefile
TELE_RES_DIR := vendor/sprd/telephony-res

################# apn
APN_VERSION := $(shell cat frameworks/base/core/res/res/xml/apns.xml|grep "<apns version"|cut -d \" -f 2)
apn_src_file := $(TELE_RES_DIR)/apn/apns-conf_$(APN_VERSION).xml
apn_src_file_v2 := $(TELE_RES_DIR)/apn/apns-conf_$(APN_VERSION)_v2.xml
ifneq (,$(wildcard $(apn_src_file)))

ifneq ($(filter $(strip $(PLATFORM_VERSION)),Q 10 R 11),)
PRODUCT_COPY_FILES += \
    $(apn_src_file_v2):product/etc/apns-conf.xml
else
PRODUCT_COPY_FILES += \
    $(apn_src_file):system/etc/apns-conf.xml
endif

PRODUCT_COPY_FILES += \
    $(apn_src_file):system/etc/old-apns-conf.xml
else
$(warning "APN config file: $(apn_src_file) not found, apn version: $(APN_VERSION)")
endif
......
```

从上面的代码中可以看出工程最终使用的是 apn_src_file_v2 文件，也就是 `vendor\sprd\telephony-res\apn\apns-conf_8_v2.xml` 文件。

因此要修改 APN 配置文件可以通过修改 `vendor\sprd\telephony-res\apn\apns-conf_8_v2.xml` 文件来实现。

