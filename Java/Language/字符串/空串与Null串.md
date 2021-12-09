空串 `""` 是长度为 0  的字符串。可以调用以下代码检查一个字符串是否为空：

```java
if (str.length() == 0)
```

或者

```java
if (str.equals(""))
```

要检查一个字符串是否为 null， 要使用以下条件：

```java
if (str == null)
```

有时要检查一个字符串既不是 null 也不为空串，可以使用以下条件：

```java
if (str != null && str.length())
```

