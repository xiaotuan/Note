关于扩展 `Android` 提供的样式，需要注意：以前使用前缀的方法不适用于 `Android` 提供的样式。相反，必须使用 style 标记的父特性，比如：

```xml
<style name="CustomTextAppearance" parent="@android:style/TextAppearance">
	<item ... your extensions go here ... />
</style>
```

