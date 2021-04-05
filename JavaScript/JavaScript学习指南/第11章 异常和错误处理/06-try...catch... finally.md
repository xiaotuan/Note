### 11.5　try...catch... finally

很多时候，try块中会包含一些对资源的引用，比如，HTTP连接或者文件。不管有没有发生错误，都需要释放这些资源，防止应用程序永远占用着资源。由于try块中可以包含很多语句，任何一条都有可能发生错误，所以在这里释放资源并不安全（因为错误可能发生在释放资源之前，这样就没有机会释放资源了）。同样，在catch中释放资源也不安全，因为catch中的代码只有在发生错误的时候才会执行。这时finally就派上用场了，不管是否发生错误，finally中的代码都会被执行。

由于还没有讲文件处理和HTTP连接，所以这里只是用一个简单的包含了console.log的语句来演示finally的作用：

```javascript
try {
   console.log("this line is executed...");
  throw new Error("whoops");
    console.log("this line is not...");
} catch(err) {
   console.log("there was an error...");
} finally {
   console.log("...always executed");
   console.log("perform cleanup here");
}
```

分别在有throw语句和没有throw语句的情况下运行这个例子。大家会发现，两种情况下finally块中的代码均被执行了。

