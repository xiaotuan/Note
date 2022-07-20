你可以把它考虑为简单地把两次调用 `time` 得到的值相减。然而 `ISO/ANSI C` 标准委员会经过审议，并没有规定用 `time_t` 类型来测量任意时间之间的秒数，他们发明了一个函数 `difftime`，该函数用来计算两个 `time_t` 值之间的秒数并以 `double` 类型返回它。

```c
#include <time.h>

double difftime(time_t time1, time_t time2);
```

对于 `Linux` 来说，`time` 函数的返回值是一个易于处理的秒数，但考虑到最大限度的可移植性，你最好使用 `difftime`。