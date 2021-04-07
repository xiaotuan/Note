### 7.2.8　Amazon Web服务

Scrapy对访问Amazon Web服务有内置支持。你可以在AWSACCESS KEY_ID设置中存储AWS访问密钥，在AWS_SECRET_ACCESS_KEY设置中存储私密密钥。默认情况下，这些设置均为空。可以在如下场景中使用：

+ 当下载以 `s3://` 开头的URL时（而不是https://等）；
+ 当通过媒体管道使用 `s3://` 路径存储文件或缩略图时；
+ 当在 `s3://` 目录中存储 `Item` 的输出Feed时。

不要将这些设置存储在 `settings.py` 文件当中，以防未来某天由于任何原因造成代码公开时被泄露。

