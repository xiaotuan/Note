[toc]

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android 12

1. NVRAM 数据结构

   ```
   0 ~ 63 位是 SN 号
   64 ~ 103 位是 IMEI 号
   104 ~ 109 位是蓝牙 MAC 地址
   110 ~ 115 位是 WiFi MAC 地址
   ```

1. 在 `vendor/mediatek/proprietary/bootable/bootloader/lk/app/mt_boot.c` 文件中获取:

   ```c
   static char bt_mac[6] = { 0 };
   
   static void reset_char_array(char* array, int length) {
   	int i = 0;
   	if (array != NULL) {
   		for (i = 0; i < length; i++) {
   			array[i] = '\0';
   		}
   	}
   }
   
   static void get_bt_mac() {
   	pal_log_err("[LK][get_bt_mac] ....\n");
   	#define BT_BUF_LEN 110 // barcode:64 + imei:40 + bt:6 + wifi:6
   	char bt_buf[BT_BUF_LEN] = { 0 };
   
   	int i = 0;
   	int tmp = 0;
   	
   	reset_char_array(bt_buf, BT_BUF_LEN + 1);
   	reset_char_array(bt_mac, 6);
   	
   	tmp = mboot_recovery_load_raw_part("proinfo", bt_buf, BT_BUF_LEN);
   	if (tmp != BT_BUF_LEN) {
   		pal_log_err("[LK][get_bt_mac] read proinfo fail, only read size %d, block size %d.\n", tmp, BT_BUF_LEN);
   		return;
   	}
   	tmp = 104;
   	for (; tmp < BT_BUF_LEN && i < 6; tmp++, i++) {
   		bt_mac[i] = bt_buf[tmp];
   	}
   	pal_log_err("[LK][get_bt_mac] Bluetooth mac: %02X%02X%02X%02X%02X%02X\n", bt_buf[104], bt_buf[105], bt_buf[106], bt_buf[107], bt_buf[108], bt_buf[109]);
   }
   ```

2. 也可以参照 `vendor/mediatek/proprietary/factory` 应用中的 `ATE_factory.cpp` 中的如下方法：

   ```cpp
   int read_bt(char *result)
   {
       int rec_size = 0;
       int rec_num = 0;
       int ret = 0;
   
       nvram_fd = NVM_GetFileDesc(AP_CFG_RDEB_FILE_BT_ADDR_LID, &rec_size, &rec_num, ISREAD);
     	LOGD("rec_size=%d,rec_num=%d\n",rec_size,rec_num);
      	if(1 != rec_num)
      	{
      		LOGD("error:unexpected record num %d\n",rec_num);
           if(sprintf(result, "%s", return_err) < 0){
   			LOGD("error:printf result infroamtion failed!\n");
   		}
      		return -1;
      	}
      	if(sizeof(g_bt_nvram) != rec_size)
      	{
      		LOGD("error:unexpected record size %d\n",rec_size);
    
    		if(sprintf(result, "%s", return_err) < 0){
   	 		LOGD("error:printf result infroamtion failed!\n");
    		}
    
      		return -1;
      	}
      	memset(&g_bt_nvram,0,rec_num*rec_size);
      	ret = read(nvram_fd.iFileDesc, &g_bt_nvram, rec_num*rec_size);
      	if(-1 == ret||rec_num*rec_size != ret)
      	{
      		LOGD("error:read bt addr fail!/n");
           if(sprintf(result, "%s", return_err) < 0){
   			LOGD("error:printf result infroamtion failed!\n");
   		}
   
      		return -1;
      	}
      	LOGD("read pre bt addr:%02x%02x%02x%02x%02x%02x\n", 
              g_bt_nvram.addr[0], g_bt_nvram.addr[1], g_bt_nvram.addr[2], g_bt_nvram.addr[3], g_bt_nvram.addr[4], g_bt_nvram.addr[5] 
       );
   
       if(sprintf(result, "%02x%02x%02x%02x%02x%02x", g_bt_nvram.addr[0], g_bt_nvram.addr[1], g_bt_nvram.addr[2], g_bt_nvram.addr[3], g_bt_nvram.addr[4], g_bt_nvram.addr[5]) < 0){
             LOGD("error:printf result infroamtion failed!\n");
       }
      	NVM_CloseFileDesc(nvram_fd);
   
       return 0;
   }
   ```

   

