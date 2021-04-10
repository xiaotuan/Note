### 10.1.5　理解Java对象BasicDBObject和DBObject

> **使用Java MongoDB驱动程序连接到MongoDB**
> 明白Java MongoDB驱动程序中的对象后，便可以开始在Java应用程序中实现MongoDB了。本节将引导您在Java应用程序中逐步实现MongoDB。
> 请执行如下步骤，使用Java MongoDB驱动程序创建第一个Java MongoDB应用程序。
> 1．如果还没有安装Java JDK，请访问http://docs.oracle.com/javase/7/docs/webnotes/ install/，按说明下载并安装用于您的开发平台的Java JDK。
> 2．确保将<jdk_install>/bin添加到了系统路径中，并能够在控制台提示符下执行命令javac和java。
> 3．从下面的网址下载Java MongoDB驱动程序，并将其存储在本书使用的示例代码文件夹code：http://central.maven.org/ maven2/org/mongodb/mongo-java-driver/2.11.3/mongo- java-driver-2.11.3.jar。
> 4．将第3步下载的JAR文件的存储位置添加到环境变量CLASSPATH。
> 5．确保启动了MongoDB服务器。
> 6．再次运行脚本文件code/hour05/generate_words.js以重置数据库words。
> 7．在文件夹code/hour10中新建一个文件，并将其命名为JavaConnect.java。
> 8．在这个文件中输入程序清单10.1所示的代码。这些代码创建MongoClient、DB和DBCollection对象，并检索文档。
> 9．将这个文件存盘。
> 10．打开一个控制台窗口，并切换到目录code/hour10。
> 11．执行下面的命令来编译这个新建的Java文件：
> 12．执行下面的命令来运行这个连接到MongoDB的Java应用程序。程序清单10.2 显示了这个应用程序的输出。
> **程序清单10.1　JavaConnect.java：在Java应用程序中连接到MongoDB数据库**
> **程序清单10.2　JavaConnect.java-output：在Java应用程序中连接到MongoDB数据库的输出**
> ▲

正如您在本书前面介绍MongoDB shell的章节中看到的，大多数数据库、集合和游标操作都将对象作为参数。这些对象定义了查询、排序、聚合以及其他运算符。文档也是以对象的方式从数据库返回的。

在MongoDB shell中，这些对象是JavaScript对象，但在Java中，表示文档和请求参数的对象都是特殊对象。服务器返回的文档是用DBObject对象表示的，这种对象提供了获取和设置文档中字段的功能。对于用作请求参数的对象，是用BasicDBObject表示的。

BasicDBObject是使用下面的构造函数创建的，其中key为JavaScript属性的名称，而value为JavaScript属性的值：

```go
BasicDBObject(key, value)
```

要给BasicDBObject对象添加属性，可使用方法append()。

例如，假设您要创建一个查询对象，用于查找第一个字母为a且长度超过6的单词。在MongoDB shell中，可使用如下代码：

```go
find({"first":"a", "size": {"$gt": 6}});
```

而在Java中，必须使用如下语法创建一个将传递给方法find()的BasicDBObject对象：

```go
BasicDBObject query = new BasicDBObject("first", "a");
query.append("size", new BasicDBObject("$gt", 6));
```

使用这种方式，可创建需要传递给MongoDB数据库请求的对象。有关执行查询、更新、聚合等需要的对象的结构，请参阅介绍MongoDB shell的第5～9章。

DBObject提供了如下方法，可用于获取和设置服务器请求返回的文档的属性。

+ get(fieldName)：返回文档中指定字段的值。
+ put(fieldName, value)：设置文档中指定字段的值。
+ putAll(map)：将一个Java对象Map作为参数，并根据其中指定的键/值对设置文档的字段。
+ toMap()：以Map对象的方式返回文档中所有的字段。

▼　Try It Yourself

```go
javac JavaConnect.java
```

```go
java JavaConnect
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.WriteConcern;
03 import com.mongodb.DB;
04 import com.mongodb.DBCollection;
05 public class JavaConnect {
06    public static void main(String[] args) {
07       try {
08          MongoClient mongoClient = new MongoClient("localhost", 27017);
09          mongoClient.setWriteConcern(WriteConcern.JOURNAL_SAFE);
10          DB db = mongoClient.getDB("words");
11          DBCollection collection = db.getCollection("word_stats");
12          System.out.println("Number of Documents: " +
13          new Long(collection.count()).toString());
14       } catch (Exception e) {
15         System.out.println(e);
16       }
17    }
18 }
```

```go
Number of Documents: 2673
```

