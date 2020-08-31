Android SDK 附带了一个称为 Application Exerciser Monkey 的强大工具，简称为 `Monkey` 。它是一个命令行工具，能在设备上模拟触摸等随机用户事件以及系统事件。目的就是模拟用户的行为来对应用程序做压力测试。虽然 `Monkey` 不会为应用程序模拟一些经典的用例场景，但是在模拟应用程序如何处理一些非预期用户行为方面他会提供非常有用的反馈。

下面的命令对指定 `<package name>` 的应用程序执行 `Monkey`，还可以用 `<event count>` 参数指定随机事件数量。

```shell
$ adb shell monkey -p <package name> <event count>
```

**用 Monkeyrunner 编写 Monkey 脚本**

更高级的 `Monkey` 用法是使用 `Monkeyrunner API` 为应用程序编写 `Python` 脚本。这对在集成开发环境中执行 `Monkey` 工具和其他操作特别有用。它还能为按键提供输入，并且能用编程方式（同样使用 Monkeyrunner API）捕获屏幕截图，以便和一组已知的正确屏幕截图比较。

> 可在 http://developer.android.com/tools/help/monkeyrunner_concepts.html#APIClasses 上查看 Monkeyrunner API。