### 23.5　POSIX时钟

POSIX时钟（原定义于POSIX.1b）所提供的时钟访问API可以支持纳秒级的时间精度，其中表示纳秒级时间值的timespec结构同样也用于nanosleep()（23.4.2节）调用。

Linux中，调用此API的程序必须以-lrt选项进行编译，从而与librt（realtime，实时）函数库相链接。

POSIX时钟API的主要系统调用包括获取时钟当前值的clock_gettime()、返回时钟分辨率的clock_getres()，以及更新时钟的clock_settime()。

