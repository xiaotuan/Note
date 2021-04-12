### 1.4 MongoDB数据类型

BSON数据格式提供了多种类型，可用于以二进制方式存储JavaScript对象。这些类型与JavaScript类型非常接近，理解它们很重要，因为查询MongoDB时，您可能要查找指定属性的值为特定类型的对象。例如，您可能在数据库中查询这样的文档：其时间戳为String 对象或Date对象。

MongoDB给每种数据类型都分配了1～255的整数ID号，以方便您按类型查询。表1.1列出了MongoDB支持的数据类型以及MongoDB用来标识它们的编号。

<center class="my_markdown"><b class="my_markdown">表1.1 MongoDB数据类型及其ID号</b></center>

| 类型 | 编号 |
| :-----  | :-----  | :-----  | :-----  |
| Double（双精度浮点数） | 1 |
| String（字符串） | 2 |
| Object（对象） | 3 |
| Array（数组） | 4 |
| Binary data（二进制数据） | 5 |
| Object ID（对象ID） | 7 |
| Boolean（布尔值） | 8 |
| Date（日期） | 9 |
| Null（空） | 10 |
| Regular expression（正则表达式） | 11 |
| JavaScript | 13 |
| Symbol（符号） | 14 |
| JavaScript（带作用域） | 15 |
| 32-bit integer（32位整数） | 16 |
| Timestamp（时间戳） | 17 |
| 64-bit integer（64位整数） | 18 |
| Min key | 255 |
| Max key | 127 |

使用MongoDB支持的各种数据类型时，需要注意的另一点是它们的排序顺序。比较不同BSON类型的值时，MongoDB使用下面的排序顺序（从小到大）：

1．Min key（内部使用的类型）。

2．Null。

3．数字（32为整数、64位整数和双精度浮点数）。

4．符号和字符串。

5．对象。

6．数组。

7．二进制数据。

8．对象ID。

9．布尔值。

10．日期和时间戳。

11．正则表达式。

12．Max key（内部使用的类型）。

