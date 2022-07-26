`Buffer` 是 Node 中的另一个全局对象，是用于处理二进制数据的一种方式。为了将二进制数据转换为字符串，需要调用套接字的 `setEncoding` 函数来改变当前使用的数据编码方式。

作为示例，可以使用如下代码来创建一个新的 `Buffer` 对象：

```js
var buf = new Buffer(string);
```

若需要将一个字符串保存在 buffer 中时，可以通过传入第二个可选参数来设置对该字符串的编码方式。支持的编码方式包括：

+ `ascii`：七位 ASCII。
+ `utf8`：多字节编码的 Unicode 字符。
+ `usc2`：两字节，little endian 方式编码的 Unicode 字符。
+ `base64`：Base64 编码。
+ `hex`：每个字节编码为两个十六进制字符。

你也可以将字符串写入到一个现有的 buffer 对象中，并指定该写入操作的偏移，数据长度和编码方式：

```js
buf.write(string);	// 写入的默认偏移为 0，默认数据长度为 buffer.length - offset，编码默认采用 utf8
```

