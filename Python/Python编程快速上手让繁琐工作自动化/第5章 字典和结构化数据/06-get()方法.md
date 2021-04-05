### 5.1.4　get()方法

在访问一个键的值之前，检查该键是否存在于字典中，这很麻烦。好在字典有一个 `get()` 方法，它有两个参数，分别为要取得其值的键，以及当该键不存在时返回的备用值。

在交互式环境中输入以下代码：

```javascript
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
```

因为 `picnicItems` 字典中没有 `'eggs'` 键，所以 `get()` 方法返回的默认值是0。不使用 `get()` 方法，代码就会产生一个错误信息，就像下面的例子：

```javascript
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
KeyError: 'eggs'
```

