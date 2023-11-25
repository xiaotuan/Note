[toc]

### 1. MTK 平台

#### 1.1 MTK 8766、Android R

修改 `device/mediateksample/tb8768p1_bsp/BoardConfig.mk` 文件，添加或修改如下宏的值：

```makefile
BOARD_MTK_SUPER_SIZE_KB := 3619840
```

#### 1.2 MTK8168

##### 1.2.1 Android R

修改 `device/mediateksample/tb8168p1_64_bsp_k510/partition/partition_ab_dynamic.xml` 文件中的如下代码：

```diff
@@ -40,6 +40,6 @@
        <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="4096" name="vbmeta_system_b" />
        <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="4096" name="vbmeta_vendor_a" />
        <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="4096" name="vbmeta_vendor_b" />
-       <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="8955904" name="super" />
+       <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="9824256" name="super" />
        <entry type="{0FC63DAF-8483-4772-8E79-3D69D8477DE4}" size="2097152" name="userdata" />
 </partition>
```

