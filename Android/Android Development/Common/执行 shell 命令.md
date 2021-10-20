[toc]

### 1. 执行 root 权限命令

#### 1. kotlin 版本

```kotlin
try {
    Runtime.getRuntime().exec(arrayOf("su", "-c", "reboot fastboot"));
} catch (IOException e) {
    e.printStackTrace();
}
```

#### 2. Java 版本

```java
try {
    Runtime.getRuntime().exec(arrayOf("su", "-c", "reboot fastboot"));
} catch (IOException e) {
    e.printStackTrace();
}
```

### 2. 执行普通权限命令

#### 2.1 Kotlin 版本

```kotlin
try {
    Runtime.getRuntime().exec(new String[] {"su", "-c", "reboot fastboot"});
} catch (IOException e) {
    e.printStackTrace();
}
```

#### 2.2 Java 版本

```java
try {
    Runtime.getRuntime().exec(new String[] {"sh", "-c", "reboot fastboot"});
} catch (IOException e) {
    e.printStackTrace();
}
```



