### 17.4.4　将字符串转换成datetime对象

如果有一个字符串的日期信息，如 `'2019/10/21 16:29:00'` 或 `'October 21, 2019'` ，需要将它转换为 `datetime` 对象，就用 `datetime.datetime.strftime()` 函数。 `strptime()` 函数与 `strftime()` 函数相反。自定义的格式字符串使用的指令与 `strftime()` 的相同。必须将该格式字符串传入 `strptime()` ，这样它就知道如何解析和理解日期字符串（ `strptime()` 函数名中p表示解析，即parse）了。

在交互式环境中输入以下代码：

```javascript
❶  >>> datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
   datetime.datetime(2019, 10, 21, 0, 0)
   >>> datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
   datetime.datetime(2019, 10, 21, 16, 29)
   >>> datetime.datetime.strptime("October of '19", "%B of '%y")
   datetime.datetime(2019, 10, 1, 0, 0)
   >>> datetime.datetime.strptime("November of '63", "%B of '%y")
   datetime.datetime(2063, 11, 1, 0, 0)
```

要从字符串 `'October 21, 2019'` 取得一个 `datetime` 对象，需要将该字符串作为第一个参数传递给 `strptime()` ，并将对应于 `'October 21, 2019'` 的定制格式字符串作为第二个参数❶。带有日期信息的字符串必须准确匹配定制的格式字符串，否则Python将抛出 `ValueError` 异常。

