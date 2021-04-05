### 17.4.1　timedelta数据类型

`datetime` 模块还提供了 `timedelta` 数据类型，它表示一个“时段”，而不是一个“时刻”。在交互式环境中输入以下代码：

```javascript
❶ >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
❷ >>> delta.days, delta.seconds, delta.microseconds
   (11, 36548, 0)
  >>> delta.total_seconds()
  986948.0
  >>> str(delta)
  '11 days, 10:09:08'
```

要创建 `timedelta` 对象，就用 `datetime.timedelta()` 函数。 `datetime. timedelta()` 函数接收关键字参数 `weeks` 、 `days` 、 `hours` 、 `minutes` 、 `seconds` 、 `milliseconds` 和 `microseconds` 。没有 `month` 和 `year` 关键字参数，这是因为“月”和“年”是可变的时间，依赖于特定月份或年份。 `timedelta` 对象拥有的总时间以天、秒、微秒来表示。这些数字分别保存在 `days` 、 `seconds` 和 `microseconds` 属性中。 `total_seconds()` 方法返回只以秒表示的时间。将一个 `timedelta` 对象传入 `str()` ，将返回格式良好的、人类可读的字符串表示形式。

在这个例子中，我们将关键字参数传入 `datetime.timedelta()` ，指定11天、10小时、9分和8秒的时间，将返回的 `timedelta` 对象保存在 `delta` 中❶。该 `timedelta` 对象的 `days` 属性为11， `seconds` 属性为36 548（10小时、9分钟、8秒，以秒表示）❷。调用 `total_seconds()` 可得到11天、10小时、9分和8秒是986 948秒。最后，将这个 `timedelta` 对象传入 `str()` ，返回一个字符串，明确解释了这段时间。

算术运算符可以用于对 `datetime` 值进行“日期运算”。例如，要计算今天之后1000天的日期，可在交互式环境中输入以下代码：

```javascript
>>> dt = datetime.datetime.now()
>>> dt
datetime.datetime(2018, 12, 2, 18, 38, 50, 636181)
>>> thousandDays = datetime.timedelta(days=1000)
>>> dt + thousandDays
datetime.datetime(2021, 8, 28, 18, 38, 50, 636181)
```

首先，生成表示当前时刻的 `datetime` 对象，将其保存在 `dt` 中。然后生成一个 `timedelta` 对象，它表示1000天，保存在 `thousandDays` 中。将 `dt` 与 `thousandDays` 相加，得到一个 `datetime` 对象，表示现在之后的1000天。Python将完成日期运算，弄清楚2018年12月2日之后的1000天将是2021年8月28日。这很有用，因为如果要从一个给定的日期计算1000天之后，需要记住每个月有多少天、闰年的因素和其他棘手的细节。 `datetime` 模块将为你处理所有这些问题。

利用+和-运算符， `timedelta` 对象可以与 `datetime` 对象或其他 `timedelta` 对象相加或相减。利用*和/运算符， `timedelta` 对象可以乘以或除以整数或浮点数。在交互式环境中输入以下代码：

```javascript
❶ >>> oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
❷ >>> aboutThirtyYears = datetime.timedelta(days=365 * 30)
   >>> oct21st
   datetime.datetime(2019, 10, 21, 16, 29)
   >>> oct21st - aboutThirtyYears
   datetime.datetime(1989, 10, 28, 16, 29)
   >>> oct21st - (2 * aboutThirtyYears)
   datetime.datetime(1959, 11, 5, 16, 29)
```

这里，我们生成了一个 `DateTime` 对象，表示2019年10月21日❶；生成了一个 `timedelta` 对象，表示大约30年的时间（我们假设每年为365天）❷。从 `oct21st` 中减去 `aboutThirtyYears` ，我们就得到一个 `datetime` 对象，它表示2019年10月21日前30年的一天。从 `oct21st` 中减去 `2 * aboutThirtyYears` ，得到一个 `datetime` 对象，它表示2019年10月21日之前60年的一天。

