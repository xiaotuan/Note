### 21.1.2　Thread类

在System.Threading命名空间下有一个Thread类，用于对线程进行管理，如创建线程、暂停线程、终止线程、合并线程、设置其优先级并获取其状态。此外，还有System.Threading.ThreadPool和System.ComponentModel.BackgroundWorker也可以实现线程处理，本章不再详细介绍。Thread类包含详细描述线程的方法和属性。Thread类常用的方法如下表所示。

| 方法名称 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| Thread | 初始化Thread类的新实例，指定允许对象在线程启动时传递给线程的委托 |
| Abort | 在调用此方法的线程上引发 ThreadAbortException，以开始终止此线程的过程 |
| Join | 阻塞调用线程，直到某个线程终止时为止 |
| ResetAbort | 取消为当前线程请求的 Abort |
| Sleep | 将当前线程阻塞指定的毫秒数 |
| Start | 使线程得以按计划执行 |

Thread类常用的属性如下表所示。

| 属性名称 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| IsAlive | 获取一个值，该值指示当前线程的执行状态 |
| IsBackground | 获取或设置一个值，该值指示某个线程是否为后台线程 |
| Name | 获取或设置线程的名称 |
| Priority | 数组类型不匹配 |
| ThreadState | 获取一个值，该值包含当前线程的状态 |

