### 12.2　用requests模块从Web下载文件

`requests` 模块让你很容易从Web下载文件，不必担心一些复杂的问题，如网络错误、连接问题和数据压缩。 `requests` 模块不是Python自带的，所以必须先安装。通过命令行，运行 `pip install --user requests` （附录A详细介绍了如何安装第三方模块）。

导入 `requests` 模块是因为Python的 `urllib2` 模块用起来太复杂。实践时，请拿一支记号笔涂黑这一段，忘记我曾提到 `urllib2` 。如果你需要从Web下载东西，使用 `requests` 模块就好了。

接下来做一个简单的测试，确保 `requests` 模块已经正确安装。在交互式环境中输入以下代码：

```javascript
>>>  import requests
```

如果没有错误信息显示，表示 `requests` 模块安装成功了。

