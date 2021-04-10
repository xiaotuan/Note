### 9.3.1　理解方法mapReduce()

> **在MongoDB shell中使用映射-归并来操作结果**
> 在本节中，您将编写一个简单的MongoDB shell脚本，使用映射-归并来操作从MongoDB示例数据集返回的数据。通过这个示例，您将熟悉如何使用Collection对象的方法mapReduce()。程序清单9.5显示了这个示例的代码。
> 第4～13行演示了方法mapReduce()的基本用法，显示了以各个字母打头的单词包含的元音字母总数。
> 第14～42行是一个更复杂的示例，其中的map函数返回的数组元素为对象，而reduce函数根据这些对象计算元音字母总数和辅音字母总数。这个示例还包含finalize函数，用于添加一个包含字符总数的字段。另外，还使用了选项query来限制数据集，使其只包含以元音字母结尾的单词。
> 请执行如下步骤，编写并运行这个对示例数据集中的文档执行映射-归并操作并显示结果的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour09中新建一个文件，并将其命名为doc_map_reduce.js。
> 4．在这个文件中输入程序清单程序清单9.5所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用mapReduce()对单词集进行映射-归并。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour09。
> 7．执行下面的命令以运行这个脚本，它对集合word_stats中的单词进行映射-归并并显示结果。程序清单9.6显示了这个脚本的输出。
> **程序清单9.5　doc_map_reduce.js：使用MongoDB shell映射-归并集合中的文档**
> **程序清单9.6　doc_map_reduce.js-output：使用MongoDB shell映射-归并集合中文档的输出**
> ▲

Collection对象提供了方法mapReduce()，可用于对数据执行映射-归并操作，再将结果返回给客户端。方法mapReduce()的语法如下：

```go
mapReduce(map, reduce, arguments)
```

参数map是一个函数，将对数据集中的每个对象执行它来生成一个键和值，这些值被加入到与键相关联的数组中，供归并阶段使用。map函数的格式如下：

```go
function(){
   <do stuff to calculate key and value>
   emit(key, value);
}
```

参数reduce是一个函数，将对map函数生成的每个对象执行它。reduce函数必须将键作为第一个参数，将与键相关联的值数组作为第二个参数，并使用值数组来计算得到与键相关联的单个值，再返回结果。reduce函数的格式如下：

```go
function(key, values){
   <do stuff to on values to calculate a single result>
   return result;
}
```

方法mapReduce()的参数arguments是一个对象，指定了检索传递给map函数的文档时使用的选项。表9.4列出了可在参数arguments中指定的选项。

在下面的映射-归并示例中，指定了选项out和query：

```go
results = myCollection.mapReduce(
   function() { emit(this.key, this.value); },
   function(key, values){ return Array.sum(values); },
   {
      out: {inline: 1},
      query: {value: {$gt: 6}
   }
);
```

<center class="my_markdown"><b class="my_markdown">表9.4　　在方法mapReduce()的参数arguments中可设置的选项</b></center>

| 选项 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| out | 这是唯一一个必不可少的选项，它指定将映射-归并操作结果输出到什么地方，可能取值如下。 | ●  **内嵌：** 在内存中执行操作，并在对客户端的响应中返回归并对象，如out: {inline:1} | ●  **输出到集合：** 指定将结果插入到一个集合中，如果指定的集合不存在，就创建它，如out: outputCollection | ●  **输出到集合并指定要采取的措施：** 指定要将结果输出到哪个数据库的哪个集合，并指定措施replace、merge或reduce，如out: {replace: outputCollection} |
| Query | 指定查询运算符，用于限制将传递给map函数的文档 |
| sort | 指定排序字段，用于在将文档传递给map函数前对其进行排序。指定的排序字段必须包含在集合的既有索引中 |
| limit | 指定最多从集合中返回多少个文档 |
| finalize | 在reduce函数执行完毕后执行，finalize函数必须将键和文档作为参数，并返回修改后的文档，如： | `finalize: function(key, document){` | `<do stuff to modify document>` | `return document;` | `}` |
| scope | 指定可在map、reduce和finalize函数中访问的全局变量 |
| jsMode | 布尔值，为true时，不将从map函数返回的表示中间数据集的JavaScript对象转换为BSON。默认为false |
| verbose | 布尔值，为true时，发送给客户端的结果中将包含时间（timing）信息。默认为true |



