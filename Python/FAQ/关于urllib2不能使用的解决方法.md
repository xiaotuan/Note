在 `Python 3` 中已经无法使用 `urllib2` 模块了（`Python 2` 好像也使用不了），可以使用 `urllib3` 模块代替，`urllib3` 的安装方法如下：

```shell
$ pip install urllib3
```

`urllib3` 的使用方法请查阅 [urllib3的使用方法](..\common\urllib3的使用方法.md)。

> 提示：其实在 urllib3 中已经包含了urllib 和 urllib2，因此，安装 urllib3 后就可以继续使用 urllib 模块了。

