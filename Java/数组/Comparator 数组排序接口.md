[toc]

### 1. 接口定义

```java
public interface Comparator<T> {
    int compare(T o1, T o2);
}
```

### 2. 实现接口

下面是一个按字符串长度排序的接口实现：

```java
class LengthComparator implements Comparator<String> {

	@Override
	public int compare(String o1, String o2) {
		return o1.length() - o2.length();
	}
	
}
```

### 3. 使用接口进行排序

```java
import java.util.Arrays;
import java.util.Comparator;

public class JavaTest {

	public static void main(String[] args) {
		String[] friends = { "Peter", "Paul", "Mary" };
		Arrays.sort(friends, new LengthComparator());
		System.out.println(Arrays.toString(friends));
	}

}

class LengthComparator implements Comparator<String> {

	@Override
	public int compare(String o1, String o2) {
		return o1.length() - o2.length();
	}
	
}
```

