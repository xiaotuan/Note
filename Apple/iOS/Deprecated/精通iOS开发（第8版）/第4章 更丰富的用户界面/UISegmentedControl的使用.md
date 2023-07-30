<center><font size="5"><b>UISegmentedControl 的使用</b></font></center>

```swift
var segmentedControl: UISegmentedControl = {
    let control = UISegmentedControl(items: ["Switches", "Button"])
    control.selectedSegmentIndex = 0
    control.addTarget(self, action: #selector(segmentedValueChanged(sender:)), for: UIControl.Event.valueChanged)
    return control
}()

@objc func segmentedValueChanged(sender: UISegmentedControl) {
    self.btn.isHidden = sender.selectedSegmentIndex != 1
    self.leftSwitch.isHidden = sender.selectedSegmentIndex != 0
    self.rightSwitch.isHidden = sender.selectedSegmentIndex != 0
}
```

