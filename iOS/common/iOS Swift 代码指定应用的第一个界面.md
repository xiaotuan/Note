iOS13更新之后增加了SceneDelegate文件，AppDelegate不再负责UI的生命周期，交给了SceneDelegate来处理，因此，我们创建根控制器的时候，就要在SceneDelegate文件中创建了，如下：



```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // Use this method to optionally configure and attach the UIWindow `window` to the provided UIWindowScene `scene`.
        // If using a storyboard, the `window` property will automatically be initialized and attached to the scene.
        // This delegate does not imply the connecting scene or session are new (see `application:configurationForConnectingSceneSession` instead).
        guard let windownScene = (scene as? UIWindowScene) else { return }
        window = UIWindow(windowScene: windownScene)
        window!.backgroundColor = UIColor.white
        window!.rootViewController = ViewController()
        window!.makeKeyAndVisible()
    }
```

