### 11.1.3　使用Java将结果集分页

> **在Java中使用skip()和limit()对MongoDB集合中的文档进行分页**
> 在本节中，您将编写一个简单的Java应用程序，它使用DBCursor对象的方法skip()和limit()方法对find()返回的大量文档进行分页。通过这个示例，您将熟悉如何使用skip()和limit()对较大的数据集进行分页。程序清单11.5显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来查找文档并以分页方式显示它们。方法displayCursor()迭代游标并显示当前页中的单词。
> 方法pageResults()接受一个skip参数，并根据它以分页方式显示以w开头的所有单词。每显示一页后，都将skip值递增，直到到达游标末尾。
> 请执行下面的步骤，创建并运行这个对示例数据集中的文档进行分页并显示结果的Java应用程序。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaFindPaging.java。
> 4．在这个文件中输入程序清单11.5所示的代码。这些代码实现了文档集分页。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.6显示了这个应用程序的输出。
> **程序清单11.5　JavaFindPaging.java：在Java应用程序中分页显示集合中的文档集**
> **程序清单11.6　JavaFindPaging.java-output：在Java应用程序中分页显示集合中的文档集的输出**
> ▲

为减少返回的文档数，一种常见的方法是进行分页。要进行分页，需要指定要在结果集中跳过的文档数，还需限制返回的文档数。跳过的文档数将不断增加，每次的增量都是前一次返回的文档数。

要对一组文档进行分页，需要使用DBCursor对象的方法limit()和skip()。方法skip()让您能够指定在返回文档前要跳过多少个文档。

每次获取下一组文档时，都增大方法skip()中指定的值，增量为前一次调用limit()时指定的值，这样就实现了数据集分页。

例如，下面的语句查找第11～20个文档：

```go
DBCursor cursor = collection.find();
cursor.limit(10);
cursor.skip(10);
```

进行分页时，务必调用方法sort()来确保文档的排列顺序不变。

▼　Try It Yourself

```go
javac JavaFindPaging.java
```

```go
java JavaFindPaging
```

```go
01 import com.mongodb.DBCursor;
02 import com.mongodb.DBObject;
03 import com.mongodb.MongoClient;
04 import com.mongodb.DB;
05 import com.mongodb.DBCollection;
06 import com.mongodb.BasicDBObject;
07 public class JavaFindPaging {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaFindPaging.pageResults(collection, 0);
14       } catch (Exception e){
15          System.out.println(e);
16       }
17    }
18    public static void displayCursor(DBCursor cursor){
19       String words = "";
20       while(cursor.hasNext()){
21          DBObject doc = cursor.next();
22          words = words.concat(doc.get("word").toString()).concat(",");
23       }
24       if(words.length() > 65){
25          words = words.substring(0, 65) + "...";
26       }
27       System.out.println(words);
28    }
29    public static void pageResults(DBCollection collection,
30                                         Integer skip) {
31       BasicDBObject query = new BasicDBObject("first", "w");
32       DBCursor cursor = collection.find(query);
33       cursor.sort(new BasicDBObject("word", 1));
34       cursor.limit(10);
35       cursor.skip(skip);
36       System.out.println("Page " + new Integer(skip+1).toString() +
37                              " to " +
38                              new Integer(skip+cursor.size()).toString() +
39                              ":");
40       JavaFindPaging.displayCursor(cursor);
41       if (cursor.size() == 10){
42          JavaFindPaging.pageResults(collection, skip+10);
43       }
44    }
45 }
```

```go
Page 1 to 10:
wage,wait,wake,walk,wall,want,war,warm,warn,warning,
Page 11 to 20:
wash,waste,watch,water,wave,way,we,weak,wealth,wealthy,
Page 21 to 30:
weapon,wear,weather,wedding,week,weekend,weigh,weight,welcome,wel...
Page 31 to 40:
well,west,western,wet,what,whatever,wheel,when,whenever,where,
Page 41 to 50:
whereas,whether,which,while,whisper,white,who,whole,whom,whose,
Page 51 to 60:
why,wide,widely,wife,wild,will,willing,win,wind,window,
Page 61 to 70:
wine,wing,winner,winter,wipe,wire,wisdom,wish,with,withdraw,
Page 71 to 80:
within,without,witness,woman,won't,wonder,wonderful,wood,wooden,w...
Page 81 to 90:
work,worker,working,works,world,worry,worth,would,wrap,write,
Page 91 to 93:
writer,writing,wrong,
```

