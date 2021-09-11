[toc]

### 1. 修改 `device/mediateksample/M863PR_64/ProjectConfig.mk` 文件

将 `MTK_LCM_PHYSICAL_ROTATION` 设置成需要的方向即可，比如 270 或者 90。例如：

```makefile
MTK_LCM_PHYSICAL_ROTATION = 270
```

### 2. 修改 `kernel-4.14/arch/arm64/configs/M863PR_64_defconfig` 文件

将 `CONFIG_MTK_LCM_PHYSICAL_ROTATION` 设置成需要的方向即可，比如 270 或者 90。例如：

```
CONFIG_MTK_LCM_PHYSICAL_ROTATION="270"
```

将屏幕宽高调换：

```makefile
CONFIG_LCM_HEIGHT="800"
CONFIG_LCM_WIDTH="1280"
```

### 3. 修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/project/M863PR_64.mk` 文件

将 `MTK_LCM_PHYSICAL_ROTATION` 设置成需要的方向即可，比如 270 或者 90。例如：

```makefile
MTK_LCM_PHYSICAL_ROTATION = 270
```

### 4. 修改 `device/mediatek/system/common/system.prop` 文件

将 `ro.wb.auto_rotation` 属性设置成 `false`，例如：

```properties
ro.wb.auto_rotation=false
```

### 5. 修改 `frameworks/base/cmds/bootanimation/BootAnimation.cpp` 文件

在 `readyToRun()` 方法的如下位置：

```cpp
// create the native surface
sp<SurfaceControl> control = session()->createSurface(String8("BootAnimation"),
                                                      resolution.getWidth(), resolution.getHeight(), PIXEL_FORMAT_RGB_565);

SurfaceComposerClient::Transaction t;
// 在此添加代码
// this guest property specifies multi-display IDs to show the boot animation
// multiple ids can be set with comma (,) as separator, for example:
// setprop persist.boot.animation.displays 19260422155234049,19261083906282754
Vector<uint64_t> physicalDisplayIds;
char displayValue[PROPERTY_VALUE_MAX] = "";
property_get(DISPLAYS_PROP_NAME, displayValue, "");
```

添加如下代码：

```cpp
Rect destRect(resolution.getWidth(), resolution.getHeight());
t.setDisplayProjection(mDisplayToken,ui::ROTATION_0,destRect,destRect);
```



