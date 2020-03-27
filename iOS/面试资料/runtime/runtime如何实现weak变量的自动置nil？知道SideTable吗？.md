**runtime如何实现weak变量的自动置nil？知道SideTable吗？**

> runtime 对注册的类会进行布局，对于 weak 修饰的对象会放入一个 hash 表中。 用 weak 指向的对象内存地址作为key，当此对象的引用计数为0的时候会 dealloc，假如 weak 指向的对象内存地址是a，那么就会以a为键， 在这个 weak表中搜索，找到所有以a为键的 weak 对象，从而设置为 nil。

**更细一点的回答：**

1.初始化时：runtime会调用objc_initWeak函数，初始化一个新的weak指针指向对象的地址。
2.添加引用时：objc_initWeak函数会调用objc_storeWeak() 函数， objc_storeWeak()的作用是更新指针指向，创建对应的弱引用表。
3.释放时,调用clearDeallocating函数。clearDeallocating函数首先根据对象地址获取所有weak指针地址的数组，然后遍历这个数组把其中的数据设为nil，最后把这个entry从weak表中删除，最后清理对象的记录。

SideTable结构体是负责管理类的引用计数表和weak表，

详解：参考自《Objective-C高级编程》一书
**1.初始化时：runtime会调用objc_initWeak函数，初始化一个新的weak指针指向对象的地址。**

``` 
{
    NSObject *obj = [[NSObject alloc] init];
    id __weak obj1 = obj;
}
```

当我们初始化一个weak变量时，runtime会调用 NSObject.mm 中的objc_initWeak函数。

``` 
// 编译器的模拟代码
 id obj1;
 objc_initWeak(&obj1, obj);
/*obj引用计数变为0，变量作用域结束*/
 objc_destroyWeak(&obj1);
```
通过objc_initWeak函数初始化“附有weak修饰符的变量（obj1）”，在变量作用域结束时通过objc_destoryWeak函数释放该变量（obj1）。

**2.添加引用时：objc_initWeak函数会调用objc_storeWeak() 函数， objc_storeWeak()的作用是更新指针指向，创建对应的弱引用表。**

objc_initWeak函数将“附有weak修饰符的变量（obj1）”初始化为0（nil）后，会将“赋值对象”（obj）作为参数，调用objc_storeWeak函数。

``` 
obj1 = 0；
obj_storeWeak(&obj1, obj);
```

**也就是说：**

weak 修饰的指针默认值是 nil （在Objective-C中向nil发送消息是安全的）

然后obj_destroyWeak函数将0（nil）作为参数，调用objc_storeWeak函数。

``` 
objc_storeWeak(&obj1, 0);
```
前面的源代码与下列源代码相同。

``` 
// 编译器的模拟代码
id obj1;
obj1 = 0;
objc_storeWeak(&obj1, obj);
/* ... obj的引用计数变为0，被置nil ... */
objc_storeWeak(&obj1, 0);
```
objc_storeWeak函数把第二个参数的赋值对象（obj）的内存地址作为键值，将第一个参数__weak修饰的属性变量（obj1）的内存地址注册到 weak 表中。如果第二个参数（obj）为0（nil），那么把变量（obj1）的地址从weak表中删除。

由于一个对象可同时赋值给多个附有__weak修饰符的变量中，所以对于一个键值，可注册多个变量的地址。

可以把objc_storeWeak(&a, b)理解为：objc_storeWeak(value, key)，并且当key变nil，将value置nil。在b非nil时，a和b指向同一个内存地址，在b变nil时，a变nil。此时向a发送消息不会崩溃：在Objective-C中向nil发送消息是安全的。

**3.释放时,调用clearDeallocating函数。clearDeallocating函数首先根据对象地址获取所有weak指针地址的数组，然后遍历这个数组把其中的数据设为nil，最后把这个entry从weak表中删除，最后清理对象的记录。**

当weak引用指向的对象被释放时，又是如何去处理weak指针的呢？当释放对象时，其基本流程如下：

1.调用objc_release
2.因为对象的引用计数为0，所以执行dealloc
3.在dealloc中，调用了_objc_rootDealloc函数
4.在_objc_rootDealloc中，调用了object_dispose函数
5.调用objc_destructInstance
6.最后调用objc_clear_deallocating

对象被释放时调用的objc_clear_deallocating函数:

1.从weak表中获取废弃对象的地址为键值的记录
2.将包含在记录中的所有附有 weak修饰符变量的地址，赋值为nil
3.将weak表中该记录删除
4.从引用计数表中删除废弃对象的地址为键值的记录

**总结:**

其实Weak表是一个hash（哈希）表，Key是weak所指对象的地址，Value是weak指针的地址（这个地址的值是所指对象指针的地址）数组。