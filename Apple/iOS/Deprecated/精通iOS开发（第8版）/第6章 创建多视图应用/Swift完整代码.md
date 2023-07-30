<center><font size="5"><b>Swift 完整代码</b></font></center>

[toc]

#####SwitchViewController.swift

```swift
import UIKit

class SwitchingViewController: UIViewController {
    
    private var switchItem: UIBarButtonItem!
    private var toolBar: UIToolbar!
    private var blueViewController: BlueViewController!
    private var yellowViewController: YellowViewController!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.switchItem = UIBarButtonItem(title: "Switch Views", style: UIBarButtonItem.Style.plain, target: self, action: #selector(barButtonClick(sender:)))
        self.toolBar = UIToolbar()
        self.toolBar.setItems([self.switchItem], animated: true)
        
        let toolbarHeight: CGFloat = 49.0
        if (SwitchingViewController.isLiuHaiScreen()) {
            let view = UIView()
            
            view.addSubview(self.toolBar)
            view.backgroundColor = UIColor(red: 248 / 255.0, green: 248 / 255.0, blue: 248 / 255.0, alpha: 1.0)
            self.view.addSubview(view)
            view.frame = CGRect(x: 0, y: self.view.frame.size.height - toolbarHeight - 39, width: self.view.frame.size.width, height: toolbarHeight + 39)
            self.toolBar.frame = CGRect(x: 0, y: 0, width: view.frame.width, height: toolbarHeight)
        } else {
            self.view.addSubview(self.toolBar)
            
            self.toolBar.frame = CGRect(x: 0, y: self.view.frame.size.height - toolbarHeight, width: self.view.frame.width, height: toolbarHeight)
        }
        
        self.blueViewController = BlueViewController()
        self.blueViewController.view.frame = self.view.frame
        switchViewController(from: nil, to: blueViewController)
    }
    
    override func didReceiveMemoryWarning() {
        if blueViewController != nil && blueViewController.view.superview == nil {
            blueViewController = nil
        }
        if yellowViewController != nil && yellowViewController.view.superview == nil {
            yellowViewController = nil
        }
    }

    @objc func barButtonClick(sender: UIBarButtonItem) {
        // Create the new view controller, if required
        if self.yellowViewController?.view.superview == nil {
            if self.yellowViewController == nil {
                self.yellowViewController = YellowViewController()
            }
        } else if self.blueViewController?.view.superview == nil {
            if self.blueViewController == nil {
                self.blueViewController = BlueViewController()
            }
        }
        
        // Switch view controllers
        if self.blueViewController != nil && self.blueViewController!.view.superview != nil {
            UIView.transition(with: self.view, duration: 0.4, options: [UIView.AnimationOptions.transitionFlipFromRight, UIView.AnimationOptions.curveEaseInOut], animations: {
                self.yellowViewController.view.frame = self.view.frame;
                self.switchViewController(from: self.blueViewController, to: self.yellowViewController)
            }, completion: nil)
            
        } else {
            UIView.transition(with: self.view, duration: 0.4, options: UIView.AnimationOptions.transitionFlipFromRight, animations: {
                self.blueViewController.view.frame = self.view.frame
                self.switchViewController(from: self.yellowViewController, to: self.blueViewController)
            }, completion: nil)
            
        }
    }
    
    private func switchViewController(from fromVC: UIViewController?, to toVC: UIViewController?) {
        if fromVC != nil {
            fromVC!.willMove(toParent: nil)
            fromVC!.view.removeFromSuperview()
            fromVC!.removeFromParent()
        }
        if toVC != nil {
            self.addChild(toVC!)
            self.view.insertSubview(toVC!.view, at: 0)
            toVC!.didMove(toParent: self)
        }
    }
    
    class func isLiuHaiScreen() -> Bool {
        let screenSize = UIScreen.instancesRespond(to: #selector(getter: UIScreen.main.currentMode)) ? UIScreen.main.currentMode?.size : nil
        if let size = screenSize {
            if !((size.width == 320 && size.height == 480)
                && (size.width == 640 && size.height == 960)
                && (size.width == 640 && size.height == 1136)
                && (size.width == 750 && size.height == 1334)
                && (size.width == 1080 && size.height == 1920)
                && (size.width == 1242 && size.height == 2208)) {
                return true
            }
        }
        return false
    }
}


```

##### BlueViewController.swift

```swift
import UIKit

class BlueViewController: UIViewController {
    
    var btn: UIButton = {
        let btn = UIButton(type: UIButton.ButtonType.system)
        btn.setTitle("Press Me", for: UIControl.State.normal)
        btn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIControl.Event.touchUpInside)
        return btn
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor = UIColor.blue
        self.view.addSubview(self.btn)
        self.btn.frame = CGRect(x: (self.view.frame.size.width - 64) / 2, y: (self.view.frame.size.height - 30) / 2, width: 64, height: 30)
    }
    
    @objc func buttonClick(sender: UIButton) {
        let alert = UIAlertController(title: "Blue View Button Pressed", message: "You pressed the button on the blue view", preferredStyle: .alert)
        let action = UIAlertAction(title: "Yes, I did", style: .default, handler: nil)
        alert.addAction(action)
        present(alert, animated: true, completion: nil)
    }
}
```

##### YellowViewController.swift

```swift
import UIKit

class YellowViewController: UIViewController {
    
    var btn: UIButton = {
        let btn = UIButton(type: UIButton.ButtonType.system)
        btn.setTitle("Press Me, Too", for: UIControl.State.normal)
        btn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIControl.Event.touchUpInside)
        return btn
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor = UIColor.yellow
        self.view.addSubview(self.btn)
        self.btn.frame = CGRect(x: (self.view.frame.width - 97) / 2, y: (self.view.frame.height - 30) / 2, width: 97, height: 30)
    }
    
    @objc func buttonClick(sender: UIButton) {
        let alert = UIAlertController(title: "Yellow View Button Pressed", message: "You pressed the button on the yellow view", preferredStyle: .alert)
        let action = UIAlertAction(title: "Yes, I did", style: .default, handler: nil)
        alert.addAction(action)
        present(alert, animated: true, completion: nil)
    }
}
```

