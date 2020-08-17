我们知道可以通过UIScreen.main.bounds来获取屏幕的尺寸，但是这个尺寸不是屏幕的真实分辨率，如果需要获取屏幕的真实分辨率，可以通过以下方法进行获取：
Objective-C版本：

```objectivec
CGSize screenSize = [UIScreen instancesRespondToSelector:@selector(currentMode)] ? [[UIScreen mainScreen] currentMode].size : null;
```

Swift版本：

```bash
let screenSize = UIScreen.instancesRespond(to: #selector(getter: UIScreen.main.currentMode)) ? UIScreen.main.currentMode?.size : nil
```

