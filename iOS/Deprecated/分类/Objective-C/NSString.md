<center><font size="5"><b>NSString</b></font></center>

**NSString+Extend.h**

```objective-c
#import <UIKit/UIKit.h>

@interface NSString (Extend)

/**
 * 根据字体计算字符串显示尺寸
 *
 * @param font  UIFont对象，用于显示该字符串的字体
 *
 * @return CGSize 返回字符串显示尺寸
 */
- (CGSize)sizeWithFont:(UIFont *)font;

/**
 * 根据字体计算字符串在指定显示宽度的情况下，需要的显示尺寸
 *
 * @param width     CGFloat 用于显示该字符串的最大宽度
 * @param font       UIFont 显示该字符串使用的字体
 * @param lineSpace     CGFloat 字符串的行间间距
 * @param lineBreakMode CGFloat 字符串截断方式
 * @return CGSize 返回字符串显示尺寸
 */
- (CGSize)sizeWithWidth:(CGFloat)width
                font:(UIFont *)font
            lineSpace:(CGFloat)lineSpace
          lineBreakMode:(CGFloat)lineBreakMode;

/**
 * 字符串是否包含中文
 *
 * @return 如果字符串包含中文，返回YES，否则返回NO
 */
- (BOOL)isContainChinese;

@end

```

**NSString+Extend.m**

```objective-c
#import "NSString+Extend.h"

@implementation NSString (Extend)

- (CGSize)sizeWithFont:(UIFont *)font {
    if (!font) {
        return CGSizeZero;
    }
    NSDictionary *attrs = @{NSFontAttributeName: font};
    return [self sizeWithAttributes:attrs];
}

- (CGSize)sizeWithWidth:(CGFloat)width
                   font:(UIFont *)font
              lineSpace:(CGFloat)lineSpace
          lineBreakMode:(CGFloat)lineBreakMode {
    if (self.length == 0 || !font) {
        return CGSizeZero;
    }
    NSMutableParagraphStyle *paraStyle = [[NSMutableParagraphStyle alloc] init];
    paraStyle.lineSpacing = lineSpace;
    paraStyle.lineBreakMode = lineBreakMode;
    NSMutableAttributedString *attributeString = [[NSMutableAttributedString alloc] initWithString:self attributes:@{NSParagraphStyleAttributeName: paraStyle, NSFontAttributeName: font}];
    CGRect rect = [attributeString boundingRectWithSize:CGSizeMake(width, 0) options:NSStringDrawingUsesLineFragmentOrigin | NSStringDrawingUsesFontLeading context:nil];
    if ((rect.size.height - font.lineHeight) <= lineSpace) {
        if ([self isContainChinese]) {
            rect.size.height -= lineSpace;
        }
    }
    return rect.size;
}

- (BOOL)isContainChinese {
    for (int i = 0; i < [self length]; i++) {
        int a = [self characterAtIndex:i];
        if (a > 0x4e00 && a < 0x9fff) {
            return YES;
        }
    }
    return NO;
}

@end
```

