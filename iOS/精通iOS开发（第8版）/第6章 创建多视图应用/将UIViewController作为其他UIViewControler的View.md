<center><font size="5"><b>将UIViewController作为其他UIViewControler的View</b></font></center>

可以将一个 `UIViewController` 的控制权交给其他 `UIViewController`， 具体方法如下。

1. 通过 `UIViewController` 的 `addChildViewController` 方法添加其他 `UIViewController` 。
2. 将要添加的 `UIViewController` 的 `view` 通过 `insertSubview` 方法插入到 `UIViewController` 中。
3. 调用将要添加的 `UIViewController` 的 `didMove` 方法通知即将到来的视图控制器，它已经作为子控制器添加到了其他控制器下。

```swift
private func switchViewController(from fromVC: UIViewController?, to toVC: UIViewController?) {
    if fromVC != nil {
        fromVC!.willMove(toParent: nil)
        fromVC!.view.removeFromSuperview()
        fromVC!.removeFromParent()
    }
    if toVC != nil {
        self.addChild(toVC!)
        self.view.insertSubview(toVC!.view, at: 0)
        toVC!.didMove(toParent: self)
    }
}
```



