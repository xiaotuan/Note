Java 语言规范要求 equals 方法具有下面的特性：

+ 自反性：对于任何非空引用 x，`x.equals(x)` 应该返回 true。
+ 对称性：对于任何引用 x 和 y，当且仅当 `y.equals(x)` 返回 true，`x.equals(y)` 也应该返回 true。
+ 传递性：对于任何引用 x、y 和 z，如果 `x.equals(y)` 返回 true，`y.equals(z)` 也返回 true，`x.equals(z)` 也应该返回 true。
+ 一致性：如果 x 和 y 引用的对象没有发生变化，返回调用 `x.equals(y)` 应该返回同样的结果。
+ 对于任意非空引用 x，`x.equals(null)` 应该返回 false。

一个标准的 equals 方法实现：

```java
public class Employee {
    ...
    @Override
    public boolean equals(Object otherObject) {
        // a quick test to see if the objects are identical
        if (this == otherObject) return true;
        
        // must return false if the explicit parameter is null
       	if (otherObject == null) return false;
        
        // if the classes don't match, they can't be equal 
        if (getClass() != otherObject.getClass()) {
            return false;
        }
        
        // now we know otherObject is a non-null Employee
        Employee other = (Employee) otherObject;
        
        // test whether the fields have identical values
        return name.equals(other.name)
            && salary == other.salary
            && hireDay.equals(other.hireDay);
    }
}
```

