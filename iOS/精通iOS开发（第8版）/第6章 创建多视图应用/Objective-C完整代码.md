<center><font size="5"><b>Objective-C 完整代码</b></font></center>

##### SwitchingViewController.m

```objc
#import "SwitchingViewController.h"
#import "BlueViewController.h"
#import "YellowViewController.h"

@interface SwitchingViewController ()

@property (nonatomic, strong) UIView *toolbarContainer;
@property (nonatomic, strong) UIToolbar *toolbar;
@property (nonatomic, strong) UIBarButtonItem *switchItem;
@property (nonatomic, strong) BlueViewController *blueController;
@property (nonatomic, strong) YellowViewController *yellowController;

@end

@implementation SwitchingViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    if ([SwitchingViewController isLiuHaiScreen]) {
        [self.toolbarContainer addSubview:self.toolbar];
        [self.view addSubview:self.toolbarContainer];
        self.toolbarContainer.frame = CGRectMake(0, self.view.frame.size.height - 49 - 39, self.view.frame.size.width, 49 + 39);
        self.toolbar.frame = CGRectMake(0, 0, self.toolbarContainer.frame.size.width, 49);
    } else {
        [self.view addSubview:self.toolbar];
        self.toolbar.frame = CGRectMake(0, self.view.frame.size.height - 49, self.view.frame.size.width, 49);
    }
    
    self.blueController.view.frame = self.view.frame;
    [self switchViewController:nil toVC:self.blueController];
}

- (void)didReceiveMemoryWarning {
    if (self.blueController != nil && self.blueController.view.superview == nil) {
        self.blueController = nil;
    }
    if (self.yellowController != nil && self.yellowController.view.superview == nil) {
        self.yellowController = nil;
    }
}

- (void)barItemClick:(UIBarButtonItem *)sender {
    __weak typeof(self) weakSelf = self;
    if (self.blueController != nil && self.blueController.view.superview != nil) {
        [UIView transitionWithView:self.view duration:0.4 options:UIViewAnimationOptionTransitionFlipFromRight | UIViewAnimationOptionCurveEaseInOut animations:^{
            weakSelf.yellowController.view.frame = self.view.frame;
            [weakSelf switchViewController:weakSelf.blueController toVC:weakSelf.yellowController];
        } completion:nil];
    } else {
        [UIView transitionWithView:self.view duration:0.4 options:UIViewAnimationOptionTransitionFlipFromRight | UIViewAnimationOptionCurveEaseInOut animations:^{
            weakSelf.blueController.view.frame = self.view.frame;
            [weakSelf switchViewController:weakSelf.yellowController toVC:weakSelf.blueController];
        } completion:nil];
    }
}

- (void)switchViewController:(UIViewController *)fromVC toVC:(UIViewController *)toVC {
    if (fromVC != nil) {
        [fromVC willMoveToParentViewController:nil];
        [fromVC.view removeFromSuperview];
        [fromVC removeFromParentViewController];
    }
    if (toVC != nil) {
        [self addChildViewController:toVC];
        [self.view insertSubview:toVC.view atIndex:0];
        [toVC didMoveToParentViewController:self];
    }
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

#pragma mark - 懒加载

- (UIBarButtonItem *)switchItem {
    if (!_switchItem) {
        _switchItem = [[UIBarButtonItem alloc] initWithTitle:@"Switch Views" style:UIBarButtonItemStylePlain target:self action:@selector(barItemClick:)];
    }
    return _switchItem;
}

- (UIToolbar *)toolbar {
    if (!_toolbar) {
        _toolbar = [[UIToolbar alloc] init];
        [_toolbar setItems:@[self.switchItem]];
    }
    return _toolbar;
}

- (UIView *)toolbarContainer {
    if (!_toolbarContainer) {
        _toolbarContainer = [UIView new];
        _toolbarContainer.backgroundColor = [UIColor colorWithRed:248 / 255.0 green:248 / 255.0 blue:248 / 255.0 alpha:1.0];
    }
    return _toolbarContainer;
}

- (BlueViewController *)blueController {
    if (!_blueController) {
        _blueController = [BlueViewController new];
    }
    return _blueController;
}

- (YellowViewController *)yellowController {
    if (!_yellowController) {
        _yellowController = [YellowViewController new];
    }
    return _yellowController;
}

@end
```

##### BlueViewController.m

```objc
#import "BlueViewController.h"

@interface BlueViewController ()

@property (nonatomic, strong) UIButton *button;

@end

@implementation BlueViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = UIColor.blueColor;
    [self.view addSubview:self.button];
    self.button.frame = CGRectMake((self.view.frame.size.width - 64) / 2, (self.view.frame.size.height - 30) / 2, 64, 30);
}

- (void)buttonClick:(UIButton *)sender {
    UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Blue View Button Pressed" message:@"You pressed the button on the blue view" preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *action = [UIAlertAction actionWithTitle:@"Yes, I did" style:UIAlertActionStyleDefault handler:nil];
    [alert addAction:action];
    [self presentViewController:alert animated:YES completion:nil];
}

#pragma mark - 懒加载

- (UIButton *)button {
    if (!_button) {
        _button = [UIButton buttonWithType:UIButtonTypeSystem];
        [_button setTitle:@"Press Me" forState:UIControlStateNormal];
        [_button addTarget:self action:@selector(buttonClick:) forControlEvents:UIControlEventTouchUpInside];
    }
    return _button;
}

@end
```

##### YellowViewController.m

```objc
#import "YellowViewController.h"

@interface YellowViewController ()

@property (nonatomic, strong) UIButton *button;

@end

@implementation YellowViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = UIColor.yellowColor;
    [self.view addSubview:self.button];
    self.button.frame = CGRectMake((self.view.frame.size.width - 97) / 2, (self.view.frame.size.height - 30) / 2, 97, 30);
}

- (void)buttonClick:(UIButton *)sender {
    UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Yellow View Button Pressed" message:@"You pressed the button on the yellow view" preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *action = [UIAlertAction actionWithTitle:@"Yes, I did" style:UIAlertActionStyleDefault handler:nil];
    [alert addAction:action];
    [self presentViewController:alert animated:YES completion:nil];
}

#pragma mark - 懒加载

- (UIButton *)button {
    if (!_button) {
        _button = [UIButton buttonWithType:UIButtonTypeSystem];
        [_button setTitle:@"Press Me, Too" forState:UIControlStateNormal];
        [_button addTarget:self action:@selector(buttonClick:) forControlEvents:UIControlEventTouchUpInside];
    }
    return _button;
}

@end
```

