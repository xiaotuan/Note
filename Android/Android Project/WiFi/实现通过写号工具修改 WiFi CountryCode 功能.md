[toc]

### 1. MTK

#### 1.1 Android 12

##### 1.1.1 MT8788

1. 修改 `kernel-4.19/arch/arm64/boot/dts/mediatek/M100BSR100/mt6771.dts` 文件如下代码：

   ```diff
   @@ -4655,6 +4655,11 @@ firmware_class.path=/vendor/firmware loop.max_part=7 clk_ignore_unused";
                   compatible =  "gpio-keys";
           };
    
   +       cust_wifi: cust_wifi {
   +               compatible = "weibu,cust_wifi";
   +               status = "okay";
   +       };
   +
    };
    
    #include "mediatek/M100BSR100/mt6358.dtsi"
   ```

2. 修改 `kernel-4.19/drivers/weibu/Kconfig` 如下代码：

   ```diff
   @@ -204,4 +204,8 @@ config WB_ACCDET_EINT_TYPE_HIGH
        bool "CONFIG_WB_ACCDET_EINT_TYPE_HIGH"
        default n
        help
   -      This is to accdet eint type high   
   \ No newline at end of file
   +      This is to accdet eint type high   
   +
   +config WB_WIFI_CC_SUPPORT
   +        bool "CONFIG_WB_WIFI_CC_SUPPORT=y"
   +        default n
   \ No newline at end of file
   ```

3. 修改 `vendor/mediatek/kernel_modules/connectivity/wlan/core/gen3/common/wlan_oid.c` 如下代码：

   ```diff
   @@ -9732,6 +9732,10 @@ wlanoidQueryEepromType(IN P_ADAPTER_T prAdapter,
    * \retval WLAN_STATUS_FAILURE
    */
    /*----------------------------------------------------------------------------*/
   +#if IS_ENABLED(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221031
   +extern uint32_t wificc;
   +#endif
   +
    WLAN_STATUS
    wlanoidSetCountryCode(IN P_ADAPTER_T prAdapter,
                         IN PVOID pvSetBuffer, IN UINT_32 u4SetBufferLen, OUT PUINT_32 pu4SetInfoLen)
   @@ -9748,6 +9752,12 @@ wlanoidSetCountryCode(IN P_ADAPTER_T prAdapter,
    
           prAdapter->rWifiVar.rConnSettings.u2CountryCode = (((UINT_16) pucCountry[0]) << 8) | ((UINT_16) pucCountry[1]);
    
   +#if IS_ENABLED(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221031
   +       prAdapter->rWifiVar.rConnSettings.u2CountryCode = (((wificc >> 8) & 0xFF) | ((wificc & 0xFF) << 8));
   +       DBGLOG(INIT, INFO, "Leo wlanoidSetCountryCode = 0x%X\n", wificc);
   +#endif
   +
   +
           /* Force to re-search country code in regulatory domains */
           prAdapter->prDomainInfo = NULL;
           rlmDomainSendCmd(prAdapter);
   ```

