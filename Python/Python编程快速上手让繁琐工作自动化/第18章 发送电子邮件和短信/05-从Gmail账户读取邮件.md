### 18.1.3　从Gmail账户读取邮件

Gmail将相互回复的邮件组织成对话主线。当你在网页浏览器或通过应用程序登录Gmail时，你真正看到的是对话主线，而不是单个邮件（即使主线中只有一封邮件）。

`ezgmail` 有 `GmailThread` 和 `GmailMessage` 对象，分别代表对话主线和单个邮件。一个 `GmailThread` 对象有一个 `messages` 属性，它持有一个 `GmailMessage` 对象的列表。 `unread()` 函数返回一个 `GmailThread` 对象的列表，这个列表可以传递给 `ezgmail.summary()` ，输出该列表中的对话主线的摘要：

```javascript
>>> import ezgmail
>>> unreadThreads = ezgmail.unread() # List of GmailThread objects.
>>> ezgmail.summary(unreadThreads)
Al, Jon - Do you want to watch RoboCop this weekend? - Dec 09
Jon - Thanks for stopping me from buying Bitcoin. - Dec 09
```

`summary()` 函数可以方便地显示对话主线的快速摘要，但是要访问特定的邮件（和邮件的部分），你需要检查 `GmailThread` 对象的 `messages` 属性。 `messages` 属性包含了一个 `GmailMessage` 对象的列表，这些对象有 `subject` （主题）、 `body` （正文）、 `timestamp` （时间戳）、 `sender` （发件人）和 `recipient` （收件人）等描述邮件的属性：

```javascript
>>> len(unreadThreads)
2
>>> str(unreadThreads[0])
"<GmailThread len=2 snippet= Do you want to watch RoboCop this weekend?'>"
>>> len(unreadThreads[0].messages)
2
>>> str(unreadThreads[0].messages[0])
"<GmailMessage from='Al Sweigart <al@inventwithpython.com>' 
to='Jon Doe
<example@gmail.com>' 
timestamp=datetime.datetime(2018, 12, 9, 13, 28, 48)
subject='RoboCop' snippet='Do you want to watch RoboCop this weekend?'>"
>>> unreadThreads[0].messages[0].subject
'RoboCop'
>>> unreadThreads[0].messages[0].body
'Do you want to watch RoboCop this weekend?\r\n'
>>> unreadThreads[0].messages[0].timestamp
datetime.datetime(2018, 12, 9, 13, 28, 48)
>>> unreadThreads[0].messages[0].sender
'Al Sweigart <al@inventwithpython.com>'
>>> unreadThreads[0].messages[0].recipient
'Jon Doe <example@gmail.com>'

```

类似于 `ezgmail.unread()` 函数， `ezgmail.relative()` 函数将返回Gmail账户中最近的25个主线。你可以传递一个可选的 `maxResults` 关键字参数来改变这个限制：

```javascript
>>> recentThreads = ezgmail.recent()
>>> len(recentThreads)
25
>>> recentThreads = ezgmail.recent(maxResults=100)
>>> len(recentThreads)
46
```

