1）监听WKWebView的标题改变

```objectivec
webView.addObserver(self, forKeyPath: "title", options: NSKeyValueObservingOptions.new, context: nil)
```

（2）监听WKWebView的加载进度

```objectivec
webView.addObserver(self, forKeyPath: "estimatedProgress", options: NSKeyValueObservingOptions.new, context: nil)
```

（3）处理监听事件

```swift
override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
    if keyPath == "estimatedProgress" {
        print("进度 \(webView.estimatedProgress)")
        progressView.progress = Float(webView.estimatedProgress)
        if (progressView.progress >= 1.0) {
            let deadline = DispatchTime.now() + 0.3
            DispatchQueue.global().asyncAfter(deadline: deadline) {
                DispatchQueue.main.async {
                    self.progressView.progress = 0;
                }
            }
        }
    } else if keyPath == "title" {
        self.navigationItem.title = webView.title;
    }
}
```