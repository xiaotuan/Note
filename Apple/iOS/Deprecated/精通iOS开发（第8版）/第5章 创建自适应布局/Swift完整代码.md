<center><font size="5"><b>Swift 完整代码</b></font></center>

```swift
import UIKit

class ViewController: UIViewController {
    
    var centerLabel: UILabel = {
        let label = UILabel()
        label.text = "Center"
        label.textAlignment = .center
        return label
    }()
    
    var leftTopLabel: UILabel = {
        let label = UILabel()
        label.text = "LeftTop"
        label.textAlignment = .left
        return label
    }()
    
    var rightTopLabel: UILabel = {
       let label = UILabel()
        label.text = "RightTop"
        label.textAlignment = .right
        return label
    }()
    
    var leftBottomLabel: UILabel = {
       let label = UILabel()
       label.text = "LeftBottom"
       label.textAlignment = .left
       return label
    }()
    
    var rightBottomLabel: UILabel = {
       let label = UILabel()
        label.text = "RightBottom"
        label.textAlignment = .right
        return label
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.addSubview(self.centerLabel)
        self.view.addSubview(self.leftTopLabel)
        self.view.addSubview(self.rightTopLabel)
        self.view.addSubview(self.leftBottomLabel)
        self.view.addSubview(self.rightBottomLabel)
        
        self.updateViewsFrame()
    }
    
    override func viewDidLayoutSubviews() {
        self.updateViewsFrame()
    }
    
    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        get {
            return UIInterfaceOrientationMask(rawValue: (UIInterfaceOrientationMask.portrait.rawValue | UIInterfaceOrientationMask.landscapeLeft.rawValue))
        }
    }

    func updateViewsFrame() {
        let size = self.view.frame.size
        self.centerLabel.frame = CGRect(x: (size.width - 80) / 2, y: (size.height - 21) / 2, width: 80, height: 21)
        self.leftTopLabel.frame = CGRect(x: 16, y: 16, width: 80, height: 21)
        self.rightTopLabel.frame = CGRect(x: size.width - 16 - 80, y: 16, width: 80, height: 21)
        self.leftBottomLabel.frame = CGRect(x: 16, y: size.height - 16 - 21, width: 100, height: 21)
        self.rightBottomLabel.frame = CGRect(x: size.width - 16 - 100, y: size.height - 16 - 21, width: 100, height: 21)
    }
}
```

