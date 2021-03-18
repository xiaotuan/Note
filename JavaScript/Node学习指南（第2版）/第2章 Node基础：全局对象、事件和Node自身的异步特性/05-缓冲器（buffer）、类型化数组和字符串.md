[toc]

### 2.2　缓冲器（buffer）、类型化数组和字符串

在早期基于浏览器的JavaScript中，从来都不需要处理二进制数据（一个8位字节流）。起初，JavaScript是用来处理那些用来访问或者输出到告警（alert）窗口和表单的字符串的值。即便Ajax让这个初衷有所改变，但客户端和服务器端的通信还是基于字符串（Unicode，统一字符编码）的。

不过当我们对JavaScript的诉求变得更加复杂时，事情就有所变化了。我们可以使用的不止Ajax，还有WebSockets。此外，浏览器所支持的功能也得到了扩充，相比于简单的表单访问，我们现在有WebGL和Canvas等新技术。

针对这个问题，在JavaScript和浏览器中，解决方案是使用 `ArrayBuffer，并` 通过类型化的数组进行操作。而在Node中，解决方案是缓冲器。

一开始这两种解决方案是不一样的。但是，当io.js和Node.js合并到Node v4.0.0中后，Node也通过V8 v4.5获得对类型化数组的支持。Node缓冲器现在使用 `Uint8Array` 实现，这是一种支持8位无符号整数的类型化数组。但是这并不意味着你可以将它们互相替换使用。在Node中， `Buffer` 类是大多数I/O使用的主要数据结构，如果换成另外一种类型化数组，你的程序就会出问题。此外，将Node缓冲器转换为类型化数组也许是可行的，但也会有问题。根据 `Buffer` 类的API文档，当你将缓冲器“转换”为类型化数组时：

+ 缓冲器的内存会被复制一份，而非共享内存；
+ 缓冲器的内存被解释成数组，而不是字节数组，也就是说， `new Uint32Array（new Buffer（[1,2,3,4]）)` 会创建一个有4个元素（ `[1,2,3,4]` ）的 `Uint32Array` ，而不是一个具有一个元素（ `[0x1020304]` 或 `[0x4030201]` ）的 `Uint32Array` 。

所以，在Node中处理八位字节流时，这两种类型你都可以用，但在大多数情况下还是用缓冲器。那么，Node缓冲器到底是什么呢？

> <img class="my_markdown" src="../images/30.png" style="zoom:50%;" />
> **什么是八位字节流**
> 为什么二进制或原始数据文件被称为八位字节流？八位字节是计算中的一个单位。长度为8bit（位），因此称为“八位字节”。在支持8位字节的系统中，八个位和一个字节是相同的。流只是一个数据序列。因此，二进制文件也就是一个八位字节序列。

Node缓冲器是存储于V8堆之外的原始二进制数据，通过 `Buffer` 类来管理。一旦分配了存储空间，就不能再修改空间的大小。

缓冲器是读写文件的默认数据类型：除非读写文件时指定一个编码，否则文件的读写都会通过缓冲器进行。

在Node v4中，你可以直接使用 `new` 关键字来创建一个缓冲器：

```python
let buf = new Buffer(24);
```

但是要注意，和 `ArrayBuffer` 不一样的是，创建一个新的Node缓冲器并不会初始化其中的内容。如果你不知道一个缓冲器是不是包含特殊或者敏感的数据，为了防止被最终的结果搞得晕头转向，最好在创建缓冲器的时候，就为其填充好数据：

```python
let buf = new Buffer(24);
buf.fill(0); // fills buffer with zeros
```

你也可以只填充部分数据，并指定起始和结束的位置就可以了。

> <img class="my_markdown" src="../images/31.png" style="zoom:50%;" />
> **在填充缓冲器的内容时指定编码**
> Node v5.7.0之后，你可以在调用 `buf.fill()` 时使用这个语法来指定编码： `buf.fill(string[, start[, end]] [, encoding])` 。

你也可以在创建新缓冲器的时候，直接向构造函数中传入一个字节数组，或者传入另一个缓冲器，又或者传入一个字符串。Node会复制这3种内容，用来创建新的缓冲器。对于字符串来说，如果编码不是UTF-8，你就需要指定编码。Node中字符串的默认编码是UTF-8（或者utf8、utf-8）。

```python
let str = 'New String';
let buf = new Buffer(str);
```

我不想把 `Buffer` 类的所有方法都讲一遍，因为Node提供了详细的文档。但是其中一些功能还是值得我们仔细研究一下的。

> <img class="my_markdown" src="../images/32.png" style="zoom:50%;" />
> **Node v4和Node v5/v6的区别**
> `raw` 和 `raws` 这两种编码在v5和之后的版本中被删掉了。

在Node v6中，构造函数已被弃用，转而使用新的缓冲器方法来创建缓冲器： `Buffer.from()、Buffer.alloc () 和Buffer.allocUnsafe ()` 。

`Buffer.from ()` 函数会复制传入的数组，然后将其装进缓冲器中返回。但是，如果传入一个具有可选的字节偏移量和长度的ArrayBuffer时，则缓冲器与ArrayBuffer会共享相同的内存。如果传入缓冲器，就会返回这个缓冲器内容的备份；传入字符串，就会返回字符串的备份。

`Buffer.alloc()` 函数创建一个填充好的、且具有指定大小的缓冲器，而 `Buffer. alloc Unsafe()` 也会创建一个指定大小的缓冲器，但是这个缓冲器可能包含一些旧数据或者敏感信息，此时就需要使用 `buf.fill()` 来填充。

以下是相关的Node代码：

```python
'use strict';
let a = [1,2,3];
let b = Buffer.from(a);
console.log(b);
let a2 = new Uint8Array([1,2,3]);
let b2 = Buffer.from(a2);
console.log(b2);
let b3 = Buffer.alloc(10);
console.log(b3);
let b4 = Buffer.allocUnsafe(10);
console.log(b4);
```

计算机会产生如下结果：

```python
<Buffer 01 02 03>
<Buffer 01 02 03>
<Buffer 00 00 00 00 00 00 00 00 00 00>
<Buffer a0 64 a3 03 00 00 00 00 01 00>
```

请注意通过 `Buffer.alloc()` 得到的数据与通过 `Buffer.allocUnsafe()` 得到的数据之间的区别。

