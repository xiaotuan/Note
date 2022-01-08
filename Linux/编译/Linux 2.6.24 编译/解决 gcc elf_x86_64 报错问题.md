[toc]

### 1. 报错信息

```log
  AS      arch/x86/vdso/vdso-note.o
  CC      arch/x86/vdso/vclock_gettime.o
  CC      arch/x86/vdso/vgetcpu.o
  CC      arch/x86/vdso/vvar.o
  SYSCALL arch/x86/vdso/vdso.so.dbg
gcc: error: elf_x86_64: 没有那个文件或目录
gcc: error: unrecognized command line option ‘-m’
/home/xiaotuan/linux-2.6.24/arch/x86/vdso/Makefile:36: recipe for target 'arch/x86/vdso/vdso.so.dbg' failed
make[2]: *** [arch/x86/vdso/vdso.so.dbg] Error 1
/home/xiaotuan/linux-2.6.24/Makefile:823: recipe for target 'arch/x86/vdso' failed
make[1]: *** [arch/x86/vdso] Error 2
Makefile:128: recipe for target 'sub-make' failed
make: *** [sub-make] Error 2
```

### 2. 报错原因

由于 gcc 4.6 不再支持 linker-style 架构。

### 3. 解决办法

将 `arch/x86/vdso/Makefile` 中，以 VDSO——LDFLAGS_vso.lds 开头所在行的 “-m elf_x86_64” 替换成 “-m64”
 将 VDSO_LDFLAGS_vdso32.lds 开头所在行的 “-m elf_x86” 替换成 “-m32”。

```diff
diff --git a/arch/x86/vdso/Makefile b/arch/x86/vdso/Makefile
index e7bff0f..2013363 100644
--- a/arch/x86/vdso/Makefile
+++ b/arch/x86/vdso/Makefile
@@ -16,8 +16,12 @@ $(obj)/vdso.o: $(obj)/vdso.so
 targets += vdso.so vdso.so.dbg vdso.lds $(vobjs-y) vdso-syms.o
 
 # The DSO images are built using a special linker script.
+#quiet_cmd_syscall = SYSCALL $@
+#      cmd_syscall = $(CC) -m elf_x86_64 -nostdlib $(SYSCFLAGS_$(@F)) \
+#                        -Wl,-T,$(filter-out FORCE,$^) -o $@
+
 quiet_cmd_syscall = SYSCALL $@
-      cmd_syscall = $(CC) -m elf_x86_64 -nostdlib $(SYSCFLAGS_$(@F)) \
+      cmd_syscall = $(CC) -m64 -nostdlib $(SYSCFLAGS_$(@F)) \
                          -Wl,-T,$(filter-out FORCE,$^) -o $@
 
 export CPPFLAGS_vdso.lds += -P -C
```

