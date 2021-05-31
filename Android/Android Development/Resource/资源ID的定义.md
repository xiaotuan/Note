当使用 `@id/text1` 方式定义 ID 时，如果这个 ID 以前没有定义过，则编译会报错。

```xml
<TextView android:id="@id/text1"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:text="@string/hell" />
```

当使用 `@+id/text1` 方式定义 ID 时，如果这个 ID 以前没有定义过，则会创建该 ID。

```xml
<TextView android:id="@+id/text1"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:text="@string/hell" />
```

也可以在 ID 资源文件中预先定义资源 ID，ID 资源文件放在 `/res/values` 子目录下。

**ID 资源文件示例**

```xml
<?xml version"1.0" encoding="utf-8" ?>
<resources>
	<item type="id" name="text" />
</resources>
```

