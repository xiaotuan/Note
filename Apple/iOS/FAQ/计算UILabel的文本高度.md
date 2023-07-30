<center><font size="5"><b>计算UILabel的文本高度</b></font></center>

**Swift版本：**

```swift
extension String {
    
    func sizeWithAttrs(width: CGFloat, font: UIFont, lineBreakMode: NSLineBreakMode, lineSpacing: CGFloat) -> CGSize {
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
    
    func hasChineseCharacter() -> Bool {
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

extension Character {
    
    func intValue() -> Int {
        var number = 0
        for scalar in String(self).unicodeScalars {
            number += Int(scalar.value)
        }
        return number
    }
}

```

