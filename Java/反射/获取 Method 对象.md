可以通过调用 `getDeclareMethods()` 方法，然后对返回的 Method 对象数组进行查找，直到发现想要的方法为止。也可以通过调用 Class 类中的 `getMethod()` 方法得到想要的方法。

`getMethod()` 的签名是：

```java
Method getMethod(String name, Class... parameterTypes)
```

例如：

```java
package com.qty.test;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.time.LocalDate;

public class JavaTest {

	public static void main(String[] args) {
		Employee harry = new Employee("Josh", 5000.0, 2022, 3, 11);
		try {
			Method ml = Employee.class.getMethod("raiseSalary", double.class);
			Method[] methods = Employee.class.getDeclaredMethods();
			for (int i = 0; i < methods.length; i++) {
				if ("raiseSalary".equals(methods[i].getName())) {
					System.out.println("Find raiseSalary method.");
				}
			}
		} catch (NoSuchMethodException | SecurityException e) {
			e.printStackTrace();
		}
	}

}

class Employee {
	// instance fields
	private String name;
	private double salary;
	private LocalDate hireDay;

	// constructor
	public Employee(String n, double s, int year, int month, int day) {
		name = n;
		salary = s;
		hireDay = LocalDate.of(year, month, day);
	}

	// a method
	public String getName() {
		return name;
	}

	// more methods
	public double getSalary() {
		return salary;
	}

	public LocalDate getHireDay() {
		return hireDay;
	}

	public void raiseSalary(double byPercent) {
		double raise = salary * byPercent / 100;
		salary += raise;
	}
}
```

