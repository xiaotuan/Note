

#### 
  5.1.2 Model做什么


Model是Shell和所有功能模块访问单页应用的数据和业务逻辑的地方。如果需要登入，我们就调用Model提供的方法。如果想获取人员列表，就从Model获取。如果想获取头像信息……，好了，你懂的。任何希望在功能模块之间共享的或者对应用极为重要的数据和业务，都应该放在Model里面。如果你对MVC架构很了解，那么你应该很了解Model。

虽然所有的业务逻辑和数据都是通过Model访问的，但并不意味着必须只能使用一个（可能非常大）JavaScript文件来存放Model。可以使用名字空间，把Model分成多个容易管理的小文件。比如，如果有一个 Model，它有 people 对象和 chat 对象，则可以把people的逻辑放到spa.model.people.js里面，把chat的逻辑放到spa.model.chat.js里面，然后把它们合并到主Model文件spa.model.js中。使用这个技巧，不管Model使用了多少个文件，暴露给Shell的接口都不会改变。

