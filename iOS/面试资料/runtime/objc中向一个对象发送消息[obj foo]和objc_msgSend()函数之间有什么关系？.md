**objc中向一个对象发送消息[obj foo]和objc_msgSend()函数之间有什么关系？**

在objc编译时，[obj foo] 会被转意为：objc_msgSend(obj, @selector(foo));。