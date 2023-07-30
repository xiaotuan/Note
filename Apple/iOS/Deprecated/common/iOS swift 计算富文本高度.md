下面是计算富文本高度的代码，其中with的值为用于显示该富文本的控件的宽度和Float的最大值构建的CGSize变量，使用ceil方法去掉高度中的小数部分，也可以使用floor方法获取最大的整数值。

```objectivec
// 计算富文本的高度
func heightOfAttributedString(_ attributedString: NSAttributedString) -> CGFloat {
    let height = attributedString.boundingRect(with: CGSize(width: UIScreen.main.bounds.size.width - 15 * 2, height: CGFloat(MAXFLOAT)), options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil).height
    return ceil(height)
}
```