4. 修改 `vendor/mediatek/kernel_modules/connectivity/wlan/core/gen3/os/linux/gl_init.c` 如下代码：

   ```diff
   @@ -772,6 +772,28 @@ static int wlanSetMacAddress(struct net_device *ndev, void *addr)
           return WLAN_STATUS_SUCCESS;
    }                              /* end of wlanSetMacAddr() */
    
   +#if IS_ENABLED(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221031
   +#include <linux/of.h>
   +#include <linux/of_device.h>
   +uint32_t wificc = 0x00;
   +static uint32_t rlmDomainAlpha2ToU32(uint8_t *pcAlpha2, uint8_t ucAlpha2Size)
   +{
   +       uint8_t ucIdx;
   +       uint32_t u4CountryCode = 0;
   +
   +       if (ucAlpha2Size > 4) {
   +               DBGLOG(RLM, ERROR, "alpha2 size %d is invalid!(max: %d)\n",
   +                       ucAlpha2Size, 4);
   +               ucAlpha2Size = 4;
   +       }
   +
   +       for (ucIdx = 0; ucIdx < ucAlpha2Size; ucIdx++)
   +               u4CountryCode |= (pcAlpha2[ucIdx] << (ucIdx * 8));
   +
   +       return u4CountryCode;
   +}
   +#endif
   +
    /*----------------------------------------------------------------------------*/
    /*!
    * \brief Load NVRAM data and translate it into REG_INFO_T
   @@ -788,6 +810,13 @@ static void glLoadNvram(IN P_GLUE_INFO_T prGlueInfo, OUT P_REG_INFO_T prRegInfo)
           UINT_8 aucTmp[2] = {0};
           PUINT_8 pucDest;
    
   +#if IS_ENABLED(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221101
   +       int ret;
   +       struct device_node *pnode = NULL;
   +       const char *country_code = "EU";
   +       char temp[5] = {0};
   +#endif
   +
           ASSERT(prGlueInfo);
           ASSERT(prRegInfo);
    
   @@ -816,6 +845,36 @@ static void glLoadNvram(IN P_GLUE_INFO_T prGlueInfo, OUT P_REG_INFO_T prRegInfo)
                   prRegInfo->au2CountryCode[0] = (UINT_16) aucTmp[0];
                   prRegInfo->au2CountryCode[1] = (UINT_16) aucTmp[1];
    
   +#if IS_ENABLED(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221031
   +       DBGLOG(INIT, INFO, "Leo before wlan cc:0x%X 0x%X \n",
   +               prRegInfo->au2CountryCode[0], prRegInfo->au2CountryCode[1]);
   +
   +       pnode = of_find_compatible_node(NULL, NULL, "weibu,cust_wifi");
   +       if (!pnode) {
   +               DBGLOG(INIT, INFO,"%s :failed to get pnode\n",__func__);
   +       }
   +
   +       ret = of_property_read_string(pnode, "wificc", (const char **)&country_code);
   +       if (ret) {
   +               DBGLOG(INIT, INFO,"[%s]: of_property_read_string wificc failed: %d\n",
   +                               __func__, ret);
   +       }
   +
   +       strcpy(temp, country_code);
   +       wificc = rlmDomainAlpha2ToU32(temp, strlen(temp));
   +
   +       prRegInfo->au2CountryCode[0] =
   +               (uint16_t) (wificc & 0xFF);
   +       prRegInfo->au2CountryCode[1] =
   +               (uint16_t) ((wificc >> 8) & 0xFF);
   +
   +       prGlueInfo->prAdapter->rWifiVar.rConnSettings.u2CountryCode = 
   +               (((UINT_16) prRegInfo->au2CountryCode[0]) << 8) | (((UINT_16) prRegInfo->au2CountryCode[1]) & BITS(0, 7));
   +
   +       DBGLOG(INIT, INFO, "Leo after wificc:%s:0x%X cc:0x%X 0x%X \n",temp,wificc, 
   +               prRegInfo->au2CountryCode[0], prRegInfo->au2CountryCode[1]);
   +#endif
   +
                   /* load default normal TX power */
                   for (i = 0; i < sizeof(TX_PWR_PARAM_T); i += sizeof(UINT_16)) {
                           kalCfgDataRead16(prGlueInfo,
   ```

