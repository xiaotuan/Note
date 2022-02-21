[toc]

### 1. 通过类名获取 Class 对象

```java
Class clazz = String.class;
```

### 2. 通过实例获取 Class 对象

```java
String str = "test";
Class clazz = str.getClass();
```

### 3. 通过类名获取 Class 对象

```java
try {
    Class clazz = Class.forName("java.lang.String");
} catch (ClassNotFoundException e) {
    e.printStackTrace();
}
```

