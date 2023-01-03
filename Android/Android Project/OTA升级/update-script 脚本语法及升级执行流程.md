目前 update-script 脚本格式是 edify，其与 amend 有何区别，暂不讨论，我们只分析其中主要的语法，以及脚本的流程控制。

**一、update-script脚本语法简介：**

 我们顺着所生成的脚本来看其中主要涉及的语法。

1. `assert(condition)`：如果 condition 参数的计算结果为 False，则停止脚本执行，否则继续执行脚本。

2. `show_progress(frac,sec)`：frac 表示进度完成的数值，sec 表示整个过程的总秒数。主要用与显示UI上的进度条。

3. `format(fs_type,partition_type,location)`：fs_type，文件系统类型，取值一般为 “yaffs2” 或 “ext4”。Partition_type，分区类型，一般取值为 “MTD” 或则 “EMMC”。主要用于格式化为指定的文件系统。事例如下：`format(”yaffs2”,”MTD”,”system”)`。

4. `mount(fs_type,partition_type,location,mount_point)`：前两个参数同上，location 要挂载的设备，mount_point 挂载点。作用：挂载一个文件系统到指定的挂载点。

5. `package_extract_dir(src_path,destination_path)`：src_path，要提取的目录，destination_path 目标目录。作用：从升级包内，提取目录到指定的位置。示例：`package_extract_dir(“system”,”/system”)`。

6. `symlink(target,src1,src2,……,srcN)`：target，字符串类型，是符号连接的目标。SrcX 代表要创建的符号连接的目标点。示例：`symlink(“toolbox”,”/system/bin/ps”)`, 建立指向 toolbox 符号连接 /system/bin/ps，值得注意的是，在建立新的符号连接之前，要断开已经存在的符号连接。

7. `set_perm(uid,gid,mode,file1,file2,……,fileN)`：作用是设置单个文件或则一系列文件的权限，最少要指定一个文件。

8. `set_perm_recursive(uid,gid,mode,dir1,dir2,……,dirN)`：作用同上，但是这里同时改变的是一个或多个目录及其文件的权限。

9. `package_extract_file(srcfile_path,desfile_paht)`：srcfile_path，要提取的文件，desfile_path，提取文件的目标位置。示例：`package_extract_file(“boot.img”,”/tmp/boot.img”)` 将升级包中的boot.img 文件拷贝到内存文件系统的 /tmp 下。

10. `write_raw_image(src-image,partition)`：src-image 源镜像文件，partition，目标分区。作用：将镜像写入目标分区。示例：`write_raw_image(“/tmp/boot.img”,”boot”)` 将 boot.img 镜像写入到系统的 boot 分区。

11. `getprop(key)`：通过指定 key 的值来获取对应的属性信息。示例：`getprop(“ro.product.device”)` 获取 ro.product.device 的属性值。

12. `ui_print(String)`: 用于在 Flash Mode 要显示的内容

13. `delete(FilePath)`:  用于删除文件的命令

14. `run_program(Shell, ScriptPath)`:  例如：`run_program("/sbin/sh", "/system/bin/install.sh")`;

15. `umount(Path)`: 卸载文件系统

16. `cmdlist`：

```
is_mounted
unmount
format
show_progress
set_progress
delete
delete_recursive
package_extract_dir
package_extract_file
retouch_binaries
undo_retouch_binaries
symlink
set_perm
set_perm_recursive
getprop
file_getprop
write_raw_image
apply_patch
apply_patch_check
apply_patch_space
read_file
sha1_check
wipe_cache
ui_print
run_program
set_bootloader_env
```

**二、updater-script脚本执行流程分析：**

