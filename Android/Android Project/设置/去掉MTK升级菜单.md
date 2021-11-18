[toc]

### 1. MTK8766、Android R

1. 修改 `device/mediatek/system/common/device.mk` 和 `device/mediatek/common/device.mk` 文件，将 `ro.vendor.mtk_system_update_support` 属性设置为 0：

   ```properties
   PRODUCT_SYSTEM_DEFAULT_PROPERTIES += ro.vendor.mtk_system_update_support=0
   ```

2. 修改 `vendor/mediatek/proprietary/packages/apps/MtkSettings/src/com/mediatek/settings/deviceinfo/CustomizeSoftwareUpdatePreferenceController.java` 文件，将 `isAvailable()` 方法返回 false 即可：

   ```diff
   @@ -42,7 +42,7 @@ public class CustomizeSoftwareUpdatePreferenceController extends AbstractPrefere
    
        @Override
        public boolean isAvailable() {
   -        return true;//mUm.isAdminUser() && isCustomizedSoftwareUpdateAvalible();
   +        return false;//mUm.isAdminUser() && isCustomizedSoftwareUpdateAvalible();
        }
    
        public static boolean isCustomizedSoftwareUpdateAvalible() {
   ```

> 提示：只用修改第二步的文件即可，第一步是 MTK 升级控制的属性，但是在实际代码中没有使用它对菜单进行控制。