# 获取结果Count值

开发过程中有时需要只获取所需数据的 `Count` 值，也就是执行获取操作后**数组中所存储的对象数量**。遇到这个需求，如果像之前一样 `NSManagedObjectContext` 执行获取操作，获取到数组然后取 `Count`，这样**对内存消耗是很大的**。

对于这个需求，苹果提供了两种常用的方式获取这个 `Count` 值。这两种获取操作，都是在数据库中完成的，**并不需要将托管对象加载到内存中**，对内存的开心也是很小的。

##1. 方法1，设置resultType

```Objective-C
// 设置过虑条件，可以根据需求设置自己的过虑条件
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"height < 2"];
// 创建请求对象，并指明操作Employee表
NSFetchRequest *fetchRequest = [NSFetchRequest fetchRequestWithEntityName:@"Employee"];
fetchRequest.predicate = predicate;
// 这一步是关键。设置返回结果类型为Count，返回结果为NSNumber类型
fetchRequest.resultType = NSCountResultType;

// 执行查询操作，返回的结果还是数组，数组中值存在一个对象，就是计算出的Count值
NSError *error = nil;
NSArray *dataList = [context executeFetchRequest:fetchRequest error:&error];
NSInteger count = [dataList.firstObject integerValue];
NSLog(@"fetch request result Employee.count = %ld", count);

// 错误处理
if (error) {
    NSLog(@"fetch request result error : %@", error);
}
```

**方法1**中设置 `NSFetchRequest` 对象的 `resultType` 为 `NSCountResultType`，获取到结果的 `Count`值。这个枚举值在之前的文章中提到过，除了 `Count` 参数，还可以设置其他三种参数。

##1.2 方法2，使用NSManagedObjectContext提供的方法

```Objective-C
// 设置过虑条件
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"height < 2"];
// 创建请求对象，指明操作Employee表
NSFetchRequest *fetchRequest = [NSFetchRequest fetchRequestWithEntityName:@"Employee"];
fetchRequest.predicate = predicate;

// 通过调用NSManagedObjectContext的countForFetchRequest:error:方法，获取请求结果count值，返回结果直接是NSUInteger类型变量
NSError *error = nil;
NSUInteger count = [context countForFetchRequest:fetchRequest error:&error];
NSLog(@"fetch request result count is : %ld", count);

// 错误处理
if (error) {
    NSLog(@"fetch request result error : %@", error);
}
```

