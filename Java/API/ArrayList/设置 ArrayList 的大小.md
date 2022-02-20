如果已经清楚或能够估计出数组可能存储的元素数量，就可以在填充数组之前调用 `ensureCapacity()` 方法：

```java
ArrayList<Employee> staff = new ArrayList<>();
staff.ensureCapacity(100);
```

也可以把初始容量传递给 ArrayList 构造器：

```java
ArrayList<Employee> staff = new ArrayList<>(100);
```

