### 12.2　使用Java删除文档

> **使用Java从集合中删除文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用DBCollection对象的方法从示例数据库的一个集合中删除文档。通过这个示例，您将熟悉如何使用Java删除文档。程序清单12.3显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，再调用其他的方法来删除文档。方法showNewDocs()显示前面创建的新文档，从而核实它们确实从集合中删除了。
> 方法removeNewDocs()使用一个查询对象来删除字段category为New的文档。
> 请执行下面的步骤，创建并运行这个从示例数据库中删除文档并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour12中新建一个文件，并将其命名为JavaDocDelete.java。
> 4．在这个文件中输入程序清单12.3所示的代码。这些代码使用remove()来删除文档。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour12。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单12.4显示了这个应用程序的输出。
> **程序清单12.3　JavaDocDelete.java：在Java应用程序中从集合中删除文档**
> **程序清单12.4　JavaDocDelete.java-output：在Java应用程序中从集合中删除文档的输出**
> ▲

在Java中，有时候需要从MongoDB集合中删除文档，以减少消耗的空间，改善性能以及保持整洁。DBCollection对象的方法remove()使得从集合中删除文档非常简单，其语法如下：

```go
remove([query])
```

其中参数query是一个BasicDBObject对象，指定要了删除哪些文档。请求将query指定的字段和值与文档的字段和值进行比较，进而删除匹配的文档。如果没有指定参数query，将删除集合中的所有文档。

例如，要删除集合words_stats中所有的文档，可使用如下代码：

```go
DBCollection collection = myDB.getCollection('word_stats');
WriteResult results = collection.remove();
```

下面的代码删除集合words_stats中所有以a打头的单词：

```go
DBCollection collection = myDB.getCollection('word_stats');
BasicDBObject query = new BasicDBObject("first", "a");
collection.remove(query);
```

▼　Try It Yourself

```go
javac JavaDocDelete.java
```

```go
java JavaDocDelete
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
09 public class JavaDocDelete {
10    public static void main(String[] args) {
11       try {
12          MongoClient mongoClient = new MongoClient("localhost", 27017);
13          mongoClient.setWriteConcern(WriteConcern.JOURNAL_SAFE);
14          DB db = mongoClient.getDB("words");
15          DBCollection collection = db.getCollection("word_stats");
16          JavaDocDelete.showNewDocs(collection, "Before delete");
17          JavaDocDelete.removeNewDocs(collection);
18          JavaDocDelete.showNewDocs(collection, "After delete");
19       } catch (Exception e) {
20          System.out.println(e);
21       }
22    }
23    public static void removeNewDocs(DBCollection collection){
24       BasicDBObject query = new BasicDBObject("category", "New");
25       WriteResult result = collection.remove(query);
26       System.out.println("Delete Result: \n" +
27            result.toString());
28    }
29    public static void showNewDocs(DBCollection collection,
30                                         String msg){
31       System.out.println("\n" + msg + ": ");
32       BasicDBObject query = new BasicDBObject("category", "New");
33       DBCursor cursor = collection.find(query);
34       while(cursor.hasNext()) {
35          DBObject doc = cursor.next();
36          System.out.println(doc);
37       }
38    }
39 }
```

```go
Before delete:
{ "_id" : { "$oid" : "52e80bc4ba4191662131feec"} , "word" : "tweet" , "first" : "t",
  "last" : "t" , "size" : 6 , "category" : "New" ,
  "stats" : { "consonants" : 3} , "letters" : [ "t" , "w" , "e"] ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "t" , "w"]} ,
                    { "type" : "vowels" , "chars" : [ "e"]}]}
{ "_id" : { "$oid" : "52e80bc4ba4191662131feea"} , "word" : "selfie" , "first" :
  "s" ,
  "last" : "e" , "size" : 6 , "category" : "New" ,
  "stats" : { "consonants" : 3 , "vowels" : 3} ,
  "letters" : [ "s" , "e" , "l" , "f" , "i"] ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "s" , "l" , "f"]} ,
                    { "type" : "vowels" , "chars" : [ "e" , "i"]}]}
{ "_id" : { "$oid" : "52e80bc4ba4191662131feeb"} , "word" : "google" , "first" :
  "g" ,
  "last" : "e" , "size" : 6 , "category" : "New" ,
  "stats" : { "consonants" : 3 , "vowels" : 2} , "letters" : [ "g" , "o" , "l" , "e"] ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "g" , "l"]} ,
  { "type" : "vowels" , "chars" : [ "o" , "e"]}]}
Delete Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "n" : 3 , "connectionId" : 36 ,
  "err" : null , "ok" : 1.0}
After delete:
```

