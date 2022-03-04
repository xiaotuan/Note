[toc]

### 1. MTK 平台

#### 1.1 MTK8766、Android R

修改 `frameworks/base/core/res/res/values/config.xml` 文件中 `config_dozeComponent` 的值为 `com.android.systemui/com.android.systemui.doze.DozeService`：

```xml
<string name="config_dozeComponent" translatable="false">com.android.systemui/com.android.systemui.doze.DozeService</string>
```

