<center><font size="5"><b>Object-C 完整代码</b></font></center>

```objc
#import "ViewController.h"

@interface ViewController () <UITextFieldDelegate>

@property (nonatomic, strong) UIImageView *logoView;
@property (nonatomic, strong) UILabel *nameLabel;
@property (nonatomic, strong) UITextField *nameTextField;
@property (nonatomic, strong) UILabel *numberLabel;
@property (nonatomic, strong) UITextField *numberTextField;
@property (nonatomic, strong) UILabel *sliderLabel;
@property (nonatomic, strong) UISlider *slider;
@property (nonatomic, strong) UISegmentedControl *segmentedControl;
@property (nonatomic, strong) UIButton *btn;
@property (nonatomic, strong) UISwitch *leftSwitch;
@property (nonatomic, strong) UISwitch *rightSwitch;
@property (nonatomic, strong) UITapGestureRecognizer *tapGesture;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor colorWithRed:254 / 255.0 green:195 / 255.0 blue:10 / 255.0 alpha:1.0];
    [self addViews];
    [self updateViewsFrame];
}

- (void)addViews {
    [self.view addGestureRecognizer:self.tapGesture];
    [self.view addSubview:self.logoView];
    [self.view addSubview:self.nameLabel];
    [self.view addSubview:self.nameTextField];
    [self.view addSubview:self.numberLabel];
    [self.view addSubview:self.numberTextField];
    [self.view addSubview:self.sliderLabel];
    [self.view addSubview:self.slider];
    [self.view addSubview:self.segmentedControl];
    [self.view addSubview:self.btn];
    [self.view addSubview:self.leftSwitch];
    [self.view addSubview:self.rightSwitch];
}

- (void)updateViewsFrame {
    CGSize size = self.view.frame.size;
    self.logoView.frame = CGRectMake((size.width - 172) / 2, 133, 172, 80);
    self.nameLabel.frame = CGRectMake(16, CGRectGetMaxY(self.logoView.frame) + 33, 80, 34);
    self.nameTextField.frame = CGRectMake(CGRectGetMaxX(self.nameLabel.frame) + 8, CGRectGetMaxY(self.logoView.frame) + 33, size.width - CGRectGetMaxX(self.nameLabel.frame) - 16 - 8, 34);
    self.numberLabel.frame = CGRectMake(16, CGRectGetMaxY(self.nameTextField.frame) + 33, 80, 34);
    self.numberTextField.frame = CGRectMake(CGRectGetMaxX(self.numberLabel.frame) + 8, CGRectGetMaxY(self.nameTextField.frame) + 33, size.width - CGRectGetMaxX(self.numberLabel.frame) - 8 - 16, 34);
    self.sliderLabel.frame = CGRectMake(16, CGRectGetMaxY(self.numberTextField.frame) + 33, 29, 31);
    self.slider.frame = CGRectMake(CGRectGetMaxX(self.sliderLabel.frame), CGRectGetMaxY(self.numberTextField.frame) + 33, size.width - CGRectGetMaxX(self.sliderLabel.frame) - 16, 31);
    self.segmentedControl.frame = CGRectMake((size.width - self.segmentedControl.frame.size.width) / 2, CGRectGetMaxY(self.slider.frame) + 33, self.segmentedControl.frame.size.width, self.segmentedControl.frame.size.height);
    self.btn.frame = CGRectMake(16, CGRectGetMaxY(self.segmentedControl.frame) + 33, size.width - 16 * 2, 31);
    self.leftSwitch.frame = CGRectMake(16, CGRectGetMaxY(self.segmentedControl.frame) + 33, self.leftSwitch.frame.size.width, self.leftSwitch.frame.size.height);
    self.rightSwitch.frame = CGRectMake(size.width - self.rightSwitch.frame.size.width - 16, CGRectGetMaxY(self.segmentedControl.frame) + 33, self.rightSwitch.frame.size.width, self.rightSwitch.frame.size.height);
}

- (void)sliderValueChange:(UISlider *)sender {
    self.sliderLabel.text = [NSString stringWithFormat:@"%d", (int)sender.value];
}

- (void)segmentedValueChange:(UISegmentedControl *)sender {
    [self.btn setHidden:sender.selectedSegmentIndex != 1];
    [self.leftSwitch setHidden:sender.selectedSegmentIndex != 0];
    [self.rightSwitch setHidden:sender.selectedSegmentIndex != 0];
}

- (void)switchValueChange:(UISwitch *)sender {
    [self.leftSwitch setOn:sender.on animated:YES];
    [self.rightSwitch setOn:sender.on animated:YES];
}

- (void)buttonClick:(UIButton *)sender {
    UIAlertController *controller = [UIAlertController alertControllerWithTitle:@"Are You Sure?" message:nil preferredStyle:UIAlertControllerStyleActionSheet];
    UIAlertAction *yesAction = [UIAlertAction actionWithTitle:@"Yes, I'm sure!" style:UIAlertActionStyleDestructive handler:^(UIAlertAction * _Nonnull action) {
        NSString *msg = [NSString stringWithFormat:@"You can breathe easy, everything went OK."];
        if (self.nameTextField.text.length > 0) {
            msg = [NSString stringWithFormat:@"You can breathe easy, %@, everything went OK.", self.nameTextField.text];
        }
        UIAlertController *controller2 = [UIAlertController alertControllerWithTitle:@"Something Was Done" message:msg preferredStyle:UIAlertControllerStyleAlert];
        UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:@"Phew!" style:UIAlertActionStyleCancel handler:nil];
        [controller2 addAction:cancelAction];
        [self presentViewController:controller2 animated:YES completion:nil];
    }];
    
    UIAlertAction *noAction = [UIAlertAction actionWithTitle:@"No way!" style:UIAlertActionStyleCancel handler:nil];
    
    [controller addAction:yesAction];
    [controller addAction:noAction];
    
    [self presentViewController:controller animated:YES completion:nil];
}

- (void)tapScreen:(UITapGestureRecognizer *)sender {
    [self.view endEditing:YES];
}

#pragma mark - UITextFieldDelegate

- (BOOL)textFieldShouldReturn:(UITextField *)textField {
    [textField resignFirstResponder];
    return true;
}

#pragma mark - 懒加载

- (UIImageView *)logoView {
    if (!_logoView) {
        _logoView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"apress_logo"]];
    }
    return _logoView;
}

- (UILabel *)nameLabel {
    if (!_nameLabel) {
        _nameLabel = [[UILabel alloc] init];
        _nameLabel.text = @"Name:";
        _nameLabel.textAlignment = NSTextAlignmentRight;
    }
    return _nameLabel;
}

- (UITextField *)nameTextField {
    if (!_nameTextField) {
        _nameTextField = [[UITextField alloc] init];
        _nameTextField.placeholder = @"Type in a name";
        _nameTextField.delegate = self;
        _nameTextField.returnKeyType = UIReturnKeyDone;
        _nameTextField.borderStyle = UITextBorderStyleRoundedRect;
    }
    return _nameTextField;
}

- (UILabel *)numberLabel {
    if (!_numberLabel) {
        _numberLabel = [UILabel new];
        _numberLabel.text = @"Number:";
        _numberLabel.textAlignment = NSTextAlignmentRight;
    }
    return _numberLabel;
}

- (UITextField *)numberTextField {
    if (!_numberTextField) {
        _numberTextField = [UITextField new];
        _numberTextField.placeholder = @"Type in a number";
        _numberTextField.delegate = self;
        _numberTextField.keyboardType = UIKeyboardTypeNumberPad;
        _numberTextField.borderStyle = UITextBorderStyleRoundedRect;
    }
    return _numberTextField;
}

- (UILabel *)sliderLabel {
    if (!_sliderLabel) {
        _sliderLabel = [UILabel new];
        _sliderLabel.text = @"50";
        _sliderLabel.textAlignment = NSTextAlignmentCenter;
    }
    return _sliderLabel;
}

- (UISlider *)slider {
    if (!_slider) {
        _slider = [UISlider new];
        _slider.maximumValue = 100;
        _slider.minimumValue = 0;
        _slider.value = 50;
        [_slider addTarget:self action:@selector(sliderValueChange:) forControlEvents:UIControlEventValueChanged];
    }
    return _slider;
}

- (UISegmentedControl *)segmentedControl {
    if (!_segmentedControl) {
        _segmentedControl = [[UISegmentedControl alloc] initWithItems:@[@"Switches", @"Button"]];
        _segmentedControl.selectedSegmentIndex = 0;
        [_segmentedControl addTarget:self action:@selector(segmentedValueChange:) forControlEvents:UIControlEventValueChanged];
    }
    return _segmentedControl;
}

- (UISwitch *)leftSwitch {
    if (!_leftSwitch) {
        _leftSwitch = [[UISwitch alloc] init];
        [_leftSwitch setOn:NO];
        [_leftSwitch addTarget:self action:@selector(switchValueChange:) forControlEvents:UIControlEventValueChanged];
    }
    return _leftSwitch;
}

- (UISwitch *)rightSwitch {
    if (!_rightSwitch) {
        _rightSwitch = [UISwitch new];
        [_rightSwitch setOn:NO];
        [_rightSwitch addTarget:self action:@selector(switchValueChange:) forControlEvents:UIControlEventValueChanged];
    }
    return _rightSwitch;
}

- (UIButton *)btn {
    if (!_btn) {
        _btn = [UIButton buttonWithType:UIButtonTypeSystem];
        [_btn setBackgroundImage:[UIImage imageNamed:@"whiteButton"] forState:UIControlStateNormal];
        [_btn setBackgroundImage:[UIImage imageNamed:@"blueButton"] forState:UIControlStateHighlighted];
        [_btn setHidden:YES];
        [_btn setTitle:@"Do Something" forState:UIControlStateNormal];
        [_btn addTarget:self action:@selector(buttonClick:) forControlEvents:UIControlEventTouchUpInside];
    }
    return _btn;
}

- (UITapGestureRecognizer *)tapGesture {
    if (!_tapGesture) {
        _tapGesture = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(tapScreen:)];
    }
    return _tapGesture;
}

@end

```

