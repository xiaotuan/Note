`remove` 函数相当于 `unlink` 函数，但是如果它的 pathname 参数是一个目录的话，其作用就相当于 `rmdir` 函数。其函数原型如下所示：

```c
#include <stdio.h>

int remove(const char *int remove(const char *pathname););
```

