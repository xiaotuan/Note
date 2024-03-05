获取 `Widevine` 安全级别方法如下（简称 L1）：

```java
import android.media.MediaDrm;

import java.util.UUID;

public String getWidevineSecurityLevel() {
    String securityLevel = null;
    UUID WIDEVINE_UUID = new UUID(0xEDEF8BA979D64ACEL, 0xA3C827DCD51D21EDL);
    String SECURITY_LEVEL_PROPERTY = "securityLevel";
	try {
        MediaDrm mediaDrm = new MediaDrm(WIDEVINE_UUID);
        securityLevel = mediaDrm.getPropertyString(SECURITY_LEVEL_PROPERTY);
    } catch (Exception e) {
        Log.d(TAG, "getWidevineSecurityLevel=>error: ", e);
    }
    return securityLevel;
}
```



