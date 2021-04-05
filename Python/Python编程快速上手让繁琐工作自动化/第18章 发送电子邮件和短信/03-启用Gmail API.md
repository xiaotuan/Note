### 18.1.1　启用Gmail API

在编写代码之前，你必须先注册一个Gmail电子邮件账户。然后，进入Gmail→API→Guides→Python→Python QuickStart，单击该页面上的Enable the Gmail API按钮，并填写弹出的表格。

填写完表格后，页面上会显示证书.json文件的链接，你需要下载并将它放在与.py文件相同的文件夹中。credentials.json文件中包含了客户端ID和客户端密码信息，这些信息应该和你的Gmail口令一样，不要与其他人分享。

然后，在交互式环境中，输入以下代码：

```javascript
>>> import ezgmail, os
>>> os.chdir(r'C:\path\to\credentials_json_file')
>>> ezgmail.init()
```

确保将当前的工作目录设置为credentials.json所在的文件夹，并且连接到因特网。 `ezgmail.init()` 函数将打开你的浏览器，并进入一个Google登录页面。

输入你的Gmail地址和口令，页面可能会弹出警告“This app isn’t verified”（此应用未验证），但这没有问题。单击Advanced按钮，然后转到Go to Quickstart (unsafe)。（如果你为别人编写Python脚本，并且不希望这个警告让他们看见，你需要了解Google的App验证过程，这不在本书的范围之内。）当下一个页面提示你“QuickStart wants to access your Google Account”（QuickStart想要访问你的Google账户）时，单击Allow按钮，然后关闭浏览器。

这会生成一个token.json文件，它让你的Python脚本访问你输入的Gmail账户。浏览器只有在找不到已有的token.json文件时才会打开登录页面。有了credentials.json和token.json，你的Python脚本就可以从你的Gmail账户发送和读取电子邮件，而不需要你在源代码中包含Gmail口令。

