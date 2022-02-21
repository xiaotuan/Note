[toc]

### 1. 示例程序

```java
```

### 2. API

#### 2.1 java.lang.Class 1.0

------

+ **Field[] getFields()	1.1**

+ **Field[] getDeclaredFields()	1.1**

`getFields()` 方法将返回一个包含 `Field` 对象的数组，这些对象记录了这个类或其超类的公有域。`getDeclaredField()` 方法也将返回包含 `Field` 对象的数组，这些对象记录了这个类的全部域。如果类中没有域，或者 Class 对象描述的是基本类型或数组类型，这些方法将返回一个长度为 0 的数组。

+ **Method[] getMethods()	1.1**

+ **Method[] getDeclareMethods()	1.1**

返回

