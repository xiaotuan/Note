### 24.3.5　使用Java从MongoDB GridFS中删除文件

> **使用Java访问和操作MongoDB GridFS存储区中的文件**
> 本节将引导您完成在Java应用程序中实现MongoDB GridFS存储的流程，包括访问MongoDB GridFS以及列出、添加、获取和删除文件的步骤。
> 在这个示例中，方法main()连接到MongoDB数据库，并调用各种方法来访问GridFS以列出、添加、获取和删除文件。
> 方法listGridFSFiles()用于在Java应用程序运行期间的各个时点显示MongoDB GridFS中当前存储的文件；方法putGridFSFile()将一个文件存储到GridFS中；方法getGridFSFile()从GridFS获取一个文件并显示其内容；方法deleteGridFSFile()从GridFS中删除文件。
> 请执行如下步骤，使用Java列出、获取、添加和删除文件。
> 1．确保启动了MongoDB服务器。
> 2．确保安装并配置了Java MongoDB驱动程序。
> 3．在文件夹code/hour24中新建一个文件，并将其命名为JavaGridFS.java。
> 4．在这个文件中输入程序清单24.1所示的代码。这些代码访问MongoDB GridFS。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour24。
> 7．执行下面的命令编译这个新的Java文件：
> 8．执行下面的命令运行这个Java应用程序。程序清单24.2显示了这个Java应用程序的输出。
> **程序清单24.1　JavaGridFS.java：使用Java列出、添加、获取和删除MongoDB GridFS中的文件**
> **程序清单24.2　JavaGridFS.py-output：使用Java列出、添加、获取和删除MongoDB GridFS中文件的输出**
> ▲

在Java中，要将文件从GridFS存储区中删除，最简单的方式是使用GridFS对象的方法remove()。这个方法将文件从MongoDB GridFS存储区中删除，其语法如下：

```go
remove(DBObject query)
remove(ObjectId, id)
remove(String filename)
```

例如，用下面的语句删除文件test.txt：

```go
GridFS myFS = new GridFS(db);
myFS.remove("test.txt");
```

▼　Try It Yourself

```go
javac JavaGridFS.java
```

```go
java JavaGridFS
```

```go
01 import com.mongodb.MongoClient;
02 import com.mongodb.DB;
03 import com.mongodb.DBObject;
04 import com.mongodb.DBCursor;
05 import com.mongodb.gridfs.*;
06 import java.io.*;
07 public class JavaGridFS {
08    public static void main(String[] args) {
09       try {
10          MongoClient mongoClient = new MongoClient("localhost", 27017);
11          DB db = mongoClient.getDB("myFS");
12          System.out.println("\nFiles Before Put:");
13          JavaGridFS.listGridFSFiles(db);
14          JavaGridFS.putGridFSFile(db);
15          System.out.println("\nFiles After Put:");
16          JavaGridFS.listGridFSFiles(db);
17          System.out.println("\nContents of Retrieve File:");
18          JavaGridFS.getGridFSFile(db);
19          JavaGridFS.deleteGridFSFile(db);
20          System.out.println("\nFiles After Delete:");
21          JavaGridFS.listGridFSFiles(db);
22       } catch (Exception e) { System.out.println(e); }
23    }
24    public static void listGridFSFiles(DB db){
25          GridFS myFS = new GridFS(db);
26          DBCursor files = myFS.getFileList();
27          for(final DBObject file : files) {
28              System.out.println(file);
29       }
30    }
31    public static void putGridFSFile(DB db){
32       try{
33          File newFile = new File("java.txt");
34          BufferedWriter output =
35               new BufferedWriter(new FileWriter(newFile));
36          output.write("Stored From Java");
37          output.close();
38          newFile = new File("java.txt");
39          GridFS myFS = new GridFS(db);
40          GridFSInputFile gridFile = myFS.createFile(newFile);
41          gridFile.save();
42       } catch (Exception e) { System.out.println(e); }
43    }
44    public static void getGridFSFile(DB db){
45       try{
46          GridFS myFS = new GridFS(db);
47          GridFSDBFile file = myFS.findOne("java.txt");
48          file.writeTo(new File("JavaRetrieved.txt"));
49          File inFile = new File("JavaRetrieved.txt");
50          BufferedReader input =
51               new BufferedReader(new FileReader(inFile));
52          System.out.println(input.readLine());
53          input.close();
54       } catch (Exception e) { System.out.println(e); }
55    }
56    public static void deleteGridFSFile(DB db){
57       GridFS myFS = new GridFS(db);
58       myFS.remove("java.txt");
59    }
60 }
```

```go
Files Before Put:
Files After Put:
{ "_id" : { "$oid" : "52f43076ba4141ceac68f0f6"} , "chunkSize" : 262144 ,
  "length" : 16 , "md5" : "5186b45e4f6a4b8ddd8ff3579148765d" , "filename" : "java. txt" ,
  "contentType" : null , "uploadDate" : { "$date" : "2014-02-07T01:01:42.586Z"} ,
  "aliases" : null }
Contents of Retrieve File:
Stored From Java
Files After Delete:
```

