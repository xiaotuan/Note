`du` 命令可以显示某个特定目录（默认情况下时当前目录）的磁盘使用情况。这一方法可用来快速判断系统上某个目录下是不是有超大文件。

默认情况下，`du` 命令会显示当前目录下所有的文件、目录和子目录的磁盘使用情况，它会以磁盘块为单位来表明每个文件或目录占用了多大存储空间。

```shell
$ du
1060	./lib64
16	./systrace/catapult/devil/devil/utils/lazy
244	./systrace/catapult/devil/devil/utils
12	./systrace/catapult/devil/devil/constants
8	./systrace/catapult/devil/devil/android/sdk/test/data/push_directory
16	./systrace/catapult/devil/devil/android/sdk/test/data
20	./systrace/catapult/devil/devil/android/sdk/test
160	./systrace/catapult/devil/devil/android/sdk
12	./systrace/catapult/devil/devil/android/ndk
60	./systrace/catapult/devil/devil/android/perf
160	./systrace/catapult/devil/devil/android/tools
12	./systrace/catapult/devil/devil/android/valgrind_tools
20	./systrace/catapult/devil/devil/android/constants
1112	./systrace/catapult/devil/devil/android
```

下面是能让 `du` 命令用起来更方便的几个命令行参数。

+ `-c`：显示所有已列出文件总的大小。
+ `-h`：按用户易读的格式输出大小，即用 K 代替千字节，用 M 替代兆字节，用 G 替代吉字节。
+ `-s`：显示每个输出参数的总计。