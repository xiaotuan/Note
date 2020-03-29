[toc]

#NSPredicate

##1. 概述

在`iOS`开发过程中，很多需求都需要用到过虑条件。例如过虑一个集合对象中存储的对象，可以通过`Foundation`框架下的`NSPredicate`类来执行这个操作。

`CoreData`中可以通过设置`NSFetchRequest`类的`predicate`属性，来设置一个`NSPredicate`类型的谓词对象当做过虑条件。通过设置这个过虑条件，可以只获取符合过虑条件的托管对象，不会将所有托管对象都加载到内存中。这样是非常节省内存和加快查找速度的，设计一个好的`NSPredicate`可以优化`CoreData`搜索性能。

## 2. 语法

`NSPredicate`更加偏向于自然语言，不像`SQLite`一样有很多固定的语法，看起来也更加清晰易懂。例如下面需要查找条件为**年龄30岁以上**，并且**包括30岁**的条件。

```Objective-C
[NSPredicate predicateWithFormat:@"age >= 30"];
```

###2.1 过虑集合对象

可以通过`NSPredicate`对`iOS`中的集合对象执行过虑操作，可以是`NSArray`、`NSSet`及其子类。对不可变数组`NSArray`执行的过虑，过虑后会返回一个`NSArray`类型的结果数组，其中存储着符合过虑条件的对象。

```Objective-C
NSArray *results = [array filteredArrayUsingPredicate:predicate];
```

对可变数组`NSMutableArray`执行的过虑条件，过虑后会直接改变原集合对象内部存储的对象，删除不符合条件的对象。

```Objective-C
[arrayM filterUsingPredicate:predicate];
```

###2.2 符合过虑条件

谓词不只可以过虑简单条件，还可以过虑复杂条件，设置复合过虑条件。

```Objective-C
[NSPredicate predicateWithFormat:@"(age < 25) AND (firstName = xiaoZhuang)"];
```

当然也可以通过`NSCompoundPredicate`对象来设置符合过虑条件，返回结果是一个`NSPredicate`的子类`NSCompoundPredicate`对象。

```Objective-C
[[NSCompoundPredicate alloc] initWithType:NSAndPredicateType subpredicates:@[predicate1, predicate2]];
```

枚举值`NSCompoundPredicateType`参数，可以设置三种复合条件，枚举值非常直观很容易懂。

+ **NSNotPredicateType**
+ **NSAnddPredicateType**
+ **NSOrPredicateType**

###2.3 基础语法

下面是列举的一些`NSPredicate`的基础语法，这些语法看起来非常容易理解，**更复杂的用法可以去看苹果的官方API**。
| 语法 | 作用 |
| :-: | :-: |
|==|判断是否相等|
|>=|大于或等于|
|<=|小于或等于|
|>|大于|
|<|小于|
|!=|不等于|
|AND 或 &&|和|
|OR 或 \|\||或|
|NOT 或 !|非|

###2.4 正则表达式

`NSPredicate`中还可以使用**正则表达式**，可以通过正则表达式完成一些复杂需求，这使得谓语的功能更加强大，例如下面是一个手机号验证的正则表达式。

```Objective-C
NSString	*mobile	=	@"^1(3[0-9]|5[0-35-9]|8[025-9])\\d{8}$";
NSPredicate	*regexmobile	=	[NSPredicate	predicateWithFormat:@"SELF	MATCHES	%@",
mobile];
```

###2.5 模糊查询

`NSPredicate`支持对数据的模糊查询，例如下面使用通配符来**匹配包含lxz的结果**，具体`CoreData`中的使用在下面会讲到。

```Objective-C
[NSPredicate predicateWithFormat:@"name LIKE %@", @"*lxz*"];
```

###2.6 KeyPath

`NSPredicate`在创建查询条件时，还支持设置被匹配目标的`keyPath`，也就是**设置更深层被匹配的目标**。例如下面设置`employee`的`name`属性为查找条件，就是用点语法设置的`keyPath`。

```Objective-C
[NSPredicate predicateWithFormat:@"employee.name = %@", @"lxz"];
```






