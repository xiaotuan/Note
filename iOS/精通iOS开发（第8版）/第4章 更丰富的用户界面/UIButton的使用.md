<center><font size="5"><b>UIButton 的使用</b></font></center>

```swift
var btn: UIButton = {
    let btn = UIButton(type: UIButton.ButtonType.custom)
    btn.setTitle("Do Something", for: UIControl.State.normal)
    btn.setBackgroundImage(UIImage(named: "whiteButton"), for: .normal)
    btn.setBackgroundImage(UIImage(named: "blueButton"), for: .highlighted)
    btn.isHidden = true
    btn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIControl.Event.touchUpInside)
    return btn
}()

@objc func buttonClick(sender: UIButton) {
    // TODO: Button click
}
```

