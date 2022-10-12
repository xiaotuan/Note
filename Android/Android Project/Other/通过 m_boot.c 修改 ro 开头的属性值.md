[toc]

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android 12

1. 修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/app/mt_boot/mt_boot.c` 文件如下代码：

   ```diff
   @@ -319,6 +319,54 @@ extern unsigned int g_fb_size;
    unsigned int logo_lk_t = 0;
    bool boot_ftrace = false;
    
   +// Add aceruuid info by qty at 2022-10-10 {{&&
   +static char bt_mac[6] = { 0 };
   +static char aceruuid[28] = { 0 };
   +
   +static int read_product_info(char *buf);
   +
   +static void reset_char_array(char* array, int length) {
   +       int i = 0;
   +       if (array != NULL) {
   +               for (i = 0; i < length; i++) {
   +                       array[i] = '\0';
   +               }
   +       }
   +}
   +
   +static void get_bt_mac() {
   +       pal_log_err("[LK][get_bt_mac] ....\n");
   +       #define BT_BUF_LEN 110 // barcode:64 + imei:40 + bt:6 + wifi:6
   +       char bt_buf[BT_BUF_LEN] = { 0 };
   +
   +       int i = 0;
   +       int tmp = 0;
   +       
   +       reset_char_array(bt_buf, BT_BUF_LEN + 1);
   +       reset_char_array(bt_mac, 6);
   +       
   +       tmp = mboot_recovery_load_raw_part("proinfo", bt_buf, BT_BUF_LEN);
   +       if (tmp != BT_BUF_LEN) {
   +               pal_log_err("[LK][get_bt_mac] read proinfo fail, only read size %d, block size %d.\n", tmp, BT_BUF_LEN);
   +               return;
   +       }
   +       tmp = 104;
   +       for (; tmp < BT_BUF_LEN && i < 6; tmp++, i++) {
   +               bt_mac[i] = bt_buf[tmp];
   +       }
   +       pal_log_err("[LK][get_bt_mac] Bluetooth mac: %02X%02X%02X%02X%02X%02X\n", bt_buf[104], bt_buf[105], bt_buf[106], bt_buf[107], bt_buf[108], bt_buf[109]);
   +}
   +
   +static void get_aceruuid() {
   +       pal_log_err("[LK][get_aceruuid] ....\n");
   +       reset_char_array(aceruuid, 28);
   +       get_bt_mac();
   +       if (sprintf(aceruuid, "000000000000000%02X%02X%02X%02X%02X%02X", bt_mac[0], bt_mac[1], bt_mac[2], bt_mac[3], bt_mac[4], bt_mac[5]) < 0) {
   +               pal_log_err("[LK][get_aceruuid] sprintf fail.\n");
   +       }
   +}
   +// &&}}
   +
    static int boot_time_via_dt(void *fdt, unsigned int *lk_boot_time)
    {
           int offset, nodeoffset, ret = 0;
   @@ -1432,6 +1480,13 @@ int boot_linux_fdt(void *kernel, unsigned *tags,
           /* Append androidboot.serialno=xxxxyyyyzzzz in cmdline */
           snprintf(tmpbuf, TMPBUF_SIZE, "%s%s", "androidboot.serialno=", sn_buf);
           cmdline_append(tmpbuf);
   +       
   +       // Add aceruuid info by qty at 2022-10-10 {{&&
   +       get_aceruuid();
   +       pal_log_err("[LK][boot_linux_fdt] aceruuid: %s.\n", aceruuid);
   +       snprintf(tmpbuf, TMPBUF_SIZE, "%s%s", "androidboot.aceruuid=", aceruuid);
   +       cmdline_append(tmpbuf);
   +       // &&}}
    
           get_reboot_reason(boot_reason);
   ```

   > 提示：代码会将 `androidboot.aceruuid=xxxxx` 值添加到 `/proc/cmdline` 中，最后在 `system/core/init/property_service.cpp` 文件中会将其解析为 `ro.boot.aceruuid` 属性和其值。

2. 修改 `system/core/init/property_service.cpp` 文件如下代码，将生成的 `ro.boot.xxxx` 属性及其值转换成需要的属性和其值：

   ```diff
   @@ -1618,6 +1722,10 @@ static void ExportKernelBootProps() {
        } prop_map[] = {
                // clang-format off
            { "ro.boot.serialno",   "ro.serialno",   UNSET, },
   +               // Create ro.device.sn property by qty at 2022-10-10
   +               { "ro.boot.serialno",   "ro.device.sn",   UNSET, },
   +               // Create ro.aceruuid property by qty at 2022-10-10
   +               { "ro.boot.aceruuid",   "ro.aceruuid",   UNSET, },
            { "ro.boot.mode",       "ro.bootmode",   "unknown", },
            { "ro.boot.baseband",   "ro.baseband",   "unknown", },
            { "ro.boot.bootloader", "ro.bootloader", "unknown", },
   ```

   