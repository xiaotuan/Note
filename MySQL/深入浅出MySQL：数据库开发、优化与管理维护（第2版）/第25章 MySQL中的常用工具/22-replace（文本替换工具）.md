

replace是MySQL自带的一个对文件中的字符串进行替换的工具，类似于Linux下的sed，不过它的使用更加简单灵活。

具体使用方法如下：

shell> replace from to [from to] . . -- file [file] . .

shell> replace from to [from to] . . < file

其中“--”表示字符串结束，文件的开始，可跟多个源文件，替换完毕后会覆盖原文件。“<”表示后面的文件作为输入，替换后的文本显示在标准输出上，不会覆盖原文件。

下面对两种方式分别举一个例子进行说明。

（1）覆盖方式（--）。

查看原文件a的内容：

[zzx@localhost～]$ more a

a1 a2 a3

b1 b2 b3

将文件a中的a1和b1分别替换为aa1和bb1：

[zzx@localhost～]$ replace a1 aa1 b1 bb1 -- a

a converted

查看替换后的文件：

[zzx@localhost～]$ more a

aa1 a2 a3

bb1 b2 b3

可以发现，文件a的内容已经是替换后的内容。

（2）非覆盖方式（<）。

查看原文件a的内容：

[zzx@localhost～]$ more a

aa1 a2 a3

bb1 b2 b3

将文件a中的“a”和“b”分别替换为“c”和“d”：

[zzx@localhost～]$ replace a c b d < a

cc1 c2 c3

dd1 d2 d3

查看替换后的文件：

[zzx@localhost～]$ more a

aa1 a2 a3

bb1 b2 b3

可以发现，文件a的内容并没有改变，仍然是替换前的内容，替换后的内容只显示在标准输出上。



