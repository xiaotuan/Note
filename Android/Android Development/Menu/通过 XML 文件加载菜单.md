[toc]

### 1. XML 菜单资源文件的结构

所有菜单文件都以相同的高级 `menu` 标记开始，后跟一系列 `group` 标记。每个 `group` 标记对应本章开头介绍的菜单项组。可以使用 `@+id` 方法为组指定 ID。每个菜单组将包含一系列菜单项，菜单项 ID 与符号名称绑定。

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- This group uses the default category. -->
    <group android:id="@+id/menuGroup_Main">

        <item
            android:id="@+id/menu_basic_view"
            android:title="Invoke BasicView" />

        <item
            android:id="@+id/menu_show_browser"
            android:title="show browser" />

        <item
            android:id="@+id/menu_search"
            android:title="search" />

    </group>

</menu>
```

### 2. 填充 XML 菜单资源文件

XML 菜单资源文件需要放在 `/res/menu` 子目录下，这会自动生成资源 ID：`R.menu.my_menu`。Android 提供了 `android.view.MenuInflater` 类，从 XML 文件填充 Menu 对象。

**Kotlin**

```kotlin
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    menuInflater.inflate(R.menu.my_menu, menu)
    return true
}
```

**Java**

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    MenuInflater inflater = getMenuInflater();	// from activity
    inflater.inflate(R.menu.my_menu, menu);
  
  	// It is important to return true to see the menu
    return true;
}
```

### 3. 响应基于 XML 的菜单项

Android  在 `onOptionsItemSelected()` 回调方法中处理菜单项。

**Kotlin**

```kotlin
override fun onOptionsItemSelected(item: MenuItem): Boolean {
    when (item.itemId) {
        R.id.menu_clean -> {
          // TODO: do something
          return true
        }
        R.id.menu_dial -> {
          // TODO: do something
          return true
        }
    }
    return super.onOptionsItemSelected(item)
}
```

**Java**

```java
@Override
protected boolean onOptionsItemSelected(MenuItem item) {
    switch (item.getItemId()) {
      case R.id.menu_clear:
        // TODO: do something
        return true;
       
      case R.id.menu_dial:
        // TODO: do something
        return true;
    }
  	return super.onOptionsItemSelected(item);
}
```

### 3. 其他 XML 菜单标记简介

#### 3.1 组类别标记

在 XML 文件中，可以使用 `menuCategory` 标记指定组的类别：

```xml
<group android:id="@+id/some_group_id"
       android:menuCategory="secondary">
</group>
```

#### 3.2 可选择行为标记

可以使用 `checkableBehavior` 标记在组级别控制可选择行为：

```xml
<group android:id="@+id/noncheckable_group"
       android:checkableBehavior="none">
</group>
```

可以使用 `checked` 标记在菜单项级别控制可选择行为：

```xml
<item android:id="..."
      android:title="..."
      android:checked="true" />
```

#### 3.3 模拟子菜单

子菜单使用菜单项下的 `menu` 元素来表示：

```xml
<item android:title="All without group">
		<menu>
  			<item .../>
 		</menu>
</item>
```

#### 3.4 菜单图标标记

可以使用 `icon` 标记将图像与菜单项关联：

```xml
<item android:id="..."
      android:icon="@drawable/some-file" />
```

#### 3.5 菜单启用/禁用标记

可以使用 `enabled` 标记启动和禁用菜单项：

```xml
<item android:id="..."
      android:enabled="true"
      android:icon="@drawable/some-file" />
```

#### 3.6 菜单项快捷键

可以使用 `alphabeticShortcut` 标记为菜单项设置快捷键：

```xml
<item android:id="..."
      android:alphabeticShortcut="a" />
```

#### 3.7 菜单可见性

可以使用 `visible` 标记控制菜单项的可见性：

```xml
<item android:id="..."
      android:visible="true" />
```

