我们知道，如果UILabel、UITextField、UIButton等控件的文本过长，将会导致文本内容显示不全。如果需要在不改变控件宽度的情况下，显示全部的文本内容，可以设置控件的如下属性：

```bash
textField?.adjustsFontSizeToFitWidth = true
```

