### 11.3　在Java应用程序中对查找操作结果进行分组

> **使用Java根据键值将文档分组**
> 在本节中，您将创建一个简单的Java应用程序，它使用DBCollection对象的方法group()从示例数据库检索文档，根据指定字段进行分组，并在服务器上执行reduce和finalize函数。通过这个示例，您将熟悉如何使用group()在服务器端对数据集进行处理，以生成分组数据。程序清单11.9显示了这个示例的代码。
> 在这个示例中，方法main()连接到MongoDB数据库，获取一个DBCollection对象，并调用其他的方法来查找文档、进行分组并显示结果。方法displayGroup()显示分组结果。
> 方法firstIsALastIsVowel()将第一个字母为a且最后一个字母为元音字母的单词分组，其中的reduce函数计算单词数，以确定每组的单词数。
> 方法firstLetterTotals()根据第一个字母分组，并计算各组中所有单词的元音字母总数和辅音字母总数。在其中的finalize函数中，将元音字母总数和辅音字母总数相加，以提供各组单词的字符总数。
> 请执行下面的步骤，创建并运行这个Java应用程序，它对示例数据集中的文档进行分组和处理，并显示结果。
> 1．确保启动了MongoDB服务器。
> 2．确保下载并安装了Java MongoDB驱动程序，并运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour11中新建一个文件，并将其命名为JavaGroup.java。
> 4．在这个文件中输入程序清单11.9所示的代码。这些代码对文档集执行group()操作。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour11。
> 7．执行下面的命令来编译这个新建的Java文件：
> 8．执行下面的命令来运行这个Java应用程序。程序清单11.10显示了这个应用程序的输出。
> **程序清单11.9　JavaGroup.java：在Java应用程序中根据字段值对单词分组以生成不同的数据**
> **程序清单11.10　JavaGroup.java-output：在Java应用程序中根据字段值对单词分组以生成不同数据的输出**
> ▲

在Java中对大型数据集执行操作时，根据文档的一个或多个字段的值将结果分组通常很有用。这也可以在取回文档后使用代码来完成，但让MongoDB服务器在原本就要迭代文档的请求中这样做，效率要高得多。

在Java中，要将查询结果分组，可使用DBCollection对象的方法group()。分组请求首先收集所有与查询匹配的文档，再对于指定键的每个不同值，都在数组中添加一个分组对象，对这些分组对象执行操作，并返回这个分组对象数组。

方法group()的语法如下：

```go
group({key, cond , initial, reduce, [finalize]})
```

其中参数key、cond和initial都是BasicDBObject对象，指定了要用来分组的字段、查询以及要使用的初始文档；参数reduce和finalize为String对象，包含以字符串方式表示的JavaScript函数，这些函数将在服务器上运行以归并文档并生成最终结果。有关这些参数的更详细信息，请参阅第9章。

为演示这个方法，下面的代码实现了简单分组，它创建了对象key、cond和initial，并以字符串的方式传入了一个reduce函数：

```go
BasicDBObject key = new BasicDBObject("first", true);
BasicDBObject cond = new BasicDBObject("last", "a");
cond.append("size", 5);
BasicDBObject initial = new BasicDBObject("count", 0);
String reduce = "function (obj, prev) { prev.count++; }";
DBObject result = collection.group(key, cond, initial, reduce);
```

方法group()以DBObject对象的方式返回分组结果。下面的代码逐项地显示了分组结果的内容：

```go
for (Object name: group.toMap().values()) {
   System.out.println(name);
}
```

▼　Try It Yourself

```go
javac JavaGroup.java
```

