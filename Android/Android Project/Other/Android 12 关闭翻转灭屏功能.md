> 提示：功能实现代码位置为：`frameworks/base/services/core/java/com/android/server/power/FaceDownDetector.java`。

修改 `frameworks/base/core/res/res/values/config.xml` 文件，将 `config_flipToScreenOffEnabled` 的值设置为 false 即可。例如：

```xml
<!-- Boolean indicating if placing the phone face down will result in a screen off. -->
<bool name="config_flipToScreenOffEnabled">false</bool>
```

