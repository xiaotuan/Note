<center><font size="5"><b>Swift 中 selector 的写法</b></font></center>

在 `Swift` 中写法如下，以为 `UIButton` 添加点击事件处理方法为例：

```swift
self.leftBtn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIButton.Event.touchUpInside)

@objc func buttonClick(sender: UIButton) {
    // 处理代码
}
```

