# CoreData: annotation: Failed to load optimized model

**一、问题来源**
使用XCode 9.x 编译运行项目时发现CoreData加载时报以下警告，但是不影响程序的正确执行。经过实验发现，如果iphone设备是ios11以下的系统时会报警告，推测ios11 sdk对CoreData做了优化，产生了*.omo优化模型。

**警告内容：**
```
CoreData: annotation: Failed to load optimized model at path '/var/containers/Bundle/Application/4A940130-0635-4810-9EB4-70020ABB232C/vpian.app/TestModel.momd/TestModel.omo'
```

**二、忽略警告内容**
针对ios11以下的设备在加载CoreData模型时指定加载*.mom路径

```Objective-C
NSURL *modelURL = [[NSBundle mainBundle] URLForResource:@"TestModel" withExtension:@"momd"];
 if(@available(iOS 11.0, *)) {} else {
    modelURL = [modelURL       URLByAppendingPathComponent:@"TestModel.mom"];
 }
```