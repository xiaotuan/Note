<center><font size="5"><b>Swift完整代码</b></font></center>

```swift
import UIKit

class ViewController: UIViewController {
    
    static let statusHeight: CGFloat = {
        return isLiuHaiScreen() ? 44 : 24;
    }()
    
    var tipLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center;
        return label
    }()
    
    var leftBtn: UIButton = {
        let btn = UIButton(type: .system)
        btn.setTitle("Left", for: .normal)
        return btn
    }()
    
    var rightBtn: UIButton = {
        let btn = UIButton(type: .system)
        btn.setTitle("Right", for: .normal)
        return btn
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.addSubview(self.tipLabel)
        self.view.addSubview(self.leftBtn)
        self.view.addSubview(self.rightBtn)
        
        self.leftBtn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIButton.Event.touchUpInside)
        self.rightBtn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIButton.Event.touchUpInside)
        
        updateViewsFrame()
    }

    @objc func buttonClick(sender: UIButton) {
        let title = sender.title(for: .normal)!
        let text = "\(title) button pressed"
        let styledText = NSMutableAttributedString(string: text)
        let attrs = [NSAttributedString.Key.font: UIFont.boldSystemFont(ofSize: self.tipLabel.font.pointSize)]
        let nameRange = (text as NSString).range(of: title)
        styledText.setAttributes(attrs, range: nameRange)

        self.tipLabel.attributedText = styledText
    }
    
    func updateViewsFrame() {
        let size = self.view.frame.size
        self.tipLabel.frame = CGRect(x: 16, y: ViewController.statusHeight + 32, width: size.width - 16 * 2, height: 21)

        self.leftBtn.frame = CGRect(x: 16, y: (size.height - 30) / 2, width: 48, height: 30)
        self.rightBtn.frame = CGRect(x: size.width - 16 - 48, y: (size.height - 30) / 2, width: 48, height: 30)
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