先看一下在测试过程中用命令 make otapackage 生成的升级脚本如下：
```shell
assert(!less_than_int(1331176658, getprop("ro.build.date.utc")));
assert(getprop("ro.product.device") == "tcc8800" ||
       getprop("ro.build.product") == "tcc8800");
show_progress(0.500000, 0);
format("yaffs2", "MTD", "system");
mount("yaffs2", "MTD", "system", "/system");
package_extract_dir("recovery", "/system");
package_extract_dir("system", "/system");
symlink("busybox", "/system/bin/cp", "/system/bin/grep",
        "/system/bin/tar", "/system/bin/unzip",
        "/system/bin/vi");
symlink("toolbox", "/system/bin/cat", "/system/bin/chmod",
        "/system/bin/chown", "/system/bin/cmp", "/system/bin/date",
        "/system/bin/dd", "/system/bin/df", "/system/bin/dmesg",
        "/system/bin/getevent", "/system/bin/getprop", "/system/bin/hd",
        "/system/bin/id", "/system/bin/ifconfig", "/system/bin/iftop",
        "/system/bin/insmod", "/system/bin/ioctl", "/system/bin/ionice",
        "/system/bin/kill", "/system/bin/ln", "/system/bin/log",
        "/system/bin/ls", "/system/bin/lsmod", "/system/bin/lsof",
        "/system/bin/mkdir", "/system/bin/mount", "/system/bin/mv",
        "/system/bin/nandread", "/system/bin/netstat",
        "/system/bin/newfs_msdos", "/system/bin/notify", "/system/bin/printenv",
        "/system/bin/ps", "/system/bin/reboot", "/system/bin/renice",
        "/system/bin/rm", "/system/bin/rmdir", "/system/bin/rmmod",
        "/system/bin/route", "/system/bin/schedtop", "/system/bin/sendevent",
        "/system/bin/setconsole", "/system/bin/setprop", "/system/bin/sleep",
        "/system/bin/smd", "/system/bin/start", "/system/bin/stop",
        "/system/bin/sync", "/system/bin/top", "/system/bin/umount",
        "/system/bin/uptime", "/system/bin/vmstat", "/system/bin/watchprops",
        "/system/bin/wipe");
set_perm_recursive(0, 0, 0755, 0644, "/system");
set_perm_recursive(0, 2000, 0755, 0755, "/system/bin");
set_perm(0, 3003, 02750, "/system/bin/netcfg");
set_perm(0, 3004, 02755, "/system/bin/ping");
set_perm(0, 2000, 06750, "/system/bin/run-as");
set_perm_recursive(1002, 1002, 0755, 0440, "/system/etc/bluetooth");
set_perm(0, 0, 0755, "/system/etc/bluetooth");
set_perm(1000, 1000, 0640, "/system/etc/bluetooth/auto_pairing.conf");
set_perm(3002, 3002, 0444, "/system/etc/bluetooth/blacklist.conf");
set_perm(1002, 1002, 0440, "/system/etc/dbus.conf");
set_perm(1014, 2000, 0550, "/system/etc/dhcpcd/dhcpcd-run-hooks");
set_perm(0, 2000, 0550, "/system/etc/init.goldfish.sh");
set_perm(0, 0, 0544, "/system/etc/install-recovery.sh");
set_perm_recursive(0, 0, 0755, 0555, "/system/etc/ppp");
set_perm_recursive(0, 2000, 0755, 0755, "/system/xbin");
set_perm(0, 0, 06755, "/system/xbin/librank");
set_perm(0, 0, 06755, "/system/xbin/procmem");
set_perm(0, 0, 06755, "/system/xbin/procrank");
set_perm(0, 0, 06755, "/system/xbin/su");
set_perm(0, 0, 06755, "/system/xbin/tcpdump");
show_progress(0.200000, 0);
show_progress(0.200000, 10);
assert(package_extract_file("boot.img", "/tmp/boot.img"),
       write_raw_image("/tmp/boot.img", "boot"),
       delete("/tmp/boot.img"));
show_progress(0.100000, 0);
unmount("/system");
```

下面分析下这个脚本的执行过程：

①比较时间戳：如果升级包较旧则终止脚本的执行。

②匹配设备信息：如果和当前的设备信息不一致，则停止脚本的执行。

③显示进度条：如果以上两步匹配则开始显示升级进度条。

④格式化 system 分区并挂载。

⑤提取包中的 recovery 以及 system 目录下的内容到系统的 /system 下。

⑥为 /system/bin/ 下的命令文件建立符号连接。

⑦设置 /system/ 下目录以及文件的属性。

⑧将包中的 boot.img 提取到 /tmp/boot.img。

⑨将 /tmp/boot.img 镜像文件写入到 boot 分区。

⑩完成后卸载 /system。

以上就是 updater-script 脚本中的语法，及其执行的具体过程。通过分析其执行流程，我们可以发现在执行过程中，并未将升级包另外解压到一个地方，而是需要什么提取什么。值得主要的是在提取 recovery 和 system 目录中的内容时，一并放在了 /system/ 下。在操作的过程中，并未删除或改变update.zip包中的任何内容。在实际的更新完成后，我们的 update.zip 包确实还存在于原来的位置。

**三、总结**

以上的九篇着重分析了 Android 系统中 Recovery 模式中的一种，即我们做好的 update.zip 包在系统更新时所走过的流程。其核心部分就是 Recovery 服务的工作原理。其他两种 FACTORY RESET、ENCRYPTED FILE SYSTEM ENABLE/DISABLE与OTA INSTALL 是相通的。重点是要理解 Recovery 服务的工作原理。另外详细分析其升级过程，对于我们在实际升级时，可以根据我们的需要做出相应的修改。