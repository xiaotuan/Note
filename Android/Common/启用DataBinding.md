<center>
  <font size="5">
  	<b>启用DataBinding</b>
  </font>
</center>

要想在项目中启用DataBinding功能，需要在app目录下的build.gradle文件中添加如下代码：

```
android {
	......
	dataBinding {
		enabled = true
	}
}
```

