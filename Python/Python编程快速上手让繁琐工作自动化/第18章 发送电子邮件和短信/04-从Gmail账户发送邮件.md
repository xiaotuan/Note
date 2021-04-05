### 18.1.2　从Gmail账户发送邮件

一旦你有了token.json文件， `ezgmail` 模块应该可以通过一个函数调用来发送邮件：

```javascript
>>> import ezgmail
>>> ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')
```

如果想将文件附加到你的电子邮件中，可以为 `send()` 函数提供一个额外的列表参数：

```javascript
>>> ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
['attachment1.jpg', 'attachment2.mp3'])
```

请注意，作为安全和反垃圾邮件功能的一部分，Gmail可能不会发送文本完全相同的重复邮件（因为这些很可能是垃圾邮件），或包含.exe或.zip文件附件的邮件（因为它们很可能是病毒）。

你也可以提供可选的关键字参数 `cc` 和 `bcc` 来抄送和密件抄送：

```javascript
>>> import ezgmail
>>> ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')
```

如果你需要记住token.json文件是针对哪个Gmail地址，你可以检查 `ezgmail.EMAIL_ ADDRESS` 。注意，这个变量只有在 `ezgmail.init()` 或其他 `ezgmail` 函数被调用后才会被填充：

```javascript
>>> import ezgmail
>>> ezgmail.init()
>>> ezgmail.EMAIL_ADDRESS
'example@gmail.com'
```

请确保一样对待token.json文件和你的口令。如果其他人获得这个文件，他们就可以访问你的Gmail账户（尽管他们无法更改你的Gmail口令）。要撤销之前发出的token.json文件，请访问 Google 账号的安全性页面，并撤销对 QuickStart 应用程序的访问。你需要运行 `ezgmail.init()` 并再次进行登录，以获得一个新的token.json文件。

