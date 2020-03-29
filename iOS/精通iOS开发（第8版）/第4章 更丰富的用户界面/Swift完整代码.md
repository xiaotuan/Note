<center><font size="5"><b>Swift 完整代码</b></font></center>

```swift
import UIKit

class ViewController: UIViewController, UITextFieldDelegate {
    
    var logo: UIImageView = {
        let image = UIImageView(image: UIImage(named: "apress_logo"))
        return image
    }()
    
    var nameLabe: UILabel = {
        let label = UILabel()
        label.text = "Name:"
        label.textAlignment = .right
        return label
    }()
    
    var nameTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Type in a name"
        textField.borderStyle = .roundedRect
        textField.returnKeyType = .done
        return textField
    }()
    
    var numberLabel: UILabel = {
        let label = UILabel()
        label.text = "Number:"
        label.textAlignment = .right
        return label
    }()
    
    var numberTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "Type in a number"
        textField.borderStyle = .roundedRect
        textField.sizeToFit()
        textField.keyboardType = .numberPad
        textField.returnKeyType = .done
        return textField
    }()
    
    var slider: UISlider = {
        let slider = UISlider()
        slider.minimumValue = 0
        slider.maximumValue = 100
        slider.value = 50
        slider.addTarget(self, action: #selector(sliderValueChange(sender:)), for: UIControl.Event.valueChanged)
        return slider
    }()
    
    var sliderLabel: UILabel = {
        let label = UILabel()
        label.text = "50";
        label.textAlignment = NSTextAlignment.center
        return label
    }()
    
    var segmentedControl: UISegmentedControl = {
        let control = UISegmentedControl(items: ["Switches", "Button"])
        control.selectedSegmentIndex = 0
        control.addTarget(self, action: #selector(segmentedValueChanged(sender:)), for: UIControl.Event.valueChanged)
        return control
    }()
    
    var leftSwitch: UISwitch = {
        let s = UISwitch()
        s.setOn(true, animated: false)
        s.addTarget(self, action: #selector(switchValueChange(sender:)), for: UIControl.Event.valueChanged)
        return s
    }()
    
    var rightSwitch: UISwitch = {
        let s = UISwitch()
        s.setOn(true, animated: false)
        s.addTarget(self, action: #selector(switchValueChange(sender:)), for: UIControl.Event.valueChanged)
        return s
    }()
    
    var btn: UIButton = {
        let btn = UIButton(type: UIButton.ButtonType.custom)
        btn.setTitle("Do Something", for: UIControl.State.normal)
        btn.setBackgroundImage(UIImage(named: "whiteButton"), for: .normal)
        btn.setBackgroundImage(UIImage(named: "blueButton"), for: .highlighted)
        btn.isHidden = true
        btn.addTarget(self, action: #selector(buttonClick(sender:)), for: UIControl.Event.touchUpInside)
        return btn
    }()
    
    var gesture: UITapGestureRecognizer!

    override func viewDidLoad() {
        super.viewDidLoad()
        self.gesture = UITapGestureRecognizer(target: self, action: #selector(tap(sender:)))
        self.view.backgroundColor = UIColor(red: 254 / 255.0, green: 195 / 255.0, blue: 10 / 255.0, alpha: 1.0)
        self.nameTextField.delegate = self
        self.numberTextField.delegate = self
        self.addViews()
        self.updateViewsFrame()
    }

    func addViews() {
        self.view.addGestureRecognizer(self.gesture)
        self.view.addSubview(self.logo)
        self.view.addSubview(self.nameLabe)
        self.view.addSubview(self.nameTextField)
        self.view.addSubview(self.numberLabel)
        self.view.addSubview(self.numberTextField)
        self.view.addSubview(self.sliderLabel)
        self.view.addSubview(self.slider)
        self.view.addSubview(self.segmentedControl)
        self.view.addSubview(self.leftSwitch)
        self.view.addSubview(self.rightSwitch)
        self.view.addSubview(self.btn)
    }
    
    func updateViewsFrame() {
        let size = self.view.frame.size;
        self.logo.frame = CGRect(x: (size.width - 172) / 2, y: 133, width: 172, height: 80)
        self.nameLabe.frame = CGRect(x: 16, y: self.logo.frame.maxY + 43, width: 80, height: 34)
        self.nameTextField.frame = CGRect(x: self.nameLabe.frame.maxX + 8, y: self.logo.frame.maxY + 43, width: size.width - self.nameLabe.frame.maxX - 16 - 8, height: 34)
        self.numberLabel.frame = CGRect(x: 16, y: self.nameLabe.frame.maxY + 43, width: 80, height: 34)
        self.numberTextField.frame = CGRect(x: self.numberLabel.frame.maxX + 8, y: self.nameTextField.frame.maxY + 43, width: size.width - self.numberLabel.frame.maxX - 16 - 8, height: 34)
        self.sliderLabel.frame = CGRect(x: 16, y: self.numberTextField.frame.maxY + 33.0, width: 29, height: 31)
        self.slider.frame = CGRect(x: self.sliderLabel.frame.maxX, y: self.numberTextField.frame.maxY + 33, width: size.width - (self.sliderLabel.frame.maxX + 16), height: 31)
        self.segmentedControl.frame = CGRect(x: (size.width - self.segmentedControl.frame.width) / 2, y: self.slider.frame.maxY + 33, width: self.segmentedControl.frame.width, height: 32)
        self.btn.frame = CGRect(x: 16, y: self.segmentedControl.frame.maxY + 33, width: size.width - 16 * 2, height: 31)
        self.leftSwitch.frame = CGRect(x: 16, y: self.segmentedControl.frame.maxY + 33, width: self.leftSwitch.frame.width, height: self.leftSwitch.frame.height)
        self.rightSwitch.frame = CGRect(x: size.width - 16 - self.rightSwitch.frame.width, y: self.segmentedControl.frame.maxY + 33, width: self.rightSwitch.frame.width, height: self.rightSwitch.frame.height)
    }
    
    @objc func segmentedValueChanged(sender: UISegmentedControl) {
        self.btn.isHidden = sender.selectedSegmentIndex != 1
        self.leftSwitch.isHidden = sender.selectedSegmentIndex != 0
        self.rightSwitch.isHidden = sender.selectedSegmentIndex != 0
    }
    
    @objc func switchValueChange(sender: UISwitch) {
        self.leftSwitch.setOn(sender.isOn, animated: true)
        self.rightSwitch.setOn(sender.isOn, animated: true)
    }
    
    @objc func sliderValueChange(sender: UISlider) {
        self.sliderLabel.text = String(Int(sender.value))
    }
    
    @objc func buttonClick(sender: UIButton) {
        let controller = UIAlertController(title: "Are You Sure?", message: nil, preferredStyle: .actionSheet)
        let yesAction = UIAlertAction(title: "Yes, I'm sure!", style: .destructive) { (action) in
            let msg = self.nameTextField.text!.isEmpty ? "You can breathe easy, everything went OK." : "You can breathe easy,  \(self.nameTextField.text!), " + "everything went OK."
            let controller2 = UIAlertController(title: "Something Was Done", message: msg, preferredStyle: .alert)
            let cancelAction = UIAlertAction(title: "Phew!", style: .cancel, handler: nil)
            controller2.addAction(cancelAction)
            self.present(controller2, animated: true, completion: nil)
        }

        let noAction = UIAlertAction(title: "No way!", style: .cancel, handler: nil)

        controller.addAction(yesAction)
        controller.addAction(noAction)

        present(controller, animated: true, completion: nil)
    }
    
    @objc func tap(sender: UITapGestureRecognizer) {
        self.view.endEditing(true)
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
}


```

