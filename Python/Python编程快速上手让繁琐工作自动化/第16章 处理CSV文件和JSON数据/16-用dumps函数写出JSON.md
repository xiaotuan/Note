### 16.4.2　用dumps函数写出JSON

`json.dumps()` 函数（它表示“dump string”，而不是“dumps”）将一个Python值转换成JSON格式的数据字符串。在交互式环境中输入以下代码：

```javascript
>>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
>>> import json
>>> stringOfJsonData = json.dumps(pythonValue)
>>> stringOfJsonData
'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
```

该值只能是以下基本Python数据类型之一：字典、列表、整型、浮点型、字符串、布尔型或 `None` 。

