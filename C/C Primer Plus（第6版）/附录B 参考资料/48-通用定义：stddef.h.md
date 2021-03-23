#### B.5.17　通用定义： `stddef.h` 

该头文件定义了一些类型和宏，如表B.5.24和表B.5.25所列。

<center class="my_markdown"><b class="my_markdown">表B.5.24　 `stddef.h` 类型</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `ptrdiff_t` | 有符号整数类型，表示两个指针之差 |
| `size_t` | 无符号整数类型，表示 `sizeof` 运算符的结果 |
| `wchar_t` | 整数类型，表示支持的本地化所指定的最大扩展字符集 |

<center class="my_markdown"><b class="my_markdown">表B.5.25　 `stddef.h` 宏</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `NULL` | 实现定义的常量，表示空指针 |
| `offsetof(type,member-designator)` | 展开为 `size_t` 类型的值，表示 `type` 类型结构的指定成员在该结构中的偏移量，以字节为单位。如果成员是一个位字段，该宏的行为是未定义的 |

**示例**

```c
#include <stddef.h>
struct car
{
     char brand[30];
     char model[30];
     double hp;
     double price;
};
int main(void)
{
     size_t into = offsetof(struct car, hp); /* hp成员的偏移量 */
     ...
```

