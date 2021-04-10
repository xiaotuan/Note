### 9.1　在MongoDB shell中对查找操作的结果进行分组

> **使用MongoDB shell根据键值将文档分组**
> 在本节中，您将编写一个简单的MongoDB shell脚本，它根据键值对从示例数据集中查询得到的文档进行分组。通过这个示例，您将熟悉如何使用Collection对象的方法group()。程序清单9.1显示了这个示例的代码。
> 首先，这个示例根据第一个字母和最后一个字母对以a打头的单词进行分组，并返回各组的单词数。注意到使用了属性initial将单词数初始化为0，并在reduce函数中将单词数递增。
> 接下来，这个示例根据第一个字母对超过13个字符的单词进行分组，并返回各组的单词数以及各组单词包含的元音字母总数。reduce函数访问每个文档的stats.vowels值，并将其加入到计数器totalVowels中。
> 最后，这个示例根据第一个字母对单词进行分组，计算每组的单词数、元音字母总数和辅音字母总数，再使用finalize函数将每组的obj.vowels和obj.consonants相加，并将结果作为方法group()返回的数组中对象的total字段。
> 请执行如下步骤，编写并运行这个将示例数据集中的文档分组并显示结果的MongoDB shell脚本。
> 1．确保启动了MongoDB服务器。
> 2．确保运行了生成数据库words的脚本文件code/hour05/generate_words.js。
> 3．在文件夹code/hour09中新建一个文件，并将其命名为doc_group.js。
> 4．在这个文件中输入程序清单程序清单9.1所示的代码。这些代码连接到数据库words，获取表示集合word_stats的Collection对象，并使用group()来将单词分组。
> 5．将这个文件存盘。
> 6．打开一个控制台窗口，并切换到目录code/hour09。
> 7．执行下面的命令以运行这个脚本，它将集合word_stats中的单词分组并显示结果。程序清单9.2显示了这个脚本的输出。
> **程序清单9.1　doc_group.js：使用MongoDB shell将集合中的文档分组**
> **程序清单9.2　doc_group.js-output：使用MongoDB shell将集合中的文档分组进行输出**
> ▲

对大型数据集执行操作时，根据文档的一个或多个字段的值将结果分组通常很有用。这也可以在取回文档后使用代码来完成，但让MongoDB服务器在原本就要迭代文档的请求中这样做，效率要高得多。

要将查询结果分组，可使用Collection对象的方法group()。分组请求首先收集所有与查询匹配的文档，再对于指定键的每个不同值，都在数组中添加一个分组对象，对这些分组对象执行操作，并返回这个分组对象数组。方法group()的语法如下：

```go
group({key, reduce, initial, [keyf], [cond], finalize})
```

下面描述了方法group()的参数。

