### 11.1.1　使用Java限制结果集的大小

> **使用limit ()将Java对象DBCursor表示的文档减少到指定的数量**
> 在本节中，您将编写一个简单的Java应用程序，它使用limit()来限制find()操作返回的结果。通过这个示例，您将熟悉如何结合使用limit()和find()，并了解limit()对结果的影响。程序清单11.1显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他方法来查找并显示数量有限的文档。方法displayCursor()迭代游标并显示找到的单词。
> 方法limitResults()接受一个limit参数，查找以p打头的单词，并返回参数limit指定的单词数。
> 请执行如下步骤，创建并运行这个Java应用程序，它在示例数据集中查找指定数量的文档并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaFindLimit.java。
> 4．在这个文件中输入程序清单11.1所示的代码。这些代码使用了方法find()和limit()。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.2显示了这个应用程序的输出。
> **程序清单11.1　JavaFindLimit.java：在Java应用程序中从集合中查找指定数量的文档**
> **程序清单11.2　JavaFindLimit.java-output：在Java应用程序中从集合中查找指定数量文档的输出**
> ▲

要限制find()或其他查询请求返回的数据量，最简单的方法是对find()操作返回的DBCursor对象调用方法limit()，它让DBCursor对象返回指定数量的文档，可避免检索的对象量超过应用程序的处理能力。

例如，下面的代码只显示集合中的前10个文档，即便匹配的文档有数千个：

```go
DBCursor cursor = wordsColl.find();
cursor.limit(10);
while(cursor.hasNext()){
   DBObject word = cursor.next();
   System.out.println(word);
}
```

▼　Try It Yourself

```go
javac JavaFindLimit.java
```

```go
java JavaFindLimit
```

```go
01 import com.mongodb.DBCursor;
02 import com.mongodb.DBObject;
03 import com.mongodb.MongoClient;
04 import com.mongodb.DB;
05 import com.mongodb.DBCollection;
06 import com.mongodb.BasicDBObject;
07 public class JavaFindLimit {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaFindLimit.limitResults(collection, 1);
14          JavaFindLimit.limitResults(collection, 3);
15          JavaFindLimit.limitResults(collection, 5);
16          JavaFindLimit.limitResults(collection, 7);
17       } catch (Exception e){
18          System.out.println(e);
19       }
20    }
21    public static void displayCursor(DBCursor cursor){
22       String words = "";
23       while(cursor.hasNext()){
24          DBObject doc = cursor.next();
25          words = words.concat(doc.get("word").toString()).concat(",");
26       }
27       if(words.length() > 65){
28          words = words.substring(0, 65) + "...";
29       }
30       System.out.println(words);
31    }
32    public static void limitResults(DBCollection collection,
33                                           Integer limit) {
34       BasicDBObject query = new BasicDBObject("first", "p");
35       DBCursor cursor = collection.find(query);
36       cursor.limit(limit);
37       System.out.println("\nP words Limited to " +
38                              limit.toString() + " :");
39       JavaFindLimit.displayCursor(cursor);
40    }
41 }
```

```go
P words Limited to 1 :
people,
P words Limited to 3 :
people,put,problem,
P words Limited to 5 :
people,put,problem,part,place,
P words Limited to 7 :
people,put,problem,part,place,program,play,
```

