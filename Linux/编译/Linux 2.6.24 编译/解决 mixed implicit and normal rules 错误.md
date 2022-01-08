[toc]

### 1. 编译报错信息

```shell
xiaotuan@xiaotuan:~/linux-2.6.24$ make
Makefile:1503: *** mixed implicit and normal rules: deprecated syntax
/home/xiaotuan/linux-2.6.24/Makefile:434: *** mixed implicit and normal rules: deprecated syntax
/home/xiaotuan/linux-2.6.24/Makefile:1503: *** mixed implicit and normal rules: deprecated syntax
make[1]: *** No rule to make target 'silentoldconfig'。 停止。
make: *** No rule to make target 'include/config/auto.conf', needed by 'include/config/kernel.release'。 停止。
```

### 2. 报错原因

`make` 版本过高造成的。

### 3. 解决办法

修改 `/linux-2.6.24/Makefile` 文件：

```diff
diff --git a/Makefile b/Makefile
index 189d8ef..3983539 100644
--- a/Makefile
+++ b/Makefile
@@ -431,7 +431,8 @@ ifeq ($(config-targets),1)
 include $(srctree)/arch/$(SRCARCH)/Makefile
 export KBUILD_DEFCONFIG
 
-config %config: scripts_basic outputmakefile FORCE
+#config %config: scripts_basic outputmakefile FORCE
+%config: scripts_basic outputmakefile FORCE
        $(Q)mkdir -p include/linux include/config
        $(Q)$(MAKE) $(build)=scripts/kconfig $@
 
@@ -1500,7 +1501,8 @@ endif
        $(Q)$(MAKE) $(build)=$(build-dir) $(target-dir)$(notdir $@)
 
 # Modules
-/ %/: prepare scripts FORCE
+#/ %/: prepare scripts FORCE
+%/: prepare scripts FORCE
        $(cmd_crmodverdir)
        $(Q)$(MAKE) KBUILD_MODULES=$(if $(CONFIG_MODULES),1) \
        $(build)=$(build-dir)

```

