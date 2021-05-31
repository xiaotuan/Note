[toc]

菜单项使用 android.view.MenuItem 表示，子菜单使用 android.view.SubMenu 表示。菜单项还育有名称、菜单项 ID、排序和 ID。可以使用排序 ID 来指定菜单项在菜单中的顺序。

一些菜单排序数字范围保留给了某些类型的菜单。辅助菜单项没有其他菜单项重要，它们以 0x30000 开始且由常量 Menu.CATEGORY_SECONDARY 定义。系统菜单项以 0x20000 开始并由常量 Menu.CATEGORY_SYSTEM 定义。交替菜单项以 0x40000 开始并由常量 Menu.CATEGORY_ALTERNATIVE 定义。容器菜单项以 0x10000 开始并由常量 Menu.CATEGORY_CONTAINER 定义。

### 1. 创建菜单

在 Android SDK 中，无需从头创建菜单对象。因为一个活动只与一个菜单关联，所以 Android 会为该活动创建此菜单，然后将它传递给 Activity 类的 onCreateOptionsMenu 回调。

**代码清单7-1** onCreateOptionMenu 方法的签名

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    // populate menu items
    ...
    return true;
}
```

填充菜单项之后，这段代码应该返回 true，使菜单可见。如果此方法返回 false，那么菜单将不可见。

**代码清单7-2** 添加菜单项

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    // call the base class to include system menus
    super.onCreateOptionsMenu(menu);
    
    menu.add(0	// Group
            , 1	// item id
            , 0	// order
            , "append");	// title
    menu.add(0, 2, 1, "item2");
    menu.add(0, 3, 2, "clear");
    
    // It is important to return true to see the menu
    return true;
}
```

组 ID、菜单项 ID 和排序 ID 都是可选的，如果不希望指定任何 ID ，可以使用 Menu.NONE。

### 2. 使用菜单组

**代码清单7-3** 使用组ID创建菜单组

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    // Group 1
    int group1 = 1;
    menu.add(group1, 1, 1, "g1.item1");
    menu.add(group1, 2, 2, "g1.item2");
    
    // Group 2
    int group2 = 2;
    menu.add(group2, 3, 3, "g2.item1");
    menu.add(group2, 4, 4, "g2.item2");
    
    return true;	// It is important to return true
}
```

请注意，菜单项 ID 和排序 ID 与组是独立的。那么组有何用呢？Android 提供了一些基于组 ID 的 android.view.Menu 类的方法。可以使用这些方法操作组中的菜单项：

```java
removeGroup(id)
setGroupCheckable(id, checkable, exclusive)
setGroupEnabled(id, boolean enabled)
setGroupVisible(id, visible)
```

setGroupCheckable 比较有趣。可以使用此方法在选中菜单项时在菜单项中显示一个勾选标记。当应用到组中时，它将为该组中的所有菜单项启用此功能。如果设置了此方法的独占标志 exclusive，那么只允许该组中的一个菜单项处于勾选状态。其他菜单项将保持未选择状态。