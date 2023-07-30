<center><font size="5"><b>Objective-C 完整代码</b></font></center>

```objc
#import "ViewController.h"

@interface ViewController ()

@property (nonatomic, strong) UILabel *centerLabel;
@property (nonatomic, strong) UILabel *leftTopLabel;
@property (nonatomic, strong) UILabel *rightTopLabel;
@property (nonatomic, strong) UILabel *leftBottomLabel;
@property (nonatomic, strong) UILabel *rightBottomLabel;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self.view addSubview:self.centerLabel];
    [self.view addSubview:self.leftTopLabel];
    [self.view addSubview:self.rightTopLabel];
    [self.view addSubview:self.leftBottomLabel];
    [self.view addSubview:self.rightBottomLabel];
    
    [self updateViewsFrame];
}

- (UIInterfaceOrientationMask)supportedInterfaceOrientations {
    return UIInterfaceOrientationMaskPortrait | UIInterfaceOrientationMaskLandscapeLeft;
}

- (void)viewDidLayoutSubviews {
    [self updateViewsFrame];
}

- (void)updateViewsFrame {
    CGSize size = self.view.frame.size;
    self.centerLabel.frame = CGRectMake((size.width - 80) / 2, (size.height - 21) / 2, 80, 21);
    self.leftTopLabel.frame = CGRectMake(16, 16, 80, 21);
    self.rightTopLabel.frame = CGRectMake(size.width - 80 - 16, 16, 80, 21);
    self.leftBottomLabel.frame = CGRectMake(16, size.height - 21 - 16, 100, 21);
    self.rightBottomLabel.frame = CGRectMake(size.width - 100 - 16, size.height - 21 - 16, 100, 21);
}

#pragma mark - 懒加载

- (UILabel *)centerLabel {
    if (!_centerLabel) {
        _centerLabel = [UILabel new];
        _centerLabel.text = @"Center";
        _centerLabel.textAlignment = NSTextAlignmentCenter;
    }
    return _centerLabel;
}

- (UILabel *)leftTopLabel {
    if (!_leftTopLabel) {
        _leftTopLabel = [UILabel new];
        _leftTopLabel.text = @"LeftTop";
        _leftTopLabel.textAlignment = NSTextAlignmentLeft;
    }
    return _leftTopLabel;
}

- (UILabel *)rightTopLabel {
    if (!_rightTopLabel) {
        _rightTopLabel = [UILabel new];
        _rightTopLabel.text = @"RightTop";
        _rightTopLabel.textAlignment = NSTextAlignmentRight;
    }
    return _rightTopLabel;
}

- (UILabel *)leftBottomLabel {
    if (!_leftBottomLabel) {
        _leftBottomLabel = [UILabel new];
        _leftBottomLabel.text = @"LeftBottom";
        _leftBottomLabel.textAlignment = NSTextAlignmentLeft;
    }
    return _leftBottomLabel;
}

- (UILabel *)rightBottomLabel {
    if (!_rightBottomLabel) {
        _rightBottomLabel = [UILabel new];
        _rightBottomLabel.text = @"RightBottom";
        _rightBottomLabel.textAlignment = NSTextAlignmentRight;
    }
    return _rightBottomLabel;
}

@end

```

