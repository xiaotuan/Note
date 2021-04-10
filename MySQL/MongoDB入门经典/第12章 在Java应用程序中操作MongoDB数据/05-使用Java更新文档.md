### 12.4　使用Java更新文档

> **使用Java更新集合中的文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用DBCollection对象的方法update()来更新示例数据库的一个集合中的既有文档。通过这个示例，您将熟悉如何在Java中使用MongoDB更新运算符来更新文档。程序清单12.7显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，再调用其他方法更新文档。方法showWord()显示更新前和更新后的文档。
> 方法updateDoc()创建一个查询对象，它从数据库获取表示单词left的文档；再创建一个更新对象，它将字段word的值改为lefty，将字段size和stats.consonants的值加1，并将字母y压入到数组字段letters中。方法resetDoc()将文档恢复原样，以演示如何将字段值减1以及如何从数组字段中弹出值。
> 请执行下面的步骤，创建并运行这个更新示例数据库中文档并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour12中新建一个文件，并将其命名为JavaDocUpdate.java。
> 4．在这个文件中输入程序清单12.7所示的代码。这些代码使用update()来更新文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour12。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单12.8显示了这个应用程序的输出。
> **程序清单12.7　JavaDocUpdate.java：在Java应用程序中更新集合中的文档**
> **程序清单12.8　JavaDocUpdate.java-output：在Java应用程序中更新集合中文档的输出**
> ▲

将文档插入集合后，经常需要使用Java根据数据变化更新它们。DBCollection对象的方法update()让您能够更新集合中的文档，它多才多艺，但使用起来非常容易。下面是方法update()的语法：

```go
update(query, update, [upsert], [multi])
```

参数query是一个BasicDBObject对象，指定了要修改哪些文档。请求将判断query指定的属性和值是否与文档的字段和值匹配，进而更新匹配的文档。参数update是一个BasicDBObject对象，指定了要如何修改与查询匹配的文档。第8章介绍了可在这个对象中使用的更新运算符。

参数upsert是个布尔值；如果为true且没有文档与查询匹配，将插入一个新文档。参数multi也是一个布尔值；如果为true将更新所有与查询匹配的文档；如果为false将只更新与查询匹配的第一个文档。

例如，对于集合中字段category为new的文档，下面的代码将其字段category改为old。在这里，upsert被设置为false，因此即便没有字段category为new的文档，也不会插入新文档；而multi被设置为true，因此将更新所有匹配的文档：

```go
BasicDBObject query = new BasicDBObject("category", "New");
BasicDBObject update = new BasicDBObject("$set",
     new BasicDBObject("category", "Old"));
update(query, update, false, true);
```

▼　Try It Yourself

```go
javac JavaDocUpdate.java
```

```go
java JavaDocUpdate
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
09 public class JavaDocUpdate {
10    public static void main(String[] args) {
11       try {
12          MongoClient mongoClient = new MongoClient("localhost", 27017);
13          mongoClient.setWriteConcern(WriteConcern.JOURNAL_SAFE);
14          DB db = mongoClient.getDB("words");
15          DBCollection collection = db.getCollection("word_stats");
16          JavaDocUpdate.showWord(collection, "Before update");
17          JavaDocUpdate.updateDoc(collection);
18          JavaDocUpdate.showWord(collection, "After update");
19          JavaDocUpdate.resetDoc(collection);
20          JavaDocUpdate.showWord(collection, "After reset");
21       } catch (Exception e) {
22          System.out.println(e);
23       }
24    }
25    public static void updateDoc(DBCollection collection){
26       BasicDBObject query = new BasicDBObject("word", "left");
27       BasicDBObject update = new BasicDBObject();
28       update.append("$set", new BasicDBObject("word", "lefty"));
29       BasicDBObject inc = new BasicDBObject("size", 1);
30       inc.append("stats.consonants", 1);
31       update.append("$inc", inc);
32       update.append("$push", new BasicDBObject("letters", "y"));
33       WriteResult result = collection.update(query, update,
34                                                      false, false);
35       System.out.println("Update Result: \n" + result.toString());
36    }
37    public static void resetDoc(DBCollection collection){
38       BasicDBObject query = new BasicDBObject("word", "lefty");
39       BasicDBObject update = new BasicDBObject();
40       update.append("$set", new BasicDBObject("word", "left"));
41       BasicDBObject inc = new BasicDBObject("size", -1);
42       inc.append("stats.consonants", -1);
43       update.append("$inc", inc);
44       update.append("$pop", new BasicDBObject("letters", 1));
45       WriteResult result = collection.update(query, update,
46                                                      false, false);
47       System.out.println("Reset Result: \n" + result.toString());
48    }
49    public static void showWord(DBCollection collection, String msg){
50       System.out.println("\n" + msg + ": ");
51       BasicDBObject query = new BasicDBObject("word",
52            new BasicDBObject("$in", new String[]{"left", "lefty"}));
53       DBCursor cursor = collection.find(query);
54       while(cursor.hasNext()) {
55          DBObject doc = cursor.next();
56          System.out.println(doc);
57       }
58    }
59 }
```

```go
Before update:
{ "_id" : { "$oid" : "52e2992e138a073440e4663c"} ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "l" , "f" , "t"]} ,
                    { "type" : "vowels" , "chars" : [ "e"]}] ,
  "first" : "l" , "last" : "t" , "letters" : [ "l" , "e" , "f" , "t"] , "size" : 4.0 ,
  "stats" : { "consonants" : 3.0 , "vowels" : 1.0} , "word" : "left"}
Update Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : true ,
  "n" : 1 , "connectionId" : 38 , "err" : null , "ok" : 1.0}
After update:
{ "_id" : { "$oid" : "52e2992e138a073440e4663c"} ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "l" , "f" , "t"]} ,
                    { "type" : "vowels" , "chars" : [ "e"]}] ,
  "first" : "l" , "last" : "t" , "letters" : [ "l" , "e" , "f" , "t" , "y"] ,
  "size" : 5.0 , "stats" : { "consonants" : 4.0 , "vowels" : 1.0} , "word" :
  "lefty"}
Reset Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : true ,
  "n" : 1 , "connectionId" : 38 , "err" : null , "ok" : 1.0}
After reset:
{ "_id" : { "$oid" : "52e2992e138a073440e4663c"} ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "l" , "f" , "t"]} ,
                    { "type" : "vowels" , "chars" : [ "e"]}] ,
  "first" : "l" , "last" : "t" , "letters" : [ "l" , "e" , "f" , "t"] , "size" : 4.0 ,
  "stats" : { "consonants" : 3.0 , "vowels" : 1.0} , "word" : "left"}
```

