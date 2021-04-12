### 3.11.1　try/catch块

为防止代码失控，可使用try/catch块来处理代码存在的问题。如果执行try块中的代码时遇到错误，将跳到catch部分处执行，而不会停止执行脚本。如果没有发生错误，将执行try块中的所有代码，且不会执行catch块中的任何代码。

例如，下面的try/catch块试图将未定义的变量badVarName的值赋给变量x：

```go
try{
 　　var x = badVarName;
} catch (err){
 　　print(err.name + ': "' + err.message + '" occurred when assigning x.');
}
```

注意到catch语句接受一个err参数，这是一个Error对象。Error对象包含属性message，该属性提供了对错误的描述；Error对象还包含属性name，这是引发的错误的类型名。

前面的代码将导致异常，进而显示如下消息：

```go
ReferenceError: "badVarName is not defined" occurred when assigning x."
```

