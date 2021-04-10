### 10.2.1　使用Java从MongoDB获取文档

> **使用Java从MongoDB检索文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用find()和findOne()从示例数据库中检索文档。通过这个示例，您将熟悉如何使用方法find()和findOne()以及如何处理响应。程序清单10.3显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，再调用其他方法来查找并显示文档。
> 方法getOne()调用方法findOne()从集合中获取单个文档，再显示该文档；方法getManyWhile()查找所有的文档，再使用while循环和方法hasNext()逐个获取这些文档，并计算总字符数。
> 方法getManyFor()查找集合中的所有文档，再使用for循环和方法next()获取前5个文档。方法getManyToArray()查找集合中的所有文档，再使用方法toArray()和参数5来获取前5个文档。
> 请执行如下步骤，创建并运行这个在示例数据集中查找文档并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour10中新建一个文件，并将其命名为JavaFind.java。
> 4．在这个文件中输入程序清单10.3所示的代码。这些代码使用了方法find()和findOne()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour10。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单10.4显示了这个应用程序的输出。
> **程序清单10.3　JavaFind.java：在Java应用程序中查找并检索集合中的文档**
> **程序清单10.4　JavaFind.java-output：在Java应用程序中查找并检索集合中文档的输出**
> ▲

DBCollection对象提供了方法find()和findOne()，它们与MongoDB shell中的同名方法类似，也分别查找一个和多个文档。

调用findOne()时，将以DBObject对象的方式从服务器返回单个文档，然后您就可根据需要在应用程序中使用这个对象，如下所示：

```go
DBObject doc = myColl.findOne();
```

DBCollection对象的方法find()返回一个DBCursor对象，这个对象表示找到的文档，但不取回它们。可以多种不同的方式迭代DBCursor对象。

可以使用while循环和方法hasNext()来判断是否到达了游标末尾，如下所示：

```go
DBCursor cursor = myColl.find();
while(cursor.hasNext()){
   DBObject doc = cursor.next();
   System.out.println(doc.toString());
}
```

还可使用方法toArray()将游标转换为Java Array对象，再使用任何Java技术迭代该对象。例如，下面的代码查找集合中的所有文档，再将前5个转换为一个List并迭代它：

```go
DBCursor cursor = collection.find();
List<DBObject> docs = cursor.toArray(5);
for(final DBObject doc : docs) {
   System.out.println(doc.toString());
}
```

▼　Try It Yourself

```go
javac JavaFind.java
```

```go
java JavaFind
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBCollection;
04 import com.mongodb.DBObject;
05 import com.mongodb.DBCursor;
06 import java.util.List;
07 public class JavaFind {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaFind.getOne(collection);
14          JavaFind.getManyWhile(collection);
15          JavaFind.getManyFor(collection);
16          JavaFind.getManyToArray(collection);
17       } catch (Exception e) {
18          System.out.println(e);
19       }
20    }
21    public static void getOne(DBCollection collection){
22       DBObject doc = collection.findOne();
23       System.out.println("Single Document: ");
24       System.out.println(doc.toString());
25    }
26    public static void getManyWhile(DBCollection collection){
27       DBCursor cursor = collection.find();
28       Long count = 0L;
29       while(cursor.hasNext()) {
30          DBObject doc = cursor.next();
31          count += (Long)Math.round((Double)doc.get("size"));
32       }
33       System.out.println("\nTotal characters using While loop: ");
34       System.out.println(count);
35    }
36    public static void getManyFor(DBCollection collection){
37       System.out.println("\nFor loop iteration: ");
38       DBCursor cursor = collection.find();
39       for(Integer i=0; i<5; i++){
40          DBObject doc = cursor.next();
41          System.out.println(doc.get("word"));
42       }
43    }
44    public static void getManyToArray(DBCollection collection){
45       System.out.println("\nConverted to array iteration: ");
46       DBCursor cursor = collection.find();
47       List<DBObject> docs = cursor.toArray(5);
48       for(final DBObject doc : docs) {
49          System.out.println(doc.get("word"));
50       }
51    }
52 }
```

```go
Single Document:
{ "_id" : { "$oid" : "52e2992e138a073440e46378"} , "word" : "the" ,
   "first" : "t" , "last" : "e" , "size" : 3.0 , "letters" : [ "t" , "h" , "e"] ,
   "stats" : { "vowels" : 1.0 , "consonants" : 2.0} ,
   "charsets" : [ { "type" : "consonants" , "chars" : [ "t" , "h"]} ,
                     { "type" : "vowels" , "chars" : [ "e"]}]}
Total characters using While loop:
16868
For loop iteration:
the
be
and
of
a
Converted to array iteration:
the
be
and
of
a
```

