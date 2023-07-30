<center><font size="5"><b>关于UITapGestureRecognizer的一些问题</b></font></center>

使用懒加载初始化 `UITapGestureRecognizer` ，然后在 `viewDidLoad` 方法中将其添加到 `view` 中，运行后发现点击 `view` 没有触发事件。

```swift
var gesture: UITapGestureRecognizer = {
 	let gesture = UITapGestureRecognizer(target: self, action: #selector(tap(sender:)))
  return gesture
}{}

override func viewDidLoad() {
  super.viewDidLoad()
	self.view.addGestureRecognizer(self.gesture)
}
```

如果把 `UITapGestureRecognizer` 移至 `viewDidLoad` 方法中初始化，`view` 就可以接收到点击事件。

```swift
var gesture: UITapGestureRecognizer!

override func viewDidLoad() {
  super.viewDidLoad()
  self.gesture = UITapGestureRecognizer(target: self, action: #selector(tap(sender:)))
  self.view.addGestureRecognizer(self.gesture)
}
```

