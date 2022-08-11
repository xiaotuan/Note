输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了。这种交互式环境称为 Django shell，是测试项目和排除其他故障的理想之地。下面是一个交互式 shell 会话示例：

```shell
(11_env) learning_log$ python3 manage.py shell
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Android>, <Topic: Chess>, <Topic: Rock Climbing>]>
>>> from learning_logs.models import Entry
>>> Entry.objects.all()
<QuerySet [<Entry: In the opening phase of the game, it' s important ...>, <Entry: Of course, these are just guidelines. It will be i...>, <Entry: The opening is the first part of the game, roughly...>, <Entry: One of the most important concepts in climbing is ...>]>
>>> 
```

