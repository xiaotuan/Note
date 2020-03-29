<center><font size="5"><b>关于设置UITextField代理报错问题</b></font></center>

使用懒加载方式初始化 `UITextField` 时， 如果在初始化的地方设置代理将会报错。

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    var nameTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Type in a name"
        textField.borderStyle = .roundedRect
        textField.returnKeyType = .done
      	textField.delegate = self
        return textField
    }()
  
}
```

因此需要将设置代理的代码移出初始化代码块

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    var nameTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Type in a name"
        textField.borderStyle = .roundedRect
        textField.returnKeyType = .done
        return textField
    }()
  
  	override func viewDidLoad() {
        super.viewDidLoad()
        self.nameTextField.delegate = self
    }
}
```

> 经测试发现，在懒加载初始化代码中使用 `self` 可能会出现问题，因此尽量不要在懒加载中引用 `self` 及其方法。