### 17.4　datetime模块

`time` 模块用于取得UNIX纪元时间戳，并加以处理。但是，如果以更方便的格式显示日期或对日期进行算术运算（例如，搞清楚205天前是什么日期或123天后是什么日期），就应该使用 `datetime` 模块。

`datetime` 模块有自己的 `datetime` 数据类型。 `datetime` 值表示一个特定的时刻。在交互式环境中输入以下代码：

```javascript
  >>> import datetime
❶ >>> datetime.datetime.now()
❷ datetime.datetime(2019, 2, 27, 11, 10, 49, 55, 53)
❸ >>> dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
❹ >>> dt.year, dt.month, dt.day
   (2019, 10, 21)
❺ >>> dt.hour, dt.minute, dt.second
   (16, 29, 0)
```

根据你的计算机的时钟，调用 `datetime.datetime.now()` ❶会返回一个 `datetime` 对象❷，以表示当前的日期和时间。这个对象包含当前时刻的年、月、日、时、分、秒和微秒。也可以利用 `datetime.datetime()` 函数❸，并向它传入代表年、月、日、时、分、秒的整数，以得到特定时刻的 `datetime` 对象。这些整数将保存在 `datetime` 对象的 `year` 、 `month` 、 `day` ❹、 `hour` 、 `minute` 和 `second` ❺属性中。

UNIX纪元时间戳可以通过 `datetime.datetime.fromtimestamp()` 转换为 `datetime` 对象。 `datetime` 对象的日期和时间将根据本地时区转换。在交互式环境中输入以下代码：

```javascript
>>> import datetime, time
>>> datetime.datetime.fromtimestamp(1000000)
datetime.datetime(1970, 1, 12, 5, 46, 40)
>>> datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2019, 10, 21, 16, 30, 0, 604980)
```

调用 `datetime.datetime.fromtimestamp()` 并传入 `1000000` ，返回一个 `datetime` 对象，表示UNIX纪元后1 000 000秒的时刻。传入 `time.time()` ，即当前时刻的UNIX纪元时间戳，则返回当前时刻的 `datetime` 对象。因此，表达式 `datetime.datetime.now()` 和 `datetime.datetime.fromtimestamp(time. time())` 做的事情相同，它们都返回当前时刻的 `datetime` 对象。

`datetime` 对象可以用比较操作符进行比较，弄清楚谁在前面。后面的 `datetime` 对象是“更大”的值。在交互式环境中输入以下代码：

```javascript
❶ >>> halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
❷ >>> newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
  >>> oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
❸ >>> halloween2019 == oct31_2019
  True
❹ >>> halloween2019 > newyears2020
  False
❺ >>> newyears2020 > halloween2019
  True
  >>> newyears2020 != oct31_2019
  True
```

为2019年10月31日的第一个时刻（午夜）创建一个 `datetime` 对象，将它保存在 `halloween2019` 中❶。为2020年1月1日的第一个时刻创建一个 `datetime` 对象，将它保存在 `newyears2020` 中❷。然后，为2019年10月31日的午夜创建另一个对象，将它保存在 `oct31_2019` 中。比较 `halloween2019` 和 `oct31_2019` ，它们是相等的❸。比较 `newyears2020` 和 `halloween2019` ， `newyears2020` 大于（晚于） `halloween2019` ❹❺。

