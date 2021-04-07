### 7.2.6　feed

feed可以让你将Scrapy抓取得到的数据输出到本地文件系统或远程服务器当中。 `FEED_URI.FEED_URI` 决定了feed的位置，该设置中可能会包含命名参数。比如， `scrapy fast -o "%(name)s_%(time)s.jl"` 将会自动以当前时间和爬虫名称（ `fast` ）填充输出文件名。如果需要使用一个自定义参数，比如 `%(foo)s` ，那么 `feed` 输出器需要你在爬虫中提供 `foo` 属性。此外，feed的存储，如S3、FTP或本地文件系统，也定义在URI中。例如， `FEED_URI='s3://mybucket/file.json'` 将使用你的Amazon凭证（ `AWS_ACCESS_KEY_ID` 和 `AWS_SECRET_ACCESS_KEY` ）上传文件到Amazon的S3当中。Feed的格式（JSON、JSON Line、CSV及XML）可以使用 `FEED_FORMAT` 确定。如果没有设定该设置，Scrapy将会根据 `FEED_URI` 的扩展名猜测格式。通过将 `FEED_STORE_EMPTY` 设置为 `True` ，可以选择输出空的feed。此外，还可以使用 `FEED_EXPORT_FIELDS` 设置，选择只输出指定的几个字段。该设置对于具有固定标题列的 `.csv` 文件尤其有用。最后， `FEED_URI_PARAMS` 用于定义对 `FEED_URI` 中任意参数进行后置处理的函数。

