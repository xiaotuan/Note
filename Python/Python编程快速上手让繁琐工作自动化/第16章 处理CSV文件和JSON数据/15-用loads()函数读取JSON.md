### 16.4.1　用loads()函数读取JSON

要将包含JSON数据的字符串转换为Python的值，就要将它传递给 `json.loads()` 函数（这个名字的意思是“load string”，而不是“loads”）。在交互式环境中输入以下代码：

```javascript
>>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
"felineIQ": null}'
>>> import json
>>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
>>> jsonDataAsPythonValue
{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
```

导入 `json` 模块后，就可以调用 `loads()` ，并向它传入一个JSON数据字符串。请注意，JSON字符串总是用双引号。它将该数据返回为一个Python字典。Python字典是没有顺序的，因此如果输出 `jsonDataAsPythonValue` ，那么键-值对可能以不同的顺序出现。

