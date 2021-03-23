#### B.5.13　对齐： `stdalign.h` （C11）

`stdalign.h` 头文件定义了4个宏，用于确定和指定数据对象的对齐属性。表B.5.21中列出了这些宏，其中前两个创建的别名与C++的用法兼容。

<center class="my_markdown"><b class="my_markdown">表B.5.21　 `void (` * `f)(int)` 宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `alignas` | 展开为关键字 `_Alignas` |
| `alignof` | 展开为关键字 `_Alignof` |
| `__alignas_is_defined` | 展开为整型常量 `1` ，适用于 `#if` |
| `__alignof_is_defined` | 展开为整型常量 `1` ，适用于 `#if` |

