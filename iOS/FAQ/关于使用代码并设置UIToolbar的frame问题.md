<center><font size="5"><b>关于使用代码并设置UIToolbar的frame问题</b></font></center>

在使用代码创建 `UIToolbar` 后，本以为该 `UIToolbar` 已经自带高度了，所以使用 `self.toolbar.frame.size.height` 做为高度来设置 `UIToolbar` 的 `frame`。编译时，`XCode` 报布局警告，界面没有显示 `UIToolbar` 的内容，经打日志发现 `UIToolbar` 没有高度。

```swift
class SwitchingViewController: UIViewController {
    
    var switchItem: UIBarButtonItem!
    var toolBar: UIToolbar!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.switchItem = UIBarButtonItem(title: "Switch Views", style: UIBarButtonItem.Style.plain, target: self, action: #selector(barButtonClick(sender:)))
        self.toolBar = UIToolbar()
        self.toolBar.setItems([self.switchItem], animated: true)
  
        self.view.addSubview(self.toolBar)

        self.toolBar.frame = CGRect(x: 0, y: self.view.frame.size.height - self.toolbar.frame.size.height, width: self.view.frame.width, height: toolbarHeight)
    }
	.....
}
```

通过指定 `UIToolbar` 的高度为 49 后显示正常，同时 `Xcode` 也没有再报警。

```swift
class SwitchingViewController: UIViewController {
    
    var switchItem: UIBarButtonItem!
    var toolBar: UIToolbar!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.switchItem = UIBarButtonItem(title: "Switch Views", style: UIBarButtonItem.Style.plain, target: self, action: #selector(barButtonClick(sender:)))
        self.toolBar = UIToolbar()
        self.toolBar.setItems([self.switchItem], animated: true)
        
      	let toolbarHeight: CGFloat = 49.0
        self.view.addSubview(self.toolBar)

        self.toolBar.frame = CGRect(x: 0, y: self.view.frame.size.height - toolbarHeight, width: self.view.frame.width, height: toolbarHeight)
    }
	.....
}
```

