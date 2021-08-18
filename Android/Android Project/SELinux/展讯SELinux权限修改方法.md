下面以 `/sys/sileadinc/tpgesture_func` 节点为例：

1. 修改 `device/sprd/mpool/sepolicy/vendor/genfs_contexts` 文件，在文件末尾添加如下代码：

   ```
   genfscon sysfs /sileadinc/tpgesture_func  u:object_r:sysfs_tpgesture:s0
   ```

   > 注意：`sysfs` 后面的路径是去掉路径中的 `sys` 路径。

2. 修改 `device/sprd/mpool/sepolicy/vendor/file.te` 文件，在文件末尾添加如下代码：

   ```
   type sysfs_tpgesture, fs_type, sysfs_type;
   ```

3. 修改要添加权限的服务或APP类型

   1. 修改 `device/sprd/mpool/sepolicy/vendor/system_app.te` 文件，在文件末尾添加如下代码：

      ```
      allow system_app sysfs_tpgesture:file rw_file_perms;
      ```

   2. 修改 `device/sprd/mpool/sepolicy/vendor/system_server.te` 文件，在文件末尾添加如下代码：

      ```
      allow system_server sysfs_tpgesture:file rw_file_perms;
      ```

      > 提示：
      >
      > 在 `device/sprd/mpool/sepolicy/vendor` 目录下没有 `platform_app.te ` 文件，如果需要给平台应用添加权限，可以在该目录下创建 `platform_app.te` 文件，并在其内容中添加权限即可，其他类型权限同理。

