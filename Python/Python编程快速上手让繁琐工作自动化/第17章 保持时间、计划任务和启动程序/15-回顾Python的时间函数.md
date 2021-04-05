### 17.5　回顾Python的时间函数

在Python中，日期和时间可能涉及好几种不同的数据类型和函数。下面回顾一下表示时间的3种不同类型的值。

+ UNIX纪元时间戳（ `time` 模块中使用）是一个浮点值或整型值，表示自1970年1月1日午夜0点以来的秒数。
+ `datetime` 对象（属于 `datetime` 模块）包含一些整型值，保存在 `year` 、 `month` 、 `day` 、 `hour` 、 `minute` 和 `second` 等属性中。
+ `timedelta` 对象（属于 `datetime` 模块）表示的是一段时间，而不是一个特定的时刻。

下面回顾一下时间函数及其参数和返回值。

+ `time.time()` 函数返回一个浮点值，表示当前时刻的UNIX纪元时间戳。
+ `time.sleep(seconds)` 函数让程序暂停 `seconds` 参数指定的秒数。
+ `datetime.datetime(year, month, day, hour, minute, second)` 函数返回参数指定的时刻的 `datetime` 对象。如果没有提供 `hour` 、 `minute` 或 `second` 参数，那么它们默认为0。
+ `datetime.datetime.now()` 函数返回当前时刻的 `datetime` 对象。
+ `datetime.datetime.fromtimestamp(epoch)` 函数返回 `epoch` 时间戳参数表示的时刻的 `datetime` 对象。
+ `datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds)` 函数返回一个表示一段时间的 `timedelta` 对象。该函数的关键字参数都是可选的，不包括 `month` 或 `year` 。
+ `total_seconds()` 方法用于 `timedelta` 对象，返回 `timedelta` 对象表示的秒数。
+ `strftime(format)` 方法返回一个时间字符串，由 `datetime` 对象表示，该时间字符串采用基于 `format` 字符串的自定义格式。详细格式参见表17-1。
+ `datetime.datetime.strptime(time_string, format)` 函数返回一个 `datetime` 对象，它的时刻由 `time_string` 指定，并利用 `format` 字符串参数来解析。详细格式参见表17-1。

