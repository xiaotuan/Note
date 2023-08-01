如果需要本地验证 AB 升级，需要将 `update_engine_client` 模块编译进去。修改 `sys/device/mediatek/common/device.mk` 文件的如下代码：

```diff
@@ -3966,6 +3966,7 @@ ifeq ($(strip $(MTK_AB_OTA_UPDATER)), yes)
 PRODUCT_PACKAGES += \
 update_engine \
 update_engine_sideload \
+update_engine_client \
 update_verifier
 
 PRODUCT_HOST_PACKAGES += \
```

编译成功后文件位于 `./out/target/product/xxx/system/bin/update_engine_client`。

可以执行如下命令查看升级命令参数说明：

```shell
GRINV1:/ $ update_engine_client  --help
Android Update Engine Client

  --allocate  (Given payload metadata, allocate space.)  type: bool  default: false
  --cancel  (Cancel the ongoing update and exit.)  type: bool  default: false
  --follow  (Follow status update changes until a final state is reached. Exit status is 0 if the update succeeded, and
1 otherwise.)  type: bool  default: false
  --headers  (A list of key-value pairs, one element of the list per line. Used when --update or --allocate is passed.)
 type: string  default: ""
  --help  (Show this help message)  type: bool  default: false
  --merge  (Wait for previous update to merge. Only available after rebooting to new slot.)  type: bool  default: false
  --metadata  (The path to the update payload metadata. Used when --verify or --allocate is passed.)  type: string  defa
ult: "/data/ota_package/metadata"
  --offset  (The offset in the payload where the CrAU update starts. Used when --update is passed.)  type: int64  defaul
t: 0
  --payload  (The URI to the update payload to use.)  type: string  default: "http://127.0.0.1:8080/payload"
  --reset_status  (Reset an already applied update and exit.)  type: bool  default: false
  --resume  (Resume a suspended update.)  type: bool  default: false
  --size  (The size of the CrAU part of the payload. If 0 is passed, it will be autodetected. Used when --update is pass
ed.)  type: int64  default: 0
  --suspend  (Suspend an ongoing update and exit.)  type: bool  default: false
  --switch_slot  (Perform just the slow switching part of OTA. Used to revert a slot switch or re-do slot switch. Valid
values are 'true' and 'false')  type: string  default: UNSPECIFIED_FLAG
  --update  (Start a new update, if no update in progress.)  type: bool  default: false
  --verify  (Given payload metadata, verify if the payload is applicable.)  type: bool  default: false

```

执行升级命令如下：

```shell
update_engine_client --payload=file:///sdcard/payload.bin --update --headers="
FILE_HASH=EL4p2lSCrEoyjczfBEi7J6mVZLZvP4PBgwyxn5t1/WI=
FILE_SIZE=657924722
METADATA_HASH=dLph3Mh2Rh2qEU3qdh25vJg3Q+LbXMT1kkVCm17mQeQ=
METADATA_SIZE=50204"
```

> 提示：
>
> + `payload.bin` 文件位于升级包里的 `payload.bin`。
> + `headers` 信息位于升级版中 `payload_properties.txt` 文件的内容，注意复制中换行。

可能需要为 `update_engine` 添加 `selinux` 权限：

```
update_engine: type=1400 audit(0.0:134): avc: denied { dac_read_search } for capability=2 scontext=u:r:update_engine:s0 tcontext=u:r:update_engine:s0 tclass=capability permissive=0
update_engine: type=1400 audit(0.0:135): avc: denied { dac_override } for capability=1 scontext=u:r:update_engine:s0 tcontext=u:r:update_engine:s0 tclass=capability permissive=0
update_engine: type=1400 audit(0.0:180): avc: denied { search } for name="/" dev="fuse" ino=720897 scontext=u:r:update_engine:s0 tcontext=u:object_r:fuse:s0 tclass=dir permissive=0
update_engine: type=1400 audit(0.0:109): avc: denied { search } for name="0" dev="tmpfs" ino=13411 scontext=u:r:update_engine:s0 tcontext=u:object_r:mnt_user_file:s0 tclass=dir permissive=0
update_engine: type=1400 audit(0.0:108): avc: denied { read } for name="primary" dev="tmpfs" ino=36806 scontext=u:r:update_engine:s0 tcontext=u:object_r:mnt_user_file:s0 tclass=lnk_file permissive=0
update_engine: type=1400 audit(0.0:108): avc: denied { read } for name="update.zip" dev="fuse" ino=557088 scontext=u:r:update_engine:s0 tcontext=u:object_r:fuse:s0 tclass=file permissive=0
update_engine: type=1400 audit(0.0:104): avc: denied { open } for path="/storage/emulated/0/update.zip" dev="fuse" ino=2760730 scontext=u:r:update_engine:s0 tcontext=u:object_r:fuse:s0 tclass=file permissive=0
```

在 `sys/device/mediatek/sepolicy/basic/non_plat/update_engine.te` 文件中添加如下权限：

```
allow update_engine update_engine:capability { dac_read_search dac_override };
allow update_engine fuse:dir { search };
allow update_engine fuse:file { read open };
allow update_engine mnt_user_file:dir { search };
allow update_engine mnt_user_file:lnk_file { read };
```

编译时 capability 违背 neverallow 规则，出错解决参考 android 11添加property遇到的selinux问题：

```
system\sepolicy\prebuilts\api\30.0\private\domain.te
system\sepolicy\private\domain.te
```

修改如下：

```diff
@@ -311,8 +311,10 @@ define(`dac_override_allowed', `{
   vold
   vold_prepare_subdirs
   zygote
+  update_engine
 }')
-neverallow ~dac_override_allowed self:global_capability_class_set dac_override;
+neverallow ~{dac_override_allowed update_engine} self:global_capability_class_set dac_override;
 # Since the kernel checks dac_read_search before dac_override, domains that
 # have dac_override should also have dac_read_search to eliminate spurious
 # denials.  Some domains have dac_read_search without having dac_override, so
@@ -323,6 +325,7 @@ neverallow ~{
   iorap_prefetcherd
   traced_perf
   traced_probes
+  update_engine
   userdebug_or_eng(`heapprofd')
 } self:global_capability_class_set dac_read_search;
```





