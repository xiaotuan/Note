<center><font size="5"><b>UITextField的使用</b></font></center>

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    var nameLabe: UILabel = {
        let label = UILabel()
        label.text = "Name:"
        label.textAlignment = .right
        return label
    }()
    
    var nameTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Type in a name"
        textField.borderStyle = .roundedRect
        textField.returnKeyType = .done
        return textField
    }()
  
  override func viewDidLoad() {
    super.viewDidLoad()
    self.numberTextField.delegate = self
   }

  func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    textField.resignFirstResponder()
    return true
  }
  
}
```

