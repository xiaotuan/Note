<center><font size="5"><b>UIAlertController 的使用</b></font></center>

**ActionAlert**

```swift
let controller2 = UIAlertController(title: "Something Was Done", message: msg, preferredStyle: .alert)
let cancelAction = UIAlertAction(title: "Phew!", style: .cancel, handler: nil)
controller2.addAction(cancelAction)
self.present(cont
```

**ActionSheet**

```swift
let controller = UIAlertController(title: "Are You Sure?", message: nil, preferredStyle: .actionSheet)
let yesAction = UIAlertAction(title: "Yes, I'm sure!", style: .destructive) { (action) in
    let msg = self.nameTextField.text!.isEmpty ? "You can breathe easy, everything went OK." : "You can breathe easy,  \(self.nameTextField.text!), " + "everything went OK."
    let controller2 = UIAlertController(title: "Something Was Done", message: msg, preferredStyle: .alert)
    let cancelAction = UIAlertAction(title: "Phew!", style: .cancel, handler: nil)
    controller2.addAction(cancelAction)
    self.present(controller2, animated: true, completion: nil)
}

let noAction = UIAlertAction(title: "No way!", style: .cancel, handler: nil)

controller.addAction(yesAction)
controller.addAction(noAction)

present(controller, animated: true, completion: nil)
```

