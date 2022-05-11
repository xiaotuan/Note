`fsetpos` 函数用于设置文件流的当前（读写）位置。它的函数原型如下所示：

```c
#include <stdio.h>

int fsetpos(FILE *stream, const fpos_t *pos);
```



