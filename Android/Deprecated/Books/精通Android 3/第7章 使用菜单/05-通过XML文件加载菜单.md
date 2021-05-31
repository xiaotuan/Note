[toc]

使用 XML 创建菜单的方法具有多种优势，比如能够命名菜单、自动排序菜单、提供菜单 ID 等。也可以实现菜单文本的本地化。

执行以下步骤来使用基于 XML 的菜单。

（1）定义一个包含菜单标记的 XML 文件。

（2）将文件放在 /res/menu 子目录下。文件的名称可以任意指定，也可以创建任意多个文件。Android 会为此菜单文件自动生成资源 ID。

（3）使用菜单文件的资源 ID，将该 XML 文件加载到菜单中。

（4）使用为每个菜单项生成的资源 ID 来响应菜单项。

### 1. XML 菜单资源文件的结构

所有菜单文件都已相同的高级 menu 标记开始，后跟一系列 group 标记。每个 group 标记对应本章开头介绍的菜单项组。可以使用 @+id 方法为组指定 ID。每个菜单组将包含一系列菜单项，菜单项 ID 与符号名称绑定。

**代码清单7-20** 包含菜单定义的 XML 文件

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android">
	<!-- This group uses the default category. -->
    <group android:id="@+id/menuGroup_Main">
    	<item android:id="@+id/menu_testPick"
              android:orderInCategory="5"
              android:title="Test Pick" />
        <item android:id="@+id/menu_testGetContent"
              android:orderInCategory="5"
              android:title="Test Get Content" />
        <item android:id="@+id/menu_clear"
              android:orderInCategory="10"
              android:title="clear" />
        <item android:id="@+id/menu_dial"
              android:orderInCategory="7"
              android:title="dial" />
        <item android:id="@+id/menu_test"
              android:orderInCategory="4"
              android:title="@string/test" />
        <item android:id="@+id/menu_show_browser"
              android:orderInCategory="5"
              android:title="show_browser" />
    </group>
</menu>
```

### 2. 填充 XML 菜单资源文件

我们假设此 XML 文件名为 my_menu.xml。需要将此文件放在 /res/menu 子目录下，这会自动生成资源 ID R.menu.my_menu。

现在看一下如何使用此菜单资源 ID 来填充选项菜单。Android 提供了 android.view.MenuInflater 类，从 XML 文件填充 Menu 对象。我们将通过此 MenuInflater 类的实例，使用 R.menu.my_menu 资源 ID 来填充菜单对象：

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

跟以前一样，在 onOptionsItemSelected 回调方法中处理菜单项。更具体来讲，对于 XML 菜单，无需为这些 ID 定义常量，无需担心它们的唯一性，因为资源 ID 的生成保证唯一性。

```java
private void onOptionsItemSelected(MenuItem item) {
    this.appendMenuItemText(item);
    if (item.getItemId() == R.id.menu_clear) {
        this.emptyText();
    } else if (item.getItemId() == R.id.menu_dial) {
        // do something
    } else if (item.getItemId() == R.id.menu_testPick) {
        // do something
    } else if (item.getItemId() == R.id.menu_testGetContent) {
        // do something
    } else if (item.getItemId() == R.id.menu_show_browser) {
        // do something
    }
    ...etc
}
```

### 4. 其他 XML 菜单标记简介

#### 4.1 组类别标记

在 XML 文件中，可以使用 menuCategory 标记指定组的类别：

```xml
<group android:id="@+id/some_group_id"
       android:menuCategory="secondary">
</group>
```

#### 4.2 可选择行为标记

可以使用 checkableBehavior 标记在组级别控制可选择行为：

```xml
<group android:id="@+id/noncheckable_group"
       android:checkableBehavior="none" />
```

可以使用 checked 标记在菜单级别控制可选择行为：

```xml
<item android:id=".."
      android:title="..."
      android:checked="true" />
```

#### 4.3 模拟子菜单的标记

子菜单使用菜单项下的 menu 元素来表示：

```xml
<item android:title="All without group">
	<menu>
    	<item>
        </item>
    </menu>
</item>
```

#### 4.4 菜单图标标记

可以使用 icon 标记将图像与菜单项关联：

```xml
<item android:id=".."
      android:icon="@drawable/some-file" />
```

#### 4.5 菜单启用/禁用标记

可以使用 enabled 标记启用和禁用菜单项：

```xml
<item android:id=".."
      android:enabled="true"
      android:icon="@drawable/some-file" />
```

#### 4.6 菜单项快捷键

可以使用 alphabeticShortcut 标记为菜单项设置快捷键：

```xml
<item android:id="..."
      android:alphabeticShortcut="a" />
```

#### 4.7 菜单可见性

可以使用 visible 标记控制菜单项的可见性：

```xml
<item android:id="..."
      android:visible="true">
</item>
```

