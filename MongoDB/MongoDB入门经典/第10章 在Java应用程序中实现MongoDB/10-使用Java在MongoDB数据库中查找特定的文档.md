### 10.2.2　使用Java在MongoDB数据库中查找特定的文档

> **使用Java从MongoDB数据库检索特定的文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用查询对象和方法find()从示例数据库检索一组特定的文档。通过这个示例，您将熟悉如何创建查询对象以及如何使用它们来显示数据库请求返回的文档。程序清单10.4显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来查找并显示特定的文档。方法displayCursor()迭代游标并显示它表示的单词。
> 方法over12()查找长度超过12的单词；方法startingABC()查找以a、b或c打头的单词；方法startEndVowels()查找以元音字母打头和结尾的单词；方法over6Vowels()查找包含的元音字母超过6个的单词；方法nonAlphaCharacters()查找包含类型为other的字符集且长度为1的单词。
> 请执行如下步骤，创建并运行这个在示例数据集中查找特定文档并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour10中新建一个文件，并将其命名为JavaFindSpecific.java。
> 4．在这个文件中输入程序清单10.5所示的代码。这些代码使用了方法find()和查询对象。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour10。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单10.6显示了这个应用程序的输出。
> **程序清单10.5　JavaFindSpecific.java：在Java应用程序中从集合中查找并检索特定文档**
> **程序清单10.6　JavaFindSpecific.java-output：在Java应用程序中从集合中查找并检索特定文档的输出**
> ▲

一般而言，您不会想从服务器检索集合中的所有文档。方法find()和findOne()让您能够向服务器发送一个查询对象，从而像在MongoDB shell中那样限制文档。

要创建查询对象，可使用本章前面描述的BasicDBObject对象。对于查询对象中为子对象的字段，可创建BasicDBObject子对象；对于其他类型（如整型、字符串和数组）的字段，可使用相应的Java类型。

例如，要创建一个查询对象来查找size=5的单词，可使用下面的代码：

```go
BasicDBObject query = new BasicDBObject("size", 5);
myColl.find(query);
```

要创建一个查询对象来查找size>5的单词，可使用下面的代码：

```go
BasicDBObject query = new BasicDBObject("size",
     new BasicDBObject("$gt", 5));
myColl.find(query);
```

要创建一个查询对象来查找第一个字母为x、y或z的单词，可使用String数组，如下所示：

```go
BasicDBObject query = new BasicDBObject("first",
     new BasicDBObject("$in", new String[]{"x", "y", "z"}));
myColl.find(query);
```

利用上述技巧可创建需要的任何查询对象：不仅能为查找操作创建查询对象，还能为其他需要查询对象的操作这样做。

▼　Try It Yourself

```go
javac JavaFindSpecific.java
```

```go
java JavaFindSpecific
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBCollection;
04 import com.mongodb.BasicDBObject;
05 import com.mongodb.DBObject;
06 import com.mongodb.DBCursor;
07 public class JavaFindSpecific {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaFindSpecific.over12(collection);
14          JavaFindSpecific.startingABC(collection);
15          JavaFindSpecific.startEndVowels(collection);
16          JavaFindSpecific.over6Vowels(collection);
17          JavaFindSpecific.nonAlphaCharacters(collection);
18       } catch (Exception e) {
19          System.out.println(e);
20       }
21    }
22    public static void displayCursor(DBCursor cursor){
23       String words = "";
24       while(cursor.hasNext()){
25          DBObject doc = cursor.next();
26          words = words.concat(doc.get("word").toString()).concat(",");
27       }
28       if(words.length() > 65){
29          words = words.substring(0, 65) + "...";
30       }
31       System.out.println(words);
32    }
33    public static void over12(DBCollection collection){
34       BasicDBObject query =
35          new BasicDBObject("size",
36               new BasicDBObject("$gt", 12));
37       DBCursor cursor = collection.find(query);
38       System.out.println("\nWords with more than 12 characters: ");
39       JavaFindSpecific.displayCursor(cursor);
40    }
41    public static void startingABC(DBCollection collection){
42       BasicDBObject query =
43          new    BasicDBObject("first",
44                  new BasicDBObject("$in", new String[]{"a","b","c"}));
45       DBCursor cursor = collection.find(query);
46       System.out.println("\nWords starting with A, B or C: ");
47       JavaFindSpecific.displayCursor(cursor);
48    }
49    public static void startEndVowels(DBCollection collection){
50       BasicDBObject query =
51            new BasicDBObject("$and", new BasicDBObject[]{
52                 new BasicDBObject("first",
53                      new BasicDBObject("$in",
54                           new String[]{"a","e","i","o","u"})),
55            new BasicDBObject("last",
56                 new BasicDBObject("$in",
57                      new String[]{"a","e","i","o","u"}))
58       });
59       query.append("size", new BasicDBObject("$gt", 5));
60       DBCursor cursor = collection.find(query);
61       System.out.println("\nWords starting and ending with a vowel: ");
62       JavaFindSpecific.displayCursor(cursor);
63    }
64    public static void over6Vowels(DBCollection collection){
65       BasicDBObject query =
66            new BasicDBObject("stats.vowels",
67                 new BasicDBObject("$gt", 5));
68       DBCursor cursor = collection.find(query);
69       System.out.println("\nWords with more than 5 vowels: ");
70       JavaFindSpecific.displayCursor(cursor);
71    }
72    public static void nonAlphaCharacters(DBCollection collection){
73       BasicDBObject query =
74            new BasicDBObject("charsets",
75                 new BasicDBObject("$elemMatch",
76                      new BasicDBObject("$and", new BasicDBObject[]{
77                           new BasicDBObject("type", "other"),
78                           new BasicDBObject("chars",
79                                new BasicDBObject("$size", 1))
80       })));
81       DBCursor cursor = collection.find(query);
82       System.out.println("\nWords with 1 non-alphabet characters: ");
83       JavaFindSpecific.displayCursor(cursor);
84    }
85 }
```

```go
Words with more than 12 characters:
international,administration,environmental,responsibility,investi...
Words starting with A, B or C:
be,and,a,can't,at,but,by,as,can,all,about,come,could,also,because...
Words starting and ending with a vowel:
include,office,experience,everyone,evidence,available,involve,any...
Words with more than 5 vowels:
international,organization,administration,investigation,communica...
Words with 1 non-alphabet characters:
don't,won't,can't,shouldn't,e-mail,long-term,so-called,mm-hmm,
```

