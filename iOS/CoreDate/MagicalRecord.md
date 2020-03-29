# MagicalRecord

根据 `Github` 上 `MagicalRecord` 的官方文档，`MagicalRecord` 的优点主要有三条：

**1. ** 清理项目中 `CoreData` 代码。
**2. ** 支持清晰、简单、一行式的查询操作。
**3. ** 当需要优化请求时，可以获取 `NSFetchRequest` 进行修改。

##1. 添加MagicalRecord到项目中

将 `MagicalRecord` 添加到项目中，和使用其他第三方一样，可以通过下载源码和 `CocoaPods` 两种方式添加。

**1. ** 从**Github**下载[MagicalRecord](https://github.com/magicalpanda/MagicalRecord)源码，将源码直接拖到项目中，后续需要手动更新源码。
**2. ** 也可以通过 `CocoaPods` 安装 `MagicalRecord`，需要在 `Podfile` 中加入下面命令，后续只需通过命令来更新。

```
pod "MagicalRecord"
```

在之前创建新项目时，通过勾选 `Use Core Data` 的方式添加 `CoreData` 到项目中，会在 `AppDelegate` 文件中生成大量 `CoreData` 相关代码。如果是大型项目，被占用的位置是很重要的。而对于 `MagicalRecord` 来说，只需要两行代码即可。

```Objective-C
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 初始化CoreData堆栈，也可以指定初始化某个CoreData堆栈
    [MagicalRecord setupCoreDataStack];
    return YES;
}

- (void)applicationWillTerminate:(UIApplication *)application {
    // 在应用退出时，应该调用cleanUp方法
    [MagicalRecord cleanUp];
}
```

`MagicalRecord` 是支持 `CoreData` 的 `.xcdatamodeld` 文件的，使得 `CoreData` 这一优点可以继续使用。建立数据结构时还是像之前使用 `CoreData` 一样，通过 `.xcdatamodeld` 文件的方式建立。

![40](./images/40.jpg)

##2. 支持iCloud

`CoreData` 是支持 `iCloud` 的，`MagicalRecord` 对 `iCloud` 相关的操作也做了封装，只需要使用 `MagicalRecord+iCloud.h` 类中提供的方法，就可以进行 `iCloud` 相关的操作。

例如下面是 `MaicalRecord+iCloud.h` 中的一个方法，需要将相关参数传入即可。

```Objective-C
- (void)setupCoreDataStackWithCloudContainer:(NSString *)containerID localStoreNamed:(NSString *)localStore;
```

##3. 创建上下文

`MagicalRecord` 对上下文的管理和创建也比较全面，下面是 `MagicalRecord` 提供的部分创建和获取上下文的代码。因为是给 `NSManagedObjectContext` 添加的 `Category`，可以直接用 `NSManagedObjectContext` 类调用，使用非常方便。

但是需要注意，虽然系统帮我们管理了上下文对象，对于**耗时操作仍然要放在后台线程中处理**，并且在**主线程中进行UI操作**。

```Objective-C
+ [NSManagedObjectContext MR_context]									// 设置默认的上下文为它的父级上下文，并发类型为NSPrivateQueueConcurrencyType
+ [NSManagedObjectContext MR_newMainQueueContext]			// 创建一个新的上下文，并发类型为NSMainQueueConcurrencyType
+ [NSManageObjectContext MR_newPrivateQueueContext]		// 创建一个新的上下文，并发类型为NSPrivateQueueConcurrencyType
+ [NSManagedObectContext MR_contextWithParent:]				// 创建一个新的上下文，允许自定义父级上下文，并发类型为NSPrivateQueueConcurrencyType
+ [NSManagedObjectContext MR_contextWithStoreCoordinator:]	// 创建一个新的上下文，并允许自定义持久化存储协调器，并发类型为NSPrivateQueueConcurrencyType
+ [NSManagedObjectContext MR_defaultContext]					// 获取默认上下文对象，项目中最基础的上下文对象，并发类型是NSMainQueueConcurrencyType
```

##4. 增删改查

`MagicalRecord` 对 `NSManagedObject` 添加了一个 `Category`，将增删改查等操作放在这个 `Category` 中，使得这些操作可以直接被 `NSManagedObject` 类及其子类调用。

###4.1 增

对于托管模型的创建非常简单，不需要像之前还需要进行上下文的操作，现在这都是 `MagicalRecord` 帮我们完成的。

```Objective-C
// 创建并插入到上下文
Employee *emp = [Employee MR_createEntity];
```

###4.2 删

```Objective-C
// 从上下文中删除当前对象
[emp MR_deleteEntity];
```

###4.3 改

```Objective-C
// 获取一个上下文对象
NSManagedObjectContext *defaultContext = [NSManagedObjectContext MR_defaultContext];

// 在当前上下文环境中创建一个新的Employee对象
Employee *emp = [Employee MR_createEntityInContext:defaultContext];
emp.name = @"lxz";
emp.brithday = [NSDate date];
emp.height = 1.7f;

// 保存修改到当期上下文中
[defaultContext MR_saveToPersistentStoreAndWait];
```

###4.4 查

```Objective-C
// 执行查找操作，并设置排序条件
NSArray *empSorted = [Employee MR_findAllSortedBy:@"height" ascending:YES];
```

##5. 自定义NSFetchRequest

下面实例代码中， `Employee` 根据已有的 `employeeFilter` 谓词对象，创建了 `employeeRequest` 请求对象，并将请求对象做修改后，从 `NSManagedObjectContext` 中获取请求结果，实现自定义查找条件。

```Objective-C
NSPredicate *employeeFilter = [NSPredicate predicateWithFormat:@"name LIKE %@", @"*lxz*"];
NSFetchRequest *employeeRequest = [Employee MR_requestAllWithPredicate:employeeFilter];
employeeRequest.fetchOffset = 10;
employeeRequest.fetchLimit = 10;
NSArray *employees = [Employee MR_executeFetchRequest:employeeRequest];
```

###5.1 参数设置

**1. ** 可以通过修改 `MR_LOGGING_DISABLED` 预编译指令的值，控制 `log` 打印。

```Objective-C
#define MR_LOGGING_DISABLED 1
```

**2. ** `MagicalRecord` 在 `DEBUG` 模式下，对模型文件发生了更改，并且没有创建新的模型文件版本。`MagicalRecord` 默认会将旧的持久化存储删除，创建新的持久化存储。

##6. MagicalRecord中文文档

[MagicalRecord中文文档](https://github.com/ios122/MagicalRecord)

