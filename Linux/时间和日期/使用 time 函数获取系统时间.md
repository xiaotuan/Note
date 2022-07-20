时间通过一个预定义的类型 `time_t` 来处理。在 `Linux` 系统中，它是一个长整型，与处理时间值的函数一起定义在头文件 `time.h` 中。

```c
#include <time.h>

time_t time(time_t *tloc);
```

你可以通过调用 `time` 函数得到底层的时间值，它返回的是从纪元开始至今的秒数。如果 `tloc` 不是一个空指针，`time` 函数还会把返回值写入 `tloc` 指针执行的位置。

```c
#include <time.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    int i;
    time_t the_time;
    
    for (i = 1; i <= 10; i++)
    {
        the_time = time((time_t *)0);
        printf("The time is %ld\n", the_time);
        sleep(2);
    }
 	
    exit(0);
}
```

