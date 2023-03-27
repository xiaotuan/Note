[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

1. 开启 AB 升级功能，修改 `vnd/vendor/mediatek/proprietary/bootable/bootloader/lk/platform/mt6761/write_protect_ab.c` 文件中 `set_write_protect(void)` 函数的如下代码：

   ```diff
   @@ -107,10 +107,12 @@ void set_write_protect(void)
                   wp_end = "logo";
    
                   pal_log_info("[%s]: Lock %s->%s \n", __func__, wp_start, wp_end);
   -               err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   -               if (err != 0)
   -                       pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   -                                   __func__, wp_start, wp_end, err);
   +               // Allows applications to read Nvram values by qty at 2023-02-01 {{&&
   +               //  err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   +               // if (err != 0)
   +               //      pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   +               //                  __func__, wp_start, wp_end, err);
   +               // &&}}
    
                   if (ab_suffix[1] == 'a') {
                           wp_start = "md1img_a";
   @@ -141,10 +143,13 @@ void set_write_protect(void)
                   }
    #endif
                   pal_log_info("[%s]: Lock %s->%s\n", __func__, wp_start, wp_end);
   -               err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   -               if (err != 0)
   -                       pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   -                                   __func__, wp_start, wp_end, err);
   +               // Allows applications to read Nvram values by qty at 2023-02-01 {{&&
   +               //err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   +               // if (err != 0)
   +                       // pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   +                                   // __func__, wp_start, wp_end, err);
   +               // &&}}
   +
    #ifdef MTK_SIM_LOCK_POWER_ON_WRITE_PROTECT
                   /* sync protect1 sml data to protect2 if needed */
                   mtk_wdt_restart();
   ```

2. 未开启 AB 升级功能，修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/platform/mt6761/write_protect.c` 文件中 `set_write_protect(void)` 函数的如下代码：

   ```diff
   @@ -107,10 +107,12 @@ void set_write_protect(void)
                   wp_end = "tee2";
    #endif
                   pal_log_info("[%s]: Lock %s->%s\n", __func__, wp_start, wp_end);
   -               err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   -               if (err != 0)
   -                       pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   -                                   __func__, wp_start, wp_end, err);
   +               // Allows applications to read Nvram values by qty at 2023-02-01 {{&&
   +               //err = partition_write_prot_set(wp_start, wp_end, WP_POWER_ON);
   +               // if (err != 0)
   +                       // pal_log_err("[%s]: Lock %s->%s failed:%d\n",
   +                                   // __func__, wp_start, wp_end, err);
   +               // &&}}
    
    #ifdef MTK_SIM_LOCK_POWER_ON_WRITE_PROTECT
                   /* sync protect1 sml data to protect2 if needed */
   ```

   