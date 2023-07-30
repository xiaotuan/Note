<center><font size="5"><b>Swift 定义类方法</b></font></center>

Swift 定义类方法是在方法的前面加 `class` 修饰符，例如：

```swift
class ViewController: UIViewController {

    class func isLiuHaiScreen() -> Bool {
        let screenSize = UIScreen.instancesRespond(to: #selector(getter: UIScreen.main.currentMode)) ? UIScreen.main.currentMode?.size : nil
        if let size = screenSize {
            if !((size.width == 320 && size.height == 480)
                && (size.width == 640 && size.height == 960)
                && (size.width == 640 && size.height == 1136)
                && (size.width == 750 && size.height == 1334)
                && (size.width == 1080 && size.height == 1920)
                && (size.width == 1242 && size.height == 2208)) {
                return true
            }
        }
        return false
    }
    
}
```