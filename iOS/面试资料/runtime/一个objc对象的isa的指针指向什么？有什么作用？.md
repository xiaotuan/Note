**一个objc对象的isa的指针指向什么？有什么作用？**

指向他的类对象,从而可以找到对象上的方法

详解：下图很好的描述了对象，类，元类之间的关系:
![enter description here](./images/1561035044625.png)

图中实线是 super_class指针，虚线是isa指针。

1.Root class (class)其实就是NSObject，NSObject是没有超类的，所以Root class(class)的superclass指向nil。
2.每个Class都有一个isa指针指向唯一的Meta class
3.Root class(meta)的superclass指向Root class(class)，也就是NSObject，形成一个回路。
4.每个Meta class的isa指针都指向Root class (meta)。
