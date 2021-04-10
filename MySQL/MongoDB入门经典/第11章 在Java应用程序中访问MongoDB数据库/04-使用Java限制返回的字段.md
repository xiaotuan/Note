### 11.1.2　使用Java限制返回的字段

> **在方法find()中使用参数fields来减少DBCursor对象表示的文档中的字段数**
> 在本节中，您将编写一个简单的Java应用程序，它在方法find()中使用参数fields来限制返回的字段。通过这个示例，您将熟悉如何使用方法find()的参数fields，并了解它对结果的影响。程序清单11.3显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来查找文档并显示其指定的字段。方法displayCursor()迭代游标并显示找到的文档。
> 方法includeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，使其只返回指定的字段；方法excludeFields()接受一个字段名列表，创建参数fields并将其传递给方法find()，以排除指定的字段。
> 请执行如下步骤，创建并运行这个Java应用程序，它在示例数据集中查找文档、限制返回的字段并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaFindFields.java。
> 4．在这个文件中输入程序清单11.3所示的代码。这些代码在调用方法find()时传递了参数fields。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.4显示了这个应用程序的输出。
> **程序清单11.3　JavaFindFields.java：在Java应用程序中限制从集合返回的文档包含的字段**
> **程序清单11.4　JavaFindFields.java-output：在Java应用程序中限制从集合返回的文档包含的字段的输出**
> ▲

为限制文档检索时返回的数据量，另一种极有效的方式是限制要返回的字段。文档可能有很多字段在有些情况下很有用，但在其他情况下没用。从MongoDB服务器检索文档时，需考虑应包含哪些字段，并只请求必要的字段。

要对DBCollection对象的方法find()从服务器返回的字段进行限制，可使用参数fields。这个参数是一个BasicDBObject对象，它使用值true来包含字段，使用值false来排除字段。

例如，要在返回文档时排除字段stats、value和comments，可使用下面的fields参数：

```go
BasicDBObject fields = new BasicDBObject("stats", false);
fields.append("value", false);
fields.append("comments", false);
DBCursor cursor = myColl.find(null, fields);
```

这里将查询对象指定成了null，因为您要查找所有的文档。

仅包含所需的字段通常更容易。例如，如果只想返回first字段为t的文档的word和size字段，可使用下面的代码：

```go
BasicDBObject query = new BasicDBObject("first", "t");
BasicDBObject fields = new BasicDBObject("word", true);
fields.append("size", true);
DBCursor cursor = myColl.find(query, fields);
```

▼　Try It Yourself

```go
javac JavaFindFields.java
```

```go
java JavaFindFields
```

```go
01 import com.mongodb.DBCursor;
02 import com.mongodb.DBObject;
03 import com.mongodb.MongoClient;
04 import com.mongodb.DB;
05 import com.mongodb.DBCollection;
06 import com.mongodb.BasicDBObject;
07 import java.util.Arrays;
08 public class JavaFindFields {
09    public static void main(String[] args) {
10       try {
11          MongoClient mongoClient = new MongoClient("localhost", 27017);
12          DB db = mongoClient.getDB("words");
13          DBCollection collection = db.getCollection("word_stats");
14          JavaFindFields.excludeFields(collection,
15               new String[]{});
16          JavaFindFields.includeFields(collection,
17               new String[]{"word"});
18          JavaFindFields.includeFields(collection,
19               new String[]{"word", "stats"});
20          JavaFindFields.excludeFields(collection,
21               new String[]{"stats", "charsets"});
22       } catch (Exception e){
23          System.out.println(e);
24       }
25    }
26    public static void displayCursor(DBCursor cursor){
27       while(cursor.hasNext()){
28          DBObject doc = cursor.next();
29          System.out.println(doc);
30       }
31    }
32    public static void includeFields(DBCollection collection,
33                                            String[] fields) {
34       BasicDBObject query = new BasicDBObject("first", "p");
35       BasicDBObject fieldDoc = new BasicDBObject();
36       for(final String field : fields) {
37          fieldDoc.append(field, 1);
38       }
39       DBCursor cursor = collection.find(query, fieldDoc);
40       cursor.limit(1);
41       System.out.println("\nIncluding " + Arrays.toString(fields) +
42                              " fields: ");
43       JavaFindFields.displayCursor(cursor);
44    }
45    public static void excludeFields(DBCollection collection,
46                                           String[] fields) {
47       BasicDBObject query = new BasicDBObject("first", "p");
48       BasicDBObject fieldDoc = new BasicDBObject();
49       for(final String field : fields) {
50          fieldDoc.append(field, false);
51       }
52       DBCursor cursor = collection.find(query, fieldDoc);
53       cursor.limit(1);
54       System.out.println("\nExcluding " + Arrays.toString(fields) +
55                              " fields: ");
56       JavaFindFields.displayCursor(cursor);
57    }
58 }
```

```go
Excluding [] fields:
{ "_id" : { "$oid" : "52e2992e138a073440e463b5"} , "word" : "people" ,
"first" : "p" ,
  "last" : "e" , "size" : 6.0 , "letters" : [ "p" , "e" , "o" , "l"] ,
  "stats" : { "vowels" : 3.0 , "consonants" : 3.0} ,
  "charsets" : [ { "type" : "consonants" , "chars" : [ "p" , "l"]} ,
                    { "type" : "vowels" , "chars" : [ "e" , "o"]}]}
Including [word] fields:
{ "_id" : { "$oid" : "52e2992e138a073440e46378"} , "word" : "the"}
Including [word, stats] fields:
{ "_id" : { "$oid" : "52e2992e138a073440e46378"} , "word" : "the" ,
  "stats" : { "vowels" : 1.0 , "consonants" : 2.0}}
Excluding [stats, charsets] fields:
{ "_id" : { "$oid" : "52e2992e138a073440e463b5"} , "word" : "people" ,
"first" : "p" ,
  "last" : "e" , "size" : 6.0 , "letters" : [ "p" , "e" , "o" , "l"]}
```

