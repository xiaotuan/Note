<center><font size="5"><b>Swift 定义类的静态变量</b></font></center>

`Swift` 定义类的静态变量是在变量定义的前面加 `static` 修饰符，例如：

```swift
class ViewController: UIViewController {
    
    static let statusHeight: CGFloat = {
        return isLiuHaiScreen() ? 44 : 24;
    }()
    
}
```