### 11.2　使用Java查找不同的字段值

> **使用Java检索一组文档中指定字段的不同值**
> 在本节中，您将编写一个Java应用程序，它使用DBCollection对象的方法distinct() 来检索示例数据库中不同的字段值。通过这个示例，您将熟练地生成数据集中的不同字段值列表。程序清单11.7显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来找出并显示不同的字段值。
> 方法sizesOfAllWords()找出并显示所有单词的各种长度；方法sizesOfQWords()找出并显示以q打头的单词的各种长度；方法firstLetterOfLongWords()找出并显示长度超过12的单词的各种长度。
> 请执行下面的步骤，创建并运行这个Java应用程序，它找出示例数据集中文档集的不同字段值，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaFindDistinct.java。
> 4．在这个文件中输入程序清单11.7所示的代码。这些代码对文档集执行distinct()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.8显示了这个应用程序的输出。
> **程序清单11.7　JavaFindDistinct.java：在Java应用程序中找出文档集中不同的字段值**
> **程序清单11.8　JavaFindDistinct.java-output：在Java应用程序中找出文档集中不同字段值的输出**
> ▲

一种很有用的MongoDB集合查询是，获取一组文档中某个字段的不同值列表。不同（distinct）意味着纵然有数千个文档，您只想知道那些独一无二的值。

DBCollection对象的方法distinct()让您能够找出指定字段的不同值列表，这种方法的语法如下：

```go
distinct(key, [query])
```

其中参数key是一个字符串，指定了要获取哪个字段的不同值。要获取子文档中字段的不同值，可使用句点语法，如stats.count。参数query是一个包含标准查询选项的对象，指定了要从哪些文档中获取不同的字段值。

例如，假设有一些包含字段first、last和age的用户文档，要获取年龄超过65岁的用户的不同姓，可使用下面的操作：

```go
BasicDBObject query = new BasicDBObject("age",
     new BasicDBObject("$gt", 5));
lastNames = myCollection.distinct('last', query);
```

方法distinct()返回一个数组，其中包含指定字段的不同值，例如：

```go
["Smith", "Jones", ...]
```

▼　Try It Yourself

```go
javac JavaFindDistinct.java
```

```go
java JavaFindDistinct
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBCollection;
04 import com.mongodb.BasicDBObject;
05 import com.mongodb.DBObject;
06 import com.mongodb.DBCursor;
07 import java.util.List;
08 public class JavaFindDistinct {
09    public static void main(String[] args) {
10       try {
11          MongoClient mongoClient = new MongoClient("localhost", 27017);
12          DB db = mongoClient.getDB("words");
13          DBCollection collection = db.getCollection("word_stats");
14          JavaFindDistinct.sizesOfAllWords(collection);
15          JavaFindDistinct.sizesOfQWords(collection);
16          JavaFindDistinct.firstLetterOfLongWords(collection);
17       } catch (Exception e) {
18          System.out.println(e);
19       }
20    }
21    public static void sizesOfAllWords(DBCollection collection){
22       List<Double> results = collection.distinct("size");
23       System.out.println("\nDistinct Sizes of words: ");
24       System.out.println(results.toString());
25    }
26    public static void sizesOfQWords(DBCollection collection){
27       BasicDBObject query = new BasicDBObject("first", "q");
28       List<Double> results = collection.distinct("size", query);
29       System.out.println("\nDistinct Sizes of words starting with Q: ");
30       System.out.println(results.toString());
31    }
32    public static void firstLetterOfLongWords(DBCollection collection){
33       BasicDBObject query =
34            new BasicDBObject("size",
35            new BasicDBObject("$gt", 12));
36       List<String> results = collection.distinct("first", query);
37       System.out.println("\nDistinct first letters of words longer " +
38                              "than 12 characters: ");
39       System.out.println(results.toString());
40    }
41 }
```

```go
Distinct Sizes of words:
[ 3.0 , 2.0 , 1.0 , 4.0 , 5.0 , 9.0 , 6.0 , 7.0 , 8.0 , 10.0 , 11.0 , 12.0 , 13.0 , 14.0]
Distinct Sizes of words starting with Q:
[ 8.0 , 5.0 , 7.0 , 4.0]
Distinct first letters of words longer than 12 characters:
[ "i" , "a" , "e" , "r" , "c" , "u" , "s" , "p" , "t"]
```

