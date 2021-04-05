### 16.4　json模块

Python的 `json` 模块处理了JSON数据字符串和Python值之间转换的所有细节，并得到了 `json.loads()` 和 `json.dumps()` 函数。JSON不能存储每一种Python值，它只能包含以下数据类型的值：字符串、整型、浮点型、布尔型、列表、字典和 `NoneType` 。JSON不能表示Python特有的对象，如 `File` 对象、CSV  `reader` 或 `writer` 对象、 `Regex` 对象或 `selenium WebElement` 对象。

