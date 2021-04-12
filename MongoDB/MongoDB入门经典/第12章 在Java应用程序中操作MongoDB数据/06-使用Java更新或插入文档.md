### 12.5　使用Java更新或插入文档

> **使用Java更新集合中的文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用方法update()对示例数据库执行upsert操作：先插入一个新文档，再更新这个文档。通过这个示例，您将熟悉如何在Java应用程序使用方法update()来执行upsert操作。程序清单12.9显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，再调用其他的方法来更新文档。方法showWord()用于显示单词被添加前后以及被更新后的情况。
> 方法addUpsert()创建一个数据库中没有的新单词，再使用upsert操作来插入这个新文档。这个文档包含的信息有些不对，因此方法updateUpsert()执行upsert操作来修复这些错误；这次更新了既有文档，演示了upsert操作的更新功能。
> 请执行如下步骤，创建并运行这个Java应用程序，它对示例数据库中的文档执行upsert操作并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour12中新建一个文件，并将其命名为JavaDocUpsert.java。
> 4．在这个文件中输入程序清单12.9所示的代码。这些代码使用update()来对文档执行upsert操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour12。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单12.10显示了这个应用程序的输出。
> **程序清单12.9　JavaDocUpsert.java：在Java应用程序中对集合中的文档执行upsert操作**
> **程序清单12.10　JavaDocUpsert.java-output：在Java应用程序中对集合中文档执行upsert操作的输出**
> ▲

在Java中，DBCollection对象的方法update()的另一种用途是，用于执行upsert操作。upsert操作先尝试更新集合中的文档；如果没有与查询匹配的文档，就使用$set运算符来创建一个新文档，并将其插入到集合中。下面显示了方法update()的语法：

```go
update(query, update, [upsert], [multi])
```

参数query指定要修改哪些文档；参数update是一个BasicDBObject对象，指定了要如何修改与查询匹配的文档。要执行upsert操作，必须将参数upsert设置为true，并将参数multi设置为false。

例如，下面的代码对name=myDoc的文档执行upsert操作。运算符$set指定了用来创建或更新文档的字段。由于参数upsert被设置为true，因此如果没有找到指定的文档，将创建它；否则就更新它：

```go
BasicDBObject query = new BasicDBObject("name", "myDoc");
BasicDBObject setOp = new BasicDBObject("name", "myDoc");
setOp.append("number", 5);
setOp.append("score", 10);
BasicDBObject update = new BasicDBObject("$set", setOp);
update(query, update, true, false);
```

▼　Try It Yourself

```go
javac JavaDocUpsert.java
```

```go
java JavaDocUpsert
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
09 public class JavaDocUpsert {
10    public static void main(String[] args) {
11       try {
12          MongoClient mongoClient = new MongoClient("localhost", 27017);
13          mongoClient.setWriteConcern(WriteConcern.JOURNAL_SAFE);
14          DB db = mongoClient.getDB("words");
15          DBCollection collection = db.getCollection("word_stats");
16          JavaDocUpsert.showWord(collection, "Before upsert");
17          JavaDocUpsert.addUpsert(collection);
18          JavaDocUpsert.updateUpsert(collection);
19       } catch (Exception e) {
20          System.out.println(e);
21       }
22    }
23    public static void showWord(DBCollection collection, String msg){
24       System.out.println("\n" + msg + ": ");
25       BasicDBObject query = new BasicDBObject("word", "righty");
26       DBObject doc = collection.findOne(query);
27       System.out.println(doc);
28    }
29    public static void addUpsert(DBCollection collection){
30       BasicDBObject query = new BasicDBObject("word", "righty");
31       BasicDBObject setOp = new BasicDBObject("word","righty");
32       setOp.append("first", "l").append("last", "y");
33       setOp.append("size", 4).append("category", "New");
34       BasicDBObject stats = new BasicDBObject("consonants", 4);
35       stats.append("vowels", 1);
36       setOp.append("stats", stats);
37       setOp.append("letters", new String[]{"r","i","g","h"});
38       BasicDBObject cons = new BasicDBObject("type", "consonants");
39       cons.append("chars", new String[]{"r","g","h"});
40       BasicDBObject vowels = new BasicDBObject("type", "vowels");
41       vowels.append("chars", new String[]{"i"});
42       BasicDBObject[] charsets = new BasicDBObject[]{cons, vowels};
43       setOp.append("charsets", charsets);
44       BasicDBObject update = new BasicDBObject("$set", setOp);
45       WriteResult result = collection.update(query, update,
46                                                       true, false);
47       System.out.println("Update as insert Result: \n" +
48                              result.toString());
49       JavaDocUpsert.showWord(collection, "After upsert as insert");
50    }
51    public static void updateUpsert(DBCollection collection){
52       BasicDBObject query = new BasicDBObject("word", "righty");
53       BasicDBObject setOp = new BasicDBObject("word","righty");
54       setOp.append("first", "l").append("last", "y");
55       setOp.append("size", 6).append("category", "New");
56       BasicDBObject stats = new BasicDBObject("consonants", 5);
57       stats.append("vowels", 1);
58       setOp.append("stats", stats);
59       setOp.append("letters", new String[]{"r","i","g","h","t","y"});
60       BasicDBObject cons = new BasicDBObject("type", "consonants");
61       cons.append("chars", new String[]{"r","g","h","t","y"});
62       BasicDBObject vowels = new BasicDBObject("type", "vowels");
63       vowels.append("chars", new String[]{"i"});
64       BasicDBObject[] charsets = new BasicDBObject[]{cons, vowels};
65       setOp.append("charsets", charsets);
66       BasicDBObject update = new BasicDBObject("$set", setOp);
67       WriteResult result = collection.update(query, update,
68                                                      true, false);
69       System.out.println("Update as insert Result: \n" +
70                              result.toString());
71       JavaDocUpsert.showWord(collection, "After upsert as update");
72    }
73 }
```

```go
Before upsert:
null
Update as insert Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : false ,
  "upserted" : {
"$oid" : "52eadfa3381e4f7e1b27b410"} , "n" : 1 , "connectionId" : 117 , "err" : null , "ok" : 1.0}
After upsert as insert:
{ "_id" : { "$oid" : "52eadfa3381e4f7e1b27b410"} , "category" : "New" ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "r" , "g" , "h"]} ,
                    { "type" : "vowels" , "chars" : [ "i"]}] ,
  "first" : "l" , "last" : "y" , "letters" : [ "r" , "i" , "g" , "h"] ,
  "size" : 4 , "stats" : { "consonants" : 4 , "vowels" : 1} , "word" : "righty"}
Update as insert Result:
{ "serverUsed" : "localhost/127.0.0.1:27017" , "updatedExisting" : true , "n" : 1 ,
"connectionId" : 117 , "err" : null , "ok" : 1.0}
After upsert as update:
{ "_id" : { "$oid" : "52eadfa3381e4f7e1b27b410"} , "category" : "New" ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "r" , "g" , "h" , "t" , "y"]} ,
                    { "type" : "vowels" , "chars" : [ "i"]}] ,
  "first" : "l" , "last" : "y" , "letters" : [ "r" , "i" , "g" , "h" , "t" , "y"] ,
  "size" : 6 , "stats" : { "consonants" : 5 , "vowels" : 1} , "word" : "righty"}
```

