`fgetpos` 函数用于获得文件流的当前（读写）位置。它的函数原型如下所示：

```c
#include <stdio.h>

int fgetpos(FILE *stream, fpos_t *pos);
```

