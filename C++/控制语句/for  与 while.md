在 C++ 中，`for` 和 `while` 循环本质上是相同的。例如，下面的 `for` 循环：

```cpp
for (init-expression; test-expression; update-expression)
{
    statement(s)
}
```

可以改写成这样：

```cpp
init-expression;
while (test-expression)
{
    statement(s);
    update-expression;
}
```

同样，下面的 `while` 循环：

```cpp
while (test-expression)
    body
```

可以改写成这样：

```cpp
for (;test-expressio;)
    body
```

