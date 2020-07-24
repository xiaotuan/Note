<center><font size="5"><b>UISwitch 的使用</b></font></center>

```swift
var leftSwitch: UISwitch = {
    let s = UISwitch()
    s.setOn(true, animated: false)
    s.addTarget(self, action: #selector(switchValueChange(sender:)), for: UIControl.Event.valueChanged)
    return s
}()

@objc func switchValueChange(sender: UISwitch) {
    self.leftSwitch.setOn(sender.isOn, animated: true)
    self.rightSwitch.setOn(sender.isOn, animated: true)
}
```

