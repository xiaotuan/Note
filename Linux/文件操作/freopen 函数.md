`freopen` 函数用于重新使用一个文件流。它的函数原型如下所示：

```c
#include <stdio.h>

FILE *freopen(const char *pathname, const char *mode, FILE *stream);
```

> 提示：`freopen` 函数的主要用途是更改与标准文本流（stderr、stdin 或 stdout）关联的文件。
