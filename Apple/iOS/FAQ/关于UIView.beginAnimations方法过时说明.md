<center><font size="5"><b>关于UIView.beginAnimations方法过时说明</b></font></center>

`UIView.beginAnimations()` 相关方法在 `iOS 13.0` 被标记为过时 `API` ，推荐使用代码块动画进行替换。

```swift
extension UIView {

    
    /* Deprecated in iOS 13.0. Please use the block-based animation API instead. */
    
    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func beginAnimations(_ animationID: String?, context: UnsafeMutableRawPointer?)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func commitAnimations()

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationDelegate(_ delegate: Any?)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationWillStart(_ selector: Selector?)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationDidStop(_ selector: Selector?)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationDuration(_ duration: TimeInterval)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationDelay(_ delay: TimeInterval)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationStart(_ startDate: Date)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationCurve(_ curve: UIView.AnimationCurve)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationRepeatCount(_ repeatCount: Float)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)

    @available(iOS, introduced: 2.0, deprecated: 13.0, message: "Use the block-based animation API instead")
    open class func setAnimationTransition(_ transition: UIView.AnimationTransition, for view: UIView, cache: Bool)
}
```

代码块动画方法：

```swift
extension UIView {

    @available(iOS 4.0, *)
    open class func animate(withDuration duration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions = [], animations: @escaping () -> Void, completion: ((Bool) -> Void)? = nil)

    @available(iOS 4.0, *)
    open class func animate(withDuration duration: TimeInterval, animations: @escaping () -> Void, completion: ((Bool) -> Void)? = nil)

    @available(iOS 4.0, *)
    open class func animate(withDuration duration: TimeInterval, animations: @escaping () -> Void)

    @available(iOS 7.0, *)
    open class func animate(withDuration duration: TimeInterval, delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options: UIView.AnimationOptions = [], animations: @escaping () -> Void, completion: ((Bool) -> Void)? = nil)

    @available(iOS 4.0, *)
    open class func transition(with view: UIView, duration: TimeInterval, options: UIView.AnimationOptions = [], animations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)

    @available(iOS 4.0, *)
    open class func transition(from fromView: UIView, to toView: UIView, duration: TimeInterval, options: UIView.AnimationOptions = [], completion: ((Bool) -> Void)? = nil)

    @available(iOS 7.0, *)
    open class func perform(_ animation: UIView.SystemAnimation, on views: [UIView], options: UIView.AnimationOptions = [], animations parallelAnimations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)

    @available(iOS 12.0, *)
    open class func modifyAnimations(withRepeatCount count: CGFloat, autoreverses: Bool, animations: () -> Void)
}
```

