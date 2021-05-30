`RegExp()` 构造函数带有两个字符串参数，其中第二个参数是可选的，第一个参数包含正则表达式的主体部分，第二个参数指定正则表达式的修饰符，不过只能传入修饰符 g、i、m或它们的组合。比如：

```js
// 全局匹配字符串中的5个数字，注意这里使用了"\\"，而不是"\"
var zipcode = new RegExp("\\d{5}", "g")
```

`RegExp()`构造函数非常有用，特别是在需要动态创建正则表达式的时候，这种情况往往没办法通过写死在代码中的正则表达式直接量来实现。例如，如果待检索的字符串是有用户输入的，就必须使用 `RegExp()` 构造函数。例如：

```js
var value = "java"
var patten = new RegExp(value + "script")
```

每个 `RegExp` 对象都包含 5 个属性。属性 source 是一个只读的字符串，包含正则表达式的文本。属性 global 是一个只读的布尔值，用以说明这个正则表达式是否带有修饰符 g。属性 ignoreCase 也是一个只读的布尔值，用以说明正则表达式是否带有修饰符 i。属性 multiline 是一个只读的布尔值，用以说明正则表达式是否带有修饰符 m。最后一个属性 lastIndex，它是一个可读/写的整数。如果匹配模式带有 g 修饰符，这个属性存储在整个字符串中下一次检索的开始位置，这个属性会被 `exec()` 和 `est()`方法用到。

`RegExp` 最主要的执行模式匹配的方法是 `exec()`。`exec()` 方法对一个指定的字符串执行一个正则表达式，如果他没有找到任何匹配，它就返回 null，但如果它找到了一个匹配，它将返回一个数组。

当调用 `exec()` 的正则表达式对象具有修饰符 g 时，它将把当前正则表达式对象的 lastIndex 属性设置为紧挨着匹配子串的字符位置。当同一个正则表达式第二次调用 `exec()` 时，它将从 lastIndex 属性所指示的字符串处开始检索。如果 `exec()` 没有发现任何匹配结果，它会将 lastIndex 重置为 0（在任何时候都可以将 lastIndex 属性设置为 0，每当在字符串中找最后一个匹配项后，再使用这个 `RegExp` 对象开始新的字符串查找之前，都应当将 lastIndex 设置为 0）。这种特殊的行为使我们可以在用正则表达式匹配字符串的过程中反复调用 `exec()`，比如：

```js
var pattern = /Java/g
var text = "JavaScript is more fun than Java!"
var result
while ((result = pattern.exec(text)) != null) {
    alert("Matched '" + result[0] + "'" + " at position " + result.index + "; next search begins at " + pattern.lastIndex)
}
```

另外一个 `RegExp` 方法是 `test()`，它的参数是一个字符串，用 `test()` 对某个字符串进行检测，如果包含正则表达式的一个匹配结果，则返回 true：

```js
var pattern = /java/i
pattern.test("JavaScript")    // 返回true
```

当一个全局正则表达式调用方法 `test()` 时，它的行为和 `exec()` 相同，因为它从 lastIndex 指定的位置处开始检索某个字符串，如果它找到了一个匹配结果，那么它就立即设置 lastIndex 为当前匹配子串的结束位置。这样一来，就可以使用 `test()` 来遍历字符串。

在 `ECMAScript 5` 中，正则表达式直接量的每次计算都会创建一个新的 `RegExp` 对象，每个新 `RegExp` 对象具有各自的 lastIndex 属性，这势必会大大减少“残留” lastIndex 对程序造成的意外影响。