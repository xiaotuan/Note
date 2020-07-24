<center><font size="5"><b>UISlider 的使用</b></font></center>

```swift
var slider: UISlider = {
    let slider = UISlider()
    slider.minimumValue = 0
    slider.maximumValue = 100
    slider.value = 50
    slider.addTarget(self, action: #selector(sliderValueChange(sender:)), for: UIControl.Event.valueChanged)
    return slider
}()

@objc func sliderValueChange(sender: UISlider) {
    self.sliderLabel.text = String(Int(sender.value))
}
```

