### 14.4　利用Google Sheets 配额

因为Google Sheets是在线的，所以很容易在多个用户之间共享工作表，这些用户可以同时访问工作表。但是，这也意味着读取和更新表的速度会比读取和更新存储在硬盘上的Excel文件要慢。此外，Google__Sheets对可以执行的读写操作数量也有限制。

根据Google的开发者指南，用户每天最多只能创建250个新的电子表格，免费的Google账户每100秒可以执行100次读取和100次写入请求。试图超过这个限度将引发 `googleapiclient. errors.HttpError` ： `Quota exceeded for quota group` 异常。EZSheets会自动捕捉到这个异常并重试请求。当这种情况发生时，读取或写入数据的函数调用将需要几秒（甚至需要一两分钟）才能返回。如果请求继续失败（如果另一个使用相同证书的脚本也在提出请求，这是有可能的），EZSheets将重新抛出这个异常。

这意味着有时你的EZSheets方法调用可能需要几秒的时间才会返回。如果你想查看你的API使用量或增加你的配额，请访问Google Cloud Platform的IAM & Admin Quotas页面，了解如何为增加的使用量付费。如果你想要自己处理HttpError异常，可以将 `ezsheets.IGNORE_ QUOTA` 设置为 `True` ，当EZSheets的方法遇到这些异常时，它就会抛出这些异常。

