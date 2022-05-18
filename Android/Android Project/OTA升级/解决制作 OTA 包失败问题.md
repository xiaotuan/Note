[toc]

### 1. MTK 平台

#### 1.1 错误信息

执行如下命令制作 OTA 升级包：

```shell
./build/tools/releasetools/ota_from_target_files -v -i V07.zip V09.zip update.zip
```

报如下错误：

```
Exception in thread Thread-63:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 801, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 754, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/blockimgdiff.py", line 1174, in diff_worker
    patch_info = compute_patch(src_file, tgt_file, imgdiff)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/blockimgdiff.py", line 53, in compute_patch
    proc = common.Run(cmd, verbose=False)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/common.py", line 228, in Run
    return subprocess.Popen(args, **kwargs)
  File "/usr/lib/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/usr/lib/python2.7/subprocess.py", line 1343, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory

Traceback (most recent call last):
  File "./build/make/tools/releasetools/ota_from_target_files", line 2258, in <module>
    main(sys.argv[1:])
  File "./build/make/tools/releasetools/ota_from_target_files", line 2237, in main
    source_file=OPTIONS.incremental_source)
  File "./build/make/tools/releasetools/ota_from_target_files", line 1992, in GenerateNonAbOtaPackage
    output_file)
  File "./build/make/tools/releasetools/ota_from_target_files", line 1417, in WriteBlockIncrementalOTAPackage
    device_specific=device_specific)
  File "./build/make/tools/releasetools/ota_from_target_files", line 683, in GetBlockDifferences
    partition)
  File "./build/make/tools/releasetools/ota_from_target_files", line 657, in GetIncrementalBlockDifferenceForPartition
    disable_imgdiff=disable_imgdiff)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/common.py", line 2630, in __init__
    b.Compute(self.path)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/blockimgdiff.py", line 372, in Compute
    self.ComputePatches(prefix)
  File "/work02/mtk/11/8766/A/mt8766_r/build/make/tools/releasetools/blockimgdiff.py", line 772, in ComputePatches
    for index, patch_info, _ in patches:
TypeError: 'NoneType' object is not iterable
```

#### 1.2 解决办法

使用对应工程编译软件，同时编译 otapackage，在执行生成 OTA 升级包命令即可。例如：

```shell
$ make -j32 2>&1 | tee build.log;make otapackage -j32 2>&1 | tee ota.log
$ ./build/tools/releasetools/ota_from_target_files -v -i V07.zip V09.zip update.zip
```

