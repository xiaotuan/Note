[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

NTC 提示宏是 `WEIBU_NTC_SUPPORT = yes`。

温度阈值属性：

+ `ro.wb.battery.high.shutdown`：高温关机温度阈值，例如 `ro.wb.battery.high.shutdown=620`

+ `ro.wb.battery.high.info`：高温弹框温度阈值，例如 `ro.wb.battery.high.info=550`

+ `ro.wb.battery.low.info`：低温弹框温度阈值（未实现，默认是 0 度），例如 `ro.wb.battery.low.info=0` 。可以参照如下代码实现：

  修改 `sys/vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/power/PowerUI.java` 文件中 `onReceive()` 方法的如下代码：

  ```diff
  @@ -329,6 +329,7 @@ public class PowerUI extends CoreStartable implements CommandQueue.Callbacks {
                                  
                                  int temperatureHighShutdown = SystemProperties.getInt("ro.wb.battery.high.shutdown", 620);
                                  int temperatureHighInfo = SystemProperties.getInt("ro.wb.battery.high.info", 550);
  +                               int temperatureLowInfo = SystemProperties.getInt("ro.wb.battery.low.info", 0);
                                  int temperatureLowShutdown = SystemProperties.getInt("ro.wb.battery.low.shutdown", -100);
                                  int ntc_support = SystemProperties.getInt("ro.wb.ntc_support", 0);
                                  
  @@ -359,7 +360,7 @@ public class PowerUI extends CoreStartable implements CommandQueue.Callbacks {
                                                  isShowingHighShutdownDialog = false;
                                                  isShowingHighTemperatureDialog = false;
                                                  isShowingLowTemperatureDialog = false;
  -                                       } else if ((temperature > temperatureLowShutdown &&  temperature <=0) && !isShowingLowTemperatureDialog) {
  +                                       } else if ((temperature > temperatureLowShutdown &&  temperature <=temperatureLowInfo) && !isShowingLowTemperatureDialog) {
                                                  Log.i("wcm>-90","temperature --> :"+temperature);
                                                  mWarnings.showLowTemperatureDialog();
                                                  isShowingHighShutdownDialog = false;
  ```

+ `ro.wb.battery.low.shutdown`：低温关机温度阈值，例如 `ro.wb.battery.low.shutdown=-100`。