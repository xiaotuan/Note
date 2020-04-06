<center><font size="5"><b>Javascript中的Array TypedArray ArrayBuffer DataView</b></font></center>

> 摘自：https://blog.csdn.net/sg202060520/article/details/79680526

1. Array最常用，应该都知道
```js
let a = [ ]
a.push(1)
console.info(a[0])
```

2. TypedArray是用来存储二进制数据的抽象数据结构，如果把他当做父类理解，那他的子类有：
```text
where TypedArray() is one of:

Int8Array();
Uint8Array();
Uint8ClampedArray();
Int16Array();
Uint16Array();
Int32Array();
Uint32Array();
Float32Array();
Float64Array();
```
语法如下：
```js
new TypedArray(); // new in ES2017
new TypedArray(length);
new TypedArray(typedArray);
new TypedArray(object);
new TypedArray(buffer [, byteOffset [, length]]);
Int16Array不能用push方法，但可以中括号赋值，比如 int16[2]=60;console.info(int16)
```

和Array的互转
1） Array转Int16Array 
`var int16 = new Int16Array([1,2,3]);console.info(int16)`

2） Int16Array 转Array
`Array.from(new Int16Array([1,2,3]))`

3. ArrayBuffer用来表示通用的、固定长度的原始二进制数据缓冲区。ArrayBuffer 不能直接操作，而是要通过类型数组对象或DataView 对象来操作，它们会将缓冲区中的数据表示为特定的格式，并通过这些格式来读写缓冲区的内容。
```js
var buffer = new ArrayBuffer(8);
console.log(buffer.byteLength);
var view = new Int32Array(buffer);
```
> 注意了：
> 1）ArrayBuffer的长度是用byteLength属性获取，不是length,还有定义好长度之后，byteLength也就定下来，跟存不存值没有关系。
> 2）别想着赋值和取值，不知道这个结构有啥用，用起来不方便，偏偏音频解码用到了

4. DataView 是一个可以从ArrayBuffer对象中读写多种数值类型的底层接口，在读写时不用考虑平台字节序问题。
```js
// create an ArrayBuffer with a size in bytes
var buffer = new ArrayBuffer(16);
// Create a couple of views
var view1 = new DataView(buffer);
var view2 = new DataView(buffer,12,4); //from byte 12 for the next 4 bytes
view1.setInt8(12, 42); // put 42 in slot 8
console.log(view2.getInt8(0));
// expected output: 42
```
> DataView似乎就是为了让ArrayBuffer可用，证明其存在价值：
> 1 )  DataView包装ArrayBuffer，使ArrayBuffer可以读写数据
> 2） 写数据需要用set方法，比如setInt8(12，42)，而读数据用get方法，比如getInt8(0)，仍然觉得没有数组好用
> 3） Array.from(dv) 会为空数组，这个最垃圾，简直是大坑,还是遍历获取吧
>
> ```js
> let dv = new DataView(new ArrayBuffer(16));
> dv.setInt8(0,10);
> Array.from(dv);
> ```
