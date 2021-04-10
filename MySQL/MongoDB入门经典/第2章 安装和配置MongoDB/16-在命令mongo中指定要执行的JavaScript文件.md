### 2.4.3 在命令mongo中指定要执行的JavaScript文件

> **MongoDB shell 脚本编程**
> 在本节中，您将创建自己的MongoDB shell脚本。本书后面要求您能够创建JavaScript文件，并在其中使用MongoDB shell命令连接到数据库、访问集合及执行各种任务。
> 请按下面的步骤创建一个JavaScript文件，它使用MongoDB shell命令输出一些信息。
> 1．创建一个名为code的文件夹，用于存储本书的示例代码。
> 2．在文件夹code中，创建一个名为hour02的文件夹。
> 3．在文件夹code/hour02中，创建文件shell_script.js。
> 4．将程序清单2.1所示的代码复制到这个文件中。这些代码包含一些基本的MongoDB shell命令，并使用print()和printjson()来输出结果。
> 5．将这个文件存盘。
> 6．启动MongoDB服务器。
> 7．再打开一个控制台窗口，并切换到目录code/hour02。
> 8．执行命令mongo shell_script.js来运行这个脚本，您将看到类似于程序清单2.2的输出。
> 9．使用命令mongo启动MongoDB shell。
> 10．在MongoDB shell中，使用命令load("shell_script.js")再次执行这个脚本。
> 输出应与您在第8步看到的相同。
> **程序清单2.1 shell_script.js：执行MongoDB shell命令并输出结果的JavaScript文件**
> **程序清单2.2 shell_script.js-output：执行MongoDB shell命令的JavaScript文件的输出**
> ▲

最常用的MongoDB shell脚本编程方法是，创建一个JavaScript文件，并直接使用命令mongo来执行它。MongoDB shell将读取JavaScript文件，逐行执行并在执行完毕后退出。

要在执行JavaScript代码时将结果输出到控制台，可使用函数print()。您还可使用MongoDB shell特有的函数printjson()，它自动设置JSON对象的格式。然而printjson()采用的格式占用的屏幕空间太多，最好使用JavaScript方法（如JSON.stringify()）来设置输出JSON对象的格式。

例如，假设您在文件get_collections.js中添加了如下JavaScript代码：

```go
db = connect("localhost/words");
printjson(db.getCollectionNames())
```

可直接在控制台中使用下面的mongo命令来执行这个脚本：

```go
mongo get_collections.js
```

这将加载该脚本、连接到数据库words并显示其中的集合。输出类似于下面这样：

```go
MongoDB shell version: 2.4.8
connecting to: test
type "help" for help
connecting to: localhost/words
[
         "system.indexes",
         "word_stats",
         "word_stats2",
         "word_stats_new",
         "words"
]
```

还可执行多个JavaScript文件，为此只需在命令mongo中用空格分隔它们，如下所示：

```go
mongo get_ collections.js load_data.js get_data.js
```

▼　Try It Yourself

```go
01 print("Hostname:");
02 print("\t"+hostname());
03 print("Date:");
04 print("\t"+Date());
05 db = connect("localhost/admin");
06 print("Admin Collections:");
07 printjson(db.getCollectionNames());
```

```go
Hostname:
         MyComputer
Date:
         Mon Jan 20 2014 13:10:36 GMT-0700 (Mountain Standard Time)
connecting to: localhost/admin
Admin Collections:
  [ "fs.chunks", "fs.files", "system.indexes", "system.users" ]
```

