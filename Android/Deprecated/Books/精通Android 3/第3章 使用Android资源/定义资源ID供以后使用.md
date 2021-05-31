分配 id 的一般模式可以是创建一个新 id，或者使用 Android 包创建的 id。但也可以预先创建 id，以后再在你自己的包中使用它们。

**代码清单3-8** 预定义一个ID

```xml
<resources>
    <item type="id" name="text" />
</resources>
```

**代码清单3-9** 重用预定义 ID

```xml
<TextView android:id="@id/text">
...
</TextView>
```