5. 修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/platform/rules.mk` 如下代码：

   ```diff
   @@ -14,4 +14,8 @@ endif
    
    ifeq ($(WB_ALSPS_EM30918_SUPPORT),yes)
    CFLAGS += -DWB_ALSPS_EM30918_SUPPORT
   -endif
   \ No newline at end of file
   +endif
   +
   +ifeq ($(CONFIG_WB_WIFI_CC_SUPPORT),yes)
   +DEFINES += CONFIG_WB_WIFI_CC_SUPPORT
   +endif
   ```

6. 修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/app/mt_boot/mt_boot.c` 如下代码：

   ```diff
   @@ -324,6 +324,7 @@ static char bt_mac[6] = { 0 };
    static char aceruuid[28] = { 0 };
    // Create ro.acersnid property by qty at 2022-10-10
    static char snid[13] = { 0 };
   +static char country_code[3] = {0};
    
    static double pow(double x, double y);
    static int read_product_info(char *buf);
   @@ -367,7 +368,7 @@ static void get_bt_mac() {
           int i = 0;
           int tmp = 0;
           
   -       reset_char_array(bt_buf, BT_BUF_LEN + 1);
   +       reset_char_array(bt_buf, BT_BUF_LEN);
           reset_char_array(bt_mac, 6);
           
           tmp = mboot_recovery_load_raw_part("proinfo", bt_buf, BT_BUF_LEN);
   @@ -382,6 +383,28 @@ static void get_bt_mac() {
           pal_log_err("[LK][get_bt_mac] Bluetooth mac: %02X%02X%02X%02X%02X%02X\n", bt_buf[104], bt_buf[105], bt_buf[106], bt_buf[107], bt_buf[108], bt_buf[109]);
    }
    
   +static void read_country_code() {
   +       pal_log_err("[LK][read_country_code] ....\n");
   +       #define COUNTRY_CODE_BUF_LEN 1024 // barcode:64 + imei:40 + bt:6 + wifi:6
   +       char country_code_buf[COUNTRY_CODE_BUF_LEN] = { 0 };
   +
   +       int i = 0;
   +       int tmp = 0;
   +       
   +       reset_char_array(country_code_buf, COUNTRY_CODE_BUF_LEN);
   +       reset_char_array(country_code, 3);
   +       
   +       tmp = mboot_recovery_load_raw_part("proinfo", country_code_buf, COUNTRY_CODE_BUF_LEN);
   +       if (tmp != COUNTRY_CODE_BUF_LEN) {
   +               pal_log_err("[LK][read_country_code] read proinfo fail, only read size %d, block size %d.\n", tmp, COUNTRY_CODE_BUF_LEN);
   +               return;
   +       }
   +       country_code[0] = country_code_buf[1022];
   +       country_code[1] = country_code_buf[1023];
   +       country_code[2] = '\0';
   +       pal_log_err("[LK][read_country_code] Country code: %s\n", country_code);
   +}
   +
    static void get_aceruuid() {
           pal_log_err("[LK][get_aceruuid] ....\n");
           reset_char_array(aceruuid, 28);
   @@ -404,11 +427,13 @@ static void get_snid(const char* sn) {
           reset_char_array(snid, 13);
           if (sn == NULL) {
                   pal_log_err("[LK][get_snid] SN is null.\n");
   -               return;
   +               sprintf(snid, "%s", "0123456789AB");
   +               return ;
           }
           len = strlen(sn);
           if (len != 22) {
                   pal_log_err("[LK][get_snid] SN length is corrent.\n");
   +               sprintf(snid, "%s", "0123456789AB");
                   return;
           }
           strncat(date_str, sn + 10, 3);
   @@ -419,6 +444,7 @@ static void get_snid(const char* sn) {
                   int_value = str_to_int(rand_code[i]);
                   if (int_value < 0) {
                           pal_log_err("[LK][get_snid] convert to int fail.\n");
   +                       sprintf(snid, "%s", "0123456789AB");
                           return;
                   }
                   sum += int_value * pow(16, j);
   @@ -427,10 +453,12 @@ static void get_snid(const char* sn) {
           version_last_char_value = str_to_int(version[1]);
           if (version_last_char_value < 0) {
                   pal_log_err("[LK][get_snid] convert to int fail.\n");
   +               sprintf(snid, "%s", "0123456789AB");
                   return;
           }
           if (sprintf(snid, "%s%06u%c%d", date_str, sum, version[0], version_last_char_value) < 0) {
                   pal_log_err("[LK][get_snid] sprintf fail.\n");
   +               sprintf(snid, "%s", "0123456789AB");
                   return;
           }
           if (version_last_char_value >= 10) {
   @@ -878,6 +906,51 @@ void get_reboot_reason(unsigned int boot_reason)
           cmdline_append("androidboot.bootreason=reboot");
    }
    
   +#if defined(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221101
   +static char *get_country_code(char *country_code) {
   +       pal_log_err("[LK][get_country_code] ....\n");
   +       #define COUNTRY_CODE_BUF_LEN 1024 // country code: 1022¡¢1023
   +       char country_code_buf[COUNTRY_CODE_BUF_LEN] = { 0 };
   +
   +       int i = 0;
   +       int tmp = 0;
   +       
   +       tmp = mboot_recovery_load_raw_part("proinfo", country_code_buf, COUNTRY_CODE_BUF_LEN);
   +       if (tmp != COUNTRY_CODE_BUF_LEN) {
   +               pal_log_err("[LK][get_country_code] read proinfo fail, only read size %d, block size %d.\n", tmp, COUNTRY_CODE_BUF_LEN);
   +               return;
   +       }
   +       country_code[0] = country_code_buf[1022];
   +       country_code[1] = country_code_buf[1023];
   +       country_code[2] = '\0';
   +       return country_code;
   +}
   +
   +static int cust_wifi_countrycode_update(void *fdt)
   +{
   +       int offset, ret;
   +       char wificc[5] = {0};
   +       
   +       get_country_code(wificc);
   +
   +       offset = fdt_node_offset_by_compatible(fdt, -1, "weibu,cust_wifi");
   +       if (offset < 0) {
   +               pal_log_err("[%s]get weibu,cust_wifi node failed\n",
   +                                       __func__);
   +               return -1;
   +       }
   +
   +       ret = fdt_setprop_string(fdt, offset, "wificc", wificc);
   +       if (ret) {
   +               pal_log_err("[%s]fdt_setprop_string wificc failed\n",
   +                       __func__);
   +               return ret;
   +       }
   + 
   +       return 0;
   + }
   +#endif
   +
    int boot_linux_fdt(void *kernel, unsigned *tags,
                      unsigned machtype,
                      void *ramdisk, unsigned ramdisk_sz)
   @@ -1099,6 +1172,10 @@ int boot_linux_fdt(void *kernel, unsigned *tags,
           }
    #endif
    
   +#if defined(CONFIG_WB_WIFI_CC_SUPPORT) //Leo 20221101
   +       cust_wifi_countrycode_update(fdt);
   +#endif
   +
           extern int get_mblock_num(void) __attribute__((weak));
    
    #if defined(MBLOCK_LIB_SUPPORT)
   @@ -1569,6 +1646,11 @@ int boot_linux_fdt(void *kernel, unsigned *tags,
           pal_log_err("[LK][boot_linux_fdt] aceruuid: %s.\n", aceruuid);
           snprintf(tmpbuf, TMPBUF_SIZE, "%s%s", "androidboot.aceruuid=", aceruuid);
           cmdline_append(tmpbuf);
   +       
   +       read_country_code();
   +       pal_log_err("[LK][boot_linux_fdt] country_code: %s.\n", country_code);
   +       snprintf(tmpbuf, TMPBUF_SIZE, "%s%s", "androidboot.wificountrycode=", country_code);
   +       cmdline_append(tmpbuf);
           // &&}}
    
           get_reboot_reason(boot_reason);
   ```

   > 注意：该文件的修改有其他功能代码修改在内，可以通过 `CONFIG_WB_WIFI_CC_SUPPORT` 宏来确定相关修改代码。