▼　Try It Yourself

```go
mongo doc_map_reduce.js
```

```go
01 mongo = new Mongo('localhost');
02 wordsDB = mongo.getDB('words');
03 wordsColl = wordsDB.getCollection('word_stats');
04 results = wordsColl.mapReduce(
05    function() { emit(this.first, this.stats.vowels); },
06    function(key, values){ return Array.sum(values); },
07    { out: {inline: 1}}
08 );
09 print("Total vowel count in words beginning with " +
10        "a certain letter: ");
11 for(i in results.results){
12    print(JSON.stringify(results.results[i]));
13 }
14 results = wordsColl.mapReduce(
15       function() { emit(this.first,
16                            { vowels: this.stats.vowels,
17                              consonants: this.stats.consonants})
18       },
19       function(key, values){
20          result = {count: values.length,
21                      vowels: 0, consonants: 0};
22          for(var i=0; i<values.length; i++){
23             if (values[i].vowels)
24                result.vowels += values[i].vowels;
25             if(values[i].consonants)
26                result.consonants += values[i].consonants;
27          }
28          return result;
29       },
30       { out: {inline: 1},
31         query: {last: {$in:['a','e','i','o','u']}},
32         finalize: function (key, obj) {
33                        obj.characters = obj.vowels + obj.consonants;
34                        return obj;
35                     }
36       }
37    );
38    print("Total words, vowels, consonants and characters in words " +
39           "beginning with a certain letter that ends with a vowel: ");
40    for(i in results.results){
41       print(JSON.stringify(results.results[i]));
42    }
```

```go
Total vowel count in words beginning with a certain letter:
{"_id":"a","value":545}
{"_id":"b","value":246}
{"_id":"c","value":713}
{"_id":"d","value":362}
{"_id":"e","value":482}
{"_id":"f","value":258}
{"_id":"g","value":134}
{"_id":"h","value":145}
{"_id":"i","value":384}
{"_id":"j","value":47}
{"_id":"k","value":22}
{"_id":"l","value":189}
{"_id":"m","value":262}
{"_id":"n","value":136}
{"_id":"o","value":204}
...
Total words, vowels, consonants and characters in words beginning with a certain
letter that ends with a vowel:
{"_id":"a","value":{"count":4,"vowels":192,"consonants":197,"characters": 389}}
{"_id":"b","value":{"count":2,"vowels":44,"consonants":52,"characters":96}}
{"_id":"c","value":{"count":6,"vowels":216,"consonants":283,"characters":  
499}}
{"_id":"d","value":{"count":7,"vowels":117,"consonants":139,"characters":  
256}}
{"_id":"e","value":{"count":5,"vowels":156,"consonants":167,"characters":  
323}}
{"_id":"f","value":{"count":6,"vowels":62,"consonants":66,"characters":  
128}}
{"_id":"g","value":{"count":3,"vowels":32,"consonants":34,"characters":66}}
{"_id":"h","value":{"count":6,"vowels":31,"consonants":34,"characters":65}}
{"_id":"i","value":{"count":2,"vowels":127,"consonants":136,"characters":  
263}}
{"_id":"j","value":{"count":5,"vowels":14,"consonants":15,"characters":  
29}}
{"_id":"k","value":{"count":3,"vowels":7,"consonants":11,"characters":18}}
{"_id":"l","value":{"count":4,"vowels":54,"consonants":56,"characters":110}}
{"_id":"m","value":{"count":3,"vowels":74,"consonants":85,"characters":159}}
{"_id":"n","value":{"count":2,"vowels":39,"consonants":39,"characters":78}}
...
```

