### 5.4.1 udev与devfs的区别

尽管devfs有这样和那样的优点，但是，在Linux 2.6内核中，devfs被认为是过时的方法，并最终被抛弃，udev取代了它。Linux VFS内核维护者Al Viro指出了几点udev取代devfs的原因：

（1）devfs所做的工作被确信可以在用户态来完成。

（2）devfs被加入内核之时，大家寄望它的质量可以迎头赶上。

（3）devfs被发现了一些可修复和无法修复的bug。

（4）对于可修复的bug，几个月前就已经被修复了，其维护者认为一切良好。

（5）对于后者，同样是相当长一段时间以来没有改观了。

（6）devfs 的维护者和作者对它感到失望并且已经停止了对代码的维护工作。

Linux内核的两位贡献者，Richard Gooch（devfs的作者）和Greg Kroah-Hartman（sysfs的主要作者）就devfs/udev进行了激烈的争论：

Greg:Richard had stated that udev was a proper replacement for DevFS.

Richard:Well, that's news to me!

Greg:DevFS should be taken out because policy should exist in userspace and not in the kernel.

Richard:SysFS, developed in large part by Greg, also implemented policy in the kernel.

Greg:DevFS was broken and unfixable

Richard:No proof. Never say never...

这段有趣的争论可意译如下：

Greg：Richard已经指出，udev是DevFS恰当的替代品。

Richard：哦，是哪个Richard说的？我怎么不知道。

Greg：DevFS应该下课，因为策略应该位于用户空间而不是内核空间。

Richard：哦，我听说，相当大部分由Greg完成的sysfs也在内核中实现了策略。

Greg：devfs很蹩脚，也不稳定。

Richard：呵呵，没证据，别那么武断……

在Richard Gooch和Greg Kroah-Hartman的争论中，Greg Kroah-Hartman使用的理论依据就在于policy（策略）不能位于内核空间。Linux设计中强调的一个基本观点是机制和策略的分离。机制是做某样事情的固定的步奏、方法，而策略就是每一个步奏所采取的不同方式。机制是相对固定的，而每个步奏采用的策略是不固定的。机制是稳定的，而策略则是灵活的，因此，在Linux内核中，不应该实现策略。Richard Gooch认为，属于策略的东西应该被移到用户空间。这就是为什么devfs位于内核空间，而udev确要移到用户空间的原因。

下面举一个通俗的例子来理解udev设计的出发点。以谈恋爱为例，Greg Kroah-Hartman认为，可以让内核提供谈恋爱的机制，但是不能在内核空间限制跟谁谈恋爱，不能把谈恋爱的策略放在内核空间。因为恋爱是自由的，用户应该可以在用户空间中实现“萝卜白菜，各有所爱”的理想，可以根据对方的外貌、籍贯、性格等自由选择。对应devfs而言，第1个相亲的女孩被命名为/dev/girl0，第2个相亲的女孩被命名为/dev/girl1，依此类推。而在用户空间实现的udev则可以使得用户实现这样的自由：不管你中意的女孩第几个来，只要它与你定义的规则符合，都命名为/dev/mygirl！

udev完全在用户态工作，利用设备加入或移除时内核所发送的热插拔事件（hotplug event）来工作。在热插拔时，设备的详细信息会由内核输出到位于/sys的sysfs文件系统。udev的设备命名策略、权限控制和事件处理都是在用户态下完成的，它利用sysfs中的信息来进行创建设备文件节点等工作。热插拔时输出到sysfs中的设备的详细信息就是相亲对象的资料（外貌、年龄、性格、籍贯等），设备命名策略等就是择偶标准。devfs是个蹩脚的婚姻介绍所，它直接指定了谁和谁谈恋爱，而udev则聪明地多，它只是把资料交给客户，让客户根据这些资料去选择和谁谈恋爱。

由于udev根据系统中硬件设备的状态动态更新设备文件，进行设备文件的创建和删除等，因此，在使用udev后，/dev目录下就会只包含系统中真正存在的设备了。

devfs与udev的另一个显著区别在于：采用devfs，当一个并不存在的/dev节点被打开的时候，devfs能自动加载对应的驱动，而udev则不这么做。这是因为udev的设计者认为Linux应该在设备被发现的时候加载驱动模块，而不是当它被访问的时候。udev的设计者认为devfs所提供的打开/dev节点时自动加载驱动的功能对于一个配置正确的计算机是多余的。系统中所有的设备都应该产生热插拔事件并加载恰当的驱动，而udev能注意到这点并且为它创建对应的设备节点。

