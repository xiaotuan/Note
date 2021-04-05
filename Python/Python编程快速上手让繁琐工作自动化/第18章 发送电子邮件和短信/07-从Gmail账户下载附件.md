### 18.1.5　从Gmail账户下载附件

`GmailMessage` 对象有一个 `attachments` 属性，它是一个邮件附件文件名的列表。可以将这些名称中的任何一个传递给 `GmailMessage` 对象的 `download Attachment()` 方法来下载文件。也可以用 `downloadAllAttachments()` 方法一次下载所有文件。默认情况下， `ezgmail` 会将附件保存到当前的工作目录中，但是你也可以给 `downloadAttachment()` 和 `downloadAllAttachments()` 传递一个额外的 `downloadFolder` 关键字参数。例如：

```javascript
>>> import ezgmail
>>> threads = ezgmail.search('vacation photos')
>>> threads[0].messages[0].attachments
['tulips.jpg', 'canal.jpg', 'bicycles.jpg']
>>> threads[0].messages[0].downloadAttachment('tulips.jpg')
>>> threads[0].messages[0].downloadAllAttachments(downloadFolder='vacat ion2019')
['tulips.jpg', 'canal.jpg', 'bicycles.jpg']
```

如果一个文件与附件的文件名相同，下载的附件会自动覆盖。

