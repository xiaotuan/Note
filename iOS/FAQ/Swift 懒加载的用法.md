<center><font size="5"><b>Swift 懒加载的用法</b></font></center>

`Swift` 懒加载用法如下：

```swift
var tipLabel: UILabel = {
    let label = UILabel()
    label.textAlignment = .center;
    return label
}()
```