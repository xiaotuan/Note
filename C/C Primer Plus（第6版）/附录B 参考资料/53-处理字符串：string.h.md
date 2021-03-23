#### B.5.22　处理字符串： `string.h` 

`string.h` 库定义了 `size_t` 类型和空指针要使用的 `NULL` 宏。 `string.h` 头文件提供了一些分析和操控字符串的函数，其中一些函数以更通用的方式处理内存。表B.5.37列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.37　字符串函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void`  * `memchr(const void`  * `s, int c,` | `size_t n);` | 在 `s` 指向对象的前 `n` 个字符中查找是否有 `c` 。如果找到，则返回首次出现 `c` 处的指针，如果未找到则返回 `NULL` |
| `int memcmp(const void` * `s1, const void`  * `s2,size_t n);` | 比较 `s1` 指向对象中的前 `n` 个字符和 `s2` 指向对象的前 `n` 个字符，每个值都解释为 `unsigned char` 类型。如果 `n` 个字符都匹配，则两个对象完全相同；否则，比较两个对象中首次不匹配的字符对。如果两个对象相同，函数返回 `0` ；如果在数值上第 `1` 个对象小于第 `2` 个对象，函数返回小于 `0` 的值；如果在数值上第 `1` 个对象大于第 `2` 个对象，函数返回大于 `0` 的值 |
| `void`  * `memcpy(void`  * `restrict s1, const` | `void`  *  `restrict s2,size_t n);` | 把 `s2` 所指向位置上的 `n` 字节拷贝到 `s1` 指向的位置上，函数返回 `s1` 的值。如果两个位置出现重叠，其行为是未定义的 |
| `void`  * `memmove(void` * `s1, const void`  * `s2,size_t n);` | 把 `s2` 所指向位置上的 `n` 字节拷贝到 `s1` 指向的位置上，其行为与拷贝类似，返回 `s1` 的值。但是，如果出现局部重叠情况，该函数会先把重叠的内容拷贝至临时位置 |
| `void`  * `memset(void`  * `s,int v, size_t n);` | 把 `v` 的值（转换为 `unsigned char` ）拷贝至 `s` 指向的前 `n` 字节中，函数返回 `s` |
| `char`  * `strcat(char`  * `restrict s1, const` | `char`  *  `restrict s2);` | 把 `s2` 指向的字符串拷贝到 `s1` 指向字符串后面， `s2` 字符串的第 `1` 个字符覆盖 `s1` 字符串的空字符。该函数返回 `s1` |
| `char`  * `strncat(char`  * `restrict s1, const char`  *  `restrict s2,size_t n);` | 把 `s2` 指向字符串的 `n` 个字符拷贝到 `s1` 指向的字符串后面（或拷贝到 `s2` 的空字符为止）。 `s2` 字符串的第 `1` 个字符覆盖 `s1` 字符串的空字符。函数返回 `s1` |
| `char`  * `strcpy(char`  * `restrict s1, const` | `char`  *  `restrict s2);` | 把 `s2` 指向的字符串拷贝到 `s1` 指向的位置。函数返回 `s1` |
| `char`  * `strncpy(char`  * `restrict s1, const char`  *  `restrict s2,size_t n);` | 把 `s2` 指向字符串的 `n` 个字符拷贝到 `s1` 指向的位置（或拷贝到 `s2` 的空字符为止）。如果在拷贝 `n` 个字符之前遇到空字符，则在拷贝字符后面添加若干个空字符，使其长度为 `n` ；如果拷贝 `n` 个字符没有遇到空字符，则不添加空字符。函数返回 `s1` |
| `int strcmp(const char` * `s1, const char`  * `s2);` | 比较 `s1` 和 `s2` 指向的两个字符串。如果完全匹配，则两字符串相同，否则比较首次出现不匹配的字符对。通过字符编码值比较字符。如果两个字符串相同，函数返回 `0` ；如果第 `1` 个字符串小于第 `2` 个字符串，函数返回小于 `0` 的值；如果第 `1` 个字符串大于第 `2` 个字符串，函数返回大于 `0` 的值 |
| `int strcoll(const char`  * `s1, const char` | * `s2);` | 与 `strcmp()` 类似，但是该函数使用当前本地化的 `LC_COLLATE` 类别（由 `setlocale()` 函数设置）所指定的排序方式进行比较 |
| `int strncmp(const char`  * `s1, const char` | * `s2, size_t n);` | 比较 `s1` 和 `s2` 指向数组中的前 `n` 个字符，或比较到第 `1` 个空字符位置。如果所有的字符对都匹配，则两个数组相同否则比较两个数组中首次不匹配的字符对。通过字符编码值比较字符。如果两个数组相同，函数返回 `0` ；如果第 `1` 个数组小于第 `2` 个数组，函数返回小于 `0` 的值；如果第 `1` 个数组大于第 `2` 个数组，函数返回大于 `0` 的值 |
| `size_t strxfrm(char` *  `restrict s1, const char`  *  `restrict s2,size_t n);` | 转换 `s2` 中的字符串，并把转换后的前 `n` 个字符（包括空字符）拷贝到 `s1` 指向的数组中。用 `strcmp()` 比较转换后的两个字符串的结果和用 `strcoll()` 比较两个未转换字符串的结果相同。函数返回转换后的字符串长度（不包括末尾的空字符） |
| `char`  * `strchr(const char`  * `s, int c);` | 查找 `s` 指向的字符串中首次出现 `c` 的位置。空字符是字符串的一部分。函数返回一个指针，指向首次出现 `c` 的位置。如果没有找到指定的 `c` 则返回 `NULL` |
| `size_t strcspn(const char`  * `s1, const char` * `s2);` | 返回 `s1` 中未出现 `s2` 中任何字符的最大起始段长度 |
| `char`  * `strpbrk(const char`  * `s1, const char` * `s2);` | 返回一个指针，指向 `s1` 中与 `s2` 任意字符匹配的第 `1` 个字符的位置。如果未发现任何匹配的字符，函数返回 `NULL` |
| `char`  * `strrchr(const char`  * `s, int c);` | 在 `s` 指向的字符串中查找末次出现 `c` 的位置（即从 `s2` 右侧开始查找字符 `c` 首次出现的位置）。空字符是字符串的一部分。如果找到，函数返回指向该位置的指针；如果未找到，则返回 `NULL` |
| `size_t strspn(const char`  * `s1, const char` * `s2);` | 返回 `s1` 中包含 `s2` 所有字符的最大起始段长度 |
| `char`  * `strstr(const char`  * `s1, const char` * `s2);` | 返回一个指针，指向 `s1` 中首次出现 `s2` 中字符序列（不包括结束的空字符）的位置。如果未找到，函数返回 `NULL` |
| `char`  * `strtok(char`  * `restrict s1, const` | `char`  *  `restrict s2);` | 该函数把 `s1` 字符串分解为单独的记号。 `s2` 字符串包含了作为记号分隔符的字符。按顺序调用该函数。第 `1` 次调用时， `s1` 应指向待分解的字符串。函数定位到非分隔符后的第 `1` 个记号分隔符，并用空字符替换它。函数返回一个指针，指向存储第 `1` 个记号的字符串。如果未找到记号，函数返回 `NULL` 。在此次调用 `strtok()` 查找字符串中的更多记号。每次调用都返回指向下一个记号的指针，如果未找到则返回 `NULL` （请参看表后面的示例） |
| `char`  *  `strerror(int errnum);` | 返回一个指针，指向与存储在 `errnum` 中的错误号相对应的错误信息字符串（依实现而异） |
| `int strlen(const char` *  `s);` | 返回字符串 `s` 中的字符数（末尾的空字除外） |

`strtok()` 函数的用法有点不寻常，下面演示一个简短的示例。

```c
#include <stdio.h>
#include <string.h>
int main(void)
{
     char data[] = " C is\t too#much\nfun!";
     const char tokseps[] = " \t\n#";  /* 分隔符 */
     char * pt;
     puts(data);
     pt = strtok(data,tokseps);         /* 首次调用 */
     while (pt)                         /* 如果pt是NULL，则退出 */
     {
          puts (pt);                    /* 显示记号 */
          pt = strtok(NULL, tokseps);   /* 下一个记号 */
     }
     return 0;
}
```

下面是该示例的输出：

```c
     C is too#much
fun!
C
is
too
much
fun!
```

