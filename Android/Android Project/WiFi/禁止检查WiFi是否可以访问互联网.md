[toc]

### 方法一

修改 `packages/modules/NetworkStack/src/com/android/server/connectivity/NetworkMonitor.java` 文件中的 `getIsCaptivePortalCheckEnabled()` 方法，让其返回 false 即可。

```java
private boolean getIsCaptivePortalCheckEnabled() {
    String symbol = CAPTIVE_PORTAL_MODE;
    int defaultValue = CAPTIVE_PORTAL_MODE_PROMPT;
    int mode = mDependencies.getSetting(mContext, symbol, defaultValue);
    return false;//mode != CAPTIVE_PORTAL_MODE_IGNORE;
}
```

### 方法二

修改 `frameworks/base/packages/SettingsProvider/src/com/android/providers/settings/DatabaseHelper.java` 文件的 `loadGlobalSettings()` 方法，在该方法中添加如下代码：

```java
loadSetting(stmt, "captive_portal_mode", 0);
```

其值可以设置为如下值：

+ `0` ：Don't attempt to detect captive portals.
+ `1`： When detecting a captive portal, display a notification that prompts the user to sign in.
+ `2`：When detecting a captive portal, immediately disconnect from the network and do not reconnect to that network in the future.

