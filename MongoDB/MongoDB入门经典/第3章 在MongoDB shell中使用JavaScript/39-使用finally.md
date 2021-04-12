### 3.11.3　使用finally

另一个很有用的异常处理工具是关键字finally，这个关键字可放在try/catch块后面。try/catch块执行完毕后，总是会执行finally块，无论是发生并捕获了错误，还是整个try块都被执行。

下面的示例演示了如何使用finally块：

```go
function testTryCatch(value){
　 try {
　　　if (value < 0){
　　　　 throw "too small";
　　　} else if (value > 10){
　　　　 throw "too big";
　　　}
　　　your_code_here
　 } catch (err) {
　　　print("The number was " + err.message);
　 } finally {
　　　print("This is always written.");
　 }
}
```

