[toc]

### 2.2.1　缓冲器、JSON、StringDecoder和UTF-8字符串

缓冲器可以转换成JSON或者字符串。为了演示，将以下内容输入一个Node文件中，然后用命令行运行这个文件：

```python
"use strict";
let buf = new Buffer('This is my pretty example');
let json = JSON.stringify(buf);
console.log(json);
```

输出如下：

```python
{"type":"Buffer",
"data":[84,104,105,115,32,105,115,32,109,121,32,112,114,101,116,
116,121,32,101,120,97,109,112,108,101]}
```

这段JSON说明了被转化的对象类型是 `Buffer` 类，后面紧跟着 `Buffer` 类中的数据。当然了，我们看到的是被存入缓冲器的字节序列，该序列是无法被阅读的。

> <img class="my_markdown" src="../images/33.png" style="zoom:50%;" />
> **ES6**
> 大多数示例代码都是使用我们所熟悉的JavaScript写的。但是我会不时地提及ES6，而且在第9章我将会着重讲解Node与ES6（ECMAScript 2015）。

让我们把这个例子完善一下，可以通过解析JSON对象来重新获取缓冲器中的数据，也可以通过 `Buffer.toString()` 方法将其转化为字符串，如例2-2所示。

**例2-2　将字符串转化为缓冲器再转化为JSON，然后再转回来**

```python
"use strict";
let buf = new Buffer('This is my pretty example');
let json = JSON.stringify(buf);
let buf2 = new Buffer(JSON.parse(json).data);
console.log(buf2.toString()); // this is my pretty example
```

`console.log()` 方法会将最初用来转化为缓冲器的字符串打印出来。 `toString()` 方法默认将字符串转化为UTF-8编码，如果想要别的字符串类型，可以传入所需要的字符串类型：

```python
console.log(buf2.toString('ascii')); // this is my pretty example
```

也可以指定转化字符串的起始和结束位置：

```python
console.log(buf2.toString('utf8', 11,17)); // pretty
```

`Buffer.toString()` 并不是唯一将缓冲器转化为字符串的方式。你也可以使用一个帮助类，即 `StringDecoder` 。这个类的唯一作用就是将缓冲器中的数据转化为UTF-8字符串。但它的实现方式略微灵活一些，而且结果是可逆的。如果使用 `buffer.toString()` 方法获取到的是不完整的UTF-8字符序列，那么它返回的也会是乱码。如果 `StringDecoder` 遇到一个不完整的字符序列，则会将它存到缓冲器中，直到序列变得完整，再输出结果。所以，如果你从流中以块为单位来获取UTF-8字符串，那么最好使用StringDecoder。

下例展示了两种字符串转换方式的区别。欧元符号（€）被编码为3个字节，但是第一个缓冲器中只包含前两个字节，第二个缓冲器包含第三个字节。

```python
"use strict";
let StringDecoder = require('string_decoder').StringDecoder;
let decoder = new StringDecoder('utf8');
let euro = new Buffer([0xE2, 0x82]);
let euro2 = new Buffer([0xAC]);
console.log(decoder.write(euro));
console.log(decoder.write(euro2));
console.log(euro.toString());
console.log(euro2.toString());
```

使用 `StringDecoder` 的时候，打印到控制台上的第一行是空行，第二行显示了欧元符号（€），而使用 `buffer.toString()` 时，两行都是乱码。

你也可以使用 `buffer.write()` 来将字符串写入一个缓冲器中。当然了，缓冲器的大小一定要能容纳得下字符所占用的字节数。同样，欧元符号需要3个字节来表示（0xE2、0x82、0xAC）：

```python
let buf = new Buffer(3);
buf.write('€','utf-8');
```

这个例子也很好地展示了UTF-8字符的数量和缓冲器中所需要的字节的数量是不一样的。要是还有疑问，使用 `buffer.length` 可以很方便地检查缓冲器的大小：

```python
console.log(buf.length); // 3
```