7. 修改 `weibu/tb8788p1_64_bsp_k419/M100BS_CC_261/config/tb8788p1_64_bsp_k419_defconfig` 文件如下代码：

   ```diff
   @@ -52,3 +52,4 @@ CONFIG_SND_SOC_AW87359=y
    ##Battery
    CONFIG_WB_HIGH_BATTERY_SUPPORT=y
    CONFIG_OV8858_MIRROR_HV=y
   +CONFIG_WB_WIFI_CC_SUPPORT=y
   ```

8. 修改 `weibu/tb8788p1_64_bsp_k419/M100BS_CC_261/config/tb8788p1_64_bsp_k419_lk.mk` 文件代码如下：

   ```diff
   @@ -4,4 +4,5 @@ BOOT_LOGO := wuxga2000
    MTK_MT6370_PMU=yes
    MTK_PROTOCOL1_RAT_CONFIG = no
    MTK_LCM_COMPATIBLE=yes
   -CUSTOM_LK_LCM="m100y_hjra104018_wuxga2000 m100bs_kd104n05_wuxga2000"
   \ No newline at end of file
   +CUSTOM_LK_LCM="m100y_hjra104018_wuxga2000 m100bs_kd104n05_wuxga2000"
   +CONFIG_WB_WIFI_CC_SUPPORT=yes
   \ No newline at end of file
   ```

   