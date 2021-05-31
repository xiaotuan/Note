### Android 上的类型安全枚举

在早期版本的 Java 中，可以用多个整型常量解决这个问题。虽然这在技术上可行，但是很容易出错。请看下面的代码：

```java
public class Machine {
    public static final int STOPPED = 10;
    public static final int INITIALIZING = 20;
    public static final int STARTING = 30;
    public static final int RUNNING = 40;
    public static final int STOPPING = 50;
    public static final int CRASHED = 60;
    
    public int mState;
    
    public Machine() {
        mState = STOPPED;
    }
    
    public int getState() {
        return mState;
    }
    
    public void setState(int state) {
        mState = state;
    }
}
```

问题是，虽然这些常量是期望的，但是没有机制保证 `setState()` 方法接收不同的值。开发者所需的是在编译时检查非法赋值。类型安全的枚举解决了这个问题，如下所示：

```java
public class Machine {
    public enum State {
        STOPPED, INITIALIZING, STARTING, RUNNING, STOPPED, CRASHED
    }
    
    private State mState;
    
    public Machine() {
        mState = State.STOPPED;
    }
    
    public State getState() {
        return mState;
    }
    
    public void setState(State state) {
        mState = state;
    }
    
}
```



