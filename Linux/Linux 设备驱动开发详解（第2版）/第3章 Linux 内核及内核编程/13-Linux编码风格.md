### 3.5.1 Linux编码风格

Linux程序的命名习惯和Windows程序的命名习惯及著名的匈牙利命名法有很大的不同。

在Windows程序中，习惯以如下方式命名宏、变量和函数：

#define PI 3.141 592 6 /*用大写字母代表宏*/ 
 
 int minValue, maxValue; /*变量：第一个单词全写，其后的单词第一个字母小写*/ 
 
 void SendData(void); /*函数：所有单词第一个字母都大写定义*/

这种命名方式在程序员中非常盛行，意思表达清晰且避免了匈牙利法的臃肿，单词之间通过首字母大写来区分。通过第1个单词的首字母是否大写可以区分名称属于变量还是属于函数，而看到整串的大写字母可以断定为宏。实际上，Windows的命名习惯并非仅限于Windows编程，大多数领域的程序开发都遵照此习惯。

但是Linux不以这种习惯命名，对应于上面的一段程序，在Linux中会被命名为：

#define PI 3.141 592 6 
 
 int min_value, max_value; 
 
 void send_data(void);

上述命名方式中，下划线大行其道，不依照Windows所采用的首字母大写以区分单词的方式。Linux的命名习惯与Windows命名习惯各有千秋，但是既然本书和本书的读者立足于编写Linux程序，代码风格理应保持与Linux开发社区的一致性。

Linux的代码缩进使用“TAB”（8个字符）。

Linux的代码括号“{”和“}”的使用原则如下。

（1）对于结构体、if/for/while/switch语句，“{”不另起一行，例如：

struct var_data { 
 
 int len; 
 
 char data[0];



};

if (a == b) { 
 
 a = c; 
 
 d = a; 
 
 }

for (i = 0; i < 10; i++) { 
 
 a = c; 
 
 d = a; 
 
 }

（2）如果if、for循环后只有1行，不要加“{”和“}”，例如：

for (i = 0; i < 10; i++) { 
 
 a = c; 
 
 }

应该改为：

for (i = 0; i < 10; i++) 
 
 a = c;

（3）if和else混用的情况下，else语句不另起一行，例如：

if (x == y) { 
 
 ... 
 
 } else if (x > y) { 
 
 ... 
 
 } else { 
 
 ... 
 
 }

（4）对于函数，“{”另起一行，譬如：

int add(int a, int b) 
 
 { 
 
 return a + b; 
 
 }

在switch/case语句方面，Linux建议switch和case对齐，例如：

switch (suffix) { 
 
 case 'G': 
 
 case 'g': 
 
 mem <<= 30; 
 
 break; 
 
 case 'M': 
 
 case 'm': 
 
 mem <<= 20; 
 
 break; 
 
 case 'K': 
 
 case 'k': 
 
 mem <<= 10; 
 
 /* fall through */ 
 
 default: 
 
 break; 
 
 }

内核下的Documentation/CodingStyle描述了Linux内核对编码风格的要求，内核下的scripts/checkpatch.pl提供了1个检查代码风格的脚本。如果我们使用scripts/checkpatch.pl检查包含如下代码块的源程序：



for (i = 0; i < 10; i++) { 
 
 a = c; 
 
 }

就会产生“WARNING: braces {} are not necessary for single statement blocks”的警告。

另外，请注意代码中空格的应用，譬如“forٮ(iٮ=ٮ0; ٮiٮ<ٮ10; ٮi++)ٮ{”语句中“ٮ”都是空格。

