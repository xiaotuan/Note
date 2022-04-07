[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

1. 修改 `device/mediatek/common/device.mk` 文件

   ```diff
   @@ -4269,18 +4269,18 @@ PRODUCT_PACKAGES += InProcessTetheringResOverlay
    PRODUCT_PACKAGES += GoogleTetheringResOverlay
    
    # Stk APP built in according to package.
   -ifneq ($(strip $(MTK_TB_WIFI_3G_MODE)),WIFI_ONLY)
   -# if telephony add on not support, no need to install telephony add on related APKs
   -  ifeq ($(strip $(MTK_TELEPHONY_ADD_ON_POLICY)), 0)
   -    ifneq ($(strip $(MTK_TC1_COMMON_SERVICE)), yes)
   -      PRODUCT_PACKAGES += Stk1
   -    else
   -      PRODUCT_PACKAGES += Stk
   -    endif
   -  else
   -    PRODUCT_PACKAGES += Stk
   -  endif
   -endif
   +# ifneq ($(strip $(MTK_TB_WIFI_3G_MODE)),WIFI_ONLY)
   +# # if telephony add on not support, no need to install telephony add on related APKs
   +#   ifeq ($(strip $(MTK_TELEPHONY_ADD_ON_POLICY)), 0)
   +#     ifneq ($(strip $(MTK_TC1_COMMON_SERVICE)), yes)
   +#       PRODUCT_PACKAGES += Stk1
   +#     else
   +#       PRODUCT_PACKAGES += Stk
   +#     endif
   +#   else
   +#     PRODUCT_PACKAGES += Stk
   +#   endif
   +# endif
    
    ifneq ($(strip $(MTK_BASIC_PACKAGE)), yes)
    # privapp-permissions whitelisting
   ```

2. 修改 `device/mediatek/system/common/device.mk` 文件

   ```diff
   @@ -3000,18 +3000,18 @@ endif
    
    
    # Stk APP built in according to package.
   -ifneq ($(strip $(MTK_TB_WIFI_3G_MODE)),WIFI_ONLY)
   -# if telephony add on not support, no need to install telephony add on related APKs
   -  ifeq ($(strip $(MSSI_MTK_TELEPHONY_ADD_ON_POLICY)), 0)
   -    ifneq ($(strip $(MSSI_MTK_TC1_COMMON_SERVICE)), yes)
   -      PRODUCT_PACKAGES += Stk1
   -    else
   -      PRODUCT_PACKAGES += Stk
   -    endif
   -  else
   -    PRODUCT_PACKAGES += Stk
   -  endif
   -endif
   +# ifneq ($(strip $(MTK_TB_WIFI_3G_MODE)),WIFI_ONLY)
   +# # if telephony add on not support, no need to install telephony add on related APKs
   +#   ifeq ($(strip $(MSSI_MTK_TELEPHONY_ADD_ON_POLICY)), 0)
   +#     ifneq ($(strip $(MSSI_MTK_TC1_COMMON_SERVICE)), yes)
   +#       PRODUCT_PACKAGES += Stk1
   +#     else
   +#       PRODUCT_PACKAGES += Stk
   +#     endif
   +#   else
   +#     PRODUCT_PACKAGES += Stk
   +#   endif
   +# endif
    
    ifneq ($(strip $(MTK_BASIC_PACKAGE)), yes)
      # privapp-permissions whitelisting
   ```

   