[toc]

### 1. 如何使用 Optional 值

有效地使用 `Optional` 的关键是要使用这样的方法：它在值不存在的情况下会产生一个可替代物，而只有在值存在的情况下才会使用这个值。

让我们来看看第一条策略。通常，在没有任何匹配时，我们会希望使用某种默认值，可能是空字符串：

```java
String result = optionalString.orElse("");	// The wrapped string, or "" if none
```

你还可以调用代码来计算默认值：

```java
String result = optionalString.orElseGet(() -> Locale.getDefault().getDisplayName());	// The function is only called when needed
```

或者可以在没有任何值时抛出异常：

```java
String result = optionalString.orElseThrow(IllegalStateException::new);	// Supply a method that yields an exception object
```

另一条使用可选值的策略是只有在其存在的情况下才消费该值。

`ifPresent` 方法会接受一个函数。如果该可选值存在，那么它会被传递给改函数。否则，不会发生任何事情。

```java
optionValue.ifPresent(v -> Process v);
```

当调用 `ifPresent` 时，从该函数不会返回任何值。如果想要处理函数的结果，应该使用 `map`：

```java
Optional<Boolean> added = optionValue.map(result::add);
```

### 2. 不适合使用 Optional 值的方式

`get` 方法会在 `Optional` 值存在的情况下获得其中包装的元素，或者在不存在的情况下抛出一个 `NoSuchElementException` 对象。因此：

```java
Optional<T> optionalValue = ...;
optionalValue.get().someMethod();
```

并不比下面的方式更安全：

```java
T value = ...;
value.someMethod();
```

### 3. 创建 Optional 值

如果想要编写方法来创建 `Optional` 对象，那么有很多方法可以用于此目的，包括 `Optional.of(result)` 和 `Optional.empty()`。例如：

```java
public static Optional<Double> inverse(Double x) {
    return x == 0 ? Optional.empty() : Optional.of(1 / x);
}
```

`ofNullable` 方法被用来作为可能出现的 null 值和可选值之间的桥梁。`Optional.ofNullable(obj)` 会在 obj 不为 null 的情况下返回 `Optional.of(obj)`，否者会返回 `Optional.empty()`。

### 4. 用 flatMap 来构建 Optional 值的函数

假设你有一个可以产生 `Optional<T>` 对象的方法 f，并且目标类型 T 具有一个可以产生 `Optional<U>` 对象的方法 g。如果它们都是普通的方法，那么你可以通过调用 `s.f().g()` 来将它们组合起来。但是这种组合没法工作，因为 `s.f()` 的类型为 `Optional<T>`，而不是 T。因此，需要调用：

```java
Optional<U> result = s.f().flatMap(T::g);
```

**示例代码：**

```java
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Optional;
import java.util.Set;

public class OptionalTest {

	public static void main(String[] args) throws IOException {
		String contents = new String(Files.readAllBytes(Paths.get("alice30.txt")), StandardCharsets.UTF_8);
		List<String> wordList = Arrays.asList(contents.split("\\PL+"));
		
		Optional<String> optionalValue = wordList.stream()
				.filter(s -> s.contains("fred"))
				.findFirst();
		System.out.println(optionalValue.orElse("No word") + " contains fred");
		
		Optional<String> optionalString = Optional.empty();
		String result = optionalString.orElse("N/A");
		System.out.println("result: " + result);
		result = optionalString.orElseGet(() -> Locale.getDefault().getDisplayName());
		System.out.println("result: " + result);
		try {
			result = optionalString.orElseThrow(IllegalStateException::new);
			System.out.println("result: " + result);
		} catch (Throwable t) {
			t.printStackTrace();
		}
		
		optionalValue = wordList.stream()
				.filter(s -> s.contains("red"))
				.findFirst();
		optionalValue.ifPresent(s -> System.out.println(s + " contains red"));
		
		Set<String> results = new HashSet<>();
		optionalValue.ifPresent(results::add);
		Optional<Boolean> added = optionalValue.map(results::add);
		System.out.println(added);
		
		System.out.println(inverse(4.0).flatMap(OptionalTest::squareRoot));
		System.out.println(inverse(-1.0).flatMap(OptionalTest::squareRoot));
		System.out.println(inverse(0.0).flatMap(OptionalTest::squareRoot));
		Optional<Double> result2 = Optional.of(-4.0).flatMap(OptionalTest::inverse).flatMap(OptionalTest::squareRoot);
		System.out.println(result2);
	}
	
	public static Optional<Double> inverse(Double x) {
		return x == 0 ? Optional.empty() : Optional.of(1 / x);
	}
	
	public static Optional<Double> squareRoot(Double x) {
		return x < 0 ? Optional.empty() : Optional.of(Math.sqrt(x));
	}
}
```

