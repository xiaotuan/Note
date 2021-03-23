#### B.5.16　布尔支持： `stdbool.h` （C99）

`stdbool.h` 头文件定义了4个宏，如表B.5.23所列。

<center class="my_markdown"><b class="my_markdown">表B.5.23　 `stdbool.h` 宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `bool` | 展开为 `_Bool` |
| `false` | 展开为整型常量 `0` |
| `true` | 展开为整型常量 `1` |
| `__bool_true_false_ are_defined` | 展开为整型常量 `1` |

