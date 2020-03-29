# iOS之前进行数据同步

就想上面**CoreData多线程**文章中讲到的，在 `iOS5` 之前存在多个 `NSManagedObjectContext` 的情况下，一个 `NSManagedObjectContext`发生更改并提交存储区后，其他 `NSManagedObjectContext` 并不知道这个改变，其他 `NSManagedObjectContext` 和本地存储的**数据时不同步的**，所以就涉及到数据同步的问题。

进行数据同步时，会遇到多种复杂情况。例如只有一个 `NSManagedObjectContext` 数据发生了改变，其他 `NSManagedObjectContext` 更新时并没有对相同的数据做改变，这样不会造成冲突，可以直接将其他 `NSManagedObjectContext` 更新。

如果在一个 `NSManagedObjectContext` 数据发生改变后，其他 `NSManagedObjectContext` 对相同的数据做了改变，而且改变的结果不同，这样在同步时就会造成冲突。下面将会按照这两种情况，分别讲一下不同情况下冲突处理方式。

##1. 简单情况下的数据同步

简单情况下的数据同步，是针对于只有一个 `NSManagedObjectContext` 的数据发生改变，并提交存储区后，其他 `NSManagedObjectContext` 更新时并没有对相同的数据做改变，只是单纯的同步数据的情况。

在 `NSManagedObjectContext` 类中，根据不同操作定义了一些通知。在一个 `NSManagedObjectContext` 发生改变时，其他地方可以通过 `NSManagedObjectContext` 中定义的通知名，来获取 `NSManagedObjectContext` 发生的改变。在 `NSManagedObjectContext` 中定义了下面三个通知：

+ **NSManagedObjectContextWillSaveNotification** `NSManagedObjectContext` 将要想存储区存储数据时，调用这个通知。在这个通知中**不能获取**发生改变相关的`NSManagedObject` 对象。
+ **NSManagedObjectContextDidSaveNotification** `NSManagedObjectContext` 向存储区存储数据后，调用这个通知。在这个通知中**可以获取**改变、添加、删除等信息，以及相关联的 `NSManagedObject` 对象。
+ **NSManagedObjectContextObjectsDidChangeNotification** 在 `NSManagedObjectContext` 中任何一个托管对象发生改变时，调用这个通知。例如修改托管对象的属性。

通过监听 `NSManagedObjectContextDidSaveNotification` 通知，获取所有 `NSManagedObjectContext` 的 `save` 操作。

```Objective-C
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(settingsContext:) name:NSManagedObjectContextDidSaveNotification object:nil];
```

不需要在通知的回调方法中，编写代码对比被修改的托管对象。`NSManagedObjectContext` 为我们提供了下面的方法，只需要将通知对象传入，**系统会自动同步数据**。

```Objective-C
- (void)mergeChangesFromContextDidSaveNotification:(NSNotification *)notification;
```

需要注意的是，由于**通知是同步执行**的，在通知对应的回调方法中所处的线程，和发出通知的 `NSManagedObjectContext` 执行操作时所处的线程是**同一个线程**，也就是系统 `performBlock:` 回调方法分配的线程。

所以其他 `NSManagedObjectContext` 在通知回调方法中，需要注意使用 `performBlock:` 方法，并在 `block` 体中执行操作。

```Objective-C
- (void)settingsContext:(NSNotification *)noti {
    [context performBlock:^{
        // 调用需要同步的NSManagedObjectContext对象的merge方法，直接将通知对象当做参数传进去即可，系统会完成同步操作
        [context mergeChangesFromContextDidSaveNotification:noti];
    }];
}
```

##2. 复杂情况下的数据同步

在一个 `NSManagedObjectContext` 对本地存储区的数据发生改变，而其他 `NSManagedObjectContext` 也对同样的数据做了改变，这样后面执行 `save` 操作的 `NSManagedObjectContext` 就会冲突，并导致后面的 `save` 操作失败，这就是复杂情况下的数据合并。

这是因为每次一个 `NSManagedObjectContext` 执行一次 `fetch` 操作后，**会报错一个本地持久化存储的状态**，当下次执行 `save` 操作时会**对比这个状态和本地持久化状态是否一样**。如果一样，则代表本地没有其他 `NSManagedObjectContext` 对存储发生过改变；如果不一样，则代表本地持久化存储被其他 `NSManagedObjectContext`改变过，这就是造成冲突的根本原因。

对于这种冲突的情况，可以通过 `NSManagedObjectContext` 对象指定解决冲突的方案，通过 `mergePolicy` 属性来设置方案。`mergePolicy` 属性有下面几种可选的策略，默认是 `NSErrorMergePolicy` 方式，这也是唯一一个有 `NSError` 返回值的选项。

+ **NSErrorMergePolicy：**默认值，当出现合并冲突时，返回一个 `NSError` 对象来描述错误，而 `NSManagedObjectContext` 和持久化存储区**不发生改变**。
+ **NSMergeByPropertyStoreTrumpMergePolicy：**以本地存储为准，使用本地存储来覆盖冲突部分。
+ **NSMergeByPropertyObjectTrumpMergePolicy：**以 `NSManagedObjectContext` 的为准，使用 `NSManagedObjectContext` 来覆盖本地存储的冲突部分。
+ **NSOverwriteMergePolicy：**以 `NSManagedObjectContext` 为准，用 `NSManagedObjectContext` 的所有 `NSManagedObject` 对象覆盖本地存储的对应对象。
+ **NSRollbackMergePolicy：**以本地存储为准，`NSManagedObjectContext` 所有的 `NSManagedObject` 对象被本地存储的对应对象所覆盖。

上面五种策略中，除了第一个 `NSErrorMergePolicy` 的策略，其他四种中 `NSMergeByPropertyStoreTrumpMergePolicy` 和 `NSRollbackMergePolicy`，以及 `NSMergeByPropertyObjectTrumpMergePolicy` 和 `NSOverwriteMergePolicy` 看起来是重复的。

其实它们并不是冲突，这四种策略的不同体现在，**对没有发生冲突的部分应该怎么处理**。`NSMergeByPropertyStoreTrumpMergePolicy` 和 `NSMergeByPropertyObjectTrumpMergePolicy` 对没有冲突的部分，未冲突部分数据并不会受到影响。而 `NSRollbackMergePolicy` 和 `NSOverwriteMergePolicy` 则是无论是否冲突，直接全部替换。