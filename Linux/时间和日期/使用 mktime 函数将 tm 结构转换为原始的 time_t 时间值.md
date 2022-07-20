要把已分解出来的 `tm` 结构再转换为原始的 `time_t` 时间值，你可以使用 `mktime` 函数：

```c
#include <time.h>

time_t mktime(struct tm *timeptr);
```

如果 `tm` 结构不能被表示为 `time_t` 值，`mktime` 将返回 -1.