### 10.4　使用Java对结果集排序

> **使用sort()以特定顺序返回Java对象DBCursor表示的文档**
> 在本节中，您将编写一个简单的Java应用程序，它使用查询对象和方法find()从示例数据库检索特定的文档集，再使用方法sort()将游标中的文档按特定顺序排列。通过这个示例，您将熟悉如何在检索并处理文档前对游标表示的文档进行排序。程序清单10.9显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，再调用其他的方法来查找特定的文档，对找到的文档进行排序并显示结果。方法displayCursor()显示排序后的单词列表。
> 方法sortWordsAscending()获取以w打头的单词并将它们按升序排列；方法sortWordsDesc()获取以w打头的单词并将它们按降序排列；方法sortWordsAscAndSize()获取以q打头的单词，并将它们首先按最后一个字母升序排列，再按长度降序排列。
> 执行下面的步骤，创建并运行这个Java应用程序，它在示例数据集中查找特定的文档，对找到的文档进行排序并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour10中新建一个文件，并将其命名为JavaFindSort.java。
> 4．在这个文件中输入程序清单10.9所示的代码。这些代码对DBCursor对象表示的文档进行排序。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour10。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单10.10显示了这个应用程序的输出。
> **程序清单10.9　JavaFindSort.java：在Java应用程序中查找集合中的特定文档并进行排序**
> **程序清单10.10　JavaFindSort.java-output：在Java应用程序中查找集合中的特定文档并进行排序的输出**
> ▲

从MongoDB数据库检索文档时，一个重要方面是对文档进行排序。只想检索特定数量（如前10个）的文档或要对结果集进行分页时，这特别有帮助。排序选项让您能够指定用于排序的文档字段和方向。

DBCursor对象的方法sort()让您能够指定要根据哪些字段对游标中的文档进行排序，并按相应的顺序返回文档。方法sort()将一个BasicDBObject作为参数，这个对象将字段名用作属性名，并使用值1（升序）和-1（降序）来指定排序顺序。

例如，要按字段name升序排列文档，可使用下面的代码：

```go
BasicDBObject sorter = new BasicDBObject("name", 1);
myCollection.find().sort(sorter);
```

在传递给方法sort()的对象中，可指定多个字段，这样文档将按这些字段排序。还可对同一个游标调用sort()方法多次，从而依次按不同的字段进行排序。例如，要首先按字段name升序排列，再按字段value降序排列，可使用下面的代码：

```go
BasicDBObject sorter = new BasicDBObject("name", 1);
sorter.append("value", -1);
myCollection.find().sort(sorter);
```

也可使用下面的代码：

```go
BasicDBObject sorter1 = new BasicDBObject("name", 1);
BasicDBObject sorter2 = new BasicDBObject("value", -1);
myCollection.find().sort(sorter1).sort(sorter2);
```

▼　Try It Yourself

```go
javac JavaFindSort.java
```

```go
java JavaFindSort
```

```go
01 import com.mongodb.DBCursor;
02 import com.mongodb.DBObject;
03 import com.mongodb.MongoClient;
04 import com.mongodb.DB;
05 import com.mongodb.DBCollection;
06 import com.mongodb.BasicDBObject;
07 public class JavaFindSort {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaFindSort.sortWordsAscending(collection);
14          JavaFindSort.sortWordsDesc(collection);
15          JavaFindSort.sortWordsAscAndSize(collection);
16       } catch (Exception e){
17          System.out.println(e);
18       }
19    }
20    public static void displayCursor(DBCursor cursor){
21       String words = "";
22       while(cursor.hasNext()){
23          DBObject doc = cursor.next();
24          words = words.concat(doc.get("word").toString()).concat(",");
25       }
26       if(words.length() > 65){
27          words = words.substring(0, 65) + "...";
28       }
29       System.out.println(words);
30    }
31    public static void sortWordsAscending(DBCollection collection) {
32       BasicDBObject query = new BasicDBObject("first", "w");
33       DBCursor cursor = collection.find(query);
34       BasicDBObject sorter = new BasicDBObject("word", 1);
35       cursor.sort(sorter);
36       System.out.println("\nW words ordered ascending: ");
37       JavaFindSort.displayCursor(cursor);
38    }
39    public static void sortWordsDesc(DBCollection collection) {
40       BasicDBObject query = new BasicDBObject("first", "w");
41       DBCursor cursor = collection.find(query);
42       BasicDBObject sorter = new BasicDBObject("word", -1);
43       cursor.sort(sorter);
44       System.out.println("\nW words ordered descending: ");
45       JavaFindSort.displayCursor(cursor);
46    }
47    public static void sortWordsAscAndSize(DBCollection collection) {
48       BasicDBObject query = new BasicDBObject("first", "q");
49       DBCursor cursor = collection.find(query);
50       BasicDBObject sorter = new BasicDBObject("last", 1);
51       sorter.append("size", -1);
52       cursor.sort(sorter);
53       System.out.println("\nQ words ordered first by last letter " +
54                              "and then by size: ");
55       JavaFindSort.displayCursor(cursor);
56    }
57 }
```

```go
W words ordered ascending:
wage,wait,wake,walk,wall,want,war,warm,warn,warning,wash,waste,wa...
W words ordered descending:
wrong,writing,writer,write,wrap,would,worth,worry,world,works,wor...
Q words ordered first by last letter and then by size:
quite,quote,quick,question,quarter,quiet,quit,quickly,quality,qui...
```

