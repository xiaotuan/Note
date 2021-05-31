LocalDate 对象的静态工厂方法：

```java
LocalDate.now();
```

使用年、月和日来构造 LocalDate 对象：

```java
LocalDate.of(1999, 12, 31);
```

通过 LocalDate 对象获取年、月和日：

```java
int year = newYearsEve.getYear();	// 1999
int month = newYearsEve.getMonthValue();	// 12
int day = newYearsEve.getDayOfMonth();	// 31
```

