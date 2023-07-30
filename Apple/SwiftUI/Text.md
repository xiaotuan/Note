[toc]

#### 使用方法

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
            .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

#### 设置字体

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
        	.font(.largeTitle)
    }
}
```

或：

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
        	.font(Font.system(size: 32))
    }
}
```

#### 设置背景色

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
        	.background(Color.blue)
    }
}
```

或：

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
            .background(Color(UIColor.init(red: 80/255.0, green: 125/255.0, blue: 232/255.0, alpha: 0.8)))
    }
}
```

#### 设置前景色

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
            .foregroundColor(.white)
    }
}
```

#### 设置行间距

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .lineSpacing(5)
    }
}
```

#### 设置外间距

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .padding(.all, 15)
    }
}
```

#### 设置边框

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .border(Color.blue, width: 5)
    }
}
```

#### 设置旋转效果

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .rotationEffect(.init(degrees: 45), anchor: .center)
    }
}
```

#### 设置模糊效果

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .blur(radius: 1)
    }
}
```

#### 设置控件尺寸

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .frame(width: 250, height: 100, alignment: .leading)
    }
}
```

#### 设置字体权重

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .fontWeight(.bold)
    }
}
```

#### 设置圆角

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello, world!\nHere's to the crazy ones.")
            .blur(radius: 1)
            .background(Color.green)
            .cornerRadius(8)
    }
}
```

