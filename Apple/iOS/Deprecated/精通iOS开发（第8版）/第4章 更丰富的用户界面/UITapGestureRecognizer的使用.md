<center><font size="5"><b>UITapGestureRecognizer的使用</b></font></center>

```swift
var gesture: UITapGestureRecognizer!

    override func viewDidLoad() {
      super.viewDidLoad()
      self.gesture = UITapGestureRecognizer(target: self, action: #selector(tap(sender:)))
			self.view.addGestureRecognizer(self.gesture)
    }

	@objc func tap(sender: UITapGestureRecognizer) {
    self.view.endEditing(true)
  }

}
```