```go
java JavaGroup
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBCollection;
04 import com.mongodb.BasicDBObject;
05 import com.mongodb.DBObject;
06 import com.mongodb.DBCursor;
07 public class JavaGroup {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("words");
12          DBCollection collection = db.getCollection("word_stats");
13          JavaGroup.firstIsALastIsVowel(collection);
14          JavaGroup.firstLetterTotals(collection);
15       } catch (Exception e) {
16          System.out.println(e);
17       }
18    }
19    public static void displayGroup(DBObject result){
20       for (Object name: result.toMap().values()) {
21          System.out.println(name);
22       }
23    }
24    public static void firstIsALastIsVowel(DBCollection collection){
25       BasicDBObject key = new BasicDBObject("first", true);
26       key.append("last", true);
27       BasicDBObject cond = new BasicDBObject("first", "a");
28       cond.append("last",
29            new BasicDBObject("$in",
30            new String[]{"a","e","i","o","u"}));
31       BasicDBObject initial = new BasicDBObject("count", 0);
32       String reduce = "function (obj, prev) { prev.count++; }";
33       DBObject result = collection.group(key, cond, initial, reduce);
34       System.out.println("\n'A' words grouped by first and last" +
35                              " letter that end with a vowel");
36       JavaGroup.displayGroup(result);
37    }
38    public static void firstLetterTotals(DBCollection collection){
39       BasicDBObject key = new BasicDBObject("first", true);
40       BasicDBObject cond = new BasicDBObject();
41       BasicDBObject initial = new BasicDBObject("vowels", 0);
42       initial.append("cons", 0);
43       String reduce = "function (obj, prev) { " +
44                               "prev.vowels += obj.stats.vowels; " +
45                               "prev.cons += obj.stats.consonants; " +
46                               "}";
47       String finalize = "function (obj) { " +
48                             "obj.total = obj.vowels + obj.cons; " +
49                             "}";
50       DBObject result = collection.group(key, cond, initial,
51                                                  reduce, finalize);
52       System.out.println("\nWords grouped by first letter " +
53                              "with totals: ");
54       JavaGroup.displayGroup(result);
55    }
56 }
```

```go
'A' words grouped by first and last letter that end with a vowel
{ "first" : "a" , "last" : "e" , "count" : 52.0}
{ "first" : "a" , "last" : "o" , "count" : 2.0}
{ "first" : "a" , "last" : "a" , "count" : 3.0}
Words grouped by first letter with totals:
{ "first" : "l" , "vowels" : 189.0 , "cons" : 299.0 , "total" : 488.0}
{ "first" : "p" , "vowels" : 550.0 , "cons" : 964.0 , "total" : 1514.0}
{ "first" : "j" , "vowels" : 47.0 , "cons" : 73.0 , "total" : 120.0}
{ "first" : "k" , "vowels" : 22.0 , "cons" : 48.0 , "total" : 70.0}
{ "first" : "u" , "vowels" : 93.0 , "cons" : 117.0 , "total" : 210.0}
{ "first" : "g" , "vowels" : 134.0 , "cons" : 240.0 , "total" : 374.0}
{ "first" : "m" , "vowels" : 262.0 , "cons" : 417.0 , "total" : 679.0}
{ "first" : "s" , "vowels" : 640.0 , "cons" : 1215.0 , "total" : 1855.0}
{ "first" : "n" , "vowels" : 136.0 , "cons" : 208.0 , "total" : 344.0}
{ "first" : "e" , "vowels" : 482.0 , "cons" : 630.0 , "total" : 1112.0}
{ "first" : "v" , "vowels" : 117.0 , "cons" : 143.0 , "total" : 260.0}
{ "first" : "r" , "vowels" : 414.0 , "cons" : 574.0 , "total" : 988.0}
{ "first" : "q" , "vowels" : 28.0 , "cons" : 32.0 , "total" : 60.0}
{ "first" : "z" , "vowels" : 2.0 , "cons" : 2.0 , "total" : 4.0}
{ "first" : "o" , "vowels" : 204.0 , "cons" : 237.0 , "total" : 441.0}
{ "first" : "a" , "vowels" : 545.0 , "cons" : 725.0 , "total" : 1270.0}
{ "first" : "c" , "vowels" : 713.0 , "cons" : 1233.0 , "total" : 1946.0}
{ "first" : "b" , "vowels" : 246.0 , "cons" : 444.0 , "total" : 690.0}
{ "first" : "t" , "vowels" : 333.0 , "cons" : 614.0 , "total" : 947.0}
{ "first" : "y" , "vowels" : 26.0 , "cons" : 41.0 , "total" : 67.0}
{ "first" : "f" , "vowels" : 258.0 , "cons" : 443.0 , "total" : 701.0}
{ "first" : "h" , "vowels" : 145.0 , "cons" : 248.0 , "total" : 393.0}
{ "first" : "i" , "vowels" : 384.0 , "cons" : 522.0 , "total" : 906.0}
{ "first" : "d" , "vowels" : 362.0 , "cons" : 585.0 , "total" : 947.0}
{ "first" : "w" , "vowels" : 161.0 , "cons" : 313.0 , "total" : 474.0}
```