+ keys：一个指定要根据哪些键进行分组的对象，其属性为要用于分组的字段。例如，要根据文档的字段first和last进行分组，可使用{key: {first: 1, last: 1}}。
+ cond：可选参数。这是一个query对象，决定了初始结果集将包含哪些文档。例如，要包含字段size的值大于5的文档，可使用{cond: {size: {$gt: 5}}。
+ initial：一个包含初始字段和初始值的初始group对象，用于在分组期间聚合数据。对于每组不同的键值，都将创建一个初始对象。最常见的情况是，使用一个计数器来跟踪与键值匹配的文档数。例如：{initial: {"count": 0}}。
+ reduce：一个接受参数obj和prev的函数（function(obj, prev)）。对于每个与查询匹配的文档，都执行这个函数。其中参数obj为当前文档，而prev是根据参数initial创建的对象。这让您能够根据obj来更新prev，如计数或累计。例如，要将计数递增，可使用{reduce: function(obj, prev) { prev.count++; }}。
+ finalize：一个接受唯一参数obj的函数（function(obj)），这个参数是对与每个键值组合匹配的最后一个文档执行reduce函数得到的。对于每个键值组合，都将对其使用reduce函数得到的最终对象调用这个函数，然后以数组的方式返回结果。
+ keyf：可选参数，用于替代参数key。可以不指定其属性为分组字段的对象，而指定一个函数，这个函数返回一个用于分组的key对象。这让您能够使用函数动态地指定要根据哪些键进行分组。

▼　Try It Yourself

```go
mongo doc_group.js
```

```go
01 mongo = new Mongo('localhost');
02 wordsDB = mongo.getDB('words');
03 wordsColl = wordsDB.getCollection('word_stats');
04 results = wordsColl.group({ key: {first: 1, last: 1},
05    cond: {first:'a',last:{$in:['a','e','i','o','u']}},
06    initial: {"count":0},
07    reduce: function (obj, prev) { prev.count++; }
08 });
09 print("'A' words grouped by first and last" +
10              " letter that end with a vowel: ");
11 results.forEach(function(item){
12    print(JSON.stringify(item));
13 });
14 results = wordsColl.group({key: {first: 1},
15    cond: {size:{$gt:13}},
16    initial: {"count":0, "totalVowels":0},
17    reduce: function (obj, prev) {
18                prev.count++;
19                prev.totalVowels += obj.stats.vowels;
20             }
21 });
22 print("Words larger than 13 character grouped by first letter : ");
23 results.forEach(function(item){
24    print(JSON.stringify(item));
25 });
26 results = wordsColl.group({key: {first: 1},
27    cond: {},
28    initial: {"count":0, "vowels":0, "consonants":0},
29    reduce: function (obj, prev) {
30                prev.count++;
31                prev.vowels += obj.stats.vowels;
32                prev.consonants += obj.stats.consonants;
33             },
34    finalize: function (obj) {
35                   obj.total = obj.vowels + obj.consonants;
36                }
37 });
38 print("Words grouped by first letter with totals: ");
39 results.forEach(function(item){
40    print(JSON.stringify(item));
41 });
```

```go
'A' words grouped by first and last letter that end with a vowel:
{"first":"a","last":"a","count":3}
{"first":"a","last":"o","count":2}
{"first":"a","last":"e","count":52}
Words larger than 13 character grouped by first letter :
{"first":"a","count":1,"totalVowels":6}
{"first":"r","count":4,"totalVowels":23}
{"first":"c","count":2,"totalVowels":11}
{"first":"t","count":1,"totalVowels":5}
{"first":"i","count":1,"totalVowels":6}
Words grouped by first letter with totals:
{"first":"t","count":163,"vowels":333,"consonants":614,"total":947}
{"first":"b","count":130,"vowels":246,"consonants":444,"total":690}
{"first":"a","count":192,"vowels":545,"consonants":725,"total":1270}
{"first":"o","count":72,"vowels":204,"consonants":237,"total":441}
{"first":"i","count":114,"vowels":384,"consonants":522,"total":906}
{"first":"h","count":77,"vowels":145,"consonants":248,"total":393}
{"first":"f","count":127,"vowels":258,"consonants":443,"total":701}
{"first":"y","count":14,"vowels":26,"consonants":41,"total":67}
{"first":"w","count":93,"vowels":161,"consonants":313,"total":474}
{"first":"d","count":143,"vowels":362,"consonants":585,"total":947}
{"first":"c","count":267,"vowels":713,"consonants":1233,"total":1946}
{"first":"s","count":307,"vowels":640,"consonants":1215,"total":1855}
{"first":"n","count":57,"vowels":136,"consonants":208,"total":344}
{"first":"g","count":67,"vowels":134,"consonants":240,"total":374}
{"first":"m","count":120,"vowels":262,"consonants":417,"total":679}
{"first":"k","count":15,"vowels":22,"consonants":48,"total":70}
{"first":"u","count":33,"vowels":93,"consonants":117,"total":210}
{"first":"p","count":220,"vowels":550,"consonants":964,"total":1514}
{"first":"j","count":22,"vowels":47,"consonants":73,"total":120}
{"first":"l","count":92,"vowels":189,"consonants":299,"total":488}
{"first":"v","count":41,"vowels":117,"consonants":143,"total":260}
{"first":"e","count":150,"vowels":482,"consonants":630,"total":1112}
{"first":"r","count":146,"vowels":414,"consonants":574,"total":988}
{"first":"q","count":10,"vowels":28,"consonants":32,"total":60}
{"first":"z","count":1,"vowels":2,"consonants":2,"total":4}
```

