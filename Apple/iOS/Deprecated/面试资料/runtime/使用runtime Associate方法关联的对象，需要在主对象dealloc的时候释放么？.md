**使用runtime Associate方法关联的对象，需要在主对象dealloc的时候释放么？**

无论在MRC下还是ARC下均不需要，被关联的对象在生命周期内要比对象本身释放的晚很多，它们会在被 NSObject -dealloc 调用的object_dispose()方法中释放。

**详解：**

``` 
1、调用 -release ：引用计数变为零
对象正在被销毁，生命周期即将结束. 
不能再有新的 __weak 弱引用，否则将指向 nil.
调用 [self dealloc]

2、 父类调用 -dealloc 
继承关系中最直接继承的父类再调用 -dealloc 
如果是 MRC 代码 则会手动释放实例变量们（iVars）
继承关系中每一层的父类 都再调用 -dealloc

>3、NSObject 调 -dealloc 
只做一件事：调用 Objective-C runtime 中object_dispose() 方法

>4. 调用 object_dispose()
为 C++ 的实例变量们（iVars）调用 destructors
为 ARC 状态下的 实例变量们（iVars） 调用 -release 
解除所有使用 runtime Associate方法关联的对象 
解除所有 __weak 引用 
调用 free()
```