<center><font size="5"><b>扩展 String 类</b></font></center>

> 注意：
>
> 1. 需要使用Character的扩展

```swift
extension String {
    
    /// 计算一行字符串在指定的字体下的尺寸
    ///
    /// - Parameters:
    ///   - font: 显示该字符串时使用的字体
    /// - Returns: 返回一行显示该字符串需要的尺寸（ CGSize ）
    public func size(font: UIFont) -> CGSize {
        let attributes = [NSAttributedString.Key.font : font]
        let size = NSString(string: self).size(withAttributes: attributes)
        return size
    }
    
    /// 计算字符串在指定宽度上需要多少高度的才能够完全显示该字符串
    ///
    /// - Parameters:
    ///   - width: 显示该字符串的最大宽度
    ///   - font: 显示该字符串时使用的字体
    ///   - lineBreakMode: 字符串的截断模式
    ///   - lineSpacing: 行间的间距
    /// - Returns: 返回在指定的宽度下，要显示完全该字符串需要的尺寸（ CGSize ）
    public func sizeWithAttrs(width: CGFloat, font: UIFont, lineBreakMode: NSLineBreakMode, lineSpacing: CGFloat) -> CGSize {
        let str = NSString(string: self)
        if (str.length == 0) {
            return CGSize.zero
        }
        let paraStyle = NSMutableParagraphStyle()
        paraStyle.lineSpacing = lineSpacing
        paraStyle.lineBreakMode = lineBreakMode
        let attr = NSMutableAttributedString(string: self, attributes: [NSAttributedString.Key.paragraphStyle: paraStyle, NSAttributedString.Key.font: font])

        var rect = attr.boundingRect(with: CGSize(width: width, height: CGFloat(MAXFLOAT)), options: [NSStringDrawingOptions.usesLineFragmentOrigin, NSStringDrawingOptions.usesFontLeading], context: nil)

        if (rect.size.height - font.lineHeight) <= lineSpacing {
            if self.hasChineseCharacter() {
                rect.size.height -= lineSpacing
            }
        }
        return rect.size
    }
    
    /// 字符串是否包含中文字符
    ///
    /// - Returns: 如果字符串中包含中文字符，返回true；否则返回false
    public func hasChineseCharacter() -> Bool {
        for s in self {
            let number = s.intValue()
            print("number: \(number)")
            if number > 0x4e00 && number < 0x9fff {
                return true
            }
        }
        return false
    }

}
```

