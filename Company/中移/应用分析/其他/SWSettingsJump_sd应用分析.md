​        SWSettingsJump_sd 应用的主要功能是实现一个和原始 Settings 应用一样的包名的应用，当第三方应用调用原始 Settings 应用时，将通过该应用跳转到朝歌的设置应用。

核心代码如下所示：

```java
@Override
protected void onResume() {
    startSetting();	
    super.onResume();
}

// 启动设置界面
private void startSetting() {
    Intent intent = new Intent();
    intent.setAction("android.settings.SETTINGS");
    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    startActivity(intent);
    finish();
}
```

