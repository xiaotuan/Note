<center><font size="5"><b>Objective-C 完整代码</b></font></center>

```objc
#import "ViewController.h"

#define STATUSHEIGHT [ViewController isLiuHaiScreen] ? 44 : 24

@interface ViewController ()

@property (nonatomic, strong) UILabel *tipLabel;
@property (nonatomic, strong) UIButton *leftBtn;
@property (nonatomic, strong) UIButton *rightBtn;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self.view addSubview:self.tipLabel];
    [self.view addSubview:self.leftBtn];
    [self.view addSubview:self.rightBtn];
    
    [self updateViewsFrame];
}

- (void)updateViewsFrame {
    CGSize size = self.view.frame.size;
    [self.tipLabel setFrame:CGRectMake(16, STATUSHEIGHT + 32, size.width - 16 * 2, 21)];
    [self.leftBtn setFrame:CGRectMake(16, (size.height - 30) / 2, 48, 30)];
    [self.rightBtn setFrame:CGRectMake(size.width - 16 - 48, (size.height - 30) / 2, 48, 30)];
}

+ (BOOL)isLiuHaiScreen {
    if ([UIScreen instanceMethodForSelector:@selector(currentMode)]) {
        CGSize size = [[UIScreen mainScreen] currentMode].size;
        if (!((size.width == 320 && size.height == 480)
              || (size.width == 640 && size.height == 960)
              || (size.width = 640 && size.height == 1136)
              || (size.width == 750 && size.height == 1334)
              || (size.width == 1080 && size.height == 1920)
              || (size.width == 1242 && size.height == 2208))) {
            return YES;
        }
    }
    return NO;
}

- (void)buttonClick:(UIButton *)sender {
    NSString *title = [sender titleForState:UIControlStateNormal];
    NSString *text = [NSString stringWithFormat:@"%@ button pressed", title];
    NSMutableAttributedString *styledText = [[NSMutableAttributedString alloc] initWithString:text];
    NSDictionary *attrs = @{NSFontAttributeName: [UIFont boldSystemFontOfSize:self.tipLabel.font.pointSize]};
    NSRange range = [text rangeOfString:title];
    [styledText setAttributes:attrs range:range];
    [self.tipLabel setAttributedText:styledText];
}

#pragma mark - 懒加载
- (UILabel *)tipLabel {
    if (!_tipLabel) {
        _tipLabel = [[UILabel alloc] init];
        _tipLabel.textAlignment = NSTextAlignmentCenter;
    }
    return _tipLabel;
}

- (UIButton *)leftBtn {
    if (!_leftBtn) {
        _leftBtn = [UIButton buttonWithType:UIButtonTypeSystem];
        [_leftBtn setTitle:@"Left" forState:UIControlStateNormal];
        [_leftBtn addTarget:self action:@selector(buttonClick:) forControlEvents:UIControlEventTouchUpInside];
    }
    return _leftBtn;
}

- (UIButton *)rightBtn {
    if (!_rightBtn) {
        _rightBtn = [UIButton buttonWithType:UIButtonTypeSystem];
        [_rightBtn setTitle:@"Right" forState:UIControlStateNormal];
        [_rightBtn addTarget:self action:@selector(buttonClick:) forControlEvents:UIControlEventTouchUpInside];
    }
    return _rightBtn;
}

@end
```

