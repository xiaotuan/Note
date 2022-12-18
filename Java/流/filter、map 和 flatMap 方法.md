`filter` 转换会产生一个流，它的元素与某种条件相匹配。下面，我们将一个字符串流转换为了只包含长单词的另一个流：

```java
List<String> wordList = ...;
Stream<String> longWords = wordList.stream().filter(w -> w.length() > 12);
```

通常，我们想要安装某种方式来转换流中的值，此时，可以使用 `map` 方法并传递执行该转换的函数。例如，我们可以像下面这样将所有单词转换为小写：

```java
Stream<String> lowercaseWords = words.stream().map(String::toLowerCase);
```

但是，通常我们可以使用 lambda 表达式来代替：

```java
Stream<String> firstLetters = words.stream().map(s -> s.substring(0, 1));
```

在使用 `map` 时，会有一个函数应用到每个元素上，并且其结果是包含了应用该函数后所产生的所有结果的流。现在，假设我们有一个函数，它返回的不是一个值，而是一个包含众多值的流：

```java
public static Stream<String> letters(String s) {
    List<String> result = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
        result.add(s.substring(i, i + 1));
    }
    return result.stream();
}
```

例如，`letters("boat")` 的返回值是流 `["b", "o", "a", "t"]`。

假设我们在一个字符串流上映射 `letters` 方法：

```java
Stream<Stream<String>> result = words.stream().map(w -> letters(w));
```

那么就会得到一个包含流的流，就像 `[...["y", "o", "u", "r"], ["b", "o", "a", "t"], ...]`。为了将其摊平为字母流 `[..."y", "o", "u", "r", "b", "o", "a", "t", ...]`，可以使用 `flatMap` 方法而不是 `map` 方法：

```java
Stream<String> flatResult = words.stream().flatMap(w -> letters(w));	// Calls letters on each word and flattens the results
```

`flatMap` 方法产生一个流，它是通过将 `mapper` 应用于当前流中所有元素所产生的结果连接到一起而获得的。（注意，这里的每个结果都是一个流。）