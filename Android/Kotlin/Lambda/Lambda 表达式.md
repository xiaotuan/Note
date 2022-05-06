[toc]

### 1. 通用写法

**Java**

```java
mView.setOnClickListener(new View.OnClickListener() {
   @Override
    public void onClick(View view) {
        
    }
});
```

**Kotlin**

```kotlin
mView.setOnClickListener(object: View.OnClickListener{
    override fun onClick(view: View?) {

    }
})
```

### 2. 接口是方法的最后一个参数写法

> 注意：下面的示例由于 Java 和 Kotlin 定义的方法不同，造成参数位置不一致。

**Java**

```java
Timer timer = new Timer();
timer.schedule(new TimerTask() {
    @Override
    public void run() {

    }
}, 1000);
```

**Kotlin**

```kotlin
var timer = Timer()
timer.schedule(1000) { 

}
```

### 3. 接口只有一个方法的简写方式

如果方法中只有一个参数，且接口只有一个回调方法，可以使用简写 Lambda：

**Java**

```java
mView.setOnClickListener(new View.OnClickListener() {
   @Override
    public void onClick(View view) {
        
    }
});
```

**Kotlin**

```kotlin
mView.setOnClickListener { view -> {
    
}}
```

