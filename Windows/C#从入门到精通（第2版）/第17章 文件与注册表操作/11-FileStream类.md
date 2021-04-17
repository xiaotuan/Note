### 17.3.1　FileStream类

FileStream称为文件流，继承于Stream类，用于读取和写入文件。使用FileStream类可以产生在磁盘或网络路径上指向文件的文件流，对文件进行读取、写入、打开和关闭操作。FileStream类支持字节和字节数组处理，有些操作比如随机文件的读/写访问，必须由FileStream对象执行。FileStream类提供的构造函数很多，最常用的构造函数如下。

public FileStream(string path, FileMode mode) 或

public FileStream(string path, FileMode mode, FileAccess access)

其中，参数path指出当前FileStream对象封装的文件的相对路径或绝对路径；参数mode指定一个FileMode枚举取值，确定如何打开或创建文件。FileMode枚举的取值及说明如下表所示。

| 取值 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| Append | 如果文件存在，就打开文件，将文件移动到文件的末尾，否则创建一个新文件。FileMode.Append仅可以与枚举FileAccess.Write联合使用 |
| Create | 创建新文件，如果存在这样的文件，就覆盖它 |
| CreateNew | 创建新文件，如果已经存在此文件，则抛出异常 |
| Open | 打开现有的文件，如果不存在所指定的文件，则抛出异常 |
| OpenOrCreate | 如果文件存在，则打开文件，否则就创建新文件。如果文件已经存在，则保留在文件中的数据 |
| Truncate | 打开现有文件，清除其内容，然后可以向文件中写入全新的数据，但是保留文件的初始创建日期；如果不存在所指定的文件，则抛出异常 |

FileAccess枚举参数规定对文件的不同访问级别，FileAccess枚举有三种类型：Read（可读）、Write（可写）、ReadWrite（可读/写），此属性可应用于基于用户的身份验证，赋予用户对文件的不同访问级别。

下表列出了FileStream类的常见成员及其说明。

| 成员名称 | 类别 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| CanWrite | 属性 | 该值指示当前流是否支持写入 |
| CanRead | 属性 | 该值指示当前流是否支持读取 |
| Length | 属性 | 获取用字节表示的流长度 |
| Position | 属性 | 获取或设置此流的当前位置 |
| FileStream | 方法 | 构造函数，初始化FileStream 类的新实例 |
| Close | 方法 | 关闭文件并释放与当前文件流关联的任何资源 |
| Flush | 方法 | 清除该流的所有缓冲区，使所有缓冲的数据被写入基础设备（如文件等） |
| Read | 方法 | 从流中读取字节块并将该数据写入给定的缓冲区中 |
| ReadByte | 方法 | 从文件中读取一个字节，并将读取位置提升一个字节 |
| Seek | 方法 | 设置当前流的读/写指针位置，需要指定偏移字节和起始位置。起始位置在枚举System.IO.SeekOrigin中定义。有3个可选值，Begin表示流的开头，Current表示流的当前读/写位置，End表示流的末尾 |
| Write | 方法 | 使用从缓冲区读取的数据将字节块写入该流 |
| WriteByte | 方法 | 将一个字节写入文件流的当前位置 |

下面对FileStream类中比较重要的几个成员进行介绍。

（1）Position属性。获取或设置此流的当前位置。属性值表示此流的当前位置。

（2）Close()方法。在创建和使用完一个流后一定要将其及时关闭。

（3）Flush()方法。在调用Close()方法之前调用Flush()方法，可以将以前写入缓冲区的任何数据都复制到文件中，并且缓冲区被清除。

（4）Seek()方法。Seek方法用于设置文件指针的位置，其调用格式为：

```c
public long Seek(long offset, SeekOrigin origin);aFile.Seek(8,SeekOrigin.Begin)
```

其中，long offset是规定文件指针以字节为单位的移动距离；SeekOrigin origin是规定开始计算的起始位置，此枚举包含3个值：Begin、Current和End。比如，若aFile是一个已经初始化的FileStream对象，则语句“aFile.Seek(8,SeekOrigin.Begin);”表示文件指针从文件的第一个字节计算起移动到文件的第8个字节处。

（5）Read()方法。Read方法用于从FileStream对象所指向的文件读数据，其调用格式为：

```c
Public  int  Read(byte[] array,int offset, int count);
```

第一个参数是被传输进来的字节数组，用以接受FileStream对象中读到的数据。第二个参数指明从文件的什么位置开始读入数据，它通常是0，表示从文件开始读取数据、写到数组，最后一个参数规定从文件中读出多少字节。

（6）Write()方法。Write方法用于向FileStream对象所指向的文件中写数据，其调用格式与Read方法相似。写入数据的流程是先获取字节数组，再把字节数据转换为字符数组，然后把这个字符数组用Write方法写入到文件中，当然在写入的过程中，可以确定在文件的什么位置写入，写多少字符等。

下面的代码用于实现打开一个现有文件并将信息显示到文本框中。

```c
01  openFileDialog1.Filter = "文本文件(*.txt)|*.txt";   //打开文件对话框的筛选器
02  openFileDialog1.ShowDialog();                      //显示打开文件对话框
03  textBox1.Text = openFileDialog1.FileName;          //在文本框中显示打开文件的文件名
04  FileStream fs = File.OpenRead(textBox1.Text);      //创建FileStream实例对象
05  byte[] b = new byte[1024];                         //创建字节数组b
06  while (fs.Read(b,0,b.Length) > 0)                  //循环读文件内容到缓冲区b中
07  {
08         textBox2.Text=Encoding.Default.GetString(b); // 将字节数组中的字节解码为字符串
09  }
```

**【代码详解】**

本例利用OpenRead方法打开现有文件并读取时，首先生成FileStream类的一个实例对象，用来记录要打开的文件路径及名称；调用FileStream类的Read方法时，使用Default编码方式的GetString方法对文件内容进行编码，并将结果显示在TextBox文本框中。

使用FileStream类读取数据不像使用StreamReader和StreamWriter类读取数据那么容易，这是因为FileStream类只能处理原始字节，这使得FileStream类可以用于任何数据文件，而不仅仅是文本文件，通过读取字节数据就可以读取类似图像和声音的文件。这种灵活性的代价是不能使用它直接读入字符串，而使用StreamWriter和StreamReader类却可以这样处理。

