# CoreData使用报重复文件错误



**报错介绍：**

我在使用`Xcode -> Editor -> Create NSManagedObject Subclass`创建`CoreData`的托管对象类后，直接运行代码，报重复文件错误。

**错误日志如下：**
```
Showing Recent Messages
Multiple commands produce '/Users/qintuanye/Library/Developer/Xcode/DerivedData/CoreDataTest-gaftovrlnvryondpxzjmfeloqmds/Build/Intermediates.noindex/CoreDataTest.build/Debug-iphonesimulator/CoreDataTest.build/Objects-normal/x86_64/Person+CoreDataClass.o':
1) Target 'CoreDataTest' (project 'CoreDataTest') has compile command with input '/Users/qintuanye/Documents/GitSpace/GitHub/CoreDataTest/CoreDataTest/Person+CoreDataClass.m'
2) Target 'CoreDataTest' (project 'CoreDataTest') has compile command with input '/Users/qintuanye/Library/Developer/Xcode/DerivedData/CoreDataTest-gaftovrlnvryondpxzjmfeloqmds/Build/Intermediates.noindex/CoreDataTest.build/Debug-iphonesimulator/CoreDataTest.build/DerivedSources/CoreDataGenerated/CoreDataTest/Person+CoreDataClass.m'
```

**问题分析：**
通过查看错误日志，发现是出现了重复的文件导致的，重复的文件就是刚才自动生成的文件。通过查看项目的`Build Phases -> Compile Sources`文件后发现并没有重复的`.m`文件。将生成的`.m`文件从`Compile Sources`中删除后可以编译通过。再次加入后编译还是报同样的问题。 而从`Complie Sources`中删除自动生成的`CoreData`的`.m`文件后，在项目中却可以正常使用这些`.m`文件中的类，因此，可能`CoreData`会在其他地方自动将这些类添加到编译中去，不需要在`Complie Sources`中添加这些文件。

**解决办法：**
将自动生成的`.m`文件从`Complie Sources`中删除即可。