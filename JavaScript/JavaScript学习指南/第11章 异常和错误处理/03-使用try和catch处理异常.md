### 11.2　使用try和catch处理异常

使用 `try…catch` 语句可以完成异常处理。它的理念是：首先“尝试”去做一些事情，一旦在做的过程中发生异常，就“捕获”这些异常。在前面的例子中，即便 `validateEmail` 处理了那些邮件中没有包含@的预期错误，但还是有可能产生非预期的错误：比如，某个开发人员不小心给 `email` 赋了一个非字符串的值。从代码来看，如果将前面例子中的 `email` 设为 `null` 、数字、对象等任何非字符串的值时都会出错，此时程序将会非常不友好地崩溃掉。为了防范这种非预期错误，可以将用于验证邮箱的代码封装在 `try…catch` 语句中，例如：

```javascript
const email = null; // whoops
try {
   const validatedEmail = validateEmail(email);
   if(validatedEmail instanceof Error) {
      console.error(`Error: ${validatedEmail.message});
   } else {
      console.log('Valid email: ${validatedEmail}');
   }
} catch(err) {
   console.error('Error: ${err.message}');
} 
```

捕获异常后，程序就不会再崩溃了，而是打印了错误日志后继续执行。不过可能还会有别的问题：如果这里需要输入一个合法的邮箱，而用户输入了无效的邮箱，那程序继续运行下去也没有意义了。不过，至少现在我们可以用一种更优雅的方式处理错误了。

注意，一旦有错误产生，执行逻辑就会立即跳转到 `catch` 块中。也就是说， `validateEmail` 调用语句后面的if语句不会再执行。也可以在 `try` 块中写入任何期望的语句，最先产生错误的语句会使执行逻辑跳转到 `catch` 块中。如果 `try` 块中的语句没有任何错误， `catch` 块中的代码就不会被执行，程序会继续运行下去。

