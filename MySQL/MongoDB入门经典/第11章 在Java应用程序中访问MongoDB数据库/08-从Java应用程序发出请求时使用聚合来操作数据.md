### 11.4　从Java应用程序发出请求时使用聚合来操作数据

> **在Java应用程序中使用聚合来生成数据**
> 在本节中，您将编写一个简单的Java应用程序，它使用DBCollection对象的方法aggregate()从示例数据库检索各种聚合数据。通过这个示例，您将熟悉如何使用aggregate()来利用聚合流水线在MongoDB服务器上处理数据，再返回结果。程序清单11.11显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他方法来聚合数据并显示结果。方法displayAggregate()显示聚合结果。
> 方法largeSmallVowels()使用了一条包含运算符$match、$group和$sort的聚合流水线，这条流水线查找以元音字母开头的单词，根据第一个字母将这些单词分组，并找出各组中最长和最短单词的长度。
> 方法top5AverageWordFirst()使用了一条包含运算符$group、$sort和$limit的聚合流水线，这条流水线根据第一个字母将单词分组，并找出单词平均长度最长的前5组。
> 请执行下面的步骤，创建并运行这个Java应用程序，它使用聚合流水线来处理示例数据集中的文档，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaAggregate.java。
> 4．在这个文件中输入程序清单11.11所示的代码。这些代码对文档集执行aggregate()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.12显示了这个应用程序的输出。
> **程序清单11.11　JavaAggregate.java：在Java应用程序中使用聚合流水线生成数据集**
> **程序清单11.12　JavaAggregate.java-output：在Java应用程序中使用聚合流水线生成数据集的输出**
> ▲

在Java应用程序中使用MongoDB时，另一个很有用的工具是聚合框架。DBCollection对象提供了对数据执行聚合操作的方法aggregate()，这个方法的语法如下：

```go
aggregate(operator, [operator, ...])
```

参数operator是一系列运算符对象，提供了用于聚合数据的流水线。这些运算符对象是使用聚合运算符创建的DBObject对象。聚合运算符在第9章介绍过，您现在应该熟悉它们。

例如，下面的代码定义了运算符$group和$limit，其中运算符$group根据字段word进行分组（并将该字段的值存储在结果文档的_id字段中），使用$avg计算size字段的平均值（并将结果存储在average字段中）。请注意，在聚合运算中引用原始文档的字段时，必须在字段名前加上$：

```go
BasicDBObject groupOps = new BasicDBObject("_id", "$word");
groupOps.append("average", new BasicDBObject("$avg", "$size"));
BasicDBObject group = new BasicDBObject("$group", groupOps);
BasicDBObject limit = new BasicDBObject("$limit", 10);
AggregationOutput result = collection.aggregate(group, limit);
```

方法aggregate()返回一个包含聚合结果的AggregationOutput对象。AggregationOutput对象的方法results()返回一个可迭代的对象，您可使用它来访问结果。为演示这一点，下面的代码逐项显示聚合结果的内容：

```go
for (Iterator<DBObject> items = result.results().iterator(); items. hasNext();){
   System.out.println(items.next());
}
```

▼　Try It Yourself

```go
javac JavaAggregate.java
```

```go
java JavaAggregate
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBCollection;
04 import com.mongodb.BasicDBObject;
05 import com.mongodb.DBObject;
06 import com.mongodb.DBCursor;
07 import com.mongodb.AggregationOutput;
08 import java.util.Iterator;
09 public class JavaAggregate {
10    public static void main(String[] args) {
11       try {
12          MongoClient mongoClient = new MongoClient("localhost", 27017);
13          DB db = mongoClient.getDB("words");
14          DBCollection collection = db.getCollection("word_stats");
15          JavaAggregate.largeSmallVowels(collection);
16          JavaAggregate.top5AverageWordFirst(collection);
17       } catch (Exception e) {
18          System.out.println(e);
19       }
20    }
21    public static void displayAggregate(AggregationOutput result){
22       for (Iterator<DBObject> items = result.results().iterator();
23             items.hasNext();){
24          System.out.println(items.next());
25       }
26    }
27    public static void largeSmallVowels(DBCollection collection){
28       BasicDBObject match = new BasicDBObject("$match",
29            new BasicDBObject("first",
30                 new BasicDBObject ("$in",
31                      new String[]{"a","e","i","o","u"})));
32       BasicDBObject groupOps = new BasicDBObject("_id", "$first");
33       groupOps.append("largest", new BasicDBObject("$max", "$size"));
34       groupOps.append("smallest", new BasicDBObject("$min", "$size"));
35       groupOps.append("total", new BasicDBObject("$sum", 1));
36       BasicDBObject group = new BasicDBObject("$group", groupOps);
37       BasicDBObject sort = new BasicDBObject("$sort",
38            new BasicDBObject("first", 1));
39       AggregationOutput result =
40            collection.aggregate(match, group, sort);
41       System.out.println("\nLargest and smallest word sizes for " +
42                              "words beginnig with a vowel: ");
43       JavaAggregate.displayAggregate(result);
44    }
45    public static void top5AverageWordFirst(DBCollection collection){
46       BasicDBObject groupOps = new BasicDBObject("_id", "$first");
47       groupOps.append("average", new BasicDBObject("$avg", "$size"));
48       BasicDBObject group = new BasicDBObject("$group", groupOps);
49       BasicDBObject sort = new BasicDBObject("$sort",
50            new BasicDBObject("average", -1));
51       BasicDBObject limit = new BasicDBObject("$limit", 5);
52       AggregationOutput result =
53            collection.aggregate(group, sort, limit);
54       System.out.println("\nFirst letter of top 5 largest average " +
55                              "word size: ");
56       JavaAggregate.displayAggregate(result);
57    }
58 }
```

```go
Largest and smallest word sizes for words beginnig with a vowel:
{ "_id" : "e" , "largest" : 13.0 , "smallest" : 3.0 , "total" : 150}
{ "_id" : "u" , "largest" : 13.0 , "smallest" : 2.0 , "total" : 33}
{ "_id" : "i" , "largest" : 14.0 , "smallest" : 1.0 , "total" : 114}
{ "_id" : "o" , "largest" : 12.0 , "smallest" : 2.0 , "total" : 72}
{ "_id" : "a" , "largest" : 14.0 , "smallest" : 1.0 , "total" : 192}
First letter of top 5 largest average word size:
{ "_id" : "i" , "average" : 7.947368421052632}
{ "_id" : "e" , "average" : 7.42}
{ "_id" : "c" , "average" : 7.292134831460674}
{ "_id" : "p" , "average" : 6.881818181818182}
{ "_id" : "r" , "average" : 6.767123287671233}
```

