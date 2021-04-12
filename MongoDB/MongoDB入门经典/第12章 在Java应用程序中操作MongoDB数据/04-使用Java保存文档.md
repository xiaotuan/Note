### 12.3　使用Java保存文档

> **使用Java将文档保存到集合中**
> 在本节中，您将创建一个简单的Java应用程序，它使用DBCollection对象的方法save()来更新示例数据库中的一个既有文档。通过这个示例，您将熟悉如何使用Java更新并保存文档对象。程序清单12.5显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来保存文档。方法showWord()显示更新前和更新后的单词ocean。
> 方法saveBlueDoc()从数据库中获取单词ocean的文档，使用put()将字段category改为blue，再使用方法save()保存这个文档。方法resetDoc()从数据库获取单词ocean的文档，使用方法put()将字段category恢复为空，再使用方法save()保存这个文档。
> 请执行如下步骤，创建并运行这个将文档保存到示例数据库中并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour12中新建一个文件，并将其命名为JavaDocSave.java。
> 4．在这个文件中输入程序清单12.5所示的代码。这些代码使用save()来保存文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour12。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单12.6显示了这个应用程序的输出。
> **程序清单12.5　JavaDocSave.java：在Java应用程序中将文档保存到集合中**
> **程序清单12.6　JavaDocSave.java-output：在Java应用程序中将文档保存到集合中的输出**
> ▲

一种更新数据库中文档的便利方式是，使用DBCollection对象的方法save()，这种方法接受一个DBObject作为参数，并将其保存到数据库中。如果指定的文档已存在于数据库中，就将其更新为指定的值；否则就插入一个新文档。

方法save()的语法如下，其中参数doc是一个要保存到集合中的DBObject或BasicDBObject对象：

```go
save(doc)
```

▼　Try It Yourself

```go
javac JavaDocSave.java
```

```go
java JavaDocSave
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.WriteConcern;
03 import com.mongodb.DB;
04 import com.mongodb.DBCollection;
05 import com.mongodb.DBObject;
06 import com.mongodb.BasicDBObject;
07 import com.mongodb.DBCursor;
08 import com.mongodb.WriteResult;
09 public class JavaDocSave {
10    public static void main(String[] args) {
11       try {
12          MongoClient mongoClient = new MongoClient("localhost", 27017);
13          mongoClient.setWriteConcern(WriteConcern.JOURNAL_SAFE);
14          DB db = mongoClient.getDB("words");
15          DBCollection collection = db.getCollection("word_stats");
16          JavaDocSave.showWord(collection, "Before save");
17          JavaDocSave.saveBlueDoc(collection);
18          JavaDocSave.showWord(collection, "After save");
19          JavaDocSave.resetDoc(collection);
20          JavaDocSave.showWord(collection, "After reset");
21       } catch (Exception e) {
22          System.out.println(e);
23       }
24    }
25    public static void saveBlueDoc(DBCollection collection){
26       BasicDBObject query = new BasicDBObject("word", "ocean");
27       DBObject word = collection.findOne(query);
28       word.put("category", "blue");
29       WriteResult result = collection.save(word);
30       System.out.println("Update Result: \n" + result.toString());
31    }
32    public static void resetDoc(DBCollection collection){
33       BasicDBObject query = new BasicDBObject("word", "ocean");
34       DBObject word = collection.findOne(query);
35       word.put("category", "");
36       WriteResult result = collection.save(word);
37       System.out.println("Update Result: \n" + result.toString());
38    }
39    public static void showWord(DBCollection collection, String msg){
40       System.out.println("\n" + msg + ": ");
41       BasicDBObject query = new BasicDBObject("word", "ocean");
42       BasicDBObject fields = new BasicDBObject("word", 1);
43       fields.append("category", 1);
44       DBObject doc = collection.findOne(query, fields);
45       System.out.println(doc);
46    }
47 }
```

```go
Before save:
{ "_id" : { "$oid" : "52e2992e138a073440e469f2"} , "word" : "ocean" ,
  "category" : ""}
Update Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : true , "n" : 1 ,
"connectionId" : 37 , "err" : null , "ok" : 1.0}
After save:
{ "_id" : { "$oid" : "52e2992e138a073440e469f2"} , "word" : "ocean" ,
"category" : "blue"}
Update Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : true , "n" : 1 ,
"connectionId" : 37 , "err" : null , "ok" : 1.0}
After reset:
{ "_id" : { "$oid" : "52e2992e138a073440e469f2"} , "word" : "ocean" ,
"category" : ""}
```

