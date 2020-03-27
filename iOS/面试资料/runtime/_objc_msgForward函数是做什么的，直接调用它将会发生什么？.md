**_objc_msgForward函数是做什么的，直接调用它将会发生什么？**

_objc_msgForward是 IMP 类型，用于消息转发的：当向一个对象发送一条消息，但它并没有实现的时候，_objc_msgForward会尝试做消息转发。

详解：_objc_msgForward在进行消息转发的过程中会涉及以下这几个方法：

 1. List itemresolveInstanceMethod:方法 (或resolveClassMethod:)。
 2. List itemforwardingTargetForSelector:方法
 3. List itemmethodSignatureForSelector:方法
 4. List itemforwardInvocation:方法
 5. List itemdoesNotRecognizeSelector: 方法

具体请见：请看Runtime在工作中的运用 第三章Runtime方法调用流程；

