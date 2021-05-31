> 摘自：<https://blog.csdn.net/arrol1786936883/article/details/82429065>

### 蓝牙默认名称设置所在文件

Android4.4：LINUX/android/external/bluetooth/bluedroid/btif/src/btif_dm.c
Android8.+：LINUX/android/system/bt/btif/src/btif_dm.cc
其他：LINUX/android/system/bt/btif/src/btif_dm.c （不同版本btif_dm.c的路径可能不同）

### 具体方法

在btif_dm.c（btif_dm.cc）中的 btif_get_default_local_name 方法用来设置蓝牙默认名称

```
static char* btif_get_default_local_name() {
    if (btif_default_local_name[0] == '\0')
    {
        int max_len = sizeof(btif_default_local_name) - 1;
        if (BTM_DEF_LOCAL_NAME[0] != '\0')
        {
            strncpy(btif_default_local_name, BTM_DEF_LOCAL_NAME, max_len);
        }
        else
        {
            char prop_model[PROPERTY_VALUE_MAX];
            property_get(PROPERTY_PRODUCT_MODEL, prop_model, "");
            strncpy(btif_default_local_name, prop_model, max_len);
        }
        btif_default_local_name[max_len] = '\0';
    }
    return btif_default_local_name;
}123456789101112131415161718
```

Android8.+的该方法有细微的改动

```
static char* btif_get_default_local_name() {
  if (btif_default_local_name[0] == '\0') {
    int max_len = sizeof(btif_default_local_name) - 1;
    if (BTM_DEF_LOCAL_NAME[0] != '\0') {
      strncpy(btif_default_local_name, BTM_DEF_LOCAL_NAME, max_len);
    } else {
      char prop_model[PROPERTY_VALUE_MAX];
      osi_property_get(PROPERTY_PRODUCT_MODEL, prop_model, "");
      strncpy(btif_default_local_name, prop_model, max_len);
    }
    btif_default_local_name[max_len] = '\0';
  }
  return btif_default_local_name;
}1234567891011121314
```

在btif_get_default_local_name方法中返回的btif_default_local_name就是蓝牙的默认名称；

方法中会先去判断BTM_DEF_LOCAL_NAME是否为空，如果不为空则将值赋给btif_default_local_name；
BTM_DEF_LOCAL_NAME在LINUX/android/device/qcom/common/bdroid_buildcfg.h文件中定义的：

```
#ifndef _BDROID_BUILDCFG_H
#define _BDROID_BUILDCFG_H
#define BTM_DEF_LOCAL_NAME "QCOM-BTD" //默认值
// Disables read remote device feature
#define MAX_ACL_CONNECTIONS 16
#define MAX_L2CAP_CHANNELS 16
#define BLE_VND_INCLUDED TRUE
// skips conn update at conn completion
#define BT_CLEAN_TURN_ON_DISABLED 1

/* Increasing SEPs to 12 from 6 to support SHO/MCast i.e. two streams per codec */
#define AVDT_NUM_SEPS 12
#endif12345678910111213
```

在bdroid_buildcfg.h文件中修改BTM_DEF_LOCAL_NAME值可以对蓝牙的默认名称进行修改。

如果一套代码供多个项目项目使用，不同项目需要显示不同的蓝牙名称，则需要走btif_get_default_local_name方法中另外一种情况：获取项目中的某一个属性来作为蓝牙名称（也可以自定义一个属性来用于设置蓝牙默认名称），前置条件：需要在bdroid_buildcfg.h中将BTM_DEF_LOCAL_NAME值置为空。

```
#define BTM_DEF_LOCAL_NAME ""1
```

源码中获取“ro.product.model”属性来设置蓝牙名称

```
#define PROPERTY_PRODUCT_MODEL "ro.product.model"
else {
            char prop_model[PROPERTY_VALUE_MAX];
            property_get(PROPERTY_PRODUCT_MODEL, prop_model, ""); //获取属性然后赋值
            strncpy(btif_default_local_name, prop_model, max_len);
 }123456
```

ro.product.model 属性在LINUX/android/device/qcom/xxx/xxx/overrides.prop中定义的（中间的x路径根据自己具体项目来确定）

```
service.adb.root=1
persist.service.adb.root=1
qemu.hw.mainkeys=1

ro.product.name=Big
ro.product.device=msm8909
ro.product.board=msm8909

ro.build.display.id=HuangDaXian
ro.product.brand=HuangDaXian
ro.product.model=Hello //调用这个值来设置默认名称，可以根据自己需求改动
ro.bluebank.sw_base=Post-CS2_0.0.032.2
ro.bluebank.iver=HuangDaXian-000-01-03-09.03.2018
ro.build.version.incremental=HuangDaXian-000-01-03-09.03.2018
ro.bluebank.hwv=V1
```