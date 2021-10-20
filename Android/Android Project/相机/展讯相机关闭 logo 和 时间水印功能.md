修改 `device/sprd/sharkl3/s9863a1h10_go_32b/module/camera/md.mk` 文件，将 `TARGET_BOARD_LOGOWATERMARK_SUPPORT` 和 `TARGET_BOARD_TIMEWATERMARK_SUPPORT` 的值设置为 false，例如：

```cpp
#watermark,logo watermark, time watermark
TARGET_BOARD_LOGOWATERMARK_SUPPORT := false
TARGET_BOARD_TIMEWATERMARK_SUPPORT := false
```
