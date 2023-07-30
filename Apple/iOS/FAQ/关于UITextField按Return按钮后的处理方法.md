<center><font size="5"><b>关于UITextField按Return按钮后的处理方法</b></font></center>

如果希望在用户按下键盘的 <kbd>return</kbd> 后隐藏键盘，需要设置 `UITextField` 的代理，并实现 `textFieldShouldReturn(_ :)` 方法。

```swift
class ViewController: UIViewController, UITextFieldDelegate {
  
  override func viewDidLoad() {
        super.viewDidLoad()
        self.nameTextField.delegate = self
  }
  
  func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    textField.endEditing(true)
    return true
  }
}
```

> 注意：按 <kbd>return</kbd> 按钮后，不会触发代理的 `textFieldDidEndEditing(_ : )` 方法，只有结束编辑后才会调用比如 `textField.endEditing(true)` 。